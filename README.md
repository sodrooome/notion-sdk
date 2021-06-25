## Python Notion

![PyPI](https://img.shields.io/pypi/v/pynotion-wrapper) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pynotion-wrapper) [![Build Status](https://travis-ci.com/sodrooome/notion-sdk.svg?branch=master)](https://travis-ci.com/sodrooome/notion-sdk)

A simple wrapper for Notion SDK written in Python

### Installation

This library only supported Python version 3.7 and above, earlier version might be work,
but it still has backward compatibility for current APIs

`pip install pynotion-wrapper`

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

This wrapper also providing `dict` representation, so it will be separate with JSON type and returned as List for relevant
object instances. For example, you can use this in `get_all_users()` and `get_all_db()` method :

```python
from notion.clients import NotionAPI

version = "2021-05-13"
secret = "YOUR_NOTION_TOKEN"
client = NotionAPI(secret, version)
print(client.get_all_users("encapsulated")) # options are `JSON` and `encapsulated`
```

If you choose in parameters for that method to `json` the output will be the same as like in the above, but if you choose
parameters as `encapsulated` the returned value will be more simple rather than extensive output like in `dict` type :

```shell
# encapsulated types
UserObjects(object='user', id='d4da784c-1c77-47e8-96bd-e917d96cd8b8', name='Ryan Febriansyah', type='person', email='ryanfebriansyah72@gmail.com')
```

Currently this wrapper only supported for retrieve Notion resources :
* Database
* Blocks
* Pages
* User

In the meantime, all APIs endpoint that provided by Notion will be adding into wrapper (for consideration itself, 
it might be delayed until Notion API already stable). All contributions are much welcomed!

