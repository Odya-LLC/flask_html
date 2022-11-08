"""
Flask-Html
-------------

This is the description for Flask-Html
"""
from setuptools import setup

long_description = """
Flask-Html
"""

setup(
    name='Flask-Html',
    version='1.0.0',
    url='https://github.com/Odya-LLC/flask_html',
    license='MIT',
    author='odya',
    author_email='mmuhtor@gmail.com',
    description='Component based html generator for flask',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['flask_html'],
    zip_safe=False,
    include_package_data=True,
    platforms=['3.6', '3.7', '3.8', '3.9', '3.10'],
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)