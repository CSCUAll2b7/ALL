def AStar(self, start, goal):
    	# takes start and goal positions of the object and creates most optimal path between them, uses lists to store child nodes 

        array = self.array
        closedSet = []
        
        openSet = [start]

        cameFrom = {}

        gScore = {}
        gScore[start] = 0

        fScore = {}
        fScore[start] = self.heuristic_cost_estimate(start, goal)

        
        while openSet != [] :
            
            current = self.lowestValue(openSet, fScore)
            if current.x == goal.x and current.y == goal.y:
                return self.reconstructPath(cameFrom, goal)
            
            openSet.remove(current)
            closedSet.append(current)

            neighbourNodes = []
            if current.x > 0:
                if array[current.x -1][current.y] == 0:
                    neighbourNodes.append(Node(current.x -1, current.y))
                    
            if current.y > 0:
                if array[current.x][current.y - 1] == 0:
                    neighbourNodes.append(Node(current.x, current.y - 1))

            if current.x != self.boundsx - 1:
                if array[current.x + 1][current.y] == 0:
                        neighbourNodes.append(Node(current.x + 1, current.y))

            if current.y != self.boundsy - 1:    
                if array[current.x][current.y + 1] == 0:
                        neighbourNodes.append(Node(current.x, current.y + 1))
                        
            for neighbour in neighbourNodes:
                if self.linearSearch(closedSet, neighbour):
                    continue
                
                tentative_gScore = gScore[current] + 1

                if not self.linearSearch(openSet, neighbour):
                    openSet.append(neighbour)
                elif tentative_gScore >= gScore[neighbour]:
                    continue
                
                cameFrom[neighbour] = current
                gScore[neighbour] = tentative_gScore
                fScore[neighbour] = gScore[neighbour] + self.heuristic_cost_estimate(neighbour, goal)
             
        return False
