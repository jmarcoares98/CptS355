# Author: Juan Marco Ares
# 4th Programming Assignment pt. 2 for 355 using Python


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
    if name[0] == '(' and name[-1] == ')':
        name = name[1:-1]
    if name[0] != '/':
        name = "/" + name
    # when dictstack is empty return message
    if (size == 0):
        return None
    else:
        for i in range(size):
            peek = dictstack[size-i-1]
            if peek != {} and peek["name"] == name:
                return peek["value"]

    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


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
    for i in range(size):
        print(opstack[size-i-1])


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
        interpretSPS(condition)

def psIfelse():
    con1 = opPop()
    con2 = opPop()
    boolop = opPop()
    if boolop == True:
        interpretSPS(con2)
    else:
        interpretSPS(con1)

def psFor():
    arr = opPop()
    final = opPop()
    increment = opPop()
    init = opPop()
    if increment > 0:
        while(init <= final):
            opPush(init)
            funct = iter(arr)
            interpretSPS(funct)
            init += increment
    else:
        while(init >= final):
            opPush(init)
            funct = iter(arr)
            interpretSPS(funct)
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
#
def interpretSPS(code): # code is a code array
    functDict = {"opPop": opPop, "opPush": opPush, "dictpPop": dictPop, "dictPush": dictPush,
                "add": add, "sub": sub, "mul": mul, "div": div, "eq": eq, "lt": lt, "gt":gt, "length":length,
                "get": get, "getinterval": getinterval, "put": put, "dup":dup, "copy": copy, "pop": pop, 
                "clear": clear, "exch": exch, "roll": roll, "stack": stack, "dict": psDict, "begin": begin,
                "end": end, "def": psDef, "if": psIf, "ifelse": psIfelse, "for": psFor}
    o = opstack
    dic = dictstack
    for c in code:
        if isinstance(c, (list, int, bool, str)):
            if isinstance(c, (list, int, bool)):
                opPush(c)
            elif c[0] == '(' or c[0] == '/':
                opPush(c)
            elif isinstance(c, str):
                x = lookup(c)
                if isinstance(x,list):
                    interpretSPS(iter(x))
                elif x in functDict.keys():
                    func = functDict[x]
                    func()
                elif isinstance(x, (str, int, bool)):
                    opPush(x)
                elif c in functDict.keys():
                    func = functDict[c]
                    func()
                else:
                    opPush(c)
        else: 
            opPush(c)

def interpreter(s): # s is a string
    interpretSPS(iter(parse(tokenize(s))))

#testing

input1 = """
        /square {
               dup mul
        } def 
        (square)
        4 square 
        dup 16 eq 
        {(pass)} {(fail)} ifelse
        stack 
        """

input2 ="""
        (facto) dup length /n exch def
        /fact {
        0 dict begin
        /n exch def
        n 2 lt
        { 1}
        {n 1 sub fact n mul }
        ifelse
        end
        } def
        n fact stack
        """


input3 = """
        /fact{
        0 dict
                begin
                        /n exch def
                        1
                        n -1 1 {mul} for
                end
        } def
        6
        fact
        stack
    """

input4 = """
        /lt6 { 6 lt } def
        1 2 3 4 5 6 4 -3 roll
        dup dup lt6 {mul mul mul} if
        stack
        clear
        """

input5 = """
        (CptS355_HW5) 4 3 getinterval 
        (355) eq 
        {(You_are_in_CptS355)} if
         stack 
        """

input6 = """
        /pow2 {/n exch def 
               (pow2_of_n_is) dup 8 n 48 add put 
                1 n -1 1 {pop 2 mul} for  
              } def
        (Calculating_pow2_of_9) dup 20 get 48 sub pow2
        stack
        """

def testPut():
    opPush("(This is a test _)")
    dup()
    opPush("/s")
    exch()
    psDef()
    opPush(15)
    opPush(48)
    put()
    if lookup("s") != "(This is a test 0)" or opPop()!= "(This is a test 0)":
        return False
    return True

def testInput1():
    if tokenize(input1) != ['/square', '{', 'dup', 'mul', '}', 'def', '(square)', '4', 'square', 
    'dup', '16', 'eq', '{', '(pass)', '}', '{', '(fail)', '}', 'ifelse', 'stack']:
        return False
    elif parse(tokenize(input1)) != ['/square', ['dup', 'mul'], 'def', '(square)', 4, 'square', 
    'dup', 16, 'eq', ['(pass)'], ['(fail)'], 'ifelse', 'stack']:
        return False
    return True

