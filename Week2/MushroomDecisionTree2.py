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
    firstRow = mData[0].copy()
    mData = mData[1:]
    return firstRow, mData


def infoGain(totEntropy, conEntropy):
    information = totEntropy - conEntropy[0]
    return information


def totalEntropy(epList):
    p = 0
    t = 0
    for index in epList:
        t += 1
        if index == 'p':
            p += 1
    e = t - p
    entropy = (((e / t) * math.log(e / t, 2)) + ((p / t) * math.log(p / t, 2)))
    return -entropy


def conditionalEntropy(dataList, epList):
    subsetTotals = []
    finalCountE = []
    finalCountP = []
    subsetList = list(set(dataList))
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
    nonZeroSet = []
    for i in range(len(subsetList)):
        if finalCountE[i] != 0 and finalCountP[i] != 0:
            nonZeroSet.append(subsetList[i])
    indexList = []
    for i in range(len(nonZeroSet)):
        for index in range(len(dataList)):
            if dataList[index] == nonZeroSet[i]:
                indexList.append(index)
    outerList = []
    for index in range(len(indexList)):
        outerList.append(epList[indexList[index]])
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
    return -sum, subsetList, indexList, outerList


def main():
    datasetNames = ['Cap Shape', 'Cap Surface', 'Cap Color', 'Bruises', 'Odor', 'Gill Attachment', 'Gill Spacing',
                    'Gill Size', 'Gill Color', 'Stalk Shape', 'Stalk Root', 'Stalk Surface Above Ring',
                    'Stalk Surface Below Ring', 'Stalk Color Above Ring', 'Stalk Color Below Ring', 'Veil Type',
                    'Veil Color', 'Ring Number', 'Ring Type', 'Spore Print Color', 'Population', 'Habitat']
    readList = readData()
    firstRow = readList[0]
    mData = readList[1]
    x = 0
    while not(len(firstRow) == 1 or len(firstRow) == 0):
        maxGain = 0
        entropy = totalEntropy(firstRow)
        gainList = []
        for index in range(len(mData)):
            conEntropy = conditionalEntropy(mData[index], firstRow)
            gain = infoGain(entropy, conEntropy)
            gainList.append(gain)
            if gain > maxGain:
                bestList = conEntropy[1:]
                maxGain = gain
                iterValue = index
        print(f'Split on: {datasetNames[iterValue]}')
        splitList = []
        for index in range(len(mData)):
            mainList = []
            for i in range(len(bestList[1])):
                mainList.append(mData[index][bestList[1][i]])
            splitList.append(mainList)
        mData = splitList
        firstRow = bestList[2]
        mData.pop(iterValue)
        datasetNames.pop(iterValue)
        x += 1


main()
