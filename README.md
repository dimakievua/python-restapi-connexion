Getting Started

Using Virtual Environments
$ pip install virtualenv

Change to desired directory and create virtual environment:
$ virtualenv env

Here’s what each folder contains:
    bin: files that interact with the virtual environment
    include: C headers that compile the Python packages
    lib: a copy of the Python version along with a site-packages folder where each dependency is installed

You should be in application folder running next steps:

In order to use this environment’s packages/resources in isolation, you need to “activate” it. 
Git-bash:
$ source env/bin/activate
(env) $

CMD:
$ env\Scripts\activate.bat

Before we test this, we need to go back to the “system” context by executing deactivate:
(env) $ deactivate
$

Install flask
$ pip install flask connexion connexion[swagger-ui]

Run application
$ python server.py

Dockerfile is placed in repo
requirments.txt list app modules and run in Dockerfile
flask==1.0.2
connexion[swagger-ui]==2.0.1

Build image:
$ docker build -t restapi:latest .

After the build completes, we can run the container:
$ docker run -d -p 5000:5000 restapi

