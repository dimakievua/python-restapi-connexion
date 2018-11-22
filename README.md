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
$ source env/Scripts/activate
(env) $

CMD:
$ env\Scripts\activate.bat

Before we test this, we need to go back to the “system” context by executing deactivate:
(env) $ deactivate
$

Install flask
$ pip install flask connexion[swagger-ui] nose

Run application
$ python server.py

Dockerfile is placed in repo
requirments.txt list app modules and run in Dockerfile
flask==1.0.2
connexion[swagger-ui]==2.0.1

Build image:
$ docker build -t restapi:latest .

By default image will be build with ENV=dev to install nore packages. For production please use env=prod
$ docker build -t restapi:latest --build-args env=prod .

After the build completes, we can run the container:
$ docker run -d -p 5000:5000 restapi

nose extends the unittest framework. It is not built-in like unittest, that’s why you should install it:
$ pip install nose swagger-tester


Together with the nose package and nosetests script will be installed on your machine, used to discover and run tests.
$ nosetests -v

To measure the code coverage in the Flask application I will use coverage.
$ pip install coverage

Now that you have it installed, to get the needed measurement data you have to run the following command:
$ coverage run –source=app_folder_path

To print the prepared report execute:
$ coverage report 
