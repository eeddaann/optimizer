import math
import gradient_descent
import plot

def main(problem):
    '''
    an implementation of the penalty method
    :param problem: an instance of a problem
    :return: returns a dictionary of {x: optimal point, function_value: the value of the objective function}
    '''
    mu=1
    results={"x":problem.initial_vector,"function_value":0,"penalty_value":0}
    while True:
        temp=gradient_descent.main(problem,results["x"],mu)
        '''
        #un-comment to plot the function
        plot.plot(problem.objective_function,problem.penalty_function,mu)
        '''
        results["x"]=temp# solves the problem using the gradient decent method
        results["penalty_value"]=problem.penalty_function(results["x"])# calculates the penalty value
        if results["penalty_value"]<=problem.penalty_epsilon:# if the penalty value is less than epsilon
            results["function_value"]=problem.objective_function(results["x"])# return the value of the objective function
            return results

        mu*=10# updates mu to be 10 times the last mu
if __name__ == "__main__":
    main()
