class DoubleLLNode(object):
  def __init__(self, key=None, value=None):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None


class LRUCache(object):

  def __init__(self, capacity):
    # Initialize class variables
    self.dic = {}
    self.head = None
    self.tail = None
    self.cap = capacity

  def print_ll(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.key, end=' ')
      tmp = tmp.next
    print()

  def get(self, key):
    # Retrieve item from provided key. Return -1 if nonexistent.
    if key not in self.dic:
      return -1

    node = self.dic[key]
    if node != self.tail:
      self.move_node_to_end(node)
    return node.value

  def move_node_to_end(self, node):
    prev = node.prev
    next = node.next
    if prev is not None:
      prev.next = next
    else:
      if next is not None:
        self.head = next
    if next is not None:
      next.prev = prev
    self.tail.next = node
    node.prev = self.tail
    node.next = None
    self.tail = node

  def set(self, key, value):
    # Set the value if the key is not present in the cache. If the cache is
    # at capacity remove the oldest item.
    if len(self.dic) == self.cap:
      del self.dic[self.head.key]
      self.head = self.head.next
      self.head.prev = None

    if key in self.dic:
      node = self.dic[key]
      node.value = value
      self.move_node_to_end(node)
    else:
      node = DoubleLLNode(key, value)
      self.dic[key] = node
      if self.head is None:
        self.head = node
        self.tail = node
      else:
        self.tail.next = node
        node.prev = self.tail
        self.tail = node


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
print(our_cache.get(1))
# returns -1 because the cache reached it's capacity and 3 was the least
# recently used entry
