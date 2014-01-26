pson
====

Python library to make querying JSON-like structures easy!

With the explosion of APIs returning JSON the use of JSON like structures (i.e what you get if you take JSON and run it through JSON.loads()) querying these types of structures is a common need.

Most people either manually traverse the structures or write their own querying logic, this library aims to solve that need by providing a general purpose querying utils. It uses the dot notation to traverse structures in a similar fashion to document databases such as MongoDB.

Examples
--------

To demonstrate by example with the following JSON:

.. code-block:: js

    json = {
     'header' : {'title' : 'Hello World', 
                 'year' : 2014}, 
     'body' : { 'translations' : [
                                    {'language' : 'french', 'translation' : 'bonjour'}, 
                                    {'language' : 'german', 'translation' : 'guten tag'}
                                 ] 
              }
    }
    
Traditional (pre-pson) approach:

.. code-block:: pycon

    >>> json['header']['title']
    'Hello World'

New pson approach:
    
.. code-block:: pycon

    >>> from pson import pathquery as pq

    >>> pq(json, 'header.title')
    'Hello World'
    
Some more pson examples:

.. code-block:: pycon

    >>> from pson import pathquery as pq

    >>> pq(json, 'header.title')
    'Hello World'
    
    # as you'd expect it can return sub-structures    
    >>> pq(json, 'body')
    {'translations': [{'translation': 'bonjour', 'language': 'french'}, {'translation': 'guten tag', 'language': 'german'}]}

    # and arrays
    >>> pq(json, 'body.translations')
    [{'translation': 'bonjour', 'language': 'french'}, {'translation': 'guten tag', 'language': 'german'}]
  
    # you can query into arrays using numerical indicies 
    >>> pq(json, 'body.translations.0.language')
    'french'

    # you can also not specify an index and get back an array where the rest of the query 
    # is applied to every element in the array
    >>> pq(json, 'body.translations.language')
    ['french', 'german']

    
How does it handle missing values ?

.. code-block:: pycon

    >>> from pson import pathquery as pq
    
    # by default it returns None rather than throwing an exception
    >>> pq(json, 'header.author')
    None
  
    # you can over-ride what it returns though
    >>> pq(json, 'header.author', missing="Unknown")
    'Unknown'
    
    # which is useful for situations like where you're building strings and don't want to deal
    # with lots of KeyError exceptions
    >>> pq(json, 'header.title') + ' by ' + pq(json, 'header.author', missing="Unknown")
    'Hello World by Unknown'
    
    

Installation
------------
TBD

Authors
------------

Built by Imran Ghory (@imranghory). Released under the MIT Licence. Contributions welcome via Github.
