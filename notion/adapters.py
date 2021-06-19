import requests
from typing import Optional, Any
from .exceptions import HTTPNotFound, HTTPRedirection, HTTPUnknown, HTTPUnauthorized


def adapter(fullpath, headers, *args: Optional) -> Any:
    """
    Method for bridging the request and response, support ``GET`` method
    :param fullpath: full-path for Notion API endpoint
    :param headers: setup Notion headers (token and notion version)
    :param args: optional arguments
    :return: generate low HTTP request into Notion APIs
    """
    request = requests.get(fullpath, headers=headers)
    if request.status_code == 200:
        return request.json()
    elif request.status_code == 404:
        raise HTTPNotFound
    elif request.status_code == 429:
        raise HTTPRedirection
    elif request.status_code == 401:
        raise HTTPUnauthorized
    raise HTTPUnknown
