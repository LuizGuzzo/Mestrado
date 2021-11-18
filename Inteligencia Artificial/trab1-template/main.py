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

    resultado = []

    timers = []
    for _ in range(10):    
        start = time.time()
        path, cost = breadth_first_search(maze_problem, viewer)
        end = time.time()
        timer = end - start
        timers.append(timer)

    viewer.update(path=path)
    viewer.pause()
    avgtime = show_table(timers,"breadth")
    if len(path) == 0:
        print("Goal is unreachable for this maze.")
    print(f"Uniform Path cost: {cost}. Number of steps: {len(path)-1}. Time: {avgtime}")

    resultado.append(["breadth",cost,len(path)-1,avgtime])

    timers = []
    for _ in range(10):    
        start = time.time()
        path, cost = A_Pathfinding(maze_problem, viewer)
        end = time.time()
        timer = end - start
        timers.append(timer)

    viewer.update(path=path)
    viewer.pause()
    avgtime = show_table(timers,"A*")
    if len(path) == 0:
        print("Goal is unreachable for this maze.")
    print(f"Uniform Path cost: {cost}. Number of steps: {len(path)-1}. Time: {avgtime}")

    resultado.append(["A*     ",cost,len(path)-1,avgtime])

    timers = []
    for _ in range(10):    
        start = time.time()
        path, cost = depth_first_search(maze_problem, viewer)
        end = time.time()
        timer = end - start
        timers.append(timer)

    viewer.update(path=path)
    viewer.pause()
    avgtime = show_table(timers,"Depth")
    if len(path) == 0:
        print("Goal is unreachable for this maze.")
    print(f"Uniform Path cost: {cost}. Number of steps: {len(path)-1}. Time: {avgtime}")

    resultado.append(["Depth  ",cost,len(path)-1,avgtime])

    timers = []
    for _ in range(10):    
        start = time.time()
        path, cost = uniform_cost_search(maze_problem, viewer)
        end = time.time()
        timer = end - start
        timers.append(timer)

    viewer.update(path=path)
    viewer.pause()
    avgtime = show_table(timers,"Uniform")
    if len(path) == 0:
        print("Goal is unreachable for this maze.")
    print(f"Uniform Path cost: {cost}. Number of steps: {len(path)-1}. Time: {avgtime}")

    resultado.append(["Uniform",cost,len(path)-1,avgtime])

    print("Tipo: \t Path Cost: \t Steps: \t Time:")
    print("-----------------------------------------------")
    for (tipo,cost,path,avgtime) in resultado:
        print(f"{tipo} \t {cost:.2f} \t {path} \t {avgtime:.4f}")

    print("OK!")

def show_table(dados,type):
    time = 0
    print("")
    print("tipo usado:",type)
    print("\t Times: \t ")
    print("---------------------------------------")
    for timer in dados:
        time += timer
        print("\t {} \t".format(timer))

    print("Tempo medio:", time/10)
    print("---------------------------------------")
    return time/10

if __name__ == "__main__":
    main()
