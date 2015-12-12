# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals

from collections import namedtuple
from .field import BaseField


field_item = namedtuple('field_item', 'name,field')


class Contract(object):
    _storage = None
    _storage_class = dict

    def __init__(self, initial=None):
        if initial is not None:
            self._storage = self._storage_class(initial)
        else:
            self._storage = self._storage_class()

    @classmethod
    def _is_field(cls, obj):
        return isinstance(obj, BaseField)

    def __getattribute__(self, key):
        """Custom attribute handling.

        If the attribute is a field, return the value returned from
        its .get() method. Otherwise, return it directly.
        """
        attr = object.__getattribute__(self, key)
        if self._is_field(attr):
            return attr.get(self, key)
        return attr

    def __setattr__(self, key, value):
        """Custom attribute handling.

        If the attribute is a field, pass the value to its .set()
        method. Otherwise, set it directly on the object.
        """
        v = object.__getattribute__(self, key)
        if self._is_field(v):
            return v.set(self, key, value)
        return object.__setattr__(self, key, value)

    def __delattr__(self, key):
        """Custom attribute handling.

        If the attribute is a field, call its .del() method.
        Otherwise, perform the action directly on the object.
        """
        v = object.__getattribute__(self, key)
        if self._is_field(v):
            return v.delete(self, key)
        return object.__delattr__(self, key)

    @classmethod
    def _iter_fields(cls):
        """Iterate over fields defined in this object

        Yields:
            tuple: (name, field)
        """
        for name in dir(cls):
            # attr = object.__getattribute__(cls, name)
            attr = getattr(cls, name)
            if cls._is_field(attr):
                yield field_item(name, attr)

    @classmethod
    def _get_fields(cls):
        return sorted(
            cls._iter_fields(),
            key=lambda x: x.field._creation_counter)

    def __repr__(self):
        return u'{0}({1})'.format(
            self.__class__.__name__,
            repr(self._storage))
