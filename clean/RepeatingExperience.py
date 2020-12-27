"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

##Script that repeates the experience 10 times, for the original file (english)


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
    for i in range(num_repetitions):
        counter_prob_1_2 = Counter_prob_1_2(file_to_read)
        counter_prob_1_2.count_words()
        count+=1       
        rows.append([count,counter_prob_1_2.get_max(),counter_prob_1_2.get_min(),counter_prob_1_2.get_mean(), counter_prob_1_2.get_execution_time()])
    
    with open("Results/Prob1_2Counter/ENG/10_experiences.txt","w") as output:
        output.write(tabulate(rows,headers=headers))

def repeat_log_2(file_to_read, num_repetitions):
    count = 0
    headers = ["Repetition", "Max value", "Min value","Mean value", "Exec.time"]
    rows = []
    for i in range(num_repetitions):
        counter_log_base_2 = Counter_log_base_2(file_to_read)
        counter_log_base_2.count_words()
        count+=1       
        rows.append([count,counter_log_base_2.get_max(),counter_log_base_2.get_min(),counter_log_base_2.get_mean(), counter_log_base_2.get_execution_time()])
    
    with open("Results/LogBase2Counter/ENG/10_experiences.txt","w") as output:
        output.write(tabulate(rows,headers=headers))


if __name__ == '__main__':
    main("TextFiles/eng_hamlet.txt",10)