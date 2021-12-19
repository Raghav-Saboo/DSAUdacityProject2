import sys
import heapq as hq


class Node(object):
  def __init__(self, key=None, value=None):
    self.key = key
    self.value = value
    self.left = None
    self.right = None

  def __lt__(self, other):
    return self.value < other.value


def traverse_tree(node, curr_path, enc_val):
  if node is None:
    return
  if node.left is None and node.right is None:
    enc_val[node.key] = curr_path
  traverse_tree(node.left, curr_path + '0', enc_val)
  traverse_tree(node.right, curr_path + '1', enc_val)


def huffman_encoding(data):
  fq = {}
  for char in data:
    if char not in fq:
      fq[char] = 0
    fq[char] += 1
  fq_list = []
  for char, fq in fq.items():
    fq_list.append(Node(char, fq))
  hq.heapify(fq_list)
  while len(fq_list) > 1:
    node1 = hq.heappop(fq_list)
    if len(fq_list) == 0:
      break
    node2 = hq.heappop(fq_list)
    par = Node('', node1.value + node2.value)
    par.left = node1
    par.right = node2
    hq.heappush(fq_list, par)
  root = hq.heappop(fq_list)
  enc_val = {}
  traverse_tree(root, '', enc_val)
  ans = ''
  for char in data:
    ans += enc_val[char]
  return ans, root


def huffman_decoding(data, root):
  enc_val = {}
  traverse_tree(root, '', enc_val)
  rv_enc_val = {}
  for char, ev in enc_val.items():
    rv_enc_val[ev] = char
  ans = ''
  cur = ''
  for char in data:
    cur += char
    if cur in rv_enc_val:
      ans += rv_enc_val[cur]
      cur = ''
  return ans


if __name__ == "__main__":
  codes = {}

  a_great_sentence = "The bird is the word"

  print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
  print("The content of the data is: {}\n".format(a_great_sentence))

  encoded_data, tree = huffman_encoding(a_great_sentence)

  print("The size of the encoded data is: {}\n".format(
      sys.getsizeof(int(encoded_data, base=2))))
  print("The content of the encoded data is: {}\n".format(encoded_data))

  decoded_data = huffman_decoding(encoded_data, tree)

  print(
      "The size of the decoded data is: {}\n".format(
          sys.getsizeof(decoded_data)))
  print("The content of the encoded data is: {}\n".format(decoded_data))
