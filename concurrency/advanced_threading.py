import threading

class SharedResource:
    def __init__(self):
        self.resource = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.resource += 1
            print(f"Resource incremented to {self.resource}")

    def decrement(self):
        with self.lock:
            self.resource -= 1
            print(f"Resource decremented to {self.resource}")

def worker_increment(shared):
    for _ in range(10):
        shared.increment()

def worker_decrement(shared):
    for _ in range(10):
        shared.decrement()

def main():
    shared = SharedResource()
    t1 = threading.Thread(target=worker_increment, args=(shared,))
    t2 = threading.Thread(target=worker_decrement, args=(shared,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# main()  # To execute the tasks
