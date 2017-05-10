import sys
a = [0,0,0,0]
def AllStringNBits(n):
    if n == 0:
        print(a)
        return
    a[n-1] =0    
    AllStringNBits(n-1)
    a[n-1] = 1
    AllStringNBits(n-1)


AllStringNBits(int(sys.argv[1]))