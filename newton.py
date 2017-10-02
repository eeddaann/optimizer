

def main(problem,x,mu=1):
    '''
        an implementation of newton method
        :param problem: an instance of a problem
        :param x: the current position
        :param mu: penalty mu
        :return: the theta for the gradient decent function
        '''
    t_old,t_new=110,100#a reasonable step if there is a math error
    try:

        while t_old-t_new>problem.newton_epsilon :
            t_old=t_new
            t_new = t_old - (problem.theta_dx(x, -problem.gradient(x, mu), t_old, mu, 1) / float(problem.theta_dx(x, -problem.gradient(x, mu), t_old, mu, 2)))  # impliments newton method
        return t_new


    finally:
        return t_new

if __name__ == "__main__":
        main()