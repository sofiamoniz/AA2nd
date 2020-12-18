import random
from collections import Counter

def read_file():
    final_words = []
    with open("example_file.txt","r") as file:
        final_words = file.read().split()
    return final_words

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
    test_words = read_file()
    #print("final ", final_words)
    test_dict = {"universidade":1, "algoritmos":1, "avancados":3} #isto aqui não vai ser preciso
    #num_events = [10,100,1000]
    #num_repetitions = [10,100,1000]
    #dicionario com todas as palavras que podem ocorrer e ir pondo o contador
    #primeiro criar ficheiros de teste, contagens exatas, com contador probabilistico e só depois o outro
    #para cada um guardar em ficheiros separados
    num_repetitions = [10]
    for word in test_dict:
        for n in range(test_dict[word]+1): #for n in num_events 1 evento é uma palavra aparecer - primeiro contagens exatas
                                            # e depois outras - fazer por blocos
                                            #com blocos quis dizer scripts acho eu (?)
            for r in num_repetitions:
                occurrences = []
                occurrences_count = [0] * (n+1)

                for i in range(r):
                    result = count_events(n)
                    occurrences.append(result)
                    occurrences_count[result] += 1
                    
                    print(word,": ",result,"->",occurrences_count[result])
                #print(occurrences)

main()