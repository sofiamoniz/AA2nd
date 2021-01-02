"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

##Script that repeates the experience 10 times, for the original file (english) and writes its results


from Counters.Exact_counter import Exact_counter
from Counters.Counter_prob_1_2 import Counter_prob_1_2
from Counters.Counter_log_base_2 import Counter_log_base_2
from ReaderAndErrors.Errors import Errors
from tabulate import tabulate

def main(file_to_read, num_repetitions):
    ###################
    # Exact counter #
    ###################
    repeat_exact(file_to_read,num_repetitions)
    ###################
    # Fixed probability 1/2 counter #
    ###################
    repeat_prob_1_2(file_to_read,num_repetitions)
    ###################
    # Log base 2 counter #
    ###################
    repeat_log_2(file_to_read,num_repetitions)

    print("\n    Repeating experience " + str(num_repetitions) + " times with Hamlet in english\n"
                +"\n--- Probabilistic counter with probability 1/2 results can be found on folder Results/Prob1_2Counter/ENG in file 10_experiences.txt"   
                +"\n--- Probabilistic counter with log base 2 results can be found on folder Results/LogBase2Counter/ENG in file 10_experiences.txt")

def repeat_exact(file_to_read, num_repetitions):
    count = 0
    headers = ["Repetition", "Max value", "Min value","Mean value", "Exec.time"]
    rows = []
    for i in range(num_repetitions):
        exact_counter = Exact_counter(file_to_read)
        exact_counter.count_words()
        count+=1       
        rows.append([count,exact_counter.get_max(),exact_counter.get_min(),exact_counter.get_mean(), exact_counter.get_execution_time()])
    
    with open("Results/ExactCounter/ENG/10_experiences.txt","w") as output:
        output.write(tabulate(rows,headers=headers))

def repeat_prob_1_2(file_to_read, num_repetitions):
    count = 0
    headers = ["Repetition", "Max value", "Min value","Mean value", "Exec.time"]
    rows = []
    headers2 = ["Repetition","Max rel error", "Min rel error", "Mean rel error"]
    rows2=[]
    for i in range(num_repetitions):
        counter_prob_1_2 = Counter_prob_1_2(file_to_read)
        counter_prob_1_2.count_words()
        prob_1_2_counter_result = counter_prob_1_2.get_final_counting()
        exact_counter = Exact_counter(file_to_read)
        exact_counter.count_words()
        exact_counter_result = exact_counter.get_final_counting()
        errors = Errors(exact_counter_result, prob_1_2_counter_result)
        errors.calculate_errors()
        count+=1       
        rows.append([count,counter_prob_1_2.get_max(),counter_prob_1_2.get_min(),counter_prob_1_2.get_mean(), counter_prob_1_2.get_execution_time()])
        rows2.append([count,errors.get_max_rel_error(), errors.get_min_rel_error(), errors.get_mean_rel_error()])
    with open("Results/Prob1_2Counter/ENG/10_experiences.txt","w") as output:
        output.write(tabulate(rows,headers=headers))
        output.write("\n\n\n")
        output.write(tabulate(rows2,headers=headers2)) 

    
def repeat_log_2(file_to_read, num_repetitions):
    count = 0
    headers = ["Repetition", "Max value", "Min value","Mean value", "Exec.time"]
    rows = []
    headers2 = ["Repetition","Max rel error", "Min rel error", "Mean rel error"]
    rows2=[]
    for i in range(num_repetitions):
        counter_log_base_2 = Counter_log_base_2(file_to_read)
        counter_log_base_2.count_words()
        counter_log_base_2_result = counter_log_base_2.get_final_counting()
        exact_counter = Exact_counter(file_to_read)
        exact_counter.count_words()
        exact_counter_result = exact_counter.get_final_counting()
        errors = Errors(exact_counter_result, counter_log_base_2_result)
        errors.calculate_errors()
        count+=1
        rows.append([count,counter_log_base_2.get_max(),counter_log_base_2.get_min(),counter_log_base_2.get_mean(), counter_log_base_2.get_execution_time()])
        rows2.append([count,errors.get_max_rel_error(), errors.get_min_rel_error(), errors.get_mean_rel_error()])
    
    with open("Results/LogBase2Counter/ENG/10_experiences.txt","w") as output:
        output.write(tabulate(rows,headers=headers))
        output.write("\n\n\n")
        output.write(tabulate(rows2,headers=headers2))


if __name__ == '__main__':
    main("TextFiles/eng_hamlet.txt",10)