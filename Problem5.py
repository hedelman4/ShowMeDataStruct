import hashlib
import time
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)

    def calc_hash(self, data):
          sha = hashlib.sha256()
          hash_str = data.encode('utf-8')
          sha.update(hash_str)
          return sha.hexdigest()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next
        return out_list

linked_list = LinkedList()

Block0 = Block(datetime.fromtimestamp(time.time()),'Block 0',linked_list.head)
linked_list.append(Block0)

Block1 = Block(datetime.fromtimestamp(time.time()),'Block 1',linked_list.head)
linked_list.append(Block1)

Block2 = Block(datetime.fromtimestamp(time.time()),'Block 2',linked_list.head)
linked_list.append(Block2)

node = linked_list.head
while node:
    print(node.value,node.value.data,node.value.previous_hash,node.value.hash)
    print(node.value.timestamp)
    node = node.next

BlockNum = 2
if BlockNum > len(linked_list.to_list()) - 1 or BlockNum <= 0:
    print('Block does not exist')
else:
    print(linked_list.to_list()[BlockNum])
