from .dataclass import ExceptionConfig


class CustomException(Exception):
    pass


class HTTPNotFound(CustomException, ExceptionConfig):
    def __init__(self):
        super(HTTPNotFound, self).__init__(f"Request to Notion API failed due resources was not found ")


class HTTPRedirection(CustomException, ExceptionConfig):
    def __init__(self):
        super(HTTPRedirection, self).__init__(f"Request to Notion API exceeds the limit.")


class HTTPUnknown(CustomException, ExceptionConfig):
    def __init__(self):
        super(HTTPUnknown, self).__init__(f"Request to Notion API failed, due to unknown status.")
        
        
class HTTPUnauthorized(CustomException):
    def __init__(self):
        super(HTTPUnauthorized, self).__init__("Request to Notion API failed, due unauthorized token.")


class ResourcesException(CustomException):
    def __init__(self):
        super(ResourcesException, self).__init__("This method / property need specify the configuration")


class JSONDecodeError(CustomException):
    def __init__(self):
        super(JSONDecodeError, self).__init__("Can't decode the JSON response")