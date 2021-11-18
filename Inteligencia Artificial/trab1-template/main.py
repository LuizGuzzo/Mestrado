import time

from src.problems import MazeProblem
from src.viewer import MazeViewer
from src.search import breadth_first_search
from src.search import A_Pathfinding
from src.search import depth_first_search
from src.search import uniform_cost_search


def main():
    maze_problem = MazeProblem(n_rows=20, n_cols=20, seed=None) # seed = none ira gerar uma seed aleatoria e ira printa-la
    viewer = MazeViewer(maze_problem, step_time_miliseconds=20, zoom=20)


    data = []
    start = time.time()
    path, cost = breadth_first_search(maze_problem, viewer)
    end = time.time()
    timer = end - start
    data.append([len(path),cost,timer])
    show_table(data,"breadth")
    viewer.update(path=path)
    viewer.pause()

    data = []
    start = time.time()
    path, cost = A_Pathfinding(maze_problem, viewer)
    end = time.time()
    timer = end - start
    data.append([len(path),cost,timer])
    show_table(data,"A*")
    viewer.update(path=path)
    viewer.pause()

    data = []
    start = time.time()
    path, cost = depth_first_search(maze_problem, viewer)
    end = time.time()
    timer = end - start
    data.append([len(path),cost,timer])
    show_table(data,"Depth")
    viewer.update(path=path)
    viewer.pause()

    data = []
    start = time.time()
    path, cost = uniform_cost_search(maze_problem, viewer)
    end = time.time()
    timer = end - start
    data.append([len(path),cost,timer])
    show_table(data,"Uniform")
    viewer.update(path=path)
    viewer.pause()

    print("OK!")

def show_table(dados,type):
    print("tipo usado:",type)
    print("Path cost: \t Number of steps: \t Time: \t ")
    print("-------------------------------------------------------")
    for (cost,path,timer) in dados:
        if path == 0:
            print("Goal is unreachable for this maze.")
        else:
            #print("%f \t %d \t %f" % (cost,path-1,timer))
            print("{} \t {} \t {}".format(cost,path-1,timer))

if __name__ == "__main__":
    main()
