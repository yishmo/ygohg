from itertools import product
from scipy.stats import hypergeom
from math import trunc

deck_sz = list(range(40, 61))
bomb_sz = list(range(1,41))
hand_sz = [5, 6]

prev = None
prevSampleSize = None

for combination in product(deck_sz, hand_sz, bomb_sz):
    popSize = combination[0]
    sampleSize = combination[1]
    successes = combination[2]

    print([popSize, successes, sampleSize])
    print("Deck Size:", popSize)
    print("Successes:", successes)
    print("Hand Size:", sampleSize)
    #new hand size tells us we need to reset prev
    if sampleSize != prevSampleSize:
        prev = None
        prevSampleSize = sampleSize
    rv = hypergeom(popSize, successes, sampleSize) 
    
    at_least_one = (1 - rv.pmf(0))
    exactly_one = rv.pmf(1)
    exactly_two = rv.pmf(2) 
    three_or_more = sum(rv.pmf(range(3, hand_sz[0] + 1)))

    print("% of at least 1:", round((at_least_one * 100), 2))
    print("% of exactly  1:", round((exactly_one* 100), 2))
    print("% of exactly  2:", round((exactly_two * 100), 2))
    print("% of 3 or more :", round((three_or_more * 100), 2))

    if prev != None:
        print('-------')
        print("C of at least 1:", round(((at_least_one - prev[0]) * 100), 2))
        print("C of exactly  1:", round(((exactly_one - prev[1]) * 100), 2))
        print("C of exactly  2:", round(((exactly_two - prev[2]) * 100), 2))
        print("C of 3 or more :", round(((three_or_more - prev[3]) * 100), 2))

    print()
    print()


    prev = [at_least_one]
    prev.append(exactly_one)
    prev.append(exactly_two)
    prev.append(three_or_more)
