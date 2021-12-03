import pandas as pd

def commonBit(position, l):
    sum = 0
    for num in l:
        #print(num)
        sum += int(num[position])
    if sum >= len(l)/2:
        return '1'
    else:
        return '0'

def uncommonBit(position, l):
    sum = 0
    for num in l:
        sum += int(num[position])
    if sum < len(l)/2:
        return '1'
    else:
        return '0'

def epsilon(l):
    length = len(l[0])
    epsilonList = []
    for i in range(length):
        bit = commonBit(i,l)
        epsilonList.append(bit)
    epsilon = int(''.join(epsilonList), 2)
    return epsilon

def gamma(l):
    length = len(l[0])
    gammaList = []
    for i in range(length):
        bit = uncommonBit(i,l)
        gammaList.append(bit)
    gamma = int(''.join(gammaList), 2)
    return gamma

def oxygen(l):
    candidates = pd.DataFrame(l,columns=['a'])
    length = len(l[0])
    remaining = len(candidates)
    for i in range(length):
        if remaining > 1:
            keepBit = commonBit(i,candidates['a'].astype(str))
            candidates = candidates[candidates['a'].apply(lambda x : x[i]==keepBit)]
            remaining = len(candidates)
    oxygenRating = int(''.join(candidates['a'].values[0]), 2)
    return oxygenRating

def c02(l):
    candidates = pd.DataFrame(l,columns=['a'])
    length = len(l[0])
    remaining = len(candidates)
    for i in range(length):
        if remaining > 1:
            keepBit = uncommonBit(i,candidates['a'].astype(str))
            candidates = candidates[candidates['a'].apply(lambda x : x[i]==keepBit)]
            remaining = len(candidates)
    c02Rating = int(''.join(candidates['a'].values[0]), 2)
    return c02Rating




if __name__ == '__main__':
    inputSeries = pd.read_csv('input.txt', header=None, dtype=[('a', str)]).values.flatten()
    epsilonValue = epsilon(inputSeries)
    gammaValue = gamma(inputSeries)
    print(f'Part 1: Epsilon in {epsilonValue}, gamma is {gammaValue} and their product is {epsilonValue * gammaValue}')

    oxygenRating = oxygen(inputSeries)
    c02Rating = c02(inputSeries)
    print(f'Part 2: Oxygen rating is {oxygenRating}, c02 rating is {c02Rating} and their product is {oxygenRating * c02Rating}')