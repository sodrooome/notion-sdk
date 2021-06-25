import requests
from notion.clients import NotionAPI
from notion.adapters import adapter


# this secret key only for mock testing
# should not be concern about that
secret = "secret_vRRyjBas5iKPicOw2tO0d1baCUObmRLo7Oe7B1aRZA2"
version = "2021-05-13"


def test_adapter():
    headers = {
        "Authorization": f"Bearer {secret}",
        "Notion-Version": version
    }
    request = adapter("https://api.notion.com/v1/databases", headers)
    return True if request == 200 else False


def test_db_success():
    config = NotionAPI(secret, version)
    request = config.get_all_db()
    assert request


def test_single_db_success():
    config = NotionAPI(secret, version)
    request = config.get_single_db("a")
    assert request


def test_users_success():
    config = NotionAPI(secret, version)
    request = config.get_all_users()
    assert request


def test_single_user():
    config = NotionAPI(secret, version)
    request = config.get_single_user("32")
    assert request


def test_single_page():
    config = NotionAPI(secret, version)
    request = config.get_single_page("1")
    assert request


def test_single_block():
    config = NotionAPI(secret, version)
    request = config.get_single_block("1")
    assert request


def test_encapsulated_obj():
    config = NotionAPI(secret, version)
    request = config.get_all_users("encapsulated")
    assert request


def test_json_obj():
    config = NotionAPI(secret, version)
    request = config.get_all_users("json")
    assert request
