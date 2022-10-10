#!/usr/bin/env python

from distutils.core import setup

setup(name='server',
      version='1.0',
      description='A budget app',
      author='Brandon Shimanek',
      author_email='brandon.j.shimanek@gmail.com',
      packages=['server'],
      entry_points={
          'console_scripts':
          ['net-server = server.__main__:main'],
      },
      include_package_data=True,
      package_data={
          '': ['*.ini']
      }
      )
