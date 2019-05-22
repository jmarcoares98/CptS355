# Author: Juan Marco Ares
# 3rd Programming Assignment for 355 using Python

# 1. Dictionaries using Pullman Transit. We assume that 
# they maintain the bus stops and their routes as dictionary
# We used a for loop to go in the loop for b and if else 
# Code referenced from geeksfromgeeks. Swapping key and value

def busStops (b):
    newDict = {}
    for (key, values) in b.items():
        for value in values:
            if value in newDict.keys():
                newDict[value].append(key)
            else:
                newDict[value] = [key]
    for (s, r) in newDict.items():
        r.sort()
    return newDict



def testbusStops():
    buses = {"Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence",
    "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview",
    "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
    "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView",
    "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight",
    "Campus"],
    "Silver": ["TransferStation", "PorchLight", "Stadium",
    "Bishop","Walmart", "Shopco", "RockeyWay"],
    "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand",
    "TacoBell", "Chinook", "Library"],
    "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview",
    "CityHall", "Stadium", "Colorado"]}

    if busStops(buses) != {'Chinook': ['Blue', 'Lentil', 'Wheat'], 'Orchard': ['Lentil',
    'Wheat'], 'Valley': ['Lentil', 'Wheat'], 'Emerald': ['Lentil'],
    'Providence': ['Lentil'], 'Stadium': ['Gray', 'Lentil', 'Silver'],
    'Main': ['Gray', 'Lentil'], 'Arbor': ['Lentil'], 'Sunnyside': ['Gray',
    'Lentil'], 'Fountain': ['Lentil'], 'Crestview': ['Gray', 'Lentil'],
    'Wheatland': ['Lentil'], 'Walmart': ['Lentil', 'Silver', 'Wheat'],
    'Bishop': ['Lentil', 'Silver', 'Wheat'], 'Derby': ['Lentil'], 'Dilke':
    ['Lentil'], 'Maple': ['Wheat'], 'Aspen': ['Wheat'], 'TerreView':
    ['Blue', 'Wheat'], 'Clay': ['Wheat'], 'Dismores': ['Wheat'], 'Martin':
    ['Wheat'], 'PorchLight': ['Silver', 'Wheat'], 'Campus': ['Wheat'],
    'TransferStation': ['Blue', 'Gray', 'Silver'], 'Shopco': ['Silver'],
    'RockeyWay': ['Silver'], 'State': ['Blue'], 'Larry': ['Blue'], 'Grand':
    ['Blue'], 'TacoBell': ['Blue'], 'Library': ['Blue'], 'Wawawai':
    ['Gray'], 'CityHall': ['Gray'], 'Colorado': ['Gray']}:
        return False
    return True


# 2. (a) addDict. this adds up the number of hours studied
# the function will return the summed values as a dictionary


def addDict(d):
    add = {}
    for i in d.values():
       for j in i:
           if j in add:
               add[j] += i[j] 
           else:
                add[j] = i[j]
    return add
    


def testaddDict():
    d = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2, '360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}
    if addDict({}) != {}:
        return False
    if addDict(d) != {'355': 8, '451': 8, '360': 9}:
        return False
    return True


# 2. (b) takes a list of weekly log dictionaries
# returns a dictionary that includes the total number of hours
# that you have studied for. The function should use MAP and REDUCE
# may need to use a helper function for it should reduce and map then add the total

def addDictN(L):
    return helperaddDictN(list(map(addDict, L)))


def helperaddDictN(nL):
    newList = {}
    for values in nL:
        for course, num in values.items():
            if course in newList:
                newList[course] += num
            else:
                newList[course] = num
    return newList


def testaddDictN():
    dN =[{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3},
    'Fri':{'355':2}, 'Sun':{'355':1}},
    {'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},
    {'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6},
    'Sun':{'355':5}}]
    if addDictN(dN) != {'355': 16, '360': 24, '451': 6}:
        return False
    return True


# 3. (a) searchDicts will take a list of dictionaries and key
# it checks each dictionary from start to end of the list. 
# if the key appears in the dictionary, it will return the value for k
# if it appears in more than one dictionary it will return the one clore to the end

def searchDicts(L, k):
    s = len(L)
    i = s - 1
    for x in range(s):
        nDict = L[i]
        for (key,val) in nDict.items():
            if key == k:
                return val
            else:
                continue
        i -= 1
    return None


def testsearchDicts():
    L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
    if searchDicts(L1,"x") != 2:
        return False
    if searchDicts(L1,"y") != False:
        return False
    if searchDicts(L1,"z") != "found":
        return False
    if searchDicts(L1,"t") != None:
        return False
    return True


