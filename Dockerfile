# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim
# Set one or more individual labels
LABEL version="0.0.1-beta"
# set the working directory in the container to /app
WORKDIR /app
# Argument to control what script to install
ARG env=dev
# Set ENV variable
ENV ENV=$env
# add the current directory to the container as /app
ADD . /app
# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirments/${ENV}.txt
# expose port 80 for the Flask app to run on
EXPOSE 5000
# define entypoint
ENTRYPOINT ["python"]
# execute the Flask app
CMD ["server.py"]
