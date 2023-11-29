import re
from sympy import Matrix, lcm
import urllib.request as urlreq

weburl = urlreq.urlopen(
    "https://firebasestorage.googleapis.com/v0/b/hack-dlrc.appspot.com/o/inputs%2Fq6%2F0.txt?alt=media&token=7caaf388-3f2c-46fe-84bb-b7bb25cc4910"
)

reactions = weburl.read().decode().split("\r\n")
new = []

sumcoeff = 0

def remove_spaces(lst):
    if type(lst) == str:
        removed_spaces = lst.replace(" ", "")
    elif type(lst) == list:
        removed_spaces = lst[0].replace(" ", "")
    return removed_spaces

for react in enumerate(reactions):
    reactions[react[0]] = remove_spaces(react[1])

for i in range(len(reactions)):
    l = reactions[i].split("->")
    reactions[i] = l

print(reactions)

for i in range(len(reactions)):
    elementList = []
    elementMatrix = []
    reactants = reactions[i][0]
    products = reactions[i][1]
    reactants = reactants.replace(' ', '').split("+")
    products = products.replace(' ', '').split("+")


    def addToMatrix(element, index, count, side):
        if (index == len(elementMatrix)):
            elementMatrix.append([])
            for x in elementList:
                elementMatrix[index].append(0)
        if (element not in elementList):
            elementList.append(element)
            for i in range(len(elementMatrix)):
                elementMatrix[i].append(0)
        column = elementList.index(element)
        elementMatrix[index][column] += count * side


    def findElements(segment, index, multiplier, side):
        elementsAndNumbers = re.split('([A-Z][a-z]?)', segment)
        i = 0
        while (i < len(elementsAndNumbers) - 1):  # last element always blank
            i += 1
            if (len(elementsAndNumbers[i]) > 0):
                if (elementsAndNumbers[i + 1].isdigit()):
                    count = int(elementsAndNumbers[i + 1]) * multiplier
                    addToMatrix(elementsAndNumbers[i], index, count, side)
                    i += 1
                else:
                    addToMatrix(elementsAndNumbers[i], index, multiplier, side)


    def compoundDecipher(compound, index, side):
        segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)', compound)
        for segment in segments:
            if segment.startswith("("):
                segment = re.split('\)([0-9]*)', segment)
                multiplier = int(segment[1])
                segment = segment[0][1:]
            else:
                multiplier = 1
            findElements(segment, index, multiplier, side)


    for i in range(len(reactants)):
        compoundDecipher(reactants[i], i, 1)
    for i in range(len(products)):
        compoundDecipher(products[i], i + len(reactants), -1)
    elementMatrix = Matrix(elementMatrix)
    elementMatrix = elementMatrix.transpose()
    solution = elementMatrix.nullspace()[0]
    multiple = lcm([val.q for val in solution])
    solution = multiple * solution
    coEffi = solution.tolist()
    print(coEffi)
    s = 0
    for i in range(len(coEffi)):
        num = coEffi[i][0]
        s += num
    s = s - coEffi[-1][0]
    print(s)
    sumcoeff += s
    print(sumcoeff)
    output = ""
    for i in range(len(reactants)):
        output += str(coEffi[i][0]) + reactants[i]
        if i < len(reactants) - 1:
            output += " + "
    output += " -> "
    for i in range(len(products)):
        output += str(coEffi[i + len(reactants)][0]) + products[i]
        if i < len(products) - 1:
            output += " + "
    print(output)

