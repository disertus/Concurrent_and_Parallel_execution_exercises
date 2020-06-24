import threading
import time

"""This exercise shows how to instantiate a thread by inheriting a Thread class and replacing its run() method
It also shows how to .start() a thread and .join() a thread to another one, so that the former waits till the 
latter finishes performing"""

def some_work():
    return [print(f'The child is playing {i}') for i in range(50)]


# threading implementation using 'class instantiation'
class ThreadOne(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('An operation performed by the Child Thread is currently in progress')
        time.sleep(3)
        some_work()
        print('The Child Thread is done.')


if __name__ == '__main__':
    print('The Main Thread is instantiating its Child')
    child_thread = ThreadOne()

    print('The Main Thread tells the Child Thread to start.')
    child_thread.start()

    # despite the child thread being launched, the Main one continues to perform operations, it does not wait
    print('\nThe Main Thread continues to do something of its own')
    time.sleep(1)
    [print(f'Main is doing {i}') for i in range(50)]

    # .join() method makes the main (or another child thread) wait until the child thread finishes its execution
    print('\nMain thread now waits the Child Thread to finish')
    child_thread.join()

    print('Both Main and Child threads are done working.')