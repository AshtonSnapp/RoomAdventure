class Room:

    def __init__(self, s_name, i_id, s_desc):

        self.name = s_name # Room name to be displayed to the player.

        self.id = i_id  # Room ID number for internal use.

        self.desc = s_desc  # Room description to be displayed when the player decides to "look around"

        self.exits = []

        self.exitDestinations = []

        self.items = []

    # TODO: Set and Get!


class Item:

    def __init__(self, s_name, i_id, s_desc, l_flags):

        self.name = s_name  # Name of the item

        self.id = i_id  # Internal item ID number

        self.desc = s_desc  # Item description to be displayed when the player decides to "look at" this item.

        self.flags = l_flags  # A list of boolean variables. Is this item a container? Can I pick it up?

    # TODO: Set and Get!

