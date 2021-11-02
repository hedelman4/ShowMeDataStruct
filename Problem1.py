import sys

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity < 1:
            sys.exit(str(capacity) + ' is an invalid cache size')
        else:
            self.items = [0 for _ in range(capacity - 1)]

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.items:
            self.index = self.items.index(key)
            for _ in range(self.index):
                self.items[self.index -_ ] = self.items[self.index -_-1]
            self.items[0] = key

            return key, self.items
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.items:
            for _ in range(len(self.items)-1):
                self.items[-_-1] = self.items[-_-2]
            self.items[0] = value
            return self.items

our_cache = LRU_Cache(6)

print(our_cache.set(1, 1));
print(our_cache.set(2, 2));
print(our_cache.set(3, 3));
print(our_cache.set(4, 4));


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

print(our_cache.set(5, 5))
print(our_cache.set(6, 6))

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache = LRU_Cache(0)

print(our_cache.set(1, 1));
print(our_cache.set(2, 2));
print(our_cache.set(3, 3));
print(our_cache.set(4, 4));


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

print(our_cache.set(5, 5))
print(our_cache.set(6, 6))

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache = LRU_Cache(-1)

print(our_cache.set(1, 1));
print(our_cache.set(2, 2));
print(our_cache.set(3, 3));
print(our_cache.set(4, 4));


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

print(our_cache.set(5, 5))
print(our_cache.set(6, 6))

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
