
import sys

import Utilities as Util

def Manager():
    arrayStack =Util.GetAnArrayStack(int(sys.argv[1]))
    for i in range(int(sys.argv[1])):
        arrayStack.push(i);
    Util.PrintStackContent(arrayStack)
    #Util.PrintLinkedList(singlyLinkedList)
    #AppUtil.PrintNewLine()
    #PrintLinkedList(ReverseInRecusion(singlyLinkedList))
    #AppUtil.PrintNewLine()
    #Util.PrintLinkedList(AlgoFunc.ReverseInChunk(singlyLinkedList,int(sys.argv[1])))
    #Util.PrintLinkedList(AlgoFunc.FindModularNode(singlyLinkedList,int(sys.argv[2])))
    #Util.PrintLinkedList(AlgoFunc.GetFractionalNode(singlyLinkedList,int(sys.argv[2])))
    return

Manager()