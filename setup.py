import io
import os
import re
from setuptools import setup, find_packages

with io.open('notion/version.py', 'rt', encoding='utf-8') as f:
	version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='pynotion-wrapper',
	version=version,
	author="Ryan Febriansyah",
	author_email="ryanfebriansyah72@gmail.com",
	description="Python SDK for Notion API client",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	url="https://github.com/sodrooome/notion-sdk",
	classifiers=[
		'Development Status :: 4 - Beta',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],
	python_requires='>=3.7',
	install_requires=[
		"requests",
	],
)
