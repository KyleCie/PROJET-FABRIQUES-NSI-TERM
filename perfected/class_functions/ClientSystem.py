from typing import Any, Iterator

class Client:
    """
    Client class, contains informations of the client, and his command.
    Have also a status of his command.
    """

    def __init__(self, firstname: str, lastname: str, address: str, 
                       command: dict[str, int], status: str) -> None:
        """
        Client class, contains informations of the client, and his command.
        Have also a status of his command.

        :param firstname: Firstname's client
        :type firstname: str
        :param lastname: Lastname's client
        :type lastname: str
        :param address: Address's client
        :type address: str
        :param command: Command's client
        :type command: dict[str, int]
        :param status: Status of his command.
        :type status: 
        :return: None
        :rtype: None
        """

        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        
        self.command = command
        self.status = status

    # representation methods

    def __str__(self) -> str:
        """
        str method (eg: str(Factory_instance))
        """

        return self.__class__.__name__ + \
               '(firstname="' + self.firstname + ', lastname="' + self.lastname + \
               ", address=" + self.address + ", command=" + str(self.command) + ", status=" + \
               self.status + '")'
    
    def __repr__(self):
        """
        representation method (eg: print(Factory_instance))
        """

        return self.__class__.__name__ + \
               '(firstname="' + self.firstname + ', lastname="' + self.lastname + \
               ", address=" + self.address + ", command=" + str(self.command) + ", status=" + \
               self.status + '")'

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

    def __add__(self, other: "Client") -> "Client":
        """
        add method (eg: foo = Factory_instance1 + Factory_instance2)
        """

        return NotImplemented
    
    def __reversed__(self) -> "Client":
        """
        reversed method (eg: foo = reversed(Factory_instance))
        """

        return NotImplemented
    
    def __contains__(self, value: Any) -> bool:
        """
        contains method (eg: value in Client_instance)
        """

        if isinstance(value, str):
            return value in self.command
        
        return NotImplemented
    
    # comparaison methods

    def __eq__(self, other: object) -> bool:
        """
        equal method (eg: if Factory_instance1 == Factory_instance2)
        """

        if isinstance(other, Client):
            return other.firstname == self.firstname and \
                   other.lastname == self.lastname and \
                   other.address == self.address and \
                   other.status == self.status

        if isinstance(other, str):
            return other == self.firstname or \
                   other == self.lastname or \
                   other == self.address or \
                   other == self.status
        
        if isinstance(other, dict):
            return other == self.command
        
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        """
        not equal method (eg: if Queue_instance1 != Queue_instance2 ...)
        For Python 3 only (Python 2 will simply use: not __eq__ method).
        """

        if isinstance(other, Client):
            return not other.firstname == self.firstname and \
                   not other.lastname == self.lastname and \
                   not other.address == self.address and \
                   not other.status == self.status

        if isinstance(other, str):
            return not other == self.firstname or \
                   not other == self.lastname or \
                   not other == self.address or \
                   not other == self.status
        
        if isinstance(other, dict):
            return not other == self.command
        
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        """
        less than method (eg: if Command_instance1 < Command_instance2)
        """
        
        return NotImplemented

    def __le__(self, other: object) -> bool:
        """
        less or equal than method (eg: if Command_instance1 <= Command_instance2)
        """
        
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        """
        greater than method (eg: if Command_instance1 > Command_instance2)
        """
        
        return NotImplemented
    
    def __ge__(self, other: object) -> bool:
        """
        greater or equal than (eg: if Command_instance1 >= Command_instance2)
        """
        
        return NotImplemented

    # bitwise methods

    def __or__(self, other: "Client") -> "Client":
        """
        or method (eg: foo = Command_instance1 | Command_instance2)
        Add the two Queues and removes the duplicates (like a set)
        """

        return NotImplemented

    def __ror__(self, other: "Client") -> "Client":
        """
        reverse or method (eg: foo = Command_instance2 | Command_instance1)
        Add the two Queues and removes the duplicates (like a set)
        but reversed compared to the __or__ method.
        """

        return NotImplemented
    
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
               self.firstname.__sizeof__() + \
               self.lastname.__sizeof__() + \
               self.address.__sizeof__() + \
               self.command.__sizeof__() + \
               self.status.__sizeof__()
    
    def __key(self) -> tuple[str, str, str, str, str]:
        """
        key function for hash method.
        """

        return (self.firstname, self.lastname, self.address, str(self.command), 
                self.status)

    # functions

    def len(self) -> int:
        """
        len call system
        """

        return self.__len__()

    def get_firstname(self) -> str:
        """
        Get the firstname of the client.
        """

        return self.firstname
    
    def get_lastname(self) -> str:
        """
        Get the lastname of the client.
        """

        return self.lastname
    
    def get_address(self) -> str:
        """
        Get the address of the client.
        """

        return self.address

    def get_command(self) -> dict[str, int]:
        """
        Get the command of the client.
        """

        return self.command

    def get_status(self) -> str:
        """
        Get the status of the command's client.
        """

        return self.status

    def set_firstname(self, firstname: str) -> None:
        """
        Change the firstname of the client (Can't be when transit !).
        """

        if self.status == "in transit":
            raise PermissionError("Can't change the firstname when the command" \
                                  "is in transit !")
        
        self.firstname = firstname

    def set_lastname(self, lastname: str) -> None:
        """
        Change the lastname of the client (Can't be when transit !).
        """

        if self.status == "in transit":
            raise PermissionError("Can't change the lastname when the command" \
                                  "is in transit !")
        
        self.lastname = lastname

    def set_address(self, address: str) -> None:
        """
        Change the address of the client (Can't be when transit !).
        """

        if self.status == "in transit":
            raise PermissionError("Can't change the address when the command" \
                                  "is in transit !")
        
        self.address = address

    def set_command(self, command: dict[str, int]) -> None:
        """
        Change the command of the client (Can't be when transit !).
        """

        if self.status == "in transit":
            raise PermissionError("Can't change the command when the command" \
                                  "is in transit !")
        
        self.command = command


    def set_status(self, status: str) -> None:
        """
        Change the status of address's client.
        """
    
        self.status = status