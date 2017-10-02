
import math
import numpy as np
from scipy.misc import derivative


class problem:
    def __init__(self,k_list,m_list,a_dict,s,c,penalty_epsilon=0.05,gradient_descent_epsilon=0.5,newton_epsilon=0.5,start_from=False):
        '''
                the constructor for our problem
                :param k_list: weber constants
                :param m_list: minimal investment for each expanse
                :param a_dict: a dictionary that keeps the proportions between expanses
                :param s: the salary
                :param c: constant expanse
                :param penalty_epsilon:
                :param gradient_descent_epsilon:
                :param newton_epsilon:
                '''
        self.k_list=k_list
        self.m_list=m_list
        self.s=s
        self.c=c
        self.a_dict=a_dict #the keys are tupels of category numbers and the value is the proportion
        self.n=len(k_list)# the number of decision variables
        self.constraints=self.__constraints_generator() #list of the constraints as  functions
        if start_from==False:
            self.initial_vector=self.__initial_vector()
        else:
            self.initial_vector=start_from
        self.penalty_epsilon=penalty_epsilon
        self.gradient_descent_epsilon=gradient_descent_epsilon
        self.newton_epsilon=newton_epsilon

    def objective_function(self,x):
        '''
        the function that we want to minimize
        :param x: a list that represents a point
        :return: the value of the objective function at the given point x
        '''
        temp=0
        for i in range(self.n):
            temp-=self.k_list[i]*math.log(float(x[i])/self.m_list[i])
        return temp

    def penalty_function(self,x):
        '''
        the sum of all the constraints
        :param x: a list that represents a point
        :return: the value of the constraints at the given point x
        '''
        penalty=0
        for c in self.constraints.values():
            penalty+=c(x)

        return penalty

    def theta_dx(self,x,z,t,mu,order):
        '''
        calculates the order's derivative of: objective_function(x+t*z)+mu*penalty_function(x+t*z) with respect to t
        :param x: the initial point
        :param z:  minus the gradient
        :param t: theta
        :param order: derivative order
        :return: the optimal theta
        '''
        try: #this function is sensetive to math errors that relates to the derivative so we try to handle them using this statement
            obj_func= derivative(lambda t:sum([-self.k_list[i]+math.log((x+t*z[i])/float(self.m_list[i])) for i in range(self.n)]),t,n=order)# the derivate of the objective function with respect to t (theta)
            con_sum=0
            for constraint in self.constraints.keys(): #iterates over the constraints
                if self.constraints[constraint](x)>0:# if constraints are active set its value, otherwise if it's not active, ignore (sets its value to zero)
                    if constraint.startswith("sal"): # if the constraint is a salary one
                        con_sum+=mu*derivative(lambda t:sum([x[i]+t*z[i] for i in range(self.n)])+self.c-self.s,t,n=order) # calculate the derivative of the salary constraint function
                    if constraint.startswith("min"): #otherwise, it's a minimum expanse constraint
                        pos=int(constraint[4:])#takes only the index of each minimum constraint
                        con_sum+=mu*derivative(lambda t:self.m_list[pos]-x[pos],t,n=order) # calculates its derivative
                    if constraint.startswith("prop"): # if the constraint is of a proportion type
                        l=[int(constraint.split("_")[1]),int(constraint.split("_")[2])] #takes from each key-value pair in the dictionary only the indexes
                        con_sum+=mu*derivative(lambda t:-float(x[l[0]]+t*z[l[0]])/(x[l[1]]+t*l[1]),t,n=order) #calculates its derivative

            return obj_func+con_sum
        except Exception as e:
            return e

    def __initial_vector(self):
        a=[self.s*(5+np.random.random())/self.n for i in range(self.n)]# heuristic for initial vector
        return a

    def __constraints_generator(self):
        constraints = {"sal": lambda x: max(sum(x) + self.c - self.s, 0)}  # salary constraint
        for m in range(self.n):
            constraints["min_%s" % (str(m))] = lambda x: max(self.m_list[m] - x[m], 0)  # minimal investment constraints

        for key in self.a_dict.keys():
            constraints["prop_%s_%s" % (str(key[0]), str(key[1]))] = lambda x: max(
                self.a_dict[key] - (x[key[0]] / float(x[key[1]])),
                0)  # proportion constraints. sets in the constraint dictionary the proportion in a format-
            # a numerator and denumerator
        return constraints

    def objective_gradient(self,x):
        # the gradient of the objective function at the point x
        return [-self.k_list[i]/float(x[i]) for i in range(self.n)]

    def gradient(self,x,mu=1):
        # the gradient of the penalty function plus the mu
        return np.array(self.objective_gradient(x))+mu*np.array(self.constraints_gradient(x))

    def constraints_gradient(self,x): #the derivative of the constraints
        con_gradient=self.n*[0]
        for constraint in self.constraints.keys():# iterates over the constraints
            if self.constraints[constraint](x) > 0: # checks if the constraint is active
                if constraint=="sal": #if the constraint is a salary one
                    con_gradient=map(lambda t:t+1,con_gradient) #salary constraint gradient
                elif constraint.startswith("min"):
                    con_gradient[int(constraint[4:])]-=1 #minimal investment constraint gradient
                else: #proportion constraint gradient
                    l=[int(constraint.split("_")[1]),int(constraint.split("_")[2])] ##takes from each key-value pair in the dictionary only the indexes
                    con_gradient[l[0]]-=1.0/float(x[l[1]]) #the derivative in the point
                    con_gradient[l[1]]+=float(x[l[0]])/(x[l[1]]**2)
        return con_gradient






















