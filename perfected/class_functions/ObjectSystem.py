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