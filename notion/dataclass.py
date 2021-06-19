import requests
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
