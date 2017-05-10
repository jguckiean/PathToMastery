import Model
import Utilities as Util
import LLAlgoFunctions as AlgoFunc

import sys


def Manager():
    singlyLinkedList =Util.CreateSinglyLinkedList(int(sys.argv[1]))
    #Util.PrintLinkedList(singlyLinkedList)
    #AppUtil.PrintNewLine()
    #PrintLinkedList(ReverseInRecusion(singlyLinkedList))
    #AppUtil.PrintNewLine()
    #Util.PrintLinkedList(AlgoFunc.ReverseInChunk(singlyLinkedList,int(sys.argv[1])))
    #Util.PrintLinkedList(AlgoFunc.FindModularNode(singlyLinkedList,int(sys.argv[2])))
    Util.PrintLinkedList(AlgoFunc.GetFractionalNode(singlyLinkedList,int(sys.argv[2])))
    return

Manager()