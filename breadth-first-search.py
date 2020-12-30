# Importing the necessary modules
from collections import defaultdict

# Defining the Adjacency List class to represent a graph
class AdjacencyList:

    # Constructor for the Adjacency List class
    def __init__(self):

        # Declaring the adjacency list (maps vertices to neighborhood lists)
        self.vertexToNeighbors = defaultdict(list)

    # Function to add an edge between vertex 'u' and vertex 'v'
    def addEdge(self, u, v):

        # Adds v to u's neighborhood list
        self.vertexToNeighbors[u].append(v)

    # Function to run a BFS and output the order in which vertices are discovered
    def runBFS(self, currVertex):

        # Stores the largest vertexID in the adjacency list 
        largestVertexID = max(self.vertexToNeighbors)

        # Stores the # of elements we'll store in our list that tracks which elements have been visited
        # Adds 1 to account for vertex #0
        maxNumVertices = largestVertexID + 1
        
        # Initializes a list of which vertices have been visited
        # Marks all vertices as not visited
        visited = [False] * maxNumVertices

        # Declares a queue for the BFS traversal
        queue = []

        # Enqueue the specified start node
        queue.append(currVertex)

        # Indicates that the starting node has been visited
        visited[currVertex] = True

        # While loop to continue while the list contains any elements
        while queue:

            # Dequeues (Removes the first element) from the list
            currVertex = queue.pop(0)    

            # Displays the starting element and leaves a single space (instead of a new line)
            print(currVertex, end = " ")

            # Evaluates each adjacent vertex of the current vertex 
            for neighbor in self.vertexToNeighbors[currVertex]:

                # Checks if the current neighbor has not been visited
                if visited[neighbor] == False:

                    # Adds the neighbor to the queue
                    queue.append(neighbor)

                    # Indicates that the neighbor has been visited
                    visited[neighbor] = True

# Instantiates an adjacency list
g = AdjacencyList()

# Adds edges to the graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# Preparing to display the BFS traversal order
print("\nHere's the Breadth-First traversal starting from vertex 2:")

# Runs the BFS and displays the order of vertex discovery
g.runBFS(2)

# Printing a new line to improve viewing
print()
