# encoding: utf-8
class _Serializable(object):
    """
        Abstract serializable class.
        All classes implemended this used for request parameters.
        It can be serializable to JSON values for request parameters.
    """

    def _to_dict(self):
        """
            Private method used for object serialization.
        """

        raise NotImplementedError()


class Entry(_Serializable):
    """
        User entry for class `Entity`
        Entry objects, which contain reference names and synonyms for `Entity`.
        For detail information about entries see
        http://docs.yige.ai/%E8%AF%8D%E5%BA%93%E6%8E%A5%E5%8F%A3.html#词库对象中的词库数组
    """

    @property
    def value(self):
        """
            Entry's value A canonical name to be used in place of the synonyms.
            Example: `New York`
            :rtype: str or unicode
        """

        return self._value

    @value.setter
    def value(self, value):
        """
            :type value: str or unicode
        """

        self._value = value

    @property
    def synonyms(self):
        """
            The array of synonyms.
            Example: `["New York", "@big Apple",
            "city that @{never, seldom, rarely} sleeps"]`
            :rtype: list of (str or unicode)
        """

        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """
            :type synonyms: list of (str or unicode)
        """
        self._synonyms = synonyms

    def __init__(self, value, synonyms):
        """Construct a `Entry` and fill default values."""
        super(Entry, self).__init__()

        self._value = value
        self._synonyms = synonyms

    """Private method used for object serialization."""
    def _to_dict(self):
        return {
            'value': self.value,
            'synonyms': self.synonyms
        }


class Entity(_Serializable):
    """
        User entity for `Request`
        `Entity` is used to create, retrieve and update user-defined entity
        objects. For detail information about entities see
    """

    @property
    def name(self):
        """
            Entity name.
            :rtype: str or unicode
        """

        return self._name

    @name.setter
    def name(self, name):
        """
            :type name: str or unicode
        """

        self._name = name

    @property
    def entries(self):
        """
            Entity entries. Array of `Entry` class objects
            :rtype: list of Entry
        """

        return self._entries

    @entries.setter
    def entries(self, entries):
        """
            :type entries: list of Entry
        """

        self._entries = entries

    def __init__(self, name, entries):
        super(Entity, self).__init__()

        self.name = name
        self.entries = entries

    def _to_dict(self):
        """
            Private method used for object serialization.
        """

        return {
            'name': self.name,
            'entries': list(map(lambda x: x._to_dict(), self.entries))
        }