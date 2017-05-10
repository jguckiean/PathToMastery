import sys

def NQueens(N):
    board = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    
    if(FindNQueensPositions(board,N,N)):
        print(board)
    else:
        print("Not Possible")    

def IsAttacked(board,x,y,length):    
    for s in range(length):
        if board[x][s] ==1:
            return True
        if board[s][y] ==1:
            return True      
    p=x
    q=y
    while p >= 0 and p<length and q>= 0 and q< length:
        if board[p][q] ==1:
            return True
        p = p+1
        q = q-1
    p=x
    q=y
    while p >= 0 and p<length and q>= 0 and q< length:
        if board[p][q] ==1:
            return True
        p = p-1
        q=q+1    
    p=x
    q=y
    while p >=0 and q >=0 :
        if board[p][q] ==1 :
            return True
        p=p-1
        q=q-1

    p=x
    q=y
    while p<length and q<length:
        if board[p][q] ==1:
            return True
        p=p+1
        q=q+1
    return False
    
    
def FindNQueensPositions(board,length,N): 
    
    if N == 0:
        return True
    
    for i in range(length):
        for j in range(length):
            if IsAttacked(board,i,j,length):
                continue
            board[i][j] =1
            if(FindNQueensPositions(board,length,N-1)):                
                return True
            board[i][j] =0
            print
    
    return False        
            
#print(range(int(sys.argv[1])))        
NQueens(int(sys.argv[1]))