===============================
yige-python
===============================


.. image:: https://img.shields.io/pypi/v/yige.svg
        :target: https://pypi.python.org/pypi/yige

.. image:: https://img.shields.io/travis/wwj718/yige.svg
        :target: https://travis-ci.org/wwj718/yige

.. image:: https://readthedocs.org/projects/yige/badge/?version=latest
        :target: https://yige-python.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/wwj718/yige/shield.svg
     :target: https://pyup.io/repos/github/wwj718/yige/
     :alt: Updates


Python library for yige


* Free software: MIT license
* Documentation: https://yige-python.readthedocs.io.

Overview
--------

The yige Python SDK makes it easy to  use yige.ai

Features
--------

*  text query
*  entity manage


Installation
---------

To install yige, simply:

.. code-block:: bash

    $ pip install yige

or install it from repo:

.. code-block:: bash

     $ pip install https://github.com/wwj718/yige-python.git


Running examples
--------

1. Find examples from 'examples' path.
2. Insert API key.

.. code-block:: python

    >>> CLIENT_ACCESS_TOKEN = '<YOUR_CLIENT_ACCESS_TOKEN>'
    ...

Usage
---------

1. send text query

.. code-block:: python

    >>> CLIENT_ACCESS_TOKEN = '<YOUR_CLIENT_ACCESS_TOKEN>'
    >>> ai = yige.Yige(CLIENT_ACCESS_TOKEN)
    >>> request = ai.text_request()
    >>> request.query = "我想买鞋" 
    >>> response = request.getresponse() #注意置信度 confidence
    >>> print(response.json())
    ...

2. post user entities

.. code-block:: python

    >>> DEV_ACCESS_TOKEN = '<YOUR_DEV_ACCESS_TOKEN>'
    >>> ai = yige.Yige(DEV_ACCESS_TOKEN)
    >>> payload= {}
    >>> payload["name"] = "脚型" # 词库名称
    >>> payload["type"] = 1 #是否定义同义词 1是  0否
    >>> payload["automated_expansion"] = 0
    >>> payload["entries"] = [] # 词库内容
    >>> entity1 =  {
                "value": "正常内旋", # 同义词中比较权威的名称
                "synonyms": [ #  同义词
                    "正常内旋",
                    "内旋正常",
                    "正常足弓",
                    "足弓正常"
                ]
            }
    >>> payload["entries"].append(entity1)
    >>> user_entities_request = ai.user_entities_request()
    >>> user_entities_request.user_entities = payload
    >>> user_entities_response = user_entities_request.getresponse() 
    >>> print(user_entities_response.json())
   ...

3. debug  console

.. code-block:: bash

    >>> yige --console
    ...

Test
--------

make test


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

