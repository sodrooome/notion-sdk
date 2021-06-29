import requests
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class BaseNotionConfig:
    token: str
    notion_version: str
    endpoint: str = "https://api.notion.com/v1/"


@dataclass
class NotionConfig:
    """
    Using __slots__ to use less memory
    """
    __slots__ = ["token", "notion_version"]
    token: str
    notion_version: str
    endpoint: str = "https://api.notion.com/v1/"

    def __post_init__(self):
        if self.notion_version and self.token is None:
            raise Exception("Need specify the configuration first")

    def __str__(self):
        """
        Representation for Notion configuration
        :return: returned as string object
        """
        return f"Your Notion Token is {self.token} and version usage is {self.notion_version}"


@dataclass
class ExceptionConfig:
    request: requests


@dataclass
class DatabaseObjects:
    object: str
    result: List

    @classmethod
    def from_dict(cls, data: dict) -> "DatabaseObjects":
        """
        Representation for Database instances, keep separate with JSON type
        :param data: database object
        :return: list of database object
        """
        return cls(object=data["object"], result=data["results"])


@dataclass
class UserObjects:
    object: str
    id: str
    name: str
    type: str
    email: str

    @classmethod
    def from_dict(cls, data: dict) -> "UserObjects":
        """
        Representation for User instances, keep separate with JSON type
        :param data: users object
        :return: list of users object
        """
        return cls(object=data["results"][0]["object"],
                   id=data["results"][0]["id"],
                   name=data["results"][0]["name"],
                   type=data["results"][0]["type"],
                   email=data["results"][0]["person"]["email"])
