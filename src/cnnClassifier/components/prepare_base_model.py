import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config


    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(input_shape=self.config.params_image_size,weights=self.config.params_weights,include_top=self.config.params_include_top)

        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    #@staticmethod is a decorator in Python used to define a method inside a class that does not require access to the instance (self) or class (cls).
    #No self or cls:A static method does not modify or access the class attributes.
    #It behaves like a regular function but is logically grouped inside a class.
    # Called using the class name or an instance
       
    #How to Know If a Method Depends on Instance Attributes (self)?
#To determine whether a method depends on instance attributes, ask yourself:
#➡️ Does the method require interaction with self.method_name() (instance methods)?

#If the answer is YES, then the method depends on instance attributes and should use self.
#If the answer is NO, then the method does NOT depend on instance attributes and could be a @staticmethod.


    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate): 
        # freeze_all -> will freeze all layers, freeze_till -> will freeze till the given layer
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model) #save model in artifacts 

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model): #saving the model in the path given in the config file
        model.save(path)
