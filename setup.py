#!/usr/bin/env python

from setuptools import setup

setup(name='sqlauthenticator',
      version='1.0',
      description='SQL Authenticator for Jupyterhub',
      author='xuchao',
      license='MIT',
      author_email='g-xuchao@tedu.cn',
      url='https://github.com/asouX/jupyterhub-sqlauthenticator',
      packages=['sqlauthenticator'],
      install_requires=[
        'passlib',
        'PyMySQL',
        'jupyterhub',
      ],
      )
