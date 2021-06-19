## Python Notion

A simple wrapper for Notion SDK written in Python

### Installation

This library only supported Python version 3.7 and above, earlier version might be work,
but it still has backward compatibility for current APIs

`pip install notion-wrapper`

### Usage

Before to do that, ensure you've setup **Notion Integration** and obtain the **Integration Token**.
You can see about the Integration in [here](https://developers.notion.com/docs).

For quick example to get all users :

```python
from notion.clients import NotionAPI

version = "2021-05-13" # notion version is required
secret = "YOUR_NOTION_TOKEN"
client = NotionAPI(secret, version)
print(client.get_all_users())
```

That following result something like :

```shell
{'object': 'list', 'results': [{'object': 'user', 'id': 'd4da784c-1c77-47e8-96bd-e917d96cd8b8', 'name': 'Ryan Febriansyah', 'avatar_url': 'https://lh4.googleusercontent.com/-O3Rzxu0oM9k/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucnDB5M-7zjHQcTqlJ0JBiAtlA5-RQ/photo.jpg', 'type': 'person', 'person': {'email': 'ryanfebriansyah72@gmail.com'}}, {'object': 'user', 'id': 'f4eb6dff-b0a9-431e-993f-970f049f1c76', 'name': 'python-sdk', 'avatar_url': None, 'type': 'bot', 'bot': {}}], 'next_cursor': None, 'has_more': False}
```


