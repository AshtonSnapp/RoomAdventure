###########################################################################################
# Name:         Ashton Snapp, Jonathan Williams
# Date:         2019 JAN 9
# Description:  Room Adventure Python
###########################################################################################

# ROOM!


class Room:

    def __init__(self, name, id):

        self.name = name

        self.id = id

        self._exits = []

        self._items = []

        self._itemDescriptions = []

        self._itemFlags = []

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, s_exit, room):
        self._exits.append(s_exit + " EXITS TO " + room)

    @exits.deleter
    def exits(self, s_exit):
        for i in self._exits:
            if self._exits[i][0:5] == s_exit:
                del self._exits[i]
            elif self._exits[i][0:4] == s_exit:
                del self._exits[i]
            elif self._exits[i][0:3] == s_exit:
                del self._exits[i]
            elif self._exits[i][0:2] == s_exit:
                del self._exits[i]

    @property
    def items(self):
        return self._items and self._itemDescriptions and self._itemFlags

    @items.setter
    def items(self, item, desc, canGrab, canUse, canOpen):
        self._items.append(item)
        self._itemDescriptions.append(desc)
        self._itemFlags.append([canGrab, canUse, canOpen])

    @items.deleter
    def items(self, item):
        for i in self._items:
            if self._items[i] == item:
                del self._items[i]
                del self._itemDescriptions[i]
                del self._itemFlags[i]
