from flask import Response, current_app
import json
import traceback


class ApplicationError(Exception):
    """Use this class when the application identifies there's been a problem and the client should be informed.

    Example: raise ApplicationError("Critical error", "DB")

    or

    raise ApplicationError("Title number invalid", "E102", http_code=400)

    or

    raise ApplicationError("Title number invalid", "E102", http_code=400, force_error_log=True)
    """

    def __init__(self, message, code, http_code=500, force_error_log=False):
        """Create an instance of the error.

        Keyword arguments:

        http_code - handler methods will use this to determine the http code to set in the returned Response
        (default 500)

        force_error_log - handler methods will use this to determine whether to log at debug or error, when
        the http code being returned is not 500 (500s are always considered live-log worthy) (default False)
        """
        Exception.__init__(self)
        self.message = message
        self.http_code = http_code
        self.code = code
        self.force_error_log = force_error_log


def unhandled_exception(e):
    """Handler method for exceptions that escape the route code without being caught.

    A consistent JSON bodied response is returned.

    Due to the lack of information available to provide to the client, and the fact there was clearly
    no opportunity for cleanup or error handling in the processing code, this should be a never-event!
    """
    current_app.logger.exception('Unhandled Exception: %s', repr(e))

    response_dict = {"error_message": "Internal Server Error", "error_code": "500"}

    # If we are logging at debug level, also return the stack trace for greater visibility
    if current_app.config.get('FLASK_LOG_LEVEL', 'INFO').upper() == 'DEBUG':
        response_dict['stacktrace'] = traceback.format_exc()

    return Response(response=json.dumps(response_dict), mimetype='application/json', status=500)


def application_error(e):
    """Handler method for ApplicationErrors raised for to inform the client of a specific scenario.

    A consistent JSON bodied response is returned.
    """
    # If http code is 500 or it has been specifically requested, log at ERROR level
    if e.http_code == 500 or e.force_error_log:
        current_app.logger.exception('Application Exception (message: %s, code: %s): %s', e.message, e.code, repr(e))
    else:
        current_app.logger.debug('Application Exception (message: %s, code: %s): %s', e.message, e.code, repr(e),
                                 exc_info=True)

    response_dict = {"error_message": e.message, "error_code": e.code}

    # If we are logging at debug level, also return the stack trace for greater visibility
    if current_app.config.get('FLASK_LOG_LEVEL', 'INFO').upper() == 'DEBUG':
        response_dict['stacktrace'] = traceback.format_exc()

    return Response(response=json.dumps(response_dict), mimetype='application/json', status=e.http_code)


def register_exception_handlers(app):
    app.register_error_handler(ApplicationError, application_error)
    app.register_error_handler(Exception, unhandled_exception)

    app.logger.info("Exception handlers registered")
