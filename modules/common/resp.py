from flask import current_app

class Response():
    def return_error(message, resp_code = 404):
        return {
            "message": message
        }, resp_code
    
    def return_internal_error(e):
        current_app.logger.error(e)
        return Response.return_error("Something went wrong", 504)
