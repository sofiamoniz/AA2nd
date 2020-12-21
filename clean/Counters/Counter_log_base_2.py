"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

import random
import time
from ReaderAndErrors.File_reader import File_reader
from collections import Counter 

##Class that acts as a probabilistic counter with log base 2

class Counter_log_base_2:

    def __init__(self, file_to_read):
        self.word_counting_dict = {}
        self.file_reader = File_reader(file_to_read)
        self.execution_time = 0

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
        start_time = time.time()
        for word in words:
            if word not in self.word_counting_dict:
                result = self.count_events(1-(1/2**0)) #P[Xi = 0 ] = 1 – 1 / 2^(i-1)
                self.word_counting_dict[word] = result
            else:
                result = self.count_events(1/(2**(self.word_counting_dict[word]-1))) #P[Xi] = 1 / 2^(i-1)
                self.word_counting_dict[word] += result
        self.execution_time = time.time() - start_time

    def write_final_counting(self,output_file):
        """
        Write in file the final counting for counter with log base 2, in descending order
        """
        word_counting_ordered = {k: v for k, v in sorted(self.word_counting_dict.items(), key=lambda item: item[1], reverse=True)}
        with open(output_file,"w") as file:
            file.write("Execution time for counter with log base 2: "+str(round(self.execution_time,3))+" seconds.\n")
            file.write("\nNumber of words counted: "+ str(len(word_counting_ordered.keys()))+"\n")
            file.write("\nFinal word counting:\n")
            for word in word_counting_ordered:
                file.write("\n"+word+" -> "+str(word_counting_ordered[word]))

    def write_top_20_words(self, output_file):
        """
        Write in file the top 20 words
        """
        k = Counter(self.word_counting_dict) 
        high = k.most_common(20)
        with open(output_file,"w") as output:
            output.write("--- Top 20 words - counter with log base 2:  " )
            for i in high:
                output.write("\n"+str(i[0])+" -> "+str(i[1]))

    def get_final_counting(self):
        """
        Getter for the dictionary with the final counting
        """
        return self.word_counting_dict