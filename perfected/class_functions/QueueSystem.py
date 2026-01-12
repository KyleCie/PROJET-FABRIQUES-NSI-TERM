from typing import Any, Iterator, Iterable

# region Queue

class Queue:
    """
    Queue class wich represent a classic FIFO buffer.
    Use a simple list for as a buffer (not ideal !).
    """

    def __init__(self) -> None:
        """
        Queue class wich represent a classic FIFO buffer.
        Use a simple list for as a buffer (not ideal !).
        """

        self.buffer: list[Any] = []
        self.end: int = -1

    # representation methods

    def __str__(self) -> str:
        """
        str method (eg: str(Queue_instance))
        """

        return str(self.buffer)

    def __repr__(self) -> str:
        """
        representation method (eg: print(Queue_instance))
        """

        return self.__class__.__name__ + \
               '(' + str(self.__len__()) + ' elements)'

    # integration methods

    def __len__(self) -> int:
        """
        length method.
        """

        return self.end+1

    def __iter__(self) -> Iterator[Any]:
        """
        iterator method (eg: for ... in Queue_instance)
        """

        for elem in self.buffer:
            yield elem

    def __add__(self, other: "Queue") -> "Queue":
        """
        add method (eg: foo = Queue_instance1 + Queue_instance2)
        """

        new_q: "Queue" = Queue()
        new_q.__set_buffer(self.buffer + other.buffer)
        new_q.end    = new_q.buffer.__len__()

        return new_q

    def __reversed__(self) -> "Queue":
        """
        reversed method (eg: foo = reversed(Queue_instance))
        """

        n_q: "Queue" = Queue()
        n_q.buffer = self.buffer.__reversed__() # type: ignore

        return n_q

    def __contains__(self, value: Any) -> bool:
        """
        contains method (eg: ?)
        """

        return self.buffer.__contains__(value)

    # comparaison methods

    def __eq__(self, other: object) -> bool:
        """
        equal method (eg: if Queue_instance1 == Queue_instance2 ...)
        """

        if isinstance(other, Queue):
            return other.buffer == self.buffer and \
                   other.end    == self.end
        
        if isinstance(other, Iterable):
            return self.buffer == list(other) # type: ignore
        
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        """
        not equal method (eg: if Queue_instance1 != Queue_instance2 ...)
        For Python 3 only (Python 2 will simply use: not __eq__ method).
        It's a weird thingy. - Kyle 18/11/25 22:48
        """

        if isinstance(other, Queue):
            return not other.buffer == self.buffer or \
                   not other.end    == self.end
        
        if isinstance(other, Iterable):
            return not self.buffer == list(other) # type: ignore
        
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        """
        less than method (eg: if Queue_instance1 < Queue_instance2)
        """

        if isinstance(other, Queue):
            return self.end < other.end
        
        return NotImplemented

    def __le__(self, other: object) -> bool:
        """
        less or equal than method (eg: if Queue_instance1 <= Queue_instance2)
        """

        if isinstance(other, Queue):
            return self.end <= other.end
        
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        """
        greater than method = (eg: if Queue_instance1 > Queue_instance2)
        """

        if isinstance(other, Queue):
            return self.end > other.end
        
        return NotImplemented
    
    def __ge__(self, other: object) -> bool:
        """
        greater or equal than method = (eg: if Queue_instance1 > Queue_instance2)
        """

        if isinstance(other, Queue):
            return self.end >= other.end
        
        return NotImplemented

    # bitwise methods

    def __or__(self, other: "Queue") -> "Queue":
        """
        or method (eg: foo = Queue_instance1 | Queue_instance2)
        Add the two Queues and removes the duplicates (like a set)
        """

        new_q = Queue()
        new_q.__set_buffer(self.buffer + other.buffer) 
        unique_values = []
        seen = set() # type: ignore #

        for value in new_q.buffer:
            if value not in seen:
                seen.add(value) # type: ignore #
                unique_values.append(value) # type: ignore #

        new_q.buffer = unique_values

        return new_q

    def __ror__(self, other: "Queue") -> "Queue":
        """
        reverse or method (eg: foo = Queue_instance2 | Queue_instance1)
        Add the two Queues and removes the duplicates (like a set)
        but reversed compared to the __or__ method.
        """
        
        new_q = other + self # reversed here.
        unique_values = []
        seen = set() # type: ignore #

        for value in new_q.buffer:
            if value not in seen:
                seen.add(value) # type: ignore #
                unique_values.append(value) # type: ignore #

        new_q.buffer = unique_values

        return new_q

    # other methods

    def __hash__(self) -> int:
        """
        hash method (eg: hash(Queue_instance))
        """

        return hash(self.__key())

    def __sizeof__(self) -> int:
        """
        sizeof method (eg: sys.getsizeof(Queue_instance))
        """

        return object.__sizeof__(self) + \
               self.buffer.__sizeof__() + \
               self.end.__sizeof__()

    def __new__(cls) -> "Queue":
        """
        new method (eg: Queue_instance())
        Not useful for this class.
        """

        return super(Queue, cls).__new__(cls)

    def __key(self) -> tuple[str, int, int]:
        """
        key function for hash method.
        """

        return (str(self.buffer), self.end, self.__sizeof__())

    def __set_buffer(self, buffer: list[Any]) -> None:
        """
        set buffer method to set the buffer of the class.
        """

        self.buffer = buffer
        self.end = buffer.__len__()

    # functions.

    def len(self) -> int:
        """
        len call system
        """

        return self.__len__()

    def add(self, value: Any) -> None:
        """
        store the value `value` in the Queue.
        """

        self.buffer.append(value)
        self.end += 1

    def madd(self, value: Iterable[Any]) -> None:
        """
        store the values of `value` iterator in the Queue.
        """

        self.buffer.extend(value)
        self.end = self.buffer.__len__()

    def sub(self) -> Any:
        """
        return the first value of the Queue
        return None if it's empty.
        """

        if not self.is_empty():
            self.end -= 1
            return self.buffer.pop(0)

        return None

    def is_empty(self) -> bool:
        """
        return a bool if the Queue is empty.
        """

        return self.end == -1

    def remove(self, element: Any, time: int) -> None:
        """
        remove `time` times the `element` from the Queue.
        if `time` is greater than the occurences of `element` if the stack,
        it will remove all the occurences of `element`.
        """

        occur = 0
        new_list = []

        for elem in self.buffer:

            if elem == element and occur < time:
                occur += 1

            else:
                new_list.append(elem) # type: ignore #
        
        self.buffer = new_list
        self.end = self.buffer.__len__()

    def count(self, element: Any) -> int:
        """
        return the number of occurences of `element`.
        """

        return self.buffer.count(element)

    def add_queue(self, queue: "Queue") -> None:
        """
        add `queue` Queue into this Queue.
        """

        for element in queue: 
            self.add(element)

