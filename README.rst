**aadbook** -- access your Azure AD contacts from the command line.

About
=====

AADBook is a fork of `GooBook <https://pypi.org/project/goobook/>`_ focusing on
making it possible to use your Azure AD contacts from the command-line and from
MUAs such as Mutt.

Installation Instructions
=========================

There is a number of ways to install Python software.

- Using pip
- Using a source tarball
- Using source directly from gitorius
- From a distribution specific repository

pip or easy_install
-------------------

This is the recommended way to install **aadbook** for most users that don't
have it available in their distribution.  When installing this way you will not
need to download anything manually.

Install like this::

    pip install aadbook

Source installation
-------------------

Download the source tarball, uncompress it, then run the install command::

    tar -xzvf aadbook-*.tar.gz
    cd aadbook-*
    sudo python ./setup.py install

Configure
=========

For most users it will be enough to to run::

    aadbook authenticate

and follow the instructions.

To get access too more settings you can create a configuration file::

    aadbook config-template > ~/.aadbookkrc

It will look like this::


   # "#" or ";" at the start of a line makes it a comment.
   [DEFAULT]
   # The following are optional, defaults are shown

   # This file is written by the Azure AD library, and should be kept secure,
   # it's like a password to your AD contacts.
   ;auth_db_filename: ~/.aadbook_auth.json

   ;cache_filename: ~/.aadbook_cache
   ;cache_expiry_hours: 24


Proxy settings
--------------

If you use a proxy you need to set the ``https_proxy`` environment variable.

Mutt
----

If you want to use **aadbook** from mutt.

Set in your .muttrc file::

    set query_command="aadbook query '%s'"

to query address book.

Usage
=====

To query your contacts::

    aadbook query QUERY

The cache is updated automatically according to the configuration but you can also force an update::

    aadbook reload

For more commands see::

    aadbook -h

and::

    aadbook COMMAND -h

Links, Feedback and getting involved
====================================

- PyPI home: http://pypi.python.org/pypi/aadbook
- Code Repository: http://github.com/iamFIREcracker/aadbook