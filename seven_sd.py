two_lines = """|       |
|       |
|       |"""

horizontal = "---------"

left_line = """|
|
|"""

right_line = """        |
        |
        |
"""

def printZero():
    print(horizontal)
    print(two_lines)
    print(two_lines)
    print(horizontal)

def printSix():
    print(horizontal)
    print(left_line)
    print(horizontal)
    print(two_lines)
    print(horizontal)

def printFive():
    print(horizontal)
    print(left_line)
    print(horizontal)
    print(right_line)
    print(horizontal)

def printOne():
    print(left_line)
    print(left_line)

def printTwo():
    print(horizontal)
    print(right_line)
    print(horizontal)
    print(left_line)
    print(horizontal)

def printThree():
    print(horizontal)
    print(left_line)
    print(horizontal)
    print(left_line)
    print(horizontal)

def printFour():
    print(two_lines)
    print(horizontal)
    print(left_line)

def printSeven():
    print(horizontal)
    print(left_line)
    print(left_line)

def printEight():
    print(horizontal)
    print(two_lines)
    print(horizontal)
    print(two_lines)
    print(horizontal)

def printNine():
    print(horizontal)
    print(two_lines)
    print(horizontal)
    print(left_line)

num = int(input(":"))
if num == 0:
    printZero()
elif num == 1:
    printOne()
elif num == 2:
    printTwo()
elif num == 3:
    printThree()
elif num == 4:
    printFour()
elif num == 5:
    printFive()
elif num == 6:
    printSix()
elif num == 7:
    printSeven()
elif num == 8:
    printEight()
elif num == 9:
    printNine()
