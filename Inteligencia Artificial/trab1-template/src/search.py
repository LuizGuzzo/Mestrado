
from math import inf

from collections import deque
from typing import Any, List, Union, Tuple

from src.problems import ProblemInterface
from src.viewer import ViewerInterface


class  Node:
    # The output path is generated backwards starting from
    # the goal node, hence the need to store the parent in
    # the node.
    def __init__(self, state: Any, action=None, previous_node=None, Fcost=None, weight=None):
        self.state = state
        self.action = action
        self.previous_node = previous_node
        self.Fcost = Fcost
        self.weight = weight
        

    def __repr__(self):
        return f"Node(state={self.state}, action={self.action}, previous_node={self.previous_node})"

    def __eq__(self, n) -> bool:
        return (self.state == n.state)

    # method necessary for easily checking if nodes
    # have already been added to sets or used as keys
    # in dictionaries.
    def __hash__(self):
        return hash(self.state)

def depth_first_search(problem: ProblemInterface, viewer: ViewerInterface) -> Tuple[List[Any], float]:
     # generated nodes that were not expanded yet
    to_explore = deque()

    # nodes whose neighbors were already generated
    expanded = set()

    # add the starting node to the list of nodes
    # yet to be expanded.
    state_node = Node(problem.initial_state())
    to_explore.append(state_node)

    # variable to store the goal node when it is found.
    goal_found = None

    # Repeat while we haven't found the goal and still have
    # nodes to expand. If there aren't further nodes
    # to expand in breadth-first search, the goal is
    # unreachable.
    while (len(to_explore) > 0) and (goal_found is None):
        # select next node or expansion
        state_node = to_explore.pop()

        neighbors = _generate_neighbors(state_node, problem)  # pega os vizinhos do nó

        for n in neighbors:
            if (n not in expanded) and (n not in to_explore): # verifica se ja foi expandido ou explorado
                if problem.is_goal(n.state): # verifica se é o objetivo
                    goal_found = n
                    break
                to_explore.append(n)

        expanded.add(state_node)

        #viewer.update(state_node.state, generated=to_explore, expanded=expanded)

    path = _extract_path(goal_found)
    cost = _path_cost(problem, path)

    return path, cost


def A_Pathfinding(problem: ProblemInterface, viewer: ViewerInterface) -> Tuple[List[Any], float]:

    '''
    OPEN # the set of nodes to be evaluated
    expanded # the set of nodes already evaluated
    add the start node to OPEN

    loop
        current = node in OPEN with the lowest f_cost
        remove current from OPEN
        add current to CLOSED

        if current is the target node #path has been found
            return
        
        foreach neighbour of the current node
            if neighbour is not traversable or neighbour is in CLOSED
                skip to the next neighbour
            
            if new path to neighbour is shorter OR neighbour is not in OPEN
                set f_cost of neighbour
                set parent of neighbour to current
                if neighbour is not in OPEN
                    add neighbour to OPEN

    '''
    OPEN = deque()
    CLOSED = set()

    state_node = Node(problem.initial_state(),Fcost=0)
    OPEN.append(state_node)

    goal_found = None

    while((len(OPEN)> 0) and (goal_found is None)):
        
        # acha o node do Open com menor f_cost
        # remove o node do Open
        # adiciona-o no Closed
        aux = Node(state= (-1,-1), Fcost = inf)
        
        state_node = aux #altera so para extrair o menor
        for node in OPEN:
            if node.Fcost < state_node.Fcost:
                state_node = node
        
        OPEN.remove(state_node)
        CLOSED.add(state_node)

        # verifica se o node atual é o Goal
            # sai do loop
        if problem.is_goal(state_node.state): # verifica se é o objetivo
            goal_found = state_node
            break
        
        # pega os vizinhos do node
        neighbors = _generate_neighbors(state_node, problem)  # pega os vizinhos do nó
        # para cada vizinho do node atual
        for n in neighbors:
            # verifica se o vizinho esta no closed
            if (n in CLOSED):
                # se sim pula
                continue
            # se o caminho para o vizinho for f_cost menor OU o vizinho nao esta em OPEN
            Fcost = _fcost(n.state,problem)
            if ((Fcost<n.Fcost) or (n not in OPEN)):
                # define o f_cost do vizinho
                n.Fcost = Fcost
                # define o previous_node do vizinho para o node atual
                n.previous_node = state_node
                # se o vizinho nao esta em Open
                if n not in OPEN:
                    # adiciona o vizinho no Open
                    OPEN.append(n)

        #viewer.update(state_node.state, generated=OPEN, expanded=CLOSED)

    path = _extract_path(goal_found)
    cost = _path_cost(problem, path)

    return path, cost


