import collections

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.temp = []
        self.faults = 1
        self.hits = -1

    def print_matrix(self) -> None:
        print(self.temp)

    def set(self, key:int, value:int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) < self.capacity:
            self.faults += 1
        elif len(self.cache) > self.capacity:
            print(self.cache.popitem(last=False))
            self.faults += 1
        else:
            self.hits += 1



capacity = input("Capacity: ")
capacity = int(capacity)

cache = LRUCache(capacity)

traceString = input("Trace (Example: 1 2 3): ")
trace = [int(s) for s in traceString.split(' ')]

for i in range(len(trace)):
    cache.set(trace[i], trace[i])
    #cache.print_matrix()

print("Page Hits: ", cache.hits)
print("Page Faults: ", cache.faults)
