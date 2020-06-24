import threading

"""This exercise shows how two separate threads can work on the same piece of shared data without entering the 'data
race' and continue to perform the task concurrently"""

# instantiation of the Lock, which prevents one of the threads from accessing a piece of shared memory
lock = threading.Lock()
counter = 0

def add_entities():
    global counter
    # acquire/release construction isolates a piece of memory and prevents data race between threads
    lock.acquire()
    for i in range(10_000_000):
        counter += 1
        print(counter)
    lock.release()

if __name__ == '__main__':
    # the 'target' attribute should not contain () at the end
    thread_one = threading.Thread(target=add_entities)
    thread_two = threading.Thread(target=add_entities)
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()