def breadth_first_search(problem: ProblemInterface, viewer: ViewerInterface) -> Tuple[List[Any], float]:
    # generated nodes that were not expanded yet
    to_explore = deque() # me parece ser uma lista com Pop e append bem rapidos em ambos os lados

    # nodes whose neighbors were already generated
    expanded = set() # uma coleçao desorganizada

    # add the starting node to the list of nodes
    # yet to be expanded.
    state_node = Node(problem.initial_state())
    to_explore.append(state_node)

    # variable to store the goal node when it is found.
    goal_found = None

    # Repeat while we haven't found the goal and still have
    # nodes to expand. If there aren't further nodes
    # to expand in breadth-first search, the goal is
    # unreachable.
    while (len(to_explore) > 0) and (goal_found is None):
        # select next node or expansion
        state_node = to_explore.popleft()

        neighbors = _generate_neighbors(state_node, problem)  # pega os vizinhos do nó

        for n in neighbors:
            if (n not in expanded) and (n not in to_explore): # verifica se ja foi expandido ou explorado
                if problem.is_goal(n.state): # verifica se é o objetivo
                    goal_found = n
                    break
                to_explore.append(n)

        expanded.add(state_node)

        #viewer.update(state_node.state, generated=to_explore, expanded=expanded)

    path = _extract_path(goal_found)
    cost = _path_cost(problem, path)

    return path, cost


def uniform_cost_search(problem: ProblemInterface, viewer: ViewerInterface) -> Tuple[List[Any], float]:
    to_explore = deque() # uma fila que so pode sair com prioridade qm tem o menor custo
    expanded = set() # uma coleçao de quem ja foi expandido

    state_node = Node(problem.initial_state(),weight=0)
    to_explore.append(state_node)

    goal_found = None

    """
    extrai o nó com menor peso da lista explorer
    adiciona-o no expanded
    verifica se o nó é o goal
        goalfound break
    expande os vizinhos
    para cada vizinho gerado
        calcula o seu peso (peso do no + do vizinho)
        se nao esta no expanded
            se esta no explorer mas o peso é menor
                atualiza o nó que esta no explorer pro novo previous_state e weight
            adiciona no vizinho o nó

    """


    while (len(to_explore) > 0) and (goal_found is None):
        # acha o node do to_explore com menor peso
        # remove o node do to_explore
        # adiciona-o no expanded
        aux = Node(state= (-1,-1), weight = inf)
        
        state_node = aux #altera so para extrair o menor
        for node in to_explore:
            if node.weight < state_node.weight:
                state_node = node
        
        to_explore.remove(state_node)
        expanded.add(state_node)

        # verifica se o node atual é o Goal
            # sai do loop
        if problem.is_goal(state_node.state): # verifica se é o objetivo
            goal_found = state_node
            break
        
        # pega os vizinhos do node
        neighbors = _generate_neighbors(state_node, problem)  # pega os vizinhos do nó
        # para cada vizinho do node atual
        for n in neighbors:
            weight = state_node.weight + n.weight
            # verifica se o vizinho esta no expanded
            if (n in expanded):
                # se sim pula
                continue
            # se o caminho para o vizinho for peso menor OU o vizinho nao esta em to_explore
            if ((weight < n.weight) or (n not in to_explore)):
                # define o peso do vizinho
                n.weight = weight
                # define o previous_node do vizinho para o node atual
                n.previous_node = state_node
                # se o vizinho nao esta em to_explore
                if n not in to_explore:
                    # adiciona o vizinho no to_explore
                    to_explore.append(n)

        #viewer.update(state_node.state, generated=to_explore, expanded=expanded)

    path = _extract_path(goal_found)
    cost = _path_cost(problem, path)

    return path, cost 

def _path_cost(problem: ProblemInterface, path: List[Node]) -> float:
    if len(path) == 0:
        return inf
    cost = 0
    for i in range(1, len(path)):
        cost += problem.step_cost(path[i].previous_node.state,
                                  path[i].action,
                                  path[i].state)
    return cost


def _extract_path(goal: Union[Node, None]) -> List[Node]:
    path = []
    state_node = goal
    while state_node is not None:
        path.append(state_node)
        state_node = state_node.previous_node
    path.reverse()
    return path


def _generate_neighbors(state_node: Node, problem: ProblemInterface) -> List[Node]:
    # generate neighbors of the current state
    neighbors = []
    state = state_node.state
    available_actions = problem.actions(state) # retorna os states vizinhos disponiveis do state enviado
    for action in available_actions:
        next_state = problem.transition(state, action) #action é o state repetindo

        Fcost = _fcost(next_state,problem)
        weight = _calc_weight(next_state,problem)

        neighbors.append(Node(next_state, action, state_node, Fcost, weight))
    return neighbors

def _fcost(node_state: Node, problem: ProblemInterface) -> float:
    Gcost = problem.step_cost(problem.initial_state(),None,node_state)
    Hcost = problem.heuristic_cost(node_state)
    Fcost = Gcost + Hcost
    return Fcost

def _calc_weight(node_state: Node, problem: ProblemInterface) -> float:
    #weight = problem.step_cost(problem.initial_state(),None,node_state)
    weight = problem.heuristic_cost(node_state)
    return weight