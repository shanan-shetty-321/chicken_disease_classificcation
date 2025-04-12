FROM python:3.8-slim-buster
# for using the python 3.8 slim buster image as the base image
RUN apt update -y && apt inst 
#for updating the aws cli 
WORKDIR /app
#
COPY . /app
#for copying the current directory to the container
RUN pip install -r requirements.txt
#for installing the requirements 
CMD ["python3", "app.py"]
#for running the app.py file when the container starts and since it is a linux pipeline we are mentioning python version 