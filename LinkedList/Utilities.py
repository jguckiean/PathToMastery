import Model


def PrintNewLine():
    print('\n')
    return

def CreateSinglyLinkedList(n):
    head = Model.LinkedListNode()
    head.value =0
    start = head
    c = 1
    while(c<n):
        newNode = Model.LinkedListNode()
        newNode.value =c
        head.next = newNode
        head = newNode
        c = c+1
    return start

def PrintLinkedList(listHead):
    while(listHead != None):
        print(listHead.value,end=' ')
        listHead = listHead.next
    return      