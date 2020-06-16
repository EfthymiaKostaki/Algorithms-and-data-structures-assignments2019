from collections import deque, defaultdict
import jellyfish
import sys

class Node:
    def __init__(self, word):
        self.word = word
        self.children = {}

    def getChildren(self):
        return self.children


class BKTree:
    def __init__(self):
        self.root = None
        self.to_check = None

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False


    def setRoot(self,word):
        self.root = Node(word)


    def getRoot(self):
        return self.root


    def getWord(self,node):
        return node.word


    def getChild(self,node, distance):
        if distance in node.children:
            return node.children[distance]
        return None

    def getChildren(self, node):
            return node.getChildren()


    def addChild(self, parent, distance, word):
            parent.children[distance] = Node(word)


    def BKTreeInsertion(self,word):
        if self.isEmpty():
            self.setRoot(word)
            return
        node = self.getRoot()
        
        while node != None:
             node_word = self.getWord(node)
             distance = jellyfish.levenshtein_distance(word, node_word)
             parent = node
             node = self.getChild(node, distance)
            
             if node == None:
                self.addChild(parent, distance, word)

    def IsQueueEmpty(self):
        if len(self.to_check) == 0:
            return True
        else:
            return False

    def BKTreeSearch(self, word, r):
        results = defaultdict(set)
        self.to_check = deque()
        self.to_check.append(self.root)
        
        while not self.IsQueueEmpty():
            node = self.to_check.popleft()
            node_word = self.getWord(node)
            distance = jellyfish.levenshtein_distance(word, node_word)
            if distance == r:
                results[distance].add(node)
            l = distance - r
            h = distance + r
            children = self.getChildren(node)
            
            for child in children.items():
                d = child[0]
                if l <= d <= h:
                    self.to_check.append(child[1])
        return results

    def reconstructPath(self, cameFrom, current):
        totalPath = list()
        totalPath.append(current)
        while current in cameFrom:
            current = cameFrom[current]
            totalPath.append(current)
        return totalPath[::-1]

    def AStar(self,goal):
        start = self.root.word
        openSet = set()
        openSet.add(start)
        closedSet = set()
        cameFrom = {}
        gScore = {}
        gScore[start] = 0
        fScore = {}
        fScore[start] = jellyfish.levenshtein_distance(start, goal)#heuristic

        while len(openSet) != 0:
            current = None
            currentFscore = None
            
            for pos in openSet:
                
                if current is None or fScore[pos] < currentFscore:
                    currentFscore = fScore[pos]
                    current = pos
                    
            if current == goal:
                return self.reconstructPath(cameFrom, current)

            openSet.remove(current)
            closedSet.add(current)

            for neighbor in self.BKTreeSearch(current, 1).items():
                
                for node in neighbor[1]:
                    if node.word in closedSet:
                        continue
                    tentative_gScore = gScore[current] + neighbor[0]

                    if node.word not in openSet:
                        openSet.add(node.word)

                    elif tentative_gScore >= gScore[node.word]:
                        continue
                        
                    cameFrom[node.word] = current
                    gScore[node.word] = tentative_gScore
                    fScore[node.word] = gScore[node.word] + jellyfish.levenshtein_distance(node.word, goal)#heuristic
        return start

def main():
    word = []
    tree = BKTree()
    f = open(sys.argv[1], "r")
    
    with f as graph_input:
        for line in graph_input:
            nodes = [str(x) for x in line.split()]
            if len(nodes) != 1:
                continue
            else:
                word.append(nodes[0])

    word1 = sys.argv[2]
    word1Exists = False
    word2 = sys.argv[3]
    word2Exists = False
    tree.BKTreeInsertion(word1)
    
    for i in word:
        
        if word1 != i:
            tree.BKTreeInsertion(i)
        else:
            word1Exists = True
        if word2 == i:
            word2Exists = True
            
    if word1Exists and word2Exists:
        path = tree.AStar(word2)
        print(path)
    else:
        print("One or both words don't exist")
        
        
main()
