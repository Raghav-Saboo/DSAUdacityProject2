import hashlib
import datetime


class BlockChain:
  def __init__(self):
    self.head = None
    self.lenb = 0

  def print_chain(self):
    tmp = self.head
    ind = self.lenb
    while tmp is not None:
      print('Index: ' + str(ind))
      print('Timestamp: ' + str(tmp.timestamp))
      print('Data: ' + tmp.data)
      if tmp.previous_hash is not None:
        print('Prev Hash: ' + tmp.previous_hash)
      print('Hash: ' + tmp.hash)
      print()
      ind = ind - 1
      tmp = tmp.next

  def add_block(self, data):
    self.lenb += 1
    block = Block(
        (datetime.date.today() - datetime.timedelta(
            days=len(data_list) - i)).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"), data,
        None if self.head is None else self.head.hash)
    if self.head is None:
      self.head = block
    else:
      block.next = self.head
      block.previous_hash = self.head.hash
      self.head = block


class Block:

  def __init__(self, timestamp, data, previous_hash):
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()
    self.next = None

  def calc_hash(self):
    sha = hashlib.sha256()
    sha.update(self.__repr__().encode())
    return sha.hexdigest()

  def __repr__(self):
    return 'Block(' + self.timestamp + ' ' + self.data + ' ' + (
        self.previous_hash if self.previous_hash is not None else '') + ' )'


data_list = ['Some info 1', 'Some info 2', 'Some info 3']

head = None
cur = None
ph = None

b1 = BlockChain()

for i, data in enumerate(data_list):
  b1.add_block(data)
b1.print_chain()

# test statements
b1 = BlockChain()
b1.print_chain()  # should print empty because there is no block in b1 chain

b2 = BlockChain()
b2.add_block("one")
print(b2.head.timestamp)
b2.add_block("two")
print(b2.head.timestamp)
b2.add_block("three")
print(
    b2.head.timestamp)  # all the timestamps are same because they are declared at same time (Hrs:Min)
