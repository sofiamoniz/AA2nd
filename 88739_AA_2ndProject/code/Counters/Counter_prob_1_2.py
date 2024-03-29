"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

import time
import random
from ReaderAndErrors.File_reader import File_reader
from collections import Counter 

##Class that acts as a probabilistic counter with fixed probability 1/2

class Counter_prob_1_2:

    def __init__(self, file_to_read):
        self.word_counting_dict = {}
        self.file_reader = File_reader(file_to_read)
        self.execution_time = 0

    def increment_counter(self,prob=0.5):
        """
        Return 1 with probability prob 
        Return 0 with probability (1-prob)
        """
        if random.random() < prob:
            return 1
        return 0

    def count_events(self,num_events=1, counter_prob=0.5):
        """
        Counting the number of events, using a probability of 1/2
        """

        counter_value = 0

        for i in range(num_events):
            counter_value += self.increment_counter(counter_prob) #increment counter

        return counter_value

    def count_words(self):
        """
        Counts the occurence of each word in a given file and saves it in
        a dictionary. The couting is made with a counter of fixed prob of 1/2.
        """
        self.file_reader.read_file()
        words = self.file_reader.get_final_words()
        start_time = time.time()
        for word in words:
            if word not in self.word_counting_dict:
                result = self.count_events()
                self.word_counting_dict[word] = result
            else:
                result = self.count_events()
                self.word_counting_dict[word] += result
        self.execution_time = time.time() - start_time
        self.word_counting_dict = {k: v for k, v in sorted(self.word_counting_dict.items(), key=lambda item: item[1], reverse=True)} #sort in descending order
    
    def write_final_counting(self, output_file):
        """
        Write in file the final counting for counter with probability 1/2, in descending order
        """
        with open(output_file,"w") as file:
            file.write("\nNumber of words counted: "+ str(len(self.word_counting_dict.keys()))+"\n")
            file.write("\nFinal word counting:\n")
            for word in self.word_counting_dict:
                file.write("\n"+word+" -> "+str(self.word_counting_dict[word]))

    def write_top_20_words(self, output_file):
        """
        Write in file the top 20 words
        """
        high = self.get_top_20_words()
        with open(output_file,"w") as output:
            output.write("--- Top 20 words - counter with probability 1/2:  " )
            for i in high:
                output.write("\n"+str(i[0])+" -> "+str(i[1]))

    def get_final_counting(self):
        """
        Getter for the dictionary with the final counting
        """
        return self.word_counting_dict

    def get_top_20_words(self):
        """
        Getter for the most 20 counted words
        """
        k = Counter(self.word_counting_dict) 
        return k.most_common(20)

    def get_max(self):
        """
        Getter for max counting
        """
        max_word = str(max(self.word_counting_dict, key=self.word_counting_dict.get))
        max_word_couting = str(self.word_counting_dict[max_word])
        return max_word+" : "+max_word_couting

    def get_min(self):
        """
        Getter for min counting
        """
        min_word = str(min(self.word_counting_dict, key=self.word_counting_dict.get))
        min_word_couting = str(self.word_counting_dict[min_word])
        return min_word+" : "+min_word_couting

    def get_mean(self):
        """
        Getter for mean counting
        """
        total_counting = 0
        for word in self.word_counting_dict:
            total_counting += self.word_counting_dict[word]
        return round(total_counting/len(self.word_counting_dict), 5)

    def get_execution_time(self):
        """
        Getter for execution time
        """
        return round(self.execution_time,3)