from Exact_counter import Exact_counter
from Counter_prob_1_2 import Counter_prob_1_2
from Counter_log_base_2 import Counter_log_base_2
from Errors import Errors

def main():
    #print("\nExact counter")
    exact_counter = Exact_counter("example_file.txt")
    exact_counter.count_words()
    exact_result = exact_counter.get_final_counting()

    ##não passar o número de repetições na função ; fazer isso depois nos testes
    #print("\nCounter with prob 1/2")
    counter_prob_1_2 = Counter_prob_1_2("example_file.txt")
    counter_prob_1_2.count_words()
    prob_1_2_result = counter_prob_1_2.get_final_counting()

    #print("\nCounter with log base 2")
    counter_log_base_2 = Counter_log_base_2("example_file.txt")
    counter_log_base_2.count_words()
    prob_log_result = counter_log_base_2.get_final_counting()

    print("Prob 1_2")
    errors = Errors(exact_result, prob_1_2_result)
    errors.get_errors()

    print("\nLog base 2")
    errors = Errors(exact_result, prob_log_result)
    errors.get_errors()



main()