#endregion

#region FastQueue

class Chain:
    """
    Chain class, to represent a "chain" / element (from FastQueue)
    """

    def __init__(self, value: Any = None, link: "Chain | None" = None) -> None:
        """
        Chain class, to represent a "chain" / element (from FastQueue)
        
        :param value: The value of the chain
        :type value: Any
        :param link: value to link this chain to other
        :type link: Chain | None
        """

        self.value: Any = value
        self.link: Chain | None = link

    # representation methods

    def __str__(self) -> str:
        """
        str method (eg: str(Chain_instance))
        """

        return str(self.value)

    def __repr__(self) -> str:
        """
        representation method (eg: print(Chain_instance))
        """

        return self.__class__.__name__ + \
               '(value="' + str(self.value) + '", linked=' + \
                ("True" if self.link is not None else "False") + ')'

    # integration methods

    def __len__(self) -> int:
        """
        length method.
        """

        return self.value

    def __iter__(self) -> Iterator[Any]:
        """
        iterator method (eg: for ... in Queue_instance)
        """

        for elem in self.value:
            yield elem

    # comparaison methods.

    def __eq__(self, other: object) -> bool: #type: ignore
        """
        equal method (eg: if Queue_instance1 == Queue_instance2 ...)
        """

        if isinstance(other, Chain):
            return other.value == self.value
        
        return str(self.value) == str(other)

    def __ne__(self, other: object) -> bool:
        """
        not equal method (eg: if Queue_instance1 != Queue_instance2 ...)
        For Python 3 only (Python 2 will simply use: not __eq__ method).
        It's a weird thingy. - Kyle 18/11/25 22:48
        """

        if isinstance(other, Chain):
            return not other.value == self.value
        
        return not str(self.value) == str(other)

    def __lt__(self, other: object) -> bool:
        """
        less than method (eg: if Queue_instance1 < Queue_instance2)
        """

        if isinstance(other, Chain):
            if isinstance(self.value, type(other.value)):
                return self.value < other.value
            
        return NotImplemented

    def __le__(self, other: object) -> bool:
        """
        less or equal than method (eg: if Queue_instance1 <= Queue_instance2)
        """

        if isinstance(other, Chain):
            if isinstance(self.value, type(other.value)):
                return self.value <= other.value
            
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        """
        greater than method = (eg: if Queue_instance1 > Queue_instance2)
        """

        if isinstance(other, Chain):
            if isinstance(self.value, type(other.value)):
                return self.value > other.value
            
        return NotImplemented
    
    def __ge__(self, other: object) -> bool:
        """
        greater or equal than method = (eg: if Queue_instance1 > Queue_instance2)
        """

        if isinstance(other, Chain):
            if isinstance(self.value, type(other.value)):
                return self.value >= other.value
            
        return NotImplemented

    # other methods

    def __hash__(self) -> int:
        """
        hash method (eg: hash(Queue_instance))
        """

        return hash(self.__key())

    def __sizeof__(self) -> int:
        """
        sizeof method (eg: sys.getsizeof(Queue_instance))
        """

        return object.__sizeof__(self) + \
               self.value.__sizeof__() + \
               self.link.__sizeof__()

    def __key(self) -> tuple[str, str, int]:
        """
        key function for hash method.
        """

        return (str(self.value), str(self.link), self.__sizeof__())

    # functions.

    def len(self) -> int:
        """
        len call system
        """

        return self.__len__()

    def set_link(self, link: "Chain | None") -> None:
        """
        set the link of Chain instance.
        """

        self.link = link

    def set_value(self, value: Any | None) -> None:
        """
        set the value of Chain instance.
        """

        self.value = value

    def get_link(self) -> "Chain | None":
        """
        return the link.
        """

        return self.link

    def get_value(self) -> Any:
        """
        return the value.
        """

        return self.value

