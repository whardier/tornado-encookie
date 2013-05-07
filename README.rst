tornado-encookie
================

Encrypted cookie support for Tornado Web Server

License
-------
This software is under the MIT License

Requirements
------------

* PyCrypto
* Tornado

Please file a bug for version issues.  Tested on Python 3.2.

Encryption
----------

Encryption is done using AES256 with a 32 byte block.

Example
--------

Handler

.. code:: python

    from tornadoencookie.encookie import EncookieMixin
    
    class MyHandler(tornado.web.RequestHandler, EncookieMixin):
        def get(self):
            #Get a cookie
            self.encookie.get_cookie('hello')
    
            #Get a secure cookie
            self.encookie.get_secure_cookie('hello')
    
            #Set a regular cookie
            self.encookie.set_cookie('hi', 'there')
            
            #Set a secure cookie
            self.encookie.set_secure_cookie('hello', 'Timmy')

Configuration

.. code:: python

    application = tornado.web.Application([
        (r'/', MyHandler),
    ], **{
        'encookie_secret': 'iamthecookiemons',
        },
    )
    
