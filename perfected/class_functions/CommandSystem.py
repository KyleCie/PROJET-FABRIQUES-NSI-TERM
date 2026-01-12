from typing import Iterable, Iterator, Any
from random import randint

# region Command

class Command:
    """
    Command class, create and manage commands of Objects.
    """

    def __init__(self, objects_names: Iterable[str], max_objects: Iterable[int],
                       number_of_commands: int) -> None:
        """
        Command class, create and manage commands of Objects.
    
        :param objects_names: names of the objects that will be in the commands.
        :type objects_names: Iterable[str]
        :param max_objects: number max of objects that can be in a commands, per objects.
        :type max_objects: Iterable[int]
        :param number_of_commands: the number of commands.
        :type number_of_commands: int
        """

        self.object_names = objects_names
        self.max_objects = max_objects
        self.number_commands = number_of_commands

        self.commands: list[dict[str, int]] = []

        self.__create_commands()
    
    # representation methods

    def __str__(self) -> str:
        """
        str method (eg: str(Command_instance))
        """

        return self.__class__.__name__ + \
               '(object_names="' + str(self.object_names) + ', max_objects="' + \
               str(self.max_objects) + ', number_of_commands="' + str(self.number_commands) + \
               '")'
    
    def __repr__(self):
        """
        representation method (eg: print(Command_instance))
        """

        return self.__class__.__name__ + \
               '(object_names="' + str(self.object_names) + ', max_objects="' + \
               str(self.max_objects) + ', number_of_commands="' + str(self.number_commands) + \
               '")'
    
    # integration methods

    def __len__(self) -> int:
        """
        length method.
        """

        return self.commands.__len__()
    
    def __iter__(self) -> Iterator[dict[str, int]]:
        """
        iterator method (eg: for ... in Command_instance)
        """

        for element in self.commands:
            yield element

    def __add__(self, other: "Command") -> "Command":
        """
        add method (eg: foo = Commmand_instance1 + Command_instance2)
        """

        new_c: "Command" = Command(self.object_names, self.max_objects, self.number_commands)
        new_c.commands = self.commands + other.commands

        new_c.object_names = list(set(self.object_names + other.object_names)) # type: ignore
        new_c.max_objects = max(self.max_objects, other.max_objects) # type: ignore
        new_c.number_commands = new_c.commands.__len__()

        return new_c
    
    def __reversed__(self) -> "Command":
        """
        reversed method (eg: foo = reversed(Command_instance))
        """

        new_c: "Command" = Command(self.object_names, self.max_objects, self.number_commands)
        new_c.commands = list(self.commands.__reversed__())

        return new_c
    
    def __contains__(self, value: Any) -> bool:
        """
        contains method (eg: ?)
        """

        return self.commands.__contains__(value)
    
    # comparaison methods

    def __eq__(self, other: object) -> bool:
        """
        equal method (eg: if Command_instance1 == Command_instance2)
        """

        if isinstance(other, Command):
            return other.commands == self.commands and \
                   other.max_objects == self.max_objects and \
                   other.number_commands == self.number_commands and \
                   other.object_names == self.object_names

        if isinstance(other, Iterable):
            return self.commands == list(other) # type: ignore
        
        return NotImplemented
    
    def __ne__(self, other: object) -> bool:
        """
        not equal method (eg: if Queue_instance1 != Queue_instance2 ...)
        For Python 3 only (Python 2 will simply use: not __eq__ method).
        """

        if isinstance(other, Command):
            return not other.commands == self.commands and \
                   not other.max_objects == self.max_objects and \
                   not other.number_commands == self.number_commands and \
                   not other.object_names == self.object_names
        
        if isinstance(other, Iterable):
            return not self.commands == list(other) # type: ignore
        
        return NotImplemented
    
    def __lt__(self, other: object) -> bool:
        """
        less than method (eg: if Command_instance1 < Command_instance2)
        """

        if isinstance(other, Command):
            return self.commands.__len__() < other.commands.__len__()
        
        return NotImplemented

    def __le__(self, other: object) -> bool:
        """
        less or equal than method (eg: if Command_instance1 <= Command_instance2)
        """

        if isinstance(other, Command):
            return self.commands.__len__() <= other.commands.__len__()
        
        return NotImplemented
    
    def __gt__(self, other: object) -> bool:
        """
        greater than method (eg: if Command_instance1 > Command_instance2)
        """

        if isinstance(other, Command):
            return self.commands.__len__() > other.commands.__len__()
        
        return NotImplemented
    
    def __ge__(self, other: object) -> bool:
        """
        greater or equal than (eg: if Command_instance1 >= Command_instance2)
        """
        
        if isinstance(other, Command):
            return self.commands.__len__() >= other.commands.__len__()
        
        return NotImplemented
    
    # bitwise methods

    def __or__(self, other: "Command") -> "Command":
        """
        or method (eg: foo = Command_instance1 | Command_instance2)
        Add the two Queues and removes the duplicates (like a set)
        """

        new_c = Command([], [], 0)
        new_c.commands = self.commands + other.commands
        unique_values = []
        seen = set() # type: ignore #

        for value in new_c.commands:
            if value not in seen:
                seen.add(value) # type: ignore
                unique_values.append(value) # type:ignore

        new_c.commands = unique_values

        return new_c

    def __ror__(self, other: "Command") -> "Command":
        """
        reverse or method (eg: foo = Command_instance2 | Command_instance1)
        Add the two Queues and removes the duplicates (like a set)
        but reversed compared to the __or__ method.
        """

        new_c = Command([], [], 0)
        new_c.commands = other.commands + self.commands
        unique_values = []
        seen = set() # type: ignore #

        for value in new_c.commands:
            if value not in seen:
                seen.add(value) # type: ignore #
                unique_values.append(value) # type: ignore #
        
        new_c.commands = unique_values

        return new_c

    # other methods

    def __hash__(self) -> int:
        """
        hash method (eg: hash(Command_instance))
        """

        return hash(self.__key())
    
    def __sizeof__(self) -> int:
        """
        sizeof method (eg: sys.getsizeof(Command_instance))
        """

        return object.__sizeof__(self) + \
               self.commands.__sizeof__() + \
               self.max_objects.__sizeof__() + \
               self.object_names.__sizeof__()
    
    def __key(self) -> tuple[str, str, str]:
        """
        key function for hash method.
        """

        return (str(self.commands), str(self.max_objects), str(self.object_names))
    
    def __create_commands(self) -> None:
        """
        create commands method to create an 'instance' of commands.
        """

        for _ in range(self.number_commands):
            command: dict[str, int] = {}

            for name, max_n in zip(self.object_names, self.max_objects):
                command[name] = randint(0, max_n)

            self.commands.append(command)

    # functions

    def len(self) -> int:
        """
        len call system
        """
        
        return self.__len__()
    
    def recreate_commands(self) -> None:
        """
        recreate an 'instance' of commands.
        """

        self.commands = []
        self.__create_commands()

    def sub(self) -> dict[str, int] | None:
        """
        return the first value of commands
        return None if it's empty.
        """

        if self.commands != []:
            return self.commands.pop(0)

        return None
    
# endregion