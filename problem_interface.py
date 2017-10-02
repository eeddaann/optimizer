class problem:
    def __init__(self,problem_parameters,penalty_epsilon,gradient_descent_epsilon,newton_epsilon):
        self.problem_parameters=problem_parameters #a list of all the parameters of the problem
        self.initial_vector=[] #the optimization process will start at this point
        self.penalty_epsilon=penalty_epsilon #precision of penalty method
        self.gradient_descent_epsilon=gradient_descent_epsilon #precision of gradient_descent method
        self.newton_epsilon=newton_epsilon #precision of newton method

    def objective_function(self,x):
        #calculates the value of the objective function at x=(x1,x2...xn)
        pass

    def penalty_function(self,x):
        #calculates the value of the penalty function at x=(x1,x2...xn)
        pass

    def theta_dx(self,x,z,t,mu,order):
        #calculates the order's derivative of: objective_function(x+t*z)+mu*penalty_function(x+t*z) with respect to t
        pass

    def gradient(self,x,mu=1):
        #calculates the gradient of: objective_function(x)+mu*penalty_function(x)
        pass

