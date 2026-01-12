from sys import getsizeof

from .QueueSystem import Queue, FastQueue
from .CommandSystem import Object

def queue_tester():
    """
    Test the majority of Queue class.
    """

    print("> Starting the test...")

    try:
        q_instance1 = Queue()
        q_instance2 = Queue()
        q_instance3 = Queue()
    except Exception as e:
        print("-> ERROR: unable to start due to", e)
        return
    
    print("> Running...")

    try:
        q_instance1.add("test1")
        q_instance2.add("test2")
    except Exception as e:
        print("-> ERROR: unable to add (add func) in the Queue", e)
        return
    
    print("-> 'add' function OK.")

    try:
        q_instance1.madd(["2", "2", "3", "3", "quest"])
        q_instance2.madd(["2", "2", "3", "3", "quest"])
        q_instance3.madd([1, 2, 3, 4])
    except Exception as e:
        print("-> ERROR: unable to do multiple add (madd func) due to", e)
        return
    
    print("-> 'madd' function OK.")

    try:
        result = q_instance1 != q_instance2
    except Exception as e:
        print("-> ERROR: unable to check if the Queues are not the same due to", e)
        return
    
    if result:
        print("-> 'not equal' comparaison OK.")
    else:
        print("-> WARNING: wrong result with the comparaison, error with __ne__ method ?")
    
    try:
        r1 = q_instance1.sub()
        r2 = q_instance2.sub()
    except Exception as e:
        print("-> ERROR: unable to unqueue (sub func) from the Queue due to", e)
        return

    if r1 != "test1":
        print("-> WARNING: wrong result with unqueue (expected 'test1'), got", r1)
    elif r2 != "test2":
        print("-> WARNING: wrong result with unqueue (expected 'test2'), got", r2)
    else:
        print("-> 'sub' function OK.")
    
    try:
        result = q_instance1 == q_instance2
    except Exception as e:
        print("-> ERROR: unable to check if the Queues are the same due to", e)
        return
    
    if result:
        print("-> 'equal' comparaison OK.")
    else:
        print("-> WARNING: wrong result with the comparaison , error with __eq__  method ?")

    try:
        q_instance1.remove("3", 1)
        q_instance2.remove("2", 10)
    except Exception as e:
        print("-> ERROR: unable to remove from the Queue (remove func) due to", e)
        return
    
    if q_instance1 != ["2", "2", "3", "quest"]:
        print("-> WARNING: wrong result with the comparaison, error with __ne__ | remove method ?")
        print("--> q_instance1:", q_instance1)
    elif q_instance2 != ["3", "3", "quest"]:
        print("-> WARNING: wrong result with the comparaison, error with __ne__ | remove method ? ")
        print("--> q_instance2:", q_instance2)
    else:
        print("-> 'remove' function OK.")

    try:
        result = q_instance1 > q_instance2
    except Exception as e:
        print("-> ERROR: unable to do a greater than comparaison due to", e)
        return
    
    if not result:
        print("-> WARNING: wrong result with comparaison, error with __gt__ method ?")
    else:
        print("-> 'greater than' comparaison OK.")

    try:
        result = q_instance2 < q_instance1
    except Exception as e:
        print("-> ERROR: unable to do a less than comparaison due to", e)
        return
    
    if not result:
        print("-> WARNING: wrong result with comparaison, error with __lt__ method ?")
    else:
        print("-> 'less than' comparaison OK.")

    try:
        result = q_instance1 <= q_instance3
    except Exception as e:
        print("-> ERROR: unable to do a less or equal comparaison due to", e)
        return
    
    if not result:
        print("-> WARNING: wrong result with comparaison, error with __le__ method ?")
    else:
        print("-> 'less or equal' comparaison OK.")
    
    try:
        result = q_instance1 >= q_instance3
    except Exception as e:
        print("-> ERROR: unable to do a greater or equal comparaison due to", e)
        return
    
    if not result:
        print("-> WARNING: wrong result with comparaison, error with __ge__ method ?")
    else:
        print("-> 'greater or equal' comparaison OK.")

    try:
        r_instance = q_instance1 | q_instance2
    except Exception as e:
        print("-> ERROR: unable to do a or bitwise for Queues due to", e)
        return
    
    if r_instance != ["2", "3", "quest"]:
        print("-> WARNING: wrong result with or bitwise, error with __or__ | __ror__ method ?")
        print("--> r_instance:", r_instance)
    else:
        print("-> 'or bitwise' function OK.")
    
    try:
        r_hash = hash(r_instance)
        q_hash = hash(q_instance1)
    except Exception as e:
        print("-> ERROR: unable to do a hash to the Queue due to", e)
        return
    
    if r_hash == q_hash:
        print("-> WARNING: wrong result with hash, error with __hash__ | __key method ?")
    else:
        print("-> 'hash' function OK.")

    try:
        r_size = getsizeof(r_instance)
        q_size = getsizeof(q_instance1)
    except Exception as e:
        print("-> ERROR: unable to get the size of Queue due to", e)
        return
    
    if r_size != q_size:
        print("-> WARNING: wrong result with sizes of Queues, error with __sizeof__ method ?")
        print("--> r_instance:", r_instance, ", q_instance1:", q_instance1)
        print("--> r_size:", r_size, ", q_size:", q_size)
    else:
        print("-> 'get size of' function OK.")

    print("> test finished succesfully.")

