"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

##Script that runs the first example - Hamlet in Portuguese

from Counters.Exact_counter import Exact_counter
from Counters.Counter_prob_1_2 import Counter_prob_1_2
from Counters.Counter_log_base_2 import Counter_log_base_2
from ReaderAndErrors.Errors import Errors

def main(file_to_read):
    ###################
    # Create exact counter #
    ###################
    exact_counter = Exact_counter(file_to_read)
    exact_counter.count_words()
    exact_counter_result = exact_counter.get_final_counting()
    exact_counter.write_final_counting("Results/ExactCounter/ENG/final_counting.txt")
    exact_counter.write_top_20_words("Results/ExactCounter/ENG/eng_top_20_words.txt")

    ###################
    # Create fixed probability 1/2 counter #
    ###################
    counter_prob_1_2 = Counter_prob_1_2(file_to_read)
    counter_prob_1_2.count_words()
    prob_1_2_counter_result = counter_prob_1_2.get_final_counting()
    counter_prob_1_2.write_final_counting("Results/Prob1_2Counter/ENG/final_counting.txt")
    counter_prob_1_2.write_top_20_words("Results/Prob1_2Counter/ENG/eng_top_20_words.txt")

    ###################
    # Create log base 2 counter #
    ###################
    counter_log_base_2 = Counter_log_base_2(file_to_read)
    counter_log_base_2.count_words()
    prob_log_counter_result = counter_log_base_2.get_final_counting()
    counter_log_base_2.write_final_counting("Results/LogBase2Counter/ENG/final_counting.txt")
    counter_log_base_2.write_top_20_words("Results/LogBase2Counter/ENG/eng_top_20_words.txt")

    ###################
    # Get errors for each counter #
    ###################
    errors = Errors(exact_counter_result, prob_1_2_counter_result)
    errors.write_errors("Results/Prob1_2Counter/ENG/relative_errors.txt")

    errors = Errors(exact_counter_result, prob_log_counter_result)
    errors.write_errors("Results/LogBase2Counter/ENG/relative_errors.txt")

    ###################
    # Print information to the user #
    ###################
    print("\n    English example \n"
                +"\n--- Exact counter results can be found on folder Results/ExactCounter/ENG "
                +"\n--- Probabilistic counter with probability 1/2 results can be found on folder Results/Prob1_2Counter/ENG"   
                +"\n--- Probabilistic counter with log base 2 results can be found on folder Results/LogBase2Counter/ENG")


if __name__ == '__main__':
    main("TextFiles/eng_hamlet.txt")