# 3. (b) this function takes a list of tuples and a key
# Each tuple in the input list has an integer index value and dictionary
# this fucntion checks the dictionary in each tuple starting from the end
# it will check the dictionaries in order. The beginning tuple will always be 0
# it will return the first value for key k. if not found return None
# suggest to use RECURSIVE, define a helper function with an added index as a parameter\

def searchDicts2(tL, k):
    indexSize = len(tL) - 1
    return helpersearchDicts2(tL, k, indexSize)


def helpersearchDicts2(tl2, k2, index):
    t = tl2[index]
    inDict = t[1]
    size = len(inDict.values())
    for (x, y) in inDict.items():
        if x == k2:
            return y
        if index == t[0]:
            size -= 1
            if size == index:
                return None
        else:
            continue
    return helpersearchDicts2(tl2, k2, index = t[0])


def testsearchDicts2():
    L2 = [(0,{"x":0,"y":True,"z":"zero"}),
     (0,{"x":1}),
     (1,{"y":False}),
     (1,{"x":3, "z":"three"}),
     (2,{})]
    if searchDicts2 (L2,"x") != 1:
        return False
    if searchDicts2 (L2,"y") != False:
        return False
    if searchDicts2 (L2,"z") != "zero":
        return False
    if searchDicts2 (L2,"t") != None:
        return False
    return True


# 4. (Lists) subsets
# A function subsets that takes a lists and returns a list of list
# each being one of the 2^length subsets and should appear in increasing length
# I used two for loops and imported itertools, this will help append the list

import itertools
def subsets(L):
    sz = len(L)
    res = []
    res.append([])
    for i in range(1, sz + 1):
        for j in itertools.combinations(L, i):
            res.append(list(j))
    return res

def testsubsets():
    if subsets([1,2,3]) != [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]:
        return False
    if subsets([(1,"one"),(2,"two")]) != [[],[(1,"one")],[(2,"two")],[(1,"one"),(2,"two")]]:
        return False
    if subsets([]) != [[]]:
        return False
    return True


# 5. (recursion) This function takes a grid length and width
# it will return the number of different paths from the grid map
# the map from the start to the goal. Use recursion

def numPaths(M, N):
    return helpernumPaths(0,0,(M,N))

def helpernumPaths(rw, cl, fin):
    p1 = 0
    p2 = 0
    wya = (rw,cl)

    if (wya[0] == fin[0]-1) and (wya[1] == fin[1]-1):
        return 1
    d = (rw + 1, cl)
    if(d[0] < fin[0]):
        p1 = helpernumPaths(rw + 1, cl, fin)
    rt = (rw, cl + 1)
    if(rt[1] < fin[1]):
        p2 = helpernumPaths(rw, cl + 1, fin)
    
    return p1 + p2


def testnumPaths():
    if numPaths(2,2) != 2:
        return False
    if numPaths(3,3) != 6:
        return False 
    if numPaths(4,5) != 35:
        return False
    return True


# 6. (a) Create an iterator that represents
# the sequence of prime numbers startig at 2

class iterPrimes():
    def __init__(self):
        self.current = 2
    def __next__(self):
        self.current += 1
        while True:
            for i in range(2, (self.current // 2) + 1):
                if self.current % i == 0:
                    self.current += 1
                    break
            else:
                break
        return self.current
    def __current__(self):
        return self.current
    def __iter__(self):
        return self

# 6. (b) this function takes an iterator and a positive integer value
# returns the next elements such that the next element of the iterator
# it adds to to less than the integer value

def numbersToSum(iNumbers, sum):
    newL = []
    nSum = 0
    newL.append(iNumbers.__current__())
    nSum += iNumbers.__current__()
    while True:
        iN = iNumbers.__next__()
        nSum += iN
        if nSum >= sum:
            break
        newL.append(iN)
    return newL


def testnumbersToSum():
    primes = iterPrimes()
    if numbersToSum(primes, 58) != [2, 3, 5, 7, 11, 13]:
        return False
    if numbersToSum(primes, 100) != [17, 19, 23, 29]:
        return False
    return True


testFunctions = {"busStops":testbusStops,  "addDict": testaddDict, 
"addDictN": testaddDictN, "searchDicts": testsearchDicts,
 "searchDicts2": testsearchDicts2, "subsets":testsubsets, 
 "numPaths": testnumPaths, "numbersToSum":testnumbersToSum}


if __name__ == '__main__':
    for testName,testFunc in testFunctions.items():
        print(testName,':  ',testFunc())
        print('---------------------')