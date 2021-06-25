from enum import Enum, unique


@unique
class HTTPStatus(Enum):
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    TOO_MANY_REQUESTS = 429
