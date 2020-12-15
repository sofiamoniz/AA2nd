"""
o número de eventos é o número de coisas que vais contar com o contador probabilistico. Por exemplo o número de carros 
que passam, se passarem 100 carros, são 100 eventos que contas ou não de acordo com a probabilidade do contador. 
Repetições refere-se ao número de vezes que repetes a experiência. Por exemplo, tem um contador que só adiciona metade do 
tempo(p=0.5). Para 1000 repetições tu contas o que o contador registou quando passaram 100 carros. Uma vez pode contar 50, 
outra vez conta só 48, etc. Isso são as repetições, o numero de vezes que repetiste a experiencia/simulação de contagem.
Como o contador para o mesmo número de eventos pode dar vários valores diferentes, tens de fazer várias repetições, 
para ver se ele é eficaz/preciso.
"""

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
    test_string = ["ola","adeus","algoritmos","avancados"]
    test_dict = {"ola":1, "adeus":1, "algoritmos":3}
    num_events = [10,100,1000]
    #num_repetitions = [10,100,1000]
    num_repetitions = [10]
    #print(sum(len(line.split()) for line in test_string))
    for word in test_dict:
        for n in range(test_dict[word]+1):
        #for n in [sum(len(line.split()) for line in test_string)-1]:
            for r in num_repetitions:
                occurrences = []
                occurrences_count = [0] * (n+1)
                #print('Experiment: counting {} events with fixed probability 1/2'.format(n))
                #print('Repeating the experiment {} times'.format(n))

                for i in range(r):
                    result = count_events(n)
                    occurrences.append(result)
                    occurrences_count[result] += 1
                    
                    print(word,": ",result,"->",occurrences_count[result])

main()

