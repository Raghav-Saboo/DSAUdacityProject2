import hashlib
import datetime


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

  def print_chain(self):
    tmp = self
    ind = 0
    while tmp is not None:
      print('Index: ' + str(ind))
      print('Timestamp: ' + str(tmp.timestamp))
      print('Data: ' + tmp.data)
      if tmp.previous_hash is not None:
        print('Prev Hash: ' + tmp.previous_hash)
      print('Hash: ' + tmp.hash)
      print()
      ind = ind + 1
      tmp = tmp.next

  def __repr__(self):
    return 'Block(' + self.timestamp + ' ' + self.data + ' ' + (
        self.previous_hash if self.previous_hash is not None else '') + ' )'


data_list = ['Some info 1', 'Some info 2', 'Some info 3']

head = None
cur = None
ph = None
for i, data in enumerate(data_list):
  block = Block(
      (datetime.date.today() - datetime.timedelta(
          days=len(data_list) - i)).strftime("%Y-%m-%dT%H:%M:%S.%f%Z"), data,
      ph)
  ph = block.hash
  if head is None:
    head = cur = block
  else:
    cur.next = block
    block.previous_hash = cur.hash
    cur = block

head.print_chain()
