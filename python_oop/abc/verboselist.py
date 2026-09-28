#!/usr/bin/env python3
"""The module is for verboselist"""


class VerboseList(list):
    """This class represents a verboselist"""

    # Methods
    def append(self, object):
        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items")

    def remove(self, value):
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        popped_number = super().pop(index)
        print(f"Popped [{popped_number}] from the list.")
        return popped_number


vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)
