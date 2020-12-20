import random
from collections import Counter


#Probabilistic Counter with fixed probability

def increment_counter(prob=0.5):
    """Return 1 with probability prob 
        Return 0 with probability (1-prob)"""
    if random.random() < prob:
        return 1
    return 0

def count_events(num_events=1, counter_prob=0.5):
    """Counting num_events with a fixed probability counter_prob"""

    counter_value = 0

    for i in range(num_events):
        counter_value += increment_counter(counter_prob)

    return counter_value

def main():
    test_string = ["universidade","algoritmos","algoritmos","avancados","avancados","avancados"]
    #num_events = [10,100,1000]
    #num_repetitions = [10,100,1000]
    num_repetitions = [5]
    #print(sum(len(line.split()) for line in test_string))
    for word in test_string:
        for n in range(len(test_string)): #for n in num_events
            for r in num_repetitions:

                occurrences = []
                occurrences_count = [0] * (n+1)

                for i in range(r):
                    result = count_events(n)
                    occurrences.append(result)
                    occurrences_count[result] += 1
                    
                    print(word,": ",result,"->",occurrences_count[result])

main()

