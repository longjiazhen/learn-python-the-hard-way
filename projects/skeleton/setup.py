#coding:utf-8
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My Email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packges': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}
setup(**config)