class FastQueue:
    """
    FastQueue: like the Queue class, but with a linked chains
    system.
    """

    def __init__(self) -> None:
        """
        FastQueue: like the Queue class, but with a linked chains
        system.
        """

        self.head: Chain = Chain()
        self.tail: Chain | None = None
        self.length: int = 0

    # representation methods

    def __str__(self) -> str:
        """
        str method (eg: str(FastQueue_instance))
        """

        repr_chains: str = ""
        chain: Chain | None = self.head

        while chain is not None:
            repr_chains += str(chain)
            chain = chain.get_link()

            if chain is not None:
                repr_chains += "->"

        return self.__class__.__name__ + \
               '(' + repr_chains + ')'

    def __repr__(self) -> str:
        """
        representation method (eg: print(FastQueue_instance))
        """
        
        return self.__class__.__name__ + \
               '(' + str(self.length) + ' elements)'

    # integration methods

    def __len__(self) -> int:
        """
        length method.
        """

        return self.length

    def __iter__(self) -> Iterator[Any]:
        """
        iterator method (eg: for ... in FastQueue_instance)
        """

        chain: Chain | None = self.head

        while chain is not None:
            yield chain.get_value()
            chain = chain.get_link()

    def __add__(self, other: "FastQueue") -> "FastQueue":
        """
        add method (eg: foo = FastQueue_instance1 + FastQueue_instance2)
        """

        lc: "FastQueue" = FastQueue()
        lc.madd(self)
        lc.madd(other)
        return lc

    def __reversed__(self) -> "FastQueue":
        """
        reversed method (eg: foo = reversed(FastQueue_instance))
        """

        e_l = []

        for element in self:
            e_l.append(element) # type: ignore

        e_l.reverse()
        lc = FastQueue()
        lc.madd(e_l) # type: ignore

        return lc

    def __contains__(self, value: Any) -> bool:
        """
        contains method (eg: ?)
        """

        return self.count(value) != 0

    # comparaison methods.

    def __eq__(self, other: object) -> bool: #type: ignore
        """
        equal method (eg: if FastQueue_instance1 == FastQueue_instance2 ...)
        """

        if isinstance(other, FastQueue):
            if other.length != self.length:
                return False
            
            cond_list = []

            for o_e, s_e in zip(self, other):
                cond_list.append(o_e == s_e) # type: ignore

            return all(cond_list) # type: ignore
        
        if isinstance(other, Iterable):
            if len(other) != self.length: # type: ignore
                return False
            
            cond_list = []

            for o_e, s_e in zip(self, other): # type: ignore
                cond_list.append(o_e == s_e)# type: ignore

            return all(cond_list)# type: ignore
        
        return NotImplemented 

    def __ne__(self, other: object) -> bool:
        """
        not equal method (eg: if FastQueue_instance1 != FastQueue_instance2 ...)
        For Python 3 only (Python 2 will simply use: not __eq__ method).
        It's a weird thingy. - Kyle 18/11/25 22:48
        """

        if isinstance(other, FastQueue):
            if other.length != self.length:
                return True
            
            cond_list = []

            for o_e, s_e in zip(self, other):
                cond_list.append(o_e != s_e) # type: ignore

            return not all(cond_list) # type: ignore
        
        if isinstance(other, Iterable):
            if len(other) != self.length: # type: ignore
                return True
            
            cond_list = []

            for o_e, s_e in zip(self, other): # type: ignore
                cond_list.append(o_e != s_e) # type: ignore

            return all(cond_list) # type: ignore
        
        return NotImplemented 

    def __lt__(self, other: object) -> bool:
        """
        less than method (eg: if FastQueue_instance1 < FastQueue_instance2)
        """

        if isinstance(other, FastQueue):
            return other.length > self.length
        
        return NotImplemented 

    def __le__(self, other: object) -> bool:
        """
        less or equal than method (eg: if FastQueue_instance1 <= FastQueue_instance2)
        """
        
        if isinstance(other, FastQueue):
            return other.length >= self.length
        
        return NotImplemented 

    def __gt__(self, other: object) -> bool:
        """
        greater than method = (eg: if FastQueue_instance1 > FastQueue_instance2)
        """

        if isinstance(other, FastQueue):
            return other.length < self.length
        
        return NotImplemented 
    
    def __ge__(self, other: object) -> bool:
        """
        greater or equal than method = (eg: if FastQueue_instance1 > FastQueue_instance2)
        """

        if isinstance(other, FastQueue):
            return other.length <= self.length
        
        return NotImplemented 

    # other methods

    def __hash__(self) -> int:
        """
        hash method (eg: hash(FastQueue_instance))
        """

        return hash(self.__key())

    def __sizeof__(self) -> int:
        """
        sizeof method (eg: sys.getsizeof(FastQueue_instance))
        """

        return object.__sizeof__(self) + \
               sum([e_c.__sizeof__() for e_c in self]) + \
               self.length.__sizeof__()

    def __new__(cls) -> "FastQueue":
        """
        new method (eg: FastQueue_instance())
        Not useful for this class.
        """

        return super(FastQueue, cls).__new__(cls)

    def __key(self) -> tuple[str, int, int]:
        """
        key function for hash method.
        """

        return (str([e_c for e_c in self]), self.length, self.__sizeof__())

    # functions.

    def len(self) -> int:
        """
        len call system
        """

        return self.__len__()

    def is_empty(self) -> bool:
        """
        return a bool if the FastQueue is empty.
        """

        return self.length == 0
    
    def count(self, element: Any) -> int:
        """
        return the number of occurences of `element`.
        """

        count: int = 0

        for e in self:
            if element == e:
                count += 1

        return count

    def add(self, value: Any) -> None:
        """
        store the value `value` in the FastQueue.
        """

        if self.tail is None and self.head.get_value() == None:
            self.head.set_value(value)
            self.tail = self.head.get_link()

        elif self.tail is None:
            self.head.set_link(Chain(value=value))
            self.tail = self.head.get_link()

        else:
            self.tail.set_link(Chain(value=value))
            self.prev_tail = self.tail
            self.tail = self.tail.get_link()

        self.length += 1

    def madd(self, value: Iterable[Any]) -> None:
        """
        store the values of `value` iterator in the FastQueue.
        """

        for e in value:
            self.add(e)

    def sub(self) -> Any:
        """
        return the first value of the FastQueue
        return None if it's empty.
        """

        if not self.is_empty() and self.tail is not None:
            self.length -= 1
            value = self.head

            if self.head.get_link() is not None:
                self.head = self.head.get_link() # type: ignore
            else:
                self.head = Chain()

            return value
        
        return None

    def remove(self, element: Any, time: int) -> None:
        """
        remove `time` times the `element` from the FastQueue.
        if `time` is greater than the occurences of `element` if the stack,
        it will remove all the occurences of `element`.
        """

        occur = 0
        lc = FastQueue()

        for elem in self:

            if elem == element and occur < time:
                occur += 1
            else:
                lc.add(elem)

        self.head = lc.head
        self.tail = lc.tail
        self.length = lc.length

    def add_queue(self, fast_queue: "FastQueue") -> None:
        """
        add `fast_queue` FastQueue into this FastQueue.
        """

        for element in fast_queue:
            self.add(element)

#endregion