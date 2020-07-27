import codecs
import collections

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.faults = 1
        self.hits = -1

    def set(self, key:int, value:int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) < self.capacity:
            self.faults += 1
        elif len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
            self.faults += 1
        else:
            self.hits += 1

trials = input("Trials: ")
trials = int(trials)

trace = []

with codecs.open("multi2.trc", "r", "UTF8") as inputFile:
    inputFile=inputFile.readlines()
for line in inputFile:
    trace.append(int(line))

# traceString = input("Trace: ")
# trace = [int(s) for s in traceString.strip().split()]

for i in range(trials):
    capacity = input("Capacity: ")
    capacity = int(capacity)
    cache = LRUCache(capacity)

    for j in range(len(trace)):
        cache.set(trace[j], trace[j])

    print("Page Hits: ", cache.hits)
    print("Page Faults: ", cache.faults)