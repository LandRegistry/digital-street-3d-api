# This file is the entry point.
# First we import the app object, which will get initialised as we do it. Then import methods we're about to use.
from digital_street_3d_api.app import app
from digital_street_3d_api.blueprints import register_blueprints
from digital_street_3d_api.exceptions import register_exception_handlers
from digital_street_3d_api.extensions import register_extensions

# Now we register any extensions we use into the app
register_extensions(app)
# Register the exception handlers
register_exception_handlers(app)
# Finally we register our blueprints to get our routes up and running.
register_blueprints(app)
