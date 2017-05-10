import Model

def GetAnArrayStack(capacity):
    return Model.Stack(capacity)

def TriggerStackOverFlowError():
    print('Stack Overflow')

def TriggerStackUnderFlowError():
    print('Stack Overflow')

def PrintStackContent(stack):    
    while not stack.IsUnderFlow():
        print(stack.pop(),end=' ')