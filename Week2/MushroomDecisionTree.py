# import math package
import math


def readData():
    # open and read the dataset
    dataset = open("mushroom-dataset.data", "r")
    mushrooms = []
    for num in dataset:
        row = num.strip('\n').split(',')
        mushrooms.append(row)
    mData = []
    for i in range(23):
        column = []
        for num in range(len(mushrooms)):
            column += mushrooms[num][i]
        mData.append(column)
    # get firstRow as the e/p in each of the 8124 rows and set mData as a list
    # mData list = list of 22 lists of 8124 or wtv so elements
    firstRow = mData[0].copy()
    mData = mData[1:]
    # return the firstRow and mData to be used in the main function
    return firstRow, mData


def infoGain(totEntropy, conEntropy):
    # calculate the information gain for each attribute when given a total entropy and conditional entropy
    information = totEntropy - conEntropy[0]
    return information


def totalEntropy(epList):
    p = 0
    t = 0
    # calculate the total entropy when given the number of elements left
    for index in epList:
        t += 1
        if index == 'p':
            p += 1
    e = t - p
    entropy = (((e / t) * math.log(e / t, 2)) + ((p / t) * math.log(p / t, 2)))
    # return entropy * -1
    return -entropy


def conditionalEntropy(dataList, epList):
    # create lists for total count, e, and p values
    subsetTotals = []
    finalCountE = []
    finalCountP = []
    subsetList = list(set(dataList))
    # iterate through each feature letter and count the total num of e, p, and items in each one
    for iter in range(len(subsetList)):
        numVal = 0
        numE = 0
        numP = 0
        for index in range(len(dataList)):
            if dataList[index] == subsetList[iter]:
                numVal += 1
                if epList[index] == 'e':
                    numE += 1
                else:
                    numP += 1
        subsetTotals.append(numVal)
        finalCountE.append(numE)
        finalCountP.append(numP)
    # gets all the letters in each attribute that don't have zeros in either the e/p lists
    nonZeroSet = []
    for i in range(len(subsetList)):
        if finalCountE[i] != 0 and finalCountP[i] != 0:
            nonZeroSet.append(subsetList[i])
    # get the indexes of those values for each letter in each attribute so that we can process it later
    indexList = []
    for i in range(len(nonZeroSet)):
        for index in range(len(dataList)):
            if dataList[index] == nonZeroSet[i]:
                indexList.append(index)
    # create a new ep list to be used in the next iteration
    outerList = []
    for index in range(len(indexList)):
        outerList.append(epList[indexList[index]])
    # calculate conditional entropy
    sum = 0
    sumTotal = 0
    for x in range(len(subsetTotals)):
        sumTotal += subsetTotals[x]
    for val in range(len(subsetList)):
        edible = finalCountE[val] / subsetTotals[val]
        poison = finalCountP[val] / subsetTotals[val]
        totalProb = subsetTotals[val] / sumTotal
        if edible == 1 or poison == 1:
            sum += 0
        else:
            sum += totalProb * ((edible * math.log(edible, 2)) + (poison * math.log(poison, 2)))
    # return the specified float/lists in a tuple
    return -sum, subsetList, indexList, outerList, finalCountE, finalCountP


def main():
    # dataset attribute names
    datasetNames = ['Cap Shape', 'Cap Surface', 'Cap Color', 'Bruises', 'Odor', 'Gill Attachment', 'Gill Spacing',
                    'Gill Size', 'Gill Color', 'Stalk Shape', 'Stalk Root', 'Stalk Surface Above Ring',
                    'Stalk Surface Below Ring', 'Stalk Color Above Ring', 'Stalk Color Below Ring', 'Veil Type',
                    'Veil Color', 'Ring Number', 'Ring Type', 'Spore Print Color', 'Population', 'Habitat']
    # read the data from the .data file
    readList = readData()
    firstRow = readList[0]
    mData = readList[1]
    x = 0
    space = ''
    # run while the length of edible or poison list does not equal 1 or 0
    while not (len(firstRow) == 1 or len(firstRow) == 0):
        maxGain = 0
        entropy = totalEntropy(firstRow)
        gainList = []
        for index in range(len(mData)):
            # call the entropy function with the provided data (mData) and firstRow (e/p list)
            conEntropy = conditionalEntropy(mData[index], firstRow)
            # call the gain function to calculate the gain (entropy - conditional entropy)
            gain = infoGain(entropy, conEntropy)
            gainList.append(gain)
            if gain > maxGain:
                bestList = conEntropy[1:]
                maxGain = gain
                iterValue = index
        splitList = []
        # split the lists only getting the subset values that are not zero
        # append all the subset values that do not lead to e/p to a new list
        for index in range(len(mData)):
            mainList = []
            for i in range(len(bestList[1])):
                mainList.append(mData[index][bestList[1][i]])
            splitList.append(mainList)
        # call display function to display the data
        display(bestList, datasetNames, iterValue, space)
        # set these new lists to mData and firstRow to be used in the next iteration
        mData = splitList
        firstRow = bestList[2]
        space += '   '
        x += 1


def display(bestList, datasetNames, iterValue, space):
    # split the specified values based on the criteria and display them
    print(f'{space}Split on: {datasetNames[iterValue]}')
    subsetValues = bestList[0]
    edibleList = bestList[3]
    poisonList = bestList[4]
    values = []
    for index in range(len(subsetValues)):
        # if edible list has 0, then it is poisonous
        if edibleList[index] == 0:
            print(f'{space} Mushrooms of value \'{subsetValues[index]}\' are 100% poisonous')
            values.append(subsetValues[index])
        # if poisonous list has 0, then it is edible
        elif poisonList[index] == 0:
            print(f'{space} Mushrooms of value \'{subsetValues[index]}\' are 100% edible')
            values.append(subsetValues[index])
    # get the values that are different from two sets as a list
    remValues = list((set(subsetValues) - set(values)))
    # say that they need to be split
    for index in range(len(remValues)):
        print(f'{space} Mushrooms of value \'{remValues[index]}\' need to split:')


main()
