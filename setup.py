try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Team City nosetests plugin to generate service messages',
    'author': 'Chris Smith',
    'url': 'https://github.com/Intelliflo/teamcity-nosetests',
    'download_url': 'xxx',
    'author_email': 'chris.smith@intelliflo.com',
    'version': '0.1',
    'install_requires': [ 'nose' ],
    'packages': [ 'teamcitynosetests' ],
    'scripts': [],
    'name': 'teamcitynosetests'
}

setup(**config)

