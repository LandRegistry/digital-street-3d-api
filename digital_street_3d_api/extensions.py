from flask_sqlalchemy import SQLAlchemy
from digital_street_3d_api.custom_extensions.enhanced_logging.main import EnhancedLogging
import logging
import json
import traceback
from flask import g, ctx
import collections

# Create empty extension objects here
enhanced_logging = EnhancedLogging()
db = SQLAlchemy()

def register_extensions(app):
    """Adds any previously created extension objects into the app, and does any further setup they need."""

    # This extension wraps the LogConfig extension with our own configuration (standard format JSON -> stdout
    # plus traceid parsing and propagation in a custom Requests Session)
    enhanced_logging.init_app(app)

    # Database
    db.init_app(app)

    # All done!
    app.logger.info("Extensions registered")
