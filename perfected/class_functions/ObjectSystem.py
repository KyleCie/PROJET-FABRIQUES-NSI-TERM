# region Object

class Object:
    """
    Object class, to represent an Object demand (from commands
    and from Factorys.)
    """

    def __init__(self, name: str) -> None:
        """        
        Object class, to represent an Object demand (from commands
        and from Factorys.)

        :param name: name's object.
        :type name: str
        """

        self.name: str = name
    
    # representation methods

    def __str__(self) -> str:
        """
        str method (eg: str(Objet_instance))
        """

        return self.name
    
    def __repr__(self) -> str:
        """
        representation method (eg: print(Object_instance))
        """

        return self.__class__.__name__ + \
               '(name="' + self.name + '")'

    # comparaison methods.

    def __eq__(self, value: object) -> bool:
        """
        equal method (eg: if Object_instance1 == Object_instance2)
        """

        if isinstance(value, Object):
            return value.name == self.name

        if isinstance(value, str):
            return value == self.name

        return NotImplemented

    def __ne__(self, value: object) -> bool:
        """
        not equal method (eg: if Object_instance1 != Object_instance2)
        For Python 3 only.
        """

        if isinstance(value, Object):
            return not value.name == self.name
        
        if isinstance(value, str):
            return not value == self.name
        
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        """
        less than method (eg: if Object_instance1 < Object_instance2)
        """
        
        return NotImplemented

    def __le__(self, other: object) -> bool:
        """
        less or equal than method (eg: if Object_instance1 <= Object_instance2)
        """
        
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        """
        greater than method (eg: if Object_instance1 > Object_instance2)
        """
        
        return NotImplemented
    
    def __ge__(self, other: object) -> bool:
        """
        greater or equal than (eg: if Object_instance1 >= Object_instance2)
        """
        
        return NotImplemented

    # bitwise methods

    def __or__(self, other: "Object") -> "Object":
        """
        or method (eg: foo = Object_instance1 | Object_instance2)
        Add the two Queues and removes the duplicates (like a set)
        """

        return NotImplemented

    def __ror__(self, other: "Object") -> "Object":
        """
        reverse or method (eg: foo = Object_instance2 | Object_instance1)
        Add the two Queues and removes the duplicates (like a set)
        but reversed compared to the __or__ method.
        """

        return NotImplemented

    # other mehods

    def __hash__(self) -> int:
        """
        hash method (eg: hash(Object_instance))
        """

        return hash(self.__key())
    
    def __sizeof__(self) -> int:
        """
        sizeof method (eg: sys.getsizeof(Object_instance))
        """

        return object.__sizeof__(self) + \
               self.name.__sizeof__()

    def __key(self) -> tuple[str, str]:
        """
        key function for hash method.
        """

        return (str(self), self.name)
    
    # functions.

    def get_name(self) -> str:
        """
        get the name of the Object.
        """

        return self.name
    
    def set_name(self, name: str) -> None:
        """
        Change the name of the Object.
        """

        self.name = name

# endregion