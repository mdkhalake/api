class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class MovieAlreadyExistsError(Exception):
    pass

class UpdatingMovieError(Exception):
    pass

class DeletingMovieError(Exception):
    pass

class MovieNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "MovieAlreadyExistsError": {
         "message": "Post with given name already exists",
         "status": 400
     },
     "UpdatingMovieError": {
         "message": "Updating post added by other is forbidden",
         "status": 403
     },
     "DeletingMovieError": {
         "message": "Deleting post added by other is forbidden",
         "status": 403
     },
     "MovieNotExistsError": {
         "message": "Post with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}