"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

from File_reader import File_reader

##Class that acts as an exact counter and counts the occurences of each word in file

class Exact_counter:

    def __init__(self, file_to_read):
        self.word_counting_dict = {}
        self.file_reader = File_reader(file_to_read)

    def count_words(self):
        """
        Counts the occurence of each word in a given file and saves it in
        a dictionary. The couting is made with an exact counter.
        """
        self.file_reader.read_file()
        words = self.file_reader.get_final_words()

        for w in words:
            if w not in self.word_counting_dict:
                self.word_counting_dict[w] = 1
            else:
                self.word_counting_dict[w] += 1
        
    def get_final_counting(self):
        """
        Getter for the dictionary with the final counting
        """
        return self.word_counting_dict