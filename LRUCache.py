import collections

class LRUCache:
    def __init__(self, capacity: int, faults: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.faults = faults

    def set(self, key:int, value:int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
            self.faults += 1


capacity = input("Capacity: ")
capacity = int(capacity) - 1

faults = 0

cache = LRUCache(capacity, faults)

traceString = input("Trace (Example: 1 2 3): ")
trace = [int(s) for s in traceString.split(' ')]

for x in trace:
    cache.set(trace[x], trace[x])

print("Page Faults: ", cache.faults)
