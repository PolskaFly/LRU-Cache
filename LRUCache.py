import codecs
import collections

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.faults = 0
        self.hits = 0

    def set(self, key:int, value:int):
        if key in self.cache:
            self.hits += 1
            self.cache.move_to_end(key)
        elif len(self.cache) < self.capacity:
            self.faults += 1
            self.cache[key] = value
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
            self.cache[key] = value
            self.faults += 1


trials = input("Trials: ")
trials = int(trials)

trace = []

with codecs.open("sprite.trc", "r", "UTF8") as inputFile:
    inputFile = inputFile.readlines()
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