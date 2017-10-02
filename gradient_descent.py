import numpy as np
import newton as theta


def main(problem,x,mu):
    '''
    an implementation of the gradient decent method
    :param problem: an instance of a problem
    :param x: the initial vector
    :param mu: the current mu of the penalty function
    :return: an approximation for the optimal x
    '''
    x_old=np.array([0.1]*len(x)) #just to enter the loop
    x_new=np.array(x) #the initial vector
    while np.linalg.norm(x_new-x_old)>problem.gradient_descent_epsilon:# the distance between the previous iteration and the current one, if it's less than epsilon, then finish
        x_old=x_new #updates the old x to be the new one
        x_new=x_old-theta.main(problem,x_old,mu)*np.array(problem.gradient(x_old,mu))# improves the new x using the gradient decent method, using the theta from the newton module

    return list(x_new)
if __name__ == "__main__":
    main()

