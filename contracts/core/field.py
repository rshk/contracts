# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals


class _NotSet(object):  # Just for the repr()
    def __repr__(self):
        return 'NOTSET'


NOTSET = _NotSet()

_field_creation_counter = 0


class BaseField(object):
    """
    Pseudo-descriptor, accepting field names along with instance,
    to allow better retrieving data for the instance itself.

    Warning:

        Beware that fields shouldn't carry state of their own, a part
        from the one used for generic field configuration, as they
        are shared between instances.


    Args:

        default:
            Default value (if not callable) or function
            returning default value (if callable).

        """

    default = None

    def __init__(self, default=NOTSET):
        # So we can sort them later
        global _field_creation_counter
        _field_creation_counter += 1
        self._creation_counter = _field_creation_counter

        self.default = default

    def get(self, instance, name):
        """
        Get the value for the field from the main instace,
        by looking at the first found in:

        - the updated value
        - the initial value
        - the default value
        """

        if self.default is NOTSET:
            return instance._storage[name]
        return instance._storage.get(name)

    def validate(self, instance, name, value):
        """
        The validate method should be the (updated)
        value to be used as the field value, or raise
        an exception in case it is not acceptable at all.
        """
        return value

    def set(self, instance, name, value):
        """Set the modified value for a field"""
        value = self.validate(instance, name, value)
        instance._storage[name] = value

    def delete(self, instance, name):
        """
        Delete the modified value for a field (logically
        restores the original one)
        """
        # We don't want an exception here, as we just restore
        # field to its initial value..
        instance._storage.pop(name, None)

    def __repr__(self):
        return '{name}(default={default})'.format(
            name=self.__class__.__name__,
            default=repr(self.default))
