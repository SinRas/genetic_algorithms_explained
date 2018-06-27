# *------------------* #
# Modules
???
# *------------------* #
# Agent Class
class Agent:
    """This class implements the 'Agent' for the evolution purpose.
    """
    ???
# *------------------* #
# Do GA
def ga( ??? ):
    """Do Genetic Algorithm Search
    """
    # Report Format
    report_format = '--------------\nGeneration: {}\nBest Agent Results\n{}'
    # Initialization
    agents = initialization( ??? )
    ## Main Loop
    for i in range(N_generations):
        # Assign Fitness
        agents = fitness( ??? )
        # Selection
        agents = selection( ??? )
        # Early-Stopping Criteria
        ???
        #--------------------
        # Report
        if( (verbose > 0) and ( i%10**3 == 0 ) ):
            print(report_format.format( i, str(agents[0]) )) # If you have implemented `__str__` for 'Agent'
        #--------------------
        # Cross-Over
        agents = crossover( ??? )
        # Mutation
        agents = mutation( ??? )
    # Last Sort
    agents = fitness( ??? )
    agents = sorted( agents, key = lambda agent: agent.fitness, reverse = True )
    # Report
    if( verbose > 0 ):
        print(report_format.format( i+1, str(agents[0]) ))
    # Retun
    return( agents )
# *------------------* #
# Initialize
def initialization( ??? ):
    """Initialize Agents
    """

# *------------------* #
# Fitness
def fitness( ??? ):
    """Calculate fitness for each agent.
    """

# *------------------* #
# Selection
def selection( ??? ):
    """Select (a fraction) of fittest agents.
    """

# *------------------* #
# Cross-Over
def crossover( ??? ):
    """Cross over the agents.
    """
# *------------------* #
# Mutation
def mutation( ??? ):
    """Mutate agents.
    """
# *------------------------------* #
# Main
if __name__ == '__main__':
    # Parameters
    ## Target
    ???
    ## Simulation
    N_population = ???
    N_generations = ???
    # Genetic Algorithm
    agents = ga( ??? )