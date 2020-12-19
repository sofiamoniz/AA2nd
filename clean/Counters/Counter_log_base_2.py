"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

import random
from ReaderAndErrors.File_reader import File_reader

##Class that acts as a probabilistic counter with log base 2

class Counter_log_base_2:

    def __init__(self, file_to_read):
        self.word_counting_dict = {}
        self.file_reader = File_reader(file_to_read)

    def increment_counter(self,prob):
        """
        Return 1 with probability prob 
        Return 0 with probability (1-prob)
        """
        if random.random() < prob:
            return 1
        return 0

    def count_events(self,counter_prob,num_events=1):
        """
        Counting the number of events, using logarithmic counter
        """

        counter_value = 0

        for i in range(num_events):
            counter_value += self.increment_counter(counter_prob)

        return counter_value

    def count_words(self):
        """
        Counts the occurence of each word in a given file and saves it in
        a dictionary. The couting is made with a logarithmic counter
        with base 2.
        """
        self.file_reader.read_file()
        words = self.file_reader.get_final_words()
        for word in words:
            if word not in self.word_counting_dict:
                result = self.count_events(1-(1/2**0)) #P[Xi = 0 ] = 1 – 1 / 2^(i-1)
                self.word_counting_dict[word] = result
            else:
                result = self.count_events(1/(2**(self.word_counting_dict[word]-1))) #P[Xi] = 1 / 2^(i-1)
                self.word_counting_dict[word] += result
    
    def get_final_counting(self):
        """
        Getter for the dictionary with the final counting
        """
        return self.word_counting_dict