import our_problem as op
import penalty

def main():

    print '#### kkt solution ####'
    kkt_problem = op.problem([0.7, 0.3], [300, 1], {(0, 1): 1.5}, 4000, 1000, start_from=[5000, 1000])
    print {'function_value':kkt_problem.objective_function([2100,900]),"x":[2100,900],'penalty_value':kkt_problem.penalty_function([2100,900])}
    print '#### numeric solution for kkt problem ####'
    print(penalty.main(kkt_problem))
    print '####harder problem numeric solution ####'
    harder_problem = op.problem([0.7, 0.3, 0.4, 0.6], [300, 1, 100, 50], {(0, 1): 1.5, (2, 3): 1.2}, 4000, 1000,start_from=[5100, 5200, 5300, 5400])
    print(penalty.main(harder_problem))


if __name__ == "__main__":
    main()