def fast_queue_tester():
    """
    Test the majority of FastQueue class.
    """

    print("> Starting the test...")

    try:
        q_instance1 = FastQueue()
        q_instance2 = FastQueue()
        q_instance3 = FastQueue()
    except Exception as e:
        print("-> ERROR: unable to start due to", e)
        return
    
    print("> Running...")

    try:
        q_instance1.add("test1")
        q_instance2.add("test2")
    except Exception as e:
        print("-> ERROR: unable to add (add func) in the Queue", e)
        return
    
    print("-> 'add' function OK.")

    try:
        q_instance1.madd(["2", "2", "3", "3", "quest"])
        q_instance2.madd(["2", "2", "3", "3", "quest"])
        q_instance3.madd([1, 2, 3, 4])
    except Exception as e:
        print("-> ERROR: unable to do multiple add (madd func) due to", e)
        return
    
    print("-> 'madd' function OK.")

    try:
        result = q_instance1 != q_instance2
    except Exception as e:
        print("-> ERROR: unable to check if the Queues are not the same due to", e)
        return
    
    if result:
        print("-> 'not equal' comparaison OK.")
    else:
        print("-> WARNING: wrong result with the comparaison, error with __ne__ method ?")
        print("--> q_instance1:", q_instance1)
        print("--> q_instance2:", q_instance2)
    
    try:
        r1 = q_instance1.sub()
        r2 = q_instance2.sub()
    except Exception as e:
        print("-> ERROR: unable to unqueue (sub func) from the Queue due to", e)
        return

    if r1 != "test1":
        print("-> WARNING: wrong result with unqueue (expected 'test1'), got", r1)
    elif r2 != "test2":
        print("-> WARNING: wrong result with unqueue (expected 'test2'), got", r2)
    else:
        print("-> 'sub' function OK.")
    
    try:
        result = q_instance1 == q_instance2
    except Exception as e:
        print("-> ERROR: unable to check if the Queues are the same due to", e)
        return
    
    if result:
        print("-> 'equal' comparaison OK.")
    else:
        print("-> WARNING: wrong result with the comparaison , error with __eq__  method ?")

    try:
        q_instance1.remove("3", 1)
        q_instance2.remove("2", 10)
    except Exception as e:
        print("-> ERROR: unable to remove from the Queue (remove func) due to", e)
        return
    
    if q_instance1 != ["2", "2", "3", "quest"]:
        print("-> WARNING: wrong result with the comparaison, error with __ne__ | remove method ?")
        print("--> q_instance1:", q_instance1)
    elif q_instance2 != ["3", "3", "quest"]:
        print("-> WARNING: wrong result with the comparaison, error with __ne__ | remove method ? ")
        print("--> q_instance2:", q_instance2)
    else:
        print("-> 'remove' function OK.")

    try:
        result = q_instance1 > q_instance2
    except Exception as e:
        print("-> ERROR: unable to do a greater than comparaison due to", e)
        return
    
    if not result:
        print("-> WARNING: wrong result with comparaison, error with __gt__ method ?")
    else:
        print("-> 'greater than' comparaison OK.")

    try:
        result = q_instance2 < q_instance1
    except Exception as e:
        print("-> ERROR: unable to do a less than comparaison due to", e)
        return
    
    if not result:
        print("-> WARNING: wrong result with comparaison, error with __lt__ method ?")
    else:
        print("-> 'less than' comparaison OK.")

    try:
        result = q_instance1 <= q_instance3
    except Exception as e:
        print("-> ERROR: unable to do a less or equal comparaison due to", e)
        return
    
    if not result:
        print("-> WARNING: wrong result with comparaison, error with __le__ method ?")
    else:
        print("-> 'less or equal' comparaison OK.")
    
    try:
        result = q_instance1 >= q_instance3
    except Exception as e:
        print("-> ERROR: unable to do a greater or equal comparaison due to", e)
        return
    
    if not result:
        print("-> WARNING: wrong result with comparaison, error with __ge__ method ?")
    else:
        print("-> 'greater or equal' comparaison OK.")


    r_instance = q_instance1 + q_instance2

    try:
        r_hash = hash(r_instance)
        q_hash = hash(q_instance1)
    except Exception as e:
        print("-> ERROR: unable to do a hash to the Queue due to", e)
        return
    
    if r_hash == q_hash:
        print("-> WARNING: wrong result with hash, error with __hash__ | __key method ?")
    else:
        print("-> 'hash' function OK.")

    try:
        r_size = getsizeof(r_instance)
        q_size = getsizeof(q_instance1)
    except Exception as e:
        print("-> ERROR: unable to get the size of Queue due to", e)
        return
    
    if r_size == q_size:
        print("-> WARNING: wrong result with sizes of Queues, error with __sizeof__ method ?")
        print("--> r_instance:", r_instance, ", q_instance1:", q_instance1)
        print("--> r_size:", r_size, ", q_size:", q_size)
    else:
        print("-> 'get size of' function OK.")

    print("> test finished succesfully.")

