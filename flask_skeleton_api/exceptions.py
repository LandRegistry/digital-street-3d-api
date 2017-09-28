from flask import Response, current_app
import json


class ApplicationError(Exception):
    """Use this class when the application identifies there's been a problem and the client should be informed.

    Example: raise ApplicationError("Critical error", "DB")

    or

    raise ApplicationError("Title number invalid", "E102", http_code=400)

    or

    raise ApplicationError("Title number invalid", "E102", http_code=400, live_log=True)
    """

    def __init__(self, message, code, http_code=500, live_log=False):
        """Create an instance of the error.

        Keyword arguments:

        http_code - handler methods will use this to determine the http code to set in the returned Response
        (default 500)

        live_log - handler methods will use this to determine whether to log at debug or error. This parameter only
        applies to expected application errors, as unhandled exceptions are always considered live-log worthy 
        (default False)
        """
        Exception.__init__(self)
        self.message = message
        self.http_code = http_code
        self.code = code
        self.live_log = live_log


def unhandled_exception(e):
    """Handler method for exceptions that escape the route code without being caught.

    A consistent JSON bodied response is returned.

    Due to the lack of information available to provide to the client, and the fact there was clearly
    no opportunity for cleanup or error handling in the processing code, this should be a never-event!
    """
    current_app.logger.exception('Unhandled Exception: %s', repr(e))
    return Response(response=json.dumps({"error_message": "Internal Server Error", "error_code": "500"}),
                    mimetype='application/json',
                    status=500)


def application_error(e):
    """Handler method for ApplicationErrors raised for to inform the client of a specific scenario.

    A consistent JSON bodied response is returned.
    """
    # If requested, log at ERROR level
    if e.live_log:
        current_app.logger.exception('Application Exception (message: %s, code: %s): %s', e.message, e.code, repr(e))
    else:
        current_app.logger.debug('Application Exception (message: %s, code: %s): %s', e.message, e.code, repr(e),
                                 exc_info=True)
    return Response(response=json.dumps({"error_message": e.message, "error_code": e.code}),
                    mimetype='application/json',
                    status=e.http_code)


def register_exception_handlers(app):
    app.register_error_handler(ApplicationError, application_error)
    app.register_error_handler(Exception, unhandled_exception)

    app.logger.info("Exception handlers registered")
