"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

from ReaderAndErrors.File_reader import File_reader
from collections import Counter 
import time
from tabulate import tabulate

##Class that acts as an exact counter and counts the occurences of each word in file

class Exact_counter:

    def __init__(self, file_to_read):
        self.word_counting_dict = {}
        self.file_reader = File_reader(file_to_read)
        self.execution_time = 0

    def count_words(self):
        """
        Counts the occurence of each word in a given file and saves it in
        a dictionary. The couting is made with an exact counter.
        """
        self.file_reader.read_file()
        words = self.file_reader.get_final_words()
        start_time = time.time()
        for w in words:
            if w not in self.word_counting_dict:
                self.word_counting_dict[w] = 1
            else:
                self.word_counting_dict[w] += 1
        self.execution_time = time.time() - start_time
        self.word_counting_dict = {k: v for k, v in sorted(self.word_counting_dict.items(), key=lambda item: item[1], reverse=True)}

    def write_final_counting(self, output_file):
        """
        Write in file the final counting for exact counter, in descending order
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
            output.write("--- Top 20 words - exact counter:  " )
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

    def write_table(self, prob_1_2_counter_result, prob_log_counter_result, output_file):
        """
        Write to file a comparasion table between the counters
        """
        top_20_exact = self.get_top_20_words()
        rows = []
        headers=['Word','Exact counting','Prob 1/2 counting','Pos. in prob 1/2 counter','Counting diff', 'Top 20 of prob 1/2 counter?']
        with open(output_file,"w") as output:
            output.write("Comparasion between exact counter and counter with probability 1/2\n\n")
            for i in top_20_exact:
                if i[0] in prob_1_2_counter_result:
                    if (list(prob_1_2_counter_result.keys()).index(str(i[0])) <=19): #19 bc index starts at 0
                        rows.append([str(i[0]),str(i[1]),prob_1_2_counter_result[i[0]],list(prob_1_2_counter_result.keys()).index(str(i[0])), abs(i[1]-prob_1_2_counter_result[i[0]]), 'True'])
                    else:
                        rows.append([str(i[0]),str(i[1]),prob_1_2_counter_result[i[0]],list(prob_1_2_counter_result.keys()).index(str(i[0])), abs(i[1]-prob_1_2_counter_result[i[0]]), 'False'])
                else:
                    rows.append([str(i[0]),str(i[1]),'False','---', '---'])
            output.write(tabulate(rows,headers=headers))
            output.write("\n\nComparasion between exact counter and counter with log base 2\n\n")
            rows = []
            headers=['Word','Exact counting','Prob log 2 counting','Pos. in prob log 2 counting','Counting diff', 'Top 20 of prob log 2?']
            for i in top_20_exact:
                if i[0] in prob_log_counter_result:
                    if (list(prob_log_counter_result.keys()).index(str(i[0])) <=20):
                        rows.append([str(i[0]),str(i[1]),prob_log_counter_result[i[0]],list(prob_log_counter_result.keys()).index(str(i[0])), abs(i[1]-prob_log_counter_result[i[0]]), 'True'])
                    else:
                        rows.append([str(i[0]),str(i[1]),prob_log_counter_result[i[0]],list(prob_log_counter_result.keys()).index(str(i[0])), abs(i[1]-prob_log_counter_result[i[0]]), 'False'])
                else:
                    rows.append([str(i[0]),str(i[1]),'False','---', '---'])
            output.write(tabulate(rows,headers=headers))

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

