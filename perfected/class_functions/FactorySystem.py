from typing import Any, Iterator
from time import sleep

try:
    from ObjectSystem import Object
except:
    from .ObjectSystem import Object

# region Factory

class Factory:
    """
    Factory class, create given Object (take time).
    """

    def __init__(self, object_name: Object | str, time_to_create: float | int,
                       ) -> None:
        """
        Factory class, create given Object (take time).
        
        :param object_name: name of the object that will be created from the factory.
        :type object_name: Object | str
        :param time_to_create: the time that will take the factory to create the object.
        :type time_to_create: float | int
        """

        if isinstance(object_name, Object):
            self.object_name = object_name.get_name()
        else:
            self.object_name = object_name

        self.time_to_create = time_to_create

    # representation methods

    def __str__(self) -> str:
        """
        str method (eg: str(Factory_instance))
        """

        return self.__class__.__name__ + \
               '(object_name="' + str(self.object_name) + ', time_to_create="' + \
               str(self.time_to_create) + '")'
    
    def __repr__(self):
        """
        representation method (eg: print(Factory_instance))
        """

        return self.__class__.__name__ + \
               '(object_name="' + str(self.object_name) + ', time_to_create="' + \
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

    def __add__(self, other: "Factory") -> "Factory":
        """
        add method (eg: foo = Factory_instance1 + Factory_instance2)
        """

        return NotImplemented
    
    def __reversed__(self) -> "Factory":
        """
        reversed method (eg: foo = reversed(Factory_instance))
        """

        return NotImplemented
    
    def __contains__(self, value: Any) -> bool:
        """
        contains method (eg: value in Factory_instance)
        """

        if isinstance(value, str):
            return value == self.object_name
        
        if isinstance(value, float) or isinstance(value, int):
            return value == self.time_to_create
        
        return NotImplemented

    # comparaison methods

    def __eq__(self, other: object) -> bool:
        """
        equal method (eg: if Factory_instance1 == Factory_instance2)
        """

        if isinstance(other, Factory):
            return other.object_name == self.object_name and \
                   other.time_to_create == self.time_to_create

        if isinstance(other, str):
            return self.object_name == other 
        
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        """
        not equal method (eg: if Queue_instance1 != Queue_instance2 ...)
        For Python 3 only (Python 2 will simply use: not __eq__ method).
        """

        if isinstance(other, Factory):
            return not other.object_name == self.object_name and \
                   not other.time_to_create == self.time_to_create

        if isinstance(other, str):
            return not self.object_name == other 
        
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

    def __or__(self, other: "Factory") -> "Factory":
        """
        or method (eg: foo = Factory_instance1 | Factory_instance2)
        Add the two Queues and removes the duplicates (like a set)
        """

        return NotImplemented

    def __ror__(self, other: "Factory") -> "Factory":
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
               self.object_name.__sizeof__() + \
               self.time_to_create.__sizeof__()
    
    def __key(self) -> tuple[str, str]:
        """
        key function for hash method.
        """

        return (str(self.object_name), str(self.time_to_create))
    
    # functions

    def len(self) -> int:
        """
        len call system
        """

        return self.__len__()

    def create(self) -> Object:
        """
        create an object and return it.
        """
    
        sleep(self.time_to_create)
        return Object(self.object_name)