def object_tester():
    """
    Test the majority of Object class.
    """
    print("> Starting the test...")

    try:
        o_instance1 = Object("test1")
        o_instance2 = Object("test1")
        o_instance3 = Object("test2")
    except Exception as e:
        print("-> ERROR: unable to start due to", e)
        return

    print("> Running...")

    try:
        result = o_instance1 == o_instance2
    except Exception as e:
        print("-> ERROR: unable to compare the Objects due to", e)
        return

    if result:
        print("-> 'equal' comparaison OK.")
    else:
        print("-> WARNING: wrong result with the comparaison , error with __eq__  method ?")

    try:
        result = o_instance2 != o_instance3
    except Exception as e:
        print("-> ERROR: unable to compare the Objects due to", e)
        return

    if result:
        print("-> 'not equal' comparaison OK.")
    else:
        print("-> WARNING: wrong result with the comparaison , error with __ne__  method ?")

    try:
        r_hash = hash(o_instance2)
        q_hash = hash(o_instance3)
    except Exception as e:
        print("-> ERROR: unable to do a hash to the Queue due to", e)
        return
    
    if r_hash == q_hash:
        print("-> WARNING: wrong result with hash, error with __hash__ | __key method ?")
    else:
        print("-> 'hash' function OK.")

    try:
        r_size = getsizeof(o_instance2)
        q_size = getsizeof(o_instance3)
    except Exception as e:
        print("-> ERROR: unable to get the size of Queue due to", e)
        return

    if r_size != q_size:
        print("-> WARNING: wrong result with sizes of Queues, error with __sizeof__ method ?")
        print("--> o_instance2:", o_instance2, ", o_instance3:", o_instance3)
        print("--> r_size:", r_size, ", q_size:", q_size)
    else:
        print("-> 'get size of' function OK.")

    try:
        result = o_instance2.get_name()
    except Exception as e:
        print("-> ERROR: unable to get the name of the Object due to", e)
        return

    if result != "test1":
        print("WARNING: wrong result with the name of Object, error with get_name method ?")
    else:
        print("-> 'get name' function OK.")

    try:
        o_instance2.set_name("test4")
        result = o_instance2.get_name()
    except Exception as e:
        print("-> ERROR: unable to change the name of the Object due to", e)
        return

    if result != "test4":
        print("WARNING: wrong result with the name of Object, error with get_name | set_name method ?")
    else:
        print("-> 'set name' function OK.")

    print("> test finished succesfully.")

def test():
    """
    Test all the classes.
    """
    queue_tester()
    object_tester()


if __name__ == "__main__":
    object_tester()