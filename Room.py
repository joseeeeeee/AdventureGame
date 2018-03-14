class Inventory():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def list(self):
        print ("You are carrying:")
        for item in self.items:
            print (item.get_name())

    def get(self, type):
        items_of_type = []
        for item in self.items:
            if isinstance(item, type):
                items_of_type.append(item)
        return items_of_type

    def process_command(self, command):
        result = []
        for item in self.items:
            if item.get_name() in command:
                result.append(item.process_command(command))
        return result

class Item():
    def __init__(self, name):
        self.name = name
        self.known_commands = {}

    def get_name(self):
        return self.name

    def process_command(self, command):
        for a_command in self.known_commands:
            if a_command in command:
                self.known_commands[a_command](command)


class Literature(Item):
    def __init__(self, name, contents="This item is blank."):
        Item.__init__(self, name)
        self.contents = contents
        self.known_commands["read"] = self.read
        self.known_commands["write"] = self.write(command)

    def read(self, command):
        print (self.contents)

    def write(self, contents):
        self.contents = contents


class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.items = []
        self.connectors = []
        self.rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def add_connection(self, room, connector, actions):
        for direction in actions:
            self.rooms[direction] = room
        self.connectors.append((connector, actions[0]))

    def enter_room(self, inventory):
        print (self.name)
        print
        print (self.description)
        print
        for connector in self.connectors:
            print ("There is a " + connector[0] + \
                   " that goes " + connector[1] + ".")
        print
        for item in self.items:
            print ("You see a " + item.name + " here.")
        print

    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self, direction):
        return self.rooms[direction]

    def process_command(self, command, inventory):
        if command in self.rooms.keys():
            new_room = self.next_room(command)
            return new_room
        elif "get" in command or "take" in command:
            for item in self.items:
                if item.name in command:
                    inventory.add(item)
                    self.items.remove(item)
                    return "You picked up the " + item.name + "."
                else:
                    return "I don't know what you want to pick up."
        else:
            return None


class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.items = []
        self.connectors = []
        self.rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def ass_connection(self, room, connector, actions):
        for direction in actions:
            self.rooms[direction] = room
            self.connectors.append((connector, actions[0]))

    def connect_rooms(self, direction, room):
        opposite_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        self.add_room(direction, room)
        room.add_room(opposite_direction[direction], self)

    def enter_room(self):
        print self.name
        print
        print self.description
        print
        if len(self.connectors) > 0:
            for connector in self.connectors:
                print "There is a " + connector[0]+ \
                  " that goes " + connector[1]

    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self, direction):
        return self.rooms[direction]

    def process_command(self, command, inventory):
        if command in self.rooms.keys():
            new_room = self.next_room(command)
            return new_room
        elif "get" in command:
            for item in self.items:
                if item.name in command:
                    inventory.add(item)
                    self.items.remove(item)
                    return "You picked up the " + item.name + "."
                continue
            else:
                    return "I don't know what you want to pick up."
        else:
            return None

