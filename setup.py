from setuptools import setup

setup(name='yahoo_finance',
      version='0.1',
      description='Yahoo Finance scrapper',
      url='http://github.com/howsunjow/yahoo_finance',
      author='Howsun Jow',
      author_email='howsun.jow@gmail.com',
      license='MIT',
      packages=['yahoo_finance'],
      scripts=['bin/download_major_indices'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
