"""
AA, January 2021
Assignment 2: Algoritmos Probabilísticos
Autor: Ana Sofia Fernandes, 88739
"""

##Class that calculates the errors, for each probabilistic counter, by comparing the exact counter with each one
##Of the probabilistics

class Errors:

    def __init__(self, exact_counter, prob_counter):
        self.exact_counter = exact_counter
        self.prob_counter = prob_counter
        self.min_rel_error = ""
        self.max_rel_error = ""
        self.avg_rel_error = ""

    def calculate_errors(self):
        """
        Calculates the minimum, maximum and average relative errors for the
        probabilistic counter that was passed
        """
        rel_errors = []
        for word in self.exact_counter:
            error = abs(self.exact_counter[word]-self.prob_counter[word])
            rel_error = round((error/self.exact_counter[word])*100, 3) #In percentage
            rel_errors.append(rel_error)
        rel_errors.sort()
        self.min_rel_error = str(rel_errors[0])
        self.max_rel_error = str(rel_errors[len(rel_errors)-1])
        self.avg_rel_error = str(round(sum(rel_errors)/len(rel_errors), 3))

    def get_min_rel_error(self):
        """
        Getter for the min rel error
        """
        return self.min_rel_error

    def get_max_rel_error(self):
        """
        Getter for the max rel error
        """
        return self.max_rel_error

    def get_mean_rel_error(self):
        """
        Getter for the mean rel error
        """
        return self.avg_rel_error
    

    def get_errors(self):
        """
        Getter for the relative errors
        """
        print("\n    Relative errors \n"
                    +"\n--- Minimum relative error:  %s " % (self.min_rel_error) + "%"
                    +"\n--- Maximum relative error:  %s " % (self.max_rel_error) + "%"   
                    +"\n--- Avg relative error:  %s " % (self.avg_rel_error) + "%") 

        

    

        


    
