# *------------------* #
# Modules
import time, string, random
from fuzzywuzzy import fuzz
# *------------------* #
# Agent Class
class Agent:
    """This class implements the 'Agent' for the evolution purpose.
    """
    # Constructor
    def __init__( self, length, string_content = None, name = 'Unnamed' ):
        """Default Constructor
        """
        self.length = length
        if( string_content is None ):
            self.string_content = ''.join( [random.choice(string.printable) for _ in range(self.length)] )
        else:
            self.string_content = string_content
        self.name = name
        self.fitness = None
        return
    # String Representation
    def __str__( self ):
        """String Representation of the class instance.
        """
        string_rep = """Agent Name:     {}
String Length:  {}
String Content: {}
Agent Fitness:  {}""".format( self.name, self.length, self.string_content, self.fitness )
        return( string_rep )
# *------------------* #
# Do GA
def ga( target_string, target_length, N_population, N_generations, verbose = 0 ):
    """Do Genetic Algorithm Search
    """
    # Report Format
    report_format = '--------------\nGeneration: {}\nBest Agent Results\n{}'
    # Initialization
    agents = initialization( N_population = N_population, string_length = target_length )
    ## Main Loop
    for i in range(N_generations):
        # Assign Fitness
        agents = fitness( agents = agents, target_string = target_string )
        # Selection
        agents = selection( agents = agents )
        # Early-Stopping
        best_fitness = agents[0].fitness
        if( best_fitness >= 90 ):
            break
        #--------------------
        # Report
        if( (verbose > 0) and ( i%10**3 == 0 ) ):
            print(report_format.format( i, str(agents[0]) ))
        #--------------------
        # Cross-Over
        agents = crossover( agents = agents, N_population = N_population )
        # Mutation
        agents = mutation( agents = agents )
    # Last Sort
    agents = fitness( agents=agents, target_string=target_string )
    agents = sorted( agents, key = lambda agent: agent.fitness, reverse = True )
    # Report
    if( verbose > 0 ):
        print(report_format.format( i+1, str(agents[0]) ))
    # Retun
    return( agents )
# *------------------* #
# Initialize
def initialization( N_population, string_length ):
    """Initialize Agents
    """
    agents = [ Agent( length = string_length, name = '{}'.format(i) ) for i in range(N_population) ]
    return( agents )
# *------------------* #
# Fitness
def fitness( agents, target_string ):
    """Calculate fitness for each agent given the 'target_string'.
    """
    # Update Fitness
    for agent in agents:
        agent.fitness = fuzz.ratio( agent.string_content, target_string )
    # Return
    return( agents )
# *------------------* #
# Selection
def selection( agents, ratio = 0.2 ):
    """Select a ration of fittest agents.
    """
    # Sort by Fitness
    agents = sorted( agents, key = lambda agent: agent.fitness, reverse = True )
    # Slice
    agents = agents[ :int( ratio * len(agents) ) ] # Only Top
    # agents = agents[ :int( ratio * len(agents) / 2 ) ] + agents[ -int( ratio * len(agents) ):-int( ratio * len(agents)/2 ) ] # Top and Bottom
    # Return
    return( agents )
# *------------------* #
# Cross-Over
def crossover( agents, N_population ):
    """Cross over the agents.
    """
    # Offsprings
    offsprings = []
    # Create 2 Children per Mom-Pop pair
    for _ in range( int( (N_population - 2*len(agents)) / 2 ) ):
        # Random Parents
        parent1, parent2 = random.sample( agents, 2 )
        # Children Names
        child_length = parent1.length
        child_name = '({}_{})'.format( parent1.name, parent2.name )
        child_name1, child_name2 = '{}_1'.format( child_name ), '{}_2'.format( child_name )
        # Children Content
        slice_idx = random.randrange( child_length )
        child_content1 = parent1.string_content[:slice_idx] + parent2.string_content[slice_idx:]
        child_content2 = parent2.string_content[:slice_idx] + parent1.string_content[slice_idx:]
        # To Avoid Name Overflow
        child_name1, child_name2 = 'Unnamed', 'Unnamed'
        # Add Offsprings
        offsprings.append( Agent( length = child_length, string_content = child_content1, name = child_name1 ) )
        offsprings.append( Agent( length = child_length, string_content = child_content2, name = child_name2 ) )
    # Update Agents
    agents.extend( offsprings )
    # Return
    return( agents )
# *------------------* #
# Mutation
def mutation( agents, ratio = 0.2, hard_ratio = 0.01, soft_ratio = 0.1 ):
    """Mutate Agents based on Hard, Soft Ratio.
    Hard: Mutate Quarter of String
    Soft: Mutate Single Character
    """
    # Add Parents Unchanged
    agents += agents[ :int( ratio * len(agents) ) ]
    # Mutate
    for agent in agents[ int(ratio * len(agents)): ]:
        u = random.random() # Random Number
        length = agent.length # String Length
        indices_to_mutate = [] # Indices to Mutate
        if( u <= hard_ratio ): # Hard Mutation
            indices_to_mutate = random.sample( range(length), int( 0.25 * length ) )
        elif( u <= soft_ratio ): # Soft Mutation
            indices_to_mutate = [ random.randrange( length ) ]
        else:
            continue
        # If Mutation Occured
        string_list = list( agent.string_content ) # string to list of characters
        for idx in indices_to_mutate: # Change Indices
            string_list[idx] = random.choice( string.printable )
        # Set Agent's String Content
        agent.string_content = ''.join( string_list )
    # Return
    return( agents )
# *------------------------------* #
# Main
if __name__ == '__main__':
    # Parameters
    ## Target
    target_string = "Hello World!"
    target_length = len(target_string)
    ## Simulation
    N_population = 20
    N_generations = 10**5
    # Genetic Algorithm
    agents = ga( target_string=target_string, target_length=target_length, N_population=N_population, N_generations=N_generations, verbose = 1 )


























