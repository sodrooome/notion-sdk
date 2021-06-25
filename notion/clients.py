from typing import Any
from .dataclass import NotionConfig, DatabaseObjects, UserObjects
from .adapters import adapter
from .utils import composed_dict
from .exceptions import JSONDecodeError


class NotionAPI(NotionConfig):
    def get_all_db(self, result: str = "json", **kwargs: Any) -> Any:
        """
        Retrieve all database in the workspace
        :param kwargs: arguments for selector "start_cursor" and "page_size"
        :param result: parameters for select output value. default value is JSON
        :return: Any of object
        """
        fullpath = self.endpoint + "databases"
        headers = {"Authorization": f"Bearer {self.token}", "Notion-Version": self.notion_version}
        selector = composed_dict(kwargs, "start_cursor", "page_size")
        request = adapter(fullpath, headers, selector)

        if result.lower() == "json":
            return request
        elif result.lower() == "encapsulated":
            return DatabaseObjects.from_dict(request)
        raise JSONDecodeError

    def get_single_db(self, database_id: str):
        """
        Retrieve single database based on the required ID
        :param database_id: integer of object
        :return: Any of object that relevant with required ID
        """
        fullpath = self.endpoint + f"databases/{database_id}"
        headers = {"Authorization": f"Bearer {self.token}", "Notion-Version": self.notion_version}
        request = adapter(fullpath, headers)
        return request

    def get_single_page(self, page_id: int):
        """
        Retrieve single page in workspace based on the required ID
        :param page_id: integer of object
        :return: Any of page object that relevant with required ID
        """
        fullpath = self.endpoint + f"pages/{page_id}"
        headers = {"Authorization": f"Bearer {self.token}", "Notion-Version": self.notion_version}
        request = adapter(fullpath, headers)
        return request

    def get_single_block(self, block_id: int, **kwargs: Any):
        """
        Retrieve single block in workspace based on the required ID
        :param block_id: integer of object
        :param kwargs: arguments for selector "start_cursor" and "page_size"
        :return: Any of block object that relevant with required ID
        """
        fullpath = self.endpoint + f"pages/{block_id}/children"
        headers = {"Authorization": f"Bearer {self.token}", "Notion-Version": self.notion_version}
        selector = composed_dict(kwargs, "start_cursor", "page_size")
        request = adapter(fullpath, headers, selector)
        return request

    def get_single_user(self, user_id: int):
        """
        Retrieve single detailed user
        :param user_id: Integer of object
        :return: Any of object that relevant with required ID
        """
        fullpath = self.endpoint + f"users/{user_id}"
        headers = {"Authorization": f"Bearer {self.token}", "Notion-Version": self.notion_version}
        request = adapter(fullpath, headers)
        return request

    def get_all_users(self, result: str = "json", **kwargs: Any):
        """
        Retrieve all users
        :param kwargs: arguments for selector "start_cursor" and "page_size"
        :param result: parameters for select output value. default value is JSON
        :return: Any of object
        """
        fullpath = self.endpoint + "users"
        headers = {"Authorization": f"Bearer {self.token}", "Notion-Version": self.notion_version}
        selector = composed_dict(kwargs, "start_cursor", "page_size")
        request = adapter(fullpath, headers, selector)

        if result.lower() == "json":
            return request
        elif result.lower() == "encapsulated":
            return UserObjects.from_dict(request)
        raise JSONDecodeError
