import random
from collections import Counter
from collections import defaultdict 



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
    #test_words = read_file()
    test_words = ["ola","adeus","susu","universidade","ola","rua","susu","ola","ola"]
    #test_words = ["ola","ola"]
    #dicionario com todas as palavras que podem ocorrer e ir pondo o contador
    #primeiro criar ficheiros de teste, contagens exatas, com contador probabilistico e só depois o outro
    #para cada um guardar em ficheiros separados
    num_repetitions = [10]
    num_events_dict = {}
    for word in test_words: # 1 evento é uma palavra aparecer - primeiro contagens exatas
                                        # e depois outras - fazer por blocos
                                        #com blocos quis dizer scripts acho eu (?)
        for r in num_repetitions:
            occurrences = []
            #occurrences_count = [0] * (n+1)
            occurrences_count = defaultdict(int)
            count_word = {}

            #if word not in dict_words_cout:

            for i in range(r):
                if word not in num_events_dict: #If it is the first time occurring, the num of events for counter is 1
                    result = count_events(1)
                    occurrences.append(result)
                    occurrences_count[result] += 1 
                    num_events_dict[word] = dict(occurrences_count)
                else: #If it's not the first time, we have to pass the maximum value stored in the dictionary plus one -
                    #ex - if the term already appeared one time, one will be the maximum value so we have to increment 1,
                    #once it is appearing another time
                    print("max",max(num_events_dict[word]))
                    result = count_events(max(num_events_dict[word])+1)
                    occurrences.append(result)
                    occurrences_count[result] += 1               
                    num_events_dict[word] = dict(occurrences_count)
                #dict_words_cout[word] = occurrences
                #print(word,": ",result,"->",occurrences_count[result])
            #print(occurrences_count)
        #print("maximo ", max(num_events_dict[word]))
    print(num_events_dict)
        
main()