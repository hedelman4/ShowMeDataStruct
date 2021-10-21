import sys

class Node(object):
    def __init__(self, value=None, item=None):
        self.value = value
        self.item = item
        self.left = None
        self.right = None
        self.code = ''

    def get_value(self):
        return self.value

    def get_item(self):
        return self.item

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

huffmanList = {}
def huffman_encoding(data):

    nodeList = []
    nodeCount = 0

    for _ in data.lower():
        huffmanList[_] = huffmanList.get(_,0) + 1
    sorted_huffmanList = sorted(huffmanList.items(),key=lambda x: x[1])

    for _ in range(len(sorted_huffmanList)):
        nodePop = sorted_huffmanList.pop(0)
        nodeItem = nodePop[0]
        nodeValue = nodePop[1]
        node = Node(nodeValue, nodeItem)
        nodeList.append(node)
        nodeCount += 1

    nodeIterations(nodeList, data)

    return encodedString

def nodeIterations(nodeList, data):
    newNodeList = []
    while len(nodeList) > 1:
        nodePop1 = nodeList.pop(0)
        nodePop2 = nodeList.pop(0)
        node = Node(nodePop1.value + nodePop2.value)
        node.set_left_child(nodePop1)
        node.set_right_child(nodePop2)
        newNodeList.append(node)

    if len(nodeList) == 1:
        newNodeList.append(nodeList.pop(0))

    if len(newNodeList) > 1:
        nodeIterations(newNodeList, data)

    if len(newNodeList) == 1:
        global root
        root = newNodeList[0]
        global codeDict
        codeDict = {}
        codeDict = encode(root, codeDict)
        global encodedString
        encodedString = ''
        for _ in data.lower():
            encodedString = encodedString + codeDict[_]

def encode(root, codeDict):
    if root.has_left_child():
        root.get_left_child().code = root.code + '0'
        if root.get_left_child().item:
            codeDict[root.get_left_child().item] = root.get_left_child().code
        encode(root.get_left_child(), codeDict)

    if root.has_right_child():
        root.get_right_child().code = root.code + '1'
        if root.get_right_child().item:
            codeDict[root.get_right_child().item] = root.get_right_child().code
        encode(root.get_right_child(), codeDict)

    return codeDict

def huffman_decoding(data):
    decodedString = ''
    if data[0] == 0:
        activeNode = root.get_left_child()
    else:
        activeNode = root.get_left_child()
    for _ in range(len(data)):

        if _+1 == len(data):
            decodedString = decodedString + activeNode.get_item()

        elif data[_+1] == '0':
            if activeNode.has_left_child():
                activeNode = activeNode.get_left_child()
            else:
                decodedString = decodedString + activeNode.get_item()
                activeNode = root.get_left_child()

        elif data[_+1] == '1':
            if activeNode.has_right_child():
                activeNode = activeNode.get_right_child()
            else:
                decodedString = decodedString + activeNode.get_item()
                activeNode = root.get_right_child()
    return decodedString
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
