Contracts
#########


.. image:: https://img.shields.io/travis/rshk/contracts.svg
    :target: https://travis-ci.org/rshk/contracts

.. image:: https://img.shields.io/circleci/project/rshk/contracts.svg
    :target: https://circleci.com/gh/rshk/contracts


Base library for defining lean "contract" models for Python.


Abstract
========

This is an implementation of "models" similar to those you see in most
ORMs / forms definition systems, but with the main goal of keeping
things as simple as possible.

No metaclasses or descriptors are involved; no hackish code messing up
with standard Python objects functionality either.

The idea is to have a "layered" library, providing the bare bones
needed to define your own schemas, along with some nice helpers for
common cases.


Use cases
=========

- API clients
- ORMs
- Forms



Example model definition
========================

.. code:: python

    from contracts.core import Contract, BaseField

    # Use BaseField to define your field types, eg. StringField and
    # IntegerField.

    class MyModel(BaseObject):
        first_name = StringField()
        last_name = StringField()
        age = IntegerField()

Then, create some library to make use of the schema somehow 😊.
