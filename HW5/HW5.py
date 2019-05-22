# Author: Juan Marco Ares
# 5th Programming Assignment for 355 using Python

Scope = "" # for functions that need scope 

# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    return opstack.pop(len(opstack) - 1)
    return opstack.pop(len(opstack) - 1)
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)


# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name

def dictPop():
    return dictstack.pop()
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. Note that, your interpreter will call dictPush only when Postscript “begin” operator is called. “begin” should pop the empty dictionary from the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if type(name) is str:
        newd = {name: value}
        if dictstack == []:
            dictPush((0,newd))
        else:
            (l, dict) = dictPop()
            dict[name] = value
            dictPush((l, dict))

            
    #add name:value pair to the top dictionary in the dictionary stack. Keep the '/' in the name constant. 
    # Your psDef function should pop the name and value from operand stack and call the “define” function.

#def lookup(name):
#    returnT = ()
#    size = len(dictstack)
#    if name[0] == '(' and name[-1] == ')':
#        name = name[1:-1]
#    if name[0] != '/':
#        name = "/" + name
#   # when dictstack is empty return message
#    if (size == 0):
#        return None
#    else:
#        for i in range(size):
#            peek = dictstack[size-i-1]
#            if peek != {} and peek["name"] == name:
#                return peek["value"]

# new definition for lookup for static and dynamic
def lookup(name, scope):
    if name[0] == '(' and name[-1] == ')':
        name = name[1:-1]
    if name[0] != '/':
       name = "/" + name
    if scope == "static":
        link = staticFind(name)
        if link == None:
            return None
        else:
            (l, dik) = dictstack[link]
            return dik[name]
    else: 
        for (link, dic) in reversed(dictstack):
            if name in dic:
                return dic[name]
        return None


# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
#Make sure to check the operand stack has the correct number of parameters and types of the parameters are correct.

def add():
    addition = opPop() + opPop()
    opPush(addition)

def sub():
    op1 = opPop()
    subtract = opPop() - op1
    opPush(subtract)

def mul():
    multiply = opPop() * opPop()
    opPush(multiply)

def div():
    op1 = opPop()
    divide = opPop() / op1
    opPush(divide)

def mod():
    op1 = opPop()
    modulate = opPop() % op1
    opPush(modulate)

def eq():
    equal = (opPop() == opPop())
    opPush(equal)

def lt():
    op1 = opPop()
    less = opPop() < op1
    opPush(less)

def gt():
    op1 = opPop()
    great = opPop() > op1
    opPush(great)


# String operators: define the string operators length, get, getinterval, put

# gets a string and pushes the length of the string
def length():
    strng = opPop()
    if strng[0] == '(' and strng[-1] == ')':
        strng = strng[1:-1]
    opPush(len(strng))

# gets a string and index value and pushes the ASCII value of the character
def get():
    i = opPop()
    strng = opPop()
    if strng[0] == '(' and strng[-1] == ')':
        strng = strng[1:-1]
    opPush(ord(strng[i]))

# gets a string, index and count to push the substring of that string from the start index to the count
def getinterval():
    i = opPop()
    cnt = opPop()
    strng = opPop()
    if strng[0] == '(' and strng[-1] == ')':
        strng = strng[1:-1]
    dstrng = strng[cnt:]
    nstrng = dstrng[:i]
    nstrng = "(" + nstrng + ")"
    opPush(nstrng)

# gets a string, index and ASCII value and replaces the character at index with new character string
def put():
    size = len(dictstack)
    sizestk = len(opstack)
    asci = opPop()
    i = opPop()
    strng = opPop()
    if id(strng) in opstack:
        opPop()
    if strng[0] == '(' and strng[-1] == ')':
        nstrng = strng[1:-1]
    Lstrng = list(nstrng) #makes it mutable
    dup = chr(asci)
    Lstrng[i] = dup
    b = ''.join(Lstrng)
    t = "(" + b + ")"
    #this loop will check the stack if the value is in dictstack then it will change it
    for x in range(size):
        peek = dictstack[size-x-1]
        p = peek["value"]
        if peek != {} and peek["value"] == strng:
            peek["value"] = t
    for y in opstack:
        if y == strng:
            opstack.remove(y)
    opPush(t)
        

# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack

# duplicate the top value on the stack
def dup():
    val = opPop()
    opPush(val)
    opPush(val)

# gets the count of wanted copies from the stack then push them onto the stack
def copy():
    num = opPop()
    temp = []
    c1 = 0
    c2 = 0
    # copying the range of values into a temp list array
    for i in range(num):
        x = opPop()
        temp.append(x)
        c1 += 1
        c2 += 1
    # placing the original values back to the stack    
    for j in range(num):
        opPush(temp[c1 - 1])
        c1 -= 1
    # placing the copied values into the stack    
    for k in range(num):
        opPush(temp[c2 - 1])
        c2 -= 1
    
# pop the top value from the stack 
def pop():
    return opPop()

# clears all the values in the stack
def clear():
    opstack.clear()
    dictstack.clear()

# exchange the top two stack values
def exch():
    val1 = opPop()
    val2 = opPop()
    opPush(val1)
    opPush(val2)

# moves the top count values on the stack into the nth stack position
def roll():
    num = opPop()
    pos = opPop()
    hstack = opstack[0-pos:]
    if num > 0:
        for i in range(num):
            h = hstack.pop(-1)
            hstack.insert(0, h)
    else:
        for i in range(abs(num)):
            h = hstack.pop(0)
            hstack.append(h)
    for y in range(0,pos):
        opPop()
    for x in hstack:
        opPush(x)

# display the contents of the stack
def stack():
    size = len(opstack)
    dl = len(dictstack) - 1
    for i in range(size):
        print(opstack[size-i-1])
    print("===============")
    for l in reversed(dictstack):
        if l[1] != {}:
            print("-----" + str(dl) + "---" + str(0) + "-----")
            for x in l[1]:
                print(str(x) + "   " + str(l[1][x]))
            dl = dl - 1
    print("===============")


# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

# operator takes the initial size of the dictionary from the stack and puts a brand new empty dictionary
def psDict():
    num = opPop()
    newDict = dict()
    for i in range(num):
        newDict[i] = None
    opPush(newDict)

# operator takes a dictionary from the top of the operand stack and pushes it on the dictionary stack
def begin():
    newDict = opPop()
    if isinstance(newDict, dict):
        dictPush(newDict)

# operator - pop the top dictionary from the stack and throw it away
def end():
    dictPop()
    dictPop()

# pop the name and value from the operand stack and call the define function
def psDef():
    value = opPop()
    name = opPop()
    define(name, value)

#Conditional operators: writing the methods of psIf and psIfelse

def psIf():
    condition = opPop()
    boolop = opPop()
    if boolop == True:
        interpretSPS(condition, Scope)

def psIfelse():
    con1 = opPop()
    con2 = opPop()
    boolop = opPop()
    if boolop == True:
        interpretSPS(con2, Scope)
    else:
        interpretSPS(con1, Scope)

def psFor():
    arr = opPop()
    final = opPop()
    increment = opPop()
    init = opPop()
    if increment > 0:
        while(init <= final):
            opPush(init)
            funct = iter(arr)
            interpretSPS(funct, Scope)
            init += increment
    else:
        while(init >= final):
            opPush(init)
            funct = iter(arr)
            interpretSPS(funct, Scope)
            init += increment


import re

def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}' or c == ']':
            return res
        elif c=='{' or c == '[':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code array for the inner
            # paranthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatching2(it))
        elif c.isnumeric() or c[0] == '-':
            res.append(int(c))
        else:
            res.append(c)
    return False

# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  # non matching closing paranthesis; return false since there is
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatching2(it))
        #when the tokens are numbers an when its a negative number
        elif c.isnumeric() or c[0] == '-':
            res.append(int(c))
        else:
            res.append(c)
    return res

# Write the necessary code here; again write
# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.
# code is a code array; scope is a string (either “static” or “dynamic”) 

