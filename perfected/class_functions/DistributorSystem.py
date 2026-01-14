from typing import Any, Iterator

class Distributor:
    """
    Distributor class, represent the gestion of the business.
    """

    def __init__(self, objects_names: tuple[str, ...], time_to_create: float | int,
                       commands: dict[str, int]) -> None:
        """
        Distributor class, represent the gestion of the business.

        :param objects_names: The name's of the objects.
        :type objects_names: tuple[str, ...]
        :param time_to_create: the time to create an object.
        :type time_to_create: float | int
        :param commands: commands to do.
        :type commands: dict[str, int]
        """

        self.objects_names = objects_names
        self.time_to_create = time_to_create
        self.commands = commands

    # representation methods

    def __str__(self) -> str:
        """
        str method (eg: str(Factory_instance))
        """

        return self.__class__.__name__ + \
               '(objects_names="' + str(self.objects_names) + ', time_to_create="' + \
               str(self.time_to_create) + '")'
    
    def __repr__(self) -> str:
        """
        representation method (eg: print(Factory_instance))
        """

        return self.__class__.__name__ + \
               '(objects_names="' + str(self.objects_names) + ', time_to_create="' + \
               str(self.time_to_create) + '")'

    # integration methods

    def __len__(self) -> int:
        """
        length method.
        """

        return NotImplemented

    def __iter__(self) -> Iterator[dict[str, int]]:
        """
        iterator method (eg: for ... in Factory_instance)
        """

        return NotImplemented

    def __add__(self, other: "Distributor") -> "Distributor":
        """
        add method (eg: foo = Factory_instance1 + Factory_instance2)
        """

        return NotImplemented
    
    def __reversed__(self) -> "Distributor":
        """
        reversed method (eg: foo = reversed(Factory_instance))
        """

        return NotImplemented
    
    def __contains__(self, value: Any) -> bool:
        """
        contains method (eg: value in Factory_instance)
        """

        if isinstance(value, tuple):
            return value == self.objects_names
        
        if isinstance(value, str):
            return value in self.objects_names
        
        if isinstance(value, float) or isinstance(value, int):
            return value == self.time_to_create
        
        return NotImplemented

    # comparaison methods

    def __eq__(self, other: object) -> bool:
        """
        equal method (eg: if Factory_instance1 == Factory_instance2)
        """

        if isinstance(other, Distributor):
            return other.objects_names == self.objects_names and \
                   other.time_to_create == self.time_to_create

        if isinstance(other, tuple):
            return self.objects_names == other
        
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        """
        not equal method (eg: if Queue_instance1 != Queue_instance2 ...)
        For Python 3 only (Python 2 will simply use: not __eq__ method).
        """

        if isinstance(other, Distributor):
            return not other.objects_names == self.objects_names and \
                   not other.time_to_create == self.time_to_create

        if isinstance(other, tuple):
            return not self.objects_names == other
        
        return NotImplemented
    
    def __lt__(self, other: object) -> bool:
        """
        less than method (eg: if Factory_instance1 < Factory_instance2)
        """
        
        return NotImplemented

    def __le__(self, other: object) -> bool:
        """
        less or equal than method (eg: if Factory_instance1 <= Factory_instance2)
        """
        
        return NotImplemented
    
    def __gt__(self, other: object) -> bool:
        """
        greater than method (eg: if Factory_instance1 > Factory_instance2)
        """
        
        return NotImplemented
    
    def __ge__(self, other: object) -> bool:
        """
        greater or equal than (eg: if Factory_instance1 >= Factory_instance2)
        """
        
        return NotImplemented

    # bitwise methods

    def __or__(self, other: "Distributor") -> "Distributor":
        """
        or method (eg: foo = Factory_instance1 | Factory_instance2)
        Add the two Queues and removes the duplicates (like a set)
        """

        return NotImplemented

    def __ror__(self, other: "Distributor") -> "Distributor":
        """
        reverse or method (eg: foo = Factory_instance2 | Factory_instance1)
        Add the two Queues and removes the duplicates (like a set)
        but reversed compared to the __or__ method.
        """

        return NotImplemented
    
    # other methods

    def __hash__(self) -> int:
        """
        hash method (eg: hash(Factory_instance))
        """

        return hash(self.__key())
    
    def __sizeof__(self) -> int:
        """
        sizeof method (eg: sys.getsizeof(Factory_instance))
        """

        return object.__sizeof__(self) + \
               self.objects_names.__sizeof__() + \
               self.time_to_create.__sizeof__()
    
    def __key(self) -> tuple[str, str]:
        """
        key function for hash method.
        """

        return (str(self.objects_names), str(self.time_to_create))

    # functions

    def len(self) -> int:
        """
        len call system
        """

        return self.__len__()
    
    def do_commands(self) -> None:
        """
        Do the commands for the clients.
        """

        # TODO: do this function brother.
        pass