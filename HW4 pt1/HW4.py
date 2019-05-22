# Author: Juan Marco Ares
# 4th Programming Assignment for 355 using Python

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    return opstack.pop(len(opstack) - 1)
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name

def dictPop():
    return dictstack.pop()
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    if type(d) is dict:
        dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. Note that, your interpreter will call dictPush only when Postscript “begin” operator is called. “begin” should pop the empty dictionary from the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if type(name) is str:
        newd = dict(name=name, value=value)
        dictPush(newd)
    #add name:value pair to the top dictionary in the dictionary stack. Keep the '/' in the name constant. 
    # Your psDef function should pop the name and value from operand stack and call the “define” function.

def lookup(name):
    size = len(dictstack)
    # when dictstack is empty return message
    if (size == 0):
        print("Dictionary is empty")
    else:
        for i in range(size):
            peek = dictstack[size-i-1]
            if peek != {} and peek["name"] == name:
                return peek["value"]
    # print out an ERROR message
    print("ERROR: Name not defined")

    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% -------------------------------------
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

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put

# gets a string and pushes the length of the string
def length():
    strng = opPop()
    opPush(len(strng))

# gets a string and index value and pushes the ASCII value of the character
def get():
    i = opPop()
    strng = opPop()
    opPush(ord(strng[i]))

# gets a string, index and count to push the substring of that string from the start index to the count
def getinterval():
    i = opPop()
    cnt = opPop()
    strng = opPop()
    opPush(strng[i:cnt])

# gets a string, index and ASCII value and replaces the character at index with new character string
def put():
    strng = list(opPop())
    i = opPop()
    asci = opPop()
    dup = chr(asci)
    strng[i] = dup
    b = ''.join(strng)
    opPush(b)

#--------------------------- 25% -------------------------------------
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

# exchange the top two stack values
def exch():
    val1 = opPop()
    val2 = opPop()
    opPush(val1)
    opPush(val2)

# moves the top count values on the stack into the nth stack position
def roll():
    pos = opPop()
    num = opPop()
    size = len(opstack)
    for i in range(num):
        if pos <= size:
            opstack[size - pos] = opPop()
            pos += 1

# display the contents of the stack
def stack():
    for i in opstack:
        print(i)

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

# operator takes the initial size of the dictionary from the stack and puts a brand new empty dictionary
def psDict():
    size = opPop()
    for i in range(size):
        opPush(dict())

# operator takes a dictionary from the top of the operand stack and pushes it on the dictionary stack
def begin():
    val = opPop()
    if type(val) is dict:
        dictPush(val)

# operator - pop the top dictionary from the stack and throw it away
def end():
    dictPop()

# pop the name and value from the operand stack and call the define function
def psDef():
    value = opPop()
    name = opPop()
    define(name, value)

# --------------------------------------------------------------------
## Sample tests #
# --------------------------------------------------------------------
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testLookup():
    opPush("n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

def testDefine():
    define("n2", 2)
    if lookup("n2") != 2:
        return False
    return True

def testSub():
    opPush(10)
    opPush(3)
    sub()
    if opPop() != 7:
        return False
    return True

def testMul():
    opPush(2)
    opPush(6)
    mul()
    if opPop() != 12:
        return False
    return True

def testDiv():
    opPush(13)
    opPush(13)
    div()
    if opPop() != 1:
        return False
    return True

def testMod():
    opPush(5)
    opPush(2)
    mod()
    if opPop() != 1:
        return False
    return True

def testLt():
    opPush(75)
    opPush(23)
    lt()
    if opPop() != False:
        return False
    return True

def testGt():
    opPush(75)
    opPush(23)
    gt()
    if opPop() != True:
        return False
    return True

def testEq():
    opPush(23)
    opPush(23)
    eq()
    if opPop() != True:
        return False
    return True

def testLength():
    opPush([1,2,3])
    length()
    if opPop() != 3:
        return False
    return True

def testGet():
    opPush(0)
    opPush("Cpts")
    get()
    if opPop() != 67:
        return False
    return True

def testGetinterval():
    opPush("CptS355")
    opPush(3)
    opPush(0)
    getinterval()
    if opPop() != "Cpt":
        return False
    return True

def testPut():
    opPush(48)
    opPush(6)
    opPush("Cpts355")
    put()
    if opPop() != "Cpts350":
        return False
    return True

def testDup():
    opPush(15)
    dup()
    if opPop() != opPop():
        return False
    return True

def testExch():
    opPush(6)
    opPush(9)
    exch()
    if opPop() != 6 and opPop() != 9:
        return False
    return True

def testPop():
    x = len(opstack)
    opPush(12)
    pop()
    y = len(opstack)
    if x != y:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(6)
    opPush(7)
    opPush(8)
    opPush(2)
    opPush(4)
    roll()
    if opPop() != 6 and opPop() != 5 and opPop() != 4 and opPop() != 3 and opPop() != 8 and opPop() != 7:
        return False
    return True

def testCopy():
    opPush(4)
    opPush(5)
    opPush(9)
    opPush(6)
    opPush(2)
    copy()
    if opPop() != 6 and opPop != 9 and opPop != 6 and opPop != 9:
        return False
    return True

def testClear():
    opPush(10)
    opPush("clr")
    clear()
    if len(opstack) != 0:
        return False
    return True

def testDict():
    opPush(3)
    psDict()
    if opPop() != {}:
        return False
    return True

def testBeginEnd():
    opPush("hey")
    opPush(79)
    psDef()
    begin()
    opPush("hi")
    opPush(4)
    psDef()
    end()
    if lookup("hey") != 79:
        return False
    return True

def testpsDef():
    opPush("n")
    opPush(21)
    psDef()
    if lookup("n") != 21:
        return False
    return True

def testpsDef2():
    opPush("m")
    opPush(-22)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("m") != -22:
        end()
        return False
    end()
    return True


# go on writing test code for ALL of your code here; think about edge cases,
# and other points where you are likely to make a mistake.

def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),
                 ('div', testDiv),  ('mod', testMod), ('lt', testLt), ('gt', testGt), ('eq', testEq),
                 ('length', testLength),('get', testGet), ('getinterval', testGetinterval),
                 ('put', testPut), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll),
                 ('copy', testCopy), ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd),
                 ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')

if __name__ == '__main__':
    print(main_part1())