import datetime
import json
from .utils import remove_key


def iso8601_format(date: datetime):
    """
    Method for formatting datetime into ISO-8601
    this method will be including on next release
    after ``POST`` or ``PUT`` method has been implemented
    :param date: datetime of object
    :return: Return ISO-8601 format so the Notion API will be understand
    """
    if date == remove_key:
        return date
    elif isinstance(date, datetime.datetime):
        return str(date.date())
    elif isinstance(date, datetime.date):
        return str(date)
    elif isinstance(date, str):
        return date


def json_object(object):
    """
    Method for formatting object request into JSON
    if not serialize the object, dont parse it
    :param object: representation of request
    :return: JSON-ify object
    """
    if isinstance(object, dict) or isinstance(object, list):
        return json.dumps(object)
    return object

