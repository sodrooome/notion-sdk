import requests
from typing import Optional, Any
from .exceptions import HTTPNotFound, HTTPRedirection, HTTPUnknown, HTTPUnauthorized, JSONDecodeError
from .enum import HTTPStatus


def adapter(fullpath, headers, *args: Optional) -> Any:
    """
    Method for bridging the request and response, support ``GET`` method
    :param fullpath: full-path for Notion API endpoint
    :param headers: setup Notion headers (token and notion version)
    :param args: optional arguments
    :return: generate low HTTP request into Notion APIs
    """
    try:
        request = requests.get(fullpath, headers=headers)
    except Exception:
        raise HTTPUnknown
    if request.status_code == HTTPStatus.NOT_FOUND:
        raise HTTPNotFound
    elif request.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        raise HTTPRedirection
    elif request.status_code == HTTPStatus.UNAUTHORIZED:
        raise HTTPUnauthorized
    else:
        try:
            json_object = request.json()
        except Exception:
            raise JSONDecodeError
        finally:
            pass
    return json_object