def interpretSPS(code, scope): # code is a code array
    functDict = {"opPop": opPop, "opPush": opPush, "dictpPop": dictPop, "dictPush": dictPush,
                "add": add, "sub": sub, "mul": mul, "div": div, "eq": eq, "lt": lt, "gt":gt, "length":length,
                "get": get, "getinterval": getinterval, "put": put, "dup":dup, "copy": copy, "pop": pop, 
                "clear": clear, "exch": exch, "roll": roll, "stack": stack, "dict": psDict, "begin": begin,
                "end": end, "def": psDef, "if": psIf, "ifelse": psIfelse, "for": psFor}
    o = opstack
    dic = dictstack
    link = 0
    for c in code:
        if isinstance(c, (int, bool, str)):
            if c == "true":
                c = True
                opPush(c)
            elif c == "false":
                c = False
                opPush(c)
            elif isinstance(c, (int, bool)):
                opPush(c)
            elif c[0] == '(' or c[0] == '/':
                opPush(c)
            elif isinstance(c, str):
                x = lookup(c, scope)
                if isinstance(x,list):
                    if scope == "static":
                        link = staticFind(str(c))
                        if link != None:
                            dictstack.append((link, {}))
                            interpretSPS(x,scope)
                            dictPop()
                    elif scope == "dynamic":
                        dictstack.append((link,{}))
                        interpretSPS(x, scope)
                        dictPop()
                elif c in functDict.keys():
                    func = functDict[c]
                    func()
                elif isinstance(x, (int, bool, str)):
                    opPush(x)
                else:
                    opPush(c)
        else: 
            opPush(c)

# add an argument to interpret to specify the scoping rule that will be
# applied
# s is a string; scope is a string (either “static” or “dynamic”) 
def interpreter(s, scope):
    global Scope
    Scope = scope
    interpretSPS(iter(parse(tokenize(s))), scope)

def staticFind(name):
    size = len(dictstack)
    if name[0] != '/':
        name = "/" + name
    if size == 0:
        return None
    else:
        curr = size - 1
    while True: 
        for x in dictstack[curr][1]:
            if name in x:
                return curr
        if curr == 0:
            return None
        else:
            curr = dictstack[curr][0]

# test cases
def testSSPS():
    input1 = """
            /m 50 def 
            /n 100 def
            /egg1 {/m 25 def n} def
            /chic {
            /n 1 def
            /egg2 { n } def
            m n
            egg1
            egg2
            stack } def
            n
            chic
            """

    input2 = """
            /x 10 def
            /A { x } def
            /C { /x 40 def A stack } def
            /B { /x 30 def /A { x } def C } def
            B
            """

    input3 = """
            /out true def
            /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse
            dup /x exch def stack} def
            /myput { out dup /x exch def xand } def
            /f { /out false def myput } def
            false f
            """
            
    input4 = """
            /x 10 def
            /A { x } def
            /B { /x 30 def /A { x stack } def /C { /x 40 def A } def C } def
            B
            """
    
    print("====Input 1====")
    print("Static")
    print("===============")
    Scope = "static"
    interpreter(input1,"static")

    clear()

    print("Dynamic")
    print("===============")
    interpreter(input1,"dynamic")

    clear()

    print("\n")
    print("====Input 2====")
    print("Static")
    print("===============")
    interpreter(input2,"static")

    clear()

    print("Dynamic")
    print("===============")
    interpreter(input2,"dynamic")

    clear()

    print("\n")
    print("====Input 3====")
    print("Static")
    print("===============")
    interpreter(input3,"static")

    clear()

    print("Dynamic")
    print("===============")
    interpreter(input3,"dynamic")

    clear()

    print("\n")
    print("====Input 4====")
    print("Static")
    print("===============")
    interpreter(input4,"static")

    clear()

    print("Dynamic")
    print("===============")
    interpreter(input4,"dynamic")

    clear()


def main():
    testSSPS()

if __name__ == "__main__":
    print(main())