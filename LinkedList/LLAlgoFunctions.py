
def ReverseInRecusion(current):
    if current is None:
        return
    if current.next is None:
        return current
    nextNode = current.next
    reverseList = ReverseInRecusion(nextNode)
    nextNode.next = current
    current.next = None
    return reverseList

def ReverseInChunk(head,chunkLength):
    start = head
    flag = False
    for i in range(chunkLength):
        if head.next is None:
            flag = True
            continue
        head = head.next
    temp = start
    temp = ReverseInPart(temp, chunkLength)
    start = temp
    for i in range(chunkLength-1):
        if flag:
            continue
        temp = temp.next
    if not flag:
        temp.next = ReverseInChunk(head, chunkLength)
    return start

def ReverseInPart(head,partLength):
    if(partLength==1 or head.next == None):
        return head
    current = head.next
    reversedList = ReverseInPart(head.next,partLength-1)
    current.next = head
    head.next = None
    return reversedList


def FindModularNode(head,divisor):
    start = head
    length = divisor
    while length > 0:
        if head is None:
            return start
        head = head.next
        length = length - 1
    return FindModularNode(head, divisor)


#get the n/k th node of a linked list where n is the length of the linked list
def GetFractionalNode(head,k):
    fractionalNode = None
    if(k<=0):
        return
    i=0
    while head is not None:
        head = head.next
        if i % k is 0:
            if fractionalNode is None:
                fractionalNode = head
            else:
                fractionalNode = fractionalNode.next
        i = i+1
    return fractionalNode
        



