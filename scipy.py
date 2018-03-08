import random
import math
from scipy.stats import poisson
e = 2.71828182845904523
mut = []
data = []
N = 1000000
n = 100
theta = 40
a = 7.0/4/N
#a = 0

mutation_positions = 0
class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
        self.mutation = []
def posion(mean):
    p = poisson.rvs(mean,size = 1)
    return p[0]
def mutation_generate(nt,theta,mu_positions):
    if nt == 1:
        return []
    me = theta * 1.0 / (nt*(nt-1))
    mutation_number = posion(me)
    mutations = []
    for i in range(0,mutation_number):
        mutations.append(mu_positions+i)
    return mutations


def search_tree(node):
    global mutation_positions
    if node.lchild == None:
        #print "(",node.elem,")"
        for muts in mut:
            for mtts in muts:
                #print "mut",mtts
                data[node.elem][mtts] = 1
        return
    nt = n*2-node.elem
    thetat = theta * ((e ** (-1.0 * a)) ** (node.elem-n))
    gm = mutation_generate(nt,thetat,mutation_positions)
    mut.append(gm)
    mutation_positions += len(gm)
    #print mutation_positions
    search_tree(node.lchild)
    mut.pop()


    thetat =theta * ((e ** (-1.0 * a))**(node.elem-n))
    gm = mutation_generate(nt,thetat,mutation_positions)
    mut.append(gm)
    mutation_positions += len(gm)
    print mutation_positions
    search_tree(node.rchild)
    mut.pop()

def stimulator(n,theta,a):
    Tree = []
    Tree.append(Node(-1))
    individual = []
    coalescent_point = n+1
    for i in range(1,n+1):
        individual.append(i)
        data.append([])
    data.append([])
    for i in range(1,2*n):
        Tree.append(Node(i))
    #theatat = theta
    while(individual != []):
        left_node = individual[random.randint(0, len(individual)-1)]
        individual.remove(left_node)
        right_node = individual[random.randint(0, len(individual)-1)]
        individual.remove(right_node)
        if(individual == []):
            Tree[coalescent_point].lchild = Tree[left_node]
            Tree[coalescent_point].rchild = Tree[right_node]
            break
        Tree[coalescent_point].lchild = Tree[left_node]
        Tree[coalescent_point].rchild = Tree[right_node]
        individual.append(coalescent_point)
        coalescent_point += 1
    for da in data:
        for i in range(0,500):
            da.append(0)

    search_tree(Tree[-1])
    for i in range(1,len(data)):
        for j in range(0,mutation_positions):
            print data[i][j],
        print
    #print data


stimulator(n,theta,a)
