# Import every blueprint file
from digital_street_3d_api.views import general, register_v1


def register_blueprints(app):
    """Adds all blueprint objects into the app."""
    app.register_blueprint(general.general)
    app.register_blueprint(register_v1.register_v1)

    # All done!
    app.logger.info("Blueprints registered")