def testInput2():
    if tokenize(input2) != ['(facto)', 'dup', 'length', '/n', 'exch', 'def', '/fact', '{', '0', 
    'dict', 'begin', '/n', 'exch', 'def', 'n', '2', 'lt', '{', '1', '}', '{', 'n', '1', 'sub', 'fact', 'n', 'mul', '}',
     'ifelse', 'end', '}', 'def', 'n', 'fact', 'stack']:
        return False
    elif parse(tokenize(input2)) != ['(facto)', 'dup', 'length', '/n', 'exch', 'def', '/fact', [0, 'dict', 'begin', '/n',
    'exch', 'def', 'n', 2, 'lt', [1], ['n', 1, 'sub', 'fact', 'n', 'mul'], 'ifelse', 'end'], 'def', 'n', 'fact', 'stack']:
        return False
    return True
def testInput3():
    if tokenize(input3) != ['/fact', '{', '0', 'dict', 'begin', '/n', 'exch', 'def', '1', 'n', '-1', '1', '{', 'mul', '}', 
    'for', 'end', '}', 'def', '6', 'fact', 'stack']:
        return False
    elif parse(tokenize(input3)) != ['/fact', [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1, ['mul'], 'for', 'end'],
    'def', 6, 'fact', 'stack']:
        return False
    return True

def testInput4():
    if tokenize(input4) != ['/lt6', '{', '6', 'lt', '}', 'def', '1', '2', '3', '4', '5', '6', '4', '-3', 'roll',
    'dup', 'dup', 'lt6', '{', 'mul', 'mul', 'mul', '}', 'if', 'stack', 'clear']:
        return False
    elif parse(tokenize(input4)) != ['/lt6', [6, 'lt'], 'def', 1, 2, 3, 4, 5, 6, 4, -3, 'roll', 'dup', 'dup',
    'lt6', ['mul', 'mul', 'mul'], 'if', 'stack', 'clear']:
        return False
    return True

def testInput5():
    if tokenize(input5) != ['(CptS355_HW5)', '4', '3', 'getinterval', '(355)', 'eq', '{', '(You_are_in_CptS355)', '}', 'if', 'stack']:
        return False
    elif parse(tokenize(input5)) != ['(CptS355_HW5)', 4, 3, 'getinterval', '(355)', 'eq', ['(You_are_in_CptS355)'], 'if', 'stack']:
        return False
    return True

def testInput6():
    if tokenize(input6) != ['/pow2', '{', '/n', 'exch', 'def', '(pow2_of_n_is)', 'dup', '8', 'n', '48', 'add', 'put', '1', 'n', '-1',
    '1', '{', 'pop', '2', 'mul', '}', 'for', '}', 'def', '(Calculating_pow2_of_9)', 'dup', '20', 'get', '48', 'sub', 'pow2', 'stack']:
        return False
    elif parse(tokenize(input6)) != ['/pow2', ['/n', 'exch', 'def', '(pow2_of_n_is)', 'dup', 8, 'n', 48, 'add', 'put', 1, 'n', -1, 1, 
    ['pop', 2, 'mul'], 'for'], 'def', '(Calculating_pow2_of_9)', 'dup', 20, 'get', 48, 'sub', 'pow2', 'stack']:
        return False
    return True

def testInterpreter1():
    clear()
    print("Test Interpreter Output for Input1")
    interpreter(input1)
    if opstack != ['(square)', 16, '(pass)']:
        return False
    clear()
    return True

def testInterpreter2():
    clear()
    print("Test Interpreter Output for Input2")
    interpreter(input2)
    if opstack != ['(facto)', 120]:
        return False
    clear()
    return True

def testInterpreter3():
    clear()
    print("Test Interpreter Output for Input3")
    interpreter(input3)
    if opstack != [720]:
        return False
    clear()
    return True

def testInterpreter4():
    clear()
    print("Test Interpreter Output for Input4")
    interpreter(input4)
    clear()
    return True

def testInterpreter5():
    clear()
    print("Test Interpreter Output for Input5")
    interpreter(input5)
    if opstack != ['(You_are_in_CptS355)']:
        return False
    clear()
    return True

def testInterpreter6():
    clear()
    print("Test Interpreter Output for Input6")
    interpreter(input6)
    if opstack != ['(Calculating_pow2_of_9)', '(pow2_of_9_is)', 512]:
        return False
    clear()
    return True  

def main_part2():
    testCases = [('testPut', testPut), ('testInput1', testInput1), ('testInput2', testInput2), 
                ('testInput3', testInput3), ('testInput4', testInput4),
                ('testInput5', testInput5), ("testInput6", testInput6),
                ("testInterpreter1", testInterpreter1), ("testInterpreter2", testInterpreter2),
                ("testInterpreter3", testInterpreter3), ("testInterpreter4", testInterpreter4),
                ("testInterpreter5", testInterpreter5), ("testInterpreter6", testInterpreter6)]
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return('Some Part 2 Tests Failed', failedTests)
    else:
        return('All Part 2 Tests Succeeded')

if __name__ == '__main__':
    print(main_part2())