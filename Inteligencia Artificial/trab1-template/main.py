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

    start = time.time()
    path, cost = breadth_first_search(maze_problem, viewer)
    end = time.time()
    timer = end - start
    if len(path) == 0:
        print("Goal is unreachable for this maze.")
    print(f"Breadth Path cost: {cost}. Number of steps: {len(path)-1}. Time: {timer}")
    viewer.update(path=path)
    viewer.pause()

    start = time.time()
    path, cost = A_Pathfinding(maze_problem, viewer)
    end = time.time()
    timer = end - start
    if len(path) == 0:
        print("Goal is unreachable for this maze.")
    print(f"A* Path cost: {cost}. Number of steps: {len(path)-1}. Time: {timer}")
    viewer.update(path=path)
    viewer.pause()

    start = time.time()
    path, cost = depth_first_search(maze_problem, viewer)
    end = time.time()
    timer = end - start
    if len(path) == 0:
        print("Goal is unreachable for this maze.")
    print(f"Depth Path cost: {cost}. Number of steps: {len(path)-1}. Time: {timer}")
    viewer.update(path=path)
    viewer.pause()

    start = time.time()
    path, cost = uniform_cost_search(maze_problem, viewer)
    end = time.time()
    timer = end - start
    if len(path) == 0:
        print("Goal is unreachable for this maze.")
    print(f"Uniform Path cost: {cost}. Number of steps: {len(path)-1}. Time: {timer}")
    viewer.update(path=path)
    viewer.pause()

    print("OK!")


if __name__ == "__main__":
    main()
