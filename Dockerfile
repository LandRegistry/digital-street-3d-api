# Set the base image to the base image
FROM lr_base_python_flask

# Using SQLAlchemy/Postgres?
# See how the required env vars are set here:
# http://192.168.249.38/gadgets/gadget-api/blob/master/Dockerfile

# ----
# Put your app-specific stuff here (extra yum installs etc).
# Any unique environment variables your config.py needs should also be added as ENV entries here

# ----

# The command to run the app. 
#   Eventlet is used as the (asynch) worker.
#   The python source folder is /src (mapped to outside file system in docker-compose-fragment)
#   Access log is redirected to stderr.
#   Flask app object is located at <app name>.main:app
#   Dynamic reloading is enabled
CMD ["/usr/local/bin/gunicorn", "-k", "eventlet", "--pythonpath", "/src", "--access-logfile", "-", "flask_skeleton_api.main:app", "--reload"]

# Get the python environment ready.
# Have this at the end so if the files change, all the other steps don't need to be rerun. Same reason why _test is 
# first. This ensures the container always has just what is in the requirements files as it will rerun this in a 
# clean image.
ADD requirements_test.txt requirements_test.txt
ADD requirements.txt requirements.txt
RUN pip3 install -q -r requirements.txt && \
  pip3 install -q -r requirements_test.txt
