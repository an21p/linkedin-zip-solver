import unittest
from point import Point
from solver import Solver
from visualiser import visualise_zip, grid_dict_to_list
# from parameterized import parameterized

class TestSolver(unittest.TestCase):
    def test_can_solve_grid_1(self):
        # input
        #     0   1   2
        #   +---+---+---+
        # 0 |   |   | 2 |
        #   +---+---+---+
        # 1 |   |   |   |
        #   +---+---+---+
        # 2 | 1 |   |   |
        #   +---+---+---+
        #
        #  as a dict [(r,c), Point()]
        #  [(2,0) -> 1, (0,2) -> 2]
        #
        # 2 solutions
        # [(2,0), (1,0), (0,0), (0,1), (1,1), (2,1), (2,2), (1,2), (0,2)]
        # [(2,0), (2,1), (2,2), (1,2), (1,1), (1,0), (0,0), (0,1), (0,2)]
        #
        size = 3
        grid = {}
        grid[tuple([2,0])] = Point(1)
        grid[tuple([0,2])] = Point(2)

        solver = Solver(grid, size)
        assert [(2,0), (2,1), (2,2), (1,2), (1,1), (1,0), (0,0), (0,1), (0,2)] == solver.solve()

    def test_can_solve_grid_2(self):
        # input
        #     0   1   2
        #   +---+---+---+
        # 0 |   |   | 2 |
        #   +---+...+---+
        # 1 |   |   |   |
        #   +---+...+---+
        # 2 | 1 |   |   |
        #   +---+---+---+
        #
        #  as a dict [(r,c), Point()]
        #  [(2,0) -> 1, (1,1) -> (_, ,[F,T,F,T]), (0,2) -> 2]
        #
        # only 1 solution
        # [(2,0), (2,1), (2,2), (1,2), (1,1), (1,0), (0,0), (0,1), (0,2)]
        #
        size = 3
        grid = {}
        grid[tuple([2,0])] = Point(1)
        grid[tuple([0,2])] = Point(2)
        grid[tuple([1,1])] = Point(top=True, bottom=True)


        solver = Solver(grid, size)
        assert [(2,0), (1,0), (0,0), (0,1), (1,1), (2,1), (2,2), (1,2), (0,2)] == solver.solve()

    def test_can_solve_grid_sample(self):
        size = 6
        grid = {
            (0,0): Point(1),
            (1,4): Point(4),
            (2,1): Point(10),
            (2,3): Point(3),
            (2,5): Point(9),
            (3,0): Point(2),
            (4,1): Point(6),
            (4,3): Point(5),
            (5,2): Point(7),
            (5,4): Point(8),
        }
        grid_list = grid_dict_to_list(grid, size)
        visualise_zip(grid, size, grid_list, "2025_04_21_sample_grid", False)

        solver = Solver(grid, size)
        solution = solver.solve()
        # print(solution)
        visualise_zip(grid, size, solution, "2025_04_21_sample_solution")



    def test_can_solve_grid_2025_04_21_open(self):
        size = 6
        grid = {
            (0,1): Point(3),
            (1,1): Point(2),
            (1,4): Point(5),
            (4,1): Point(1),
            (4,4): Point(6),
            (5,4): Point(4),
        }

        grid_list = grid_dict_to_list(grid, size)
        visualise_zip(grid, size, grid_list, "2025_04_21_open_grid", False)

        solver = Solver(grid, size)
        solution = solver.solve()
        print(solution)
        visualise_zip(grid, size, solution, "2025_04_21_open")

    def test_can_solve_grid_sample(self):
        size = 6
        grid = {
            (0,0): Point(1),
            (1,4): Point(4),
            (2,1): Point(10),
            (2,3): Point(3),
            (2,5): Point(9),
            (3,0): Point(2),
            (4,1): Point(6),
            (4,3): Point(5),
            (5,2): Point(7),
            (5,4): Point(8),
        }
        grid_list = grid_dict_to_list(grid, size)
        visualise_zip(grid, size, grid_list, "2025_04_21_sample_grid", False)

        solver = Solver(grid, size)
        solution = solver.solve()
        # print(solution)
        visualise_zip(grid, size, solution, "2025_04_21_sample_solution")


    def test_can_solve_grid_2025_04_21_step(self):
        size = 6
        grid = {
            (0,1): Point(3),
            (1,1): Point(2, bottom=True),
            (2,1): Point(top=True),
            (1,4): Point(5),
            (3,4): Point(bottom=True),
            (4,1): Point(1),
            (4,4): Point(6, top=True),
            (5,4): Point(4),
        }

        grid_list = grid_dict_to_list(grid, size)
        visualise_zip(grid, size, grid_list, "2025_04_21_step_grid", False)

        solver = Solver(grid, size)
        solution = solver.solve()
        print(solution)
        visualise_zip(grid, size, solution, "2025_04_21_step_solution")


    def test_can_solve_grid_2025_04_21(self):
        size = 6
        grid = {
            (0,1): Point(3),
            (1,1): Point(2, bottom=True),
            (1,2): Point(bottom=True),
            (1,4): Point(5),
            (2,0): Point(right=True),
            (2,1): Point(left=True, top=True),
            (2,2): Point(top=True),
            (2,4): Point(right=True),
            (2,5): Point(left=True),
            (3,0): Point(right=True),
            (3,1): Point(left=True),
            (3,3): Point(bottom=True),
            (3,4): Point(bottom=True, right=True),
            (3,5): Point(left=True),
            (4,1): Point(1),
            (4,3): Point(top=True),
            (4,4): Point(6,top=True),
            (5,4): Point(4),
        }

        grid_list = grid_dict_to_list(grid, size)
        visualise_zip(grid, size, grid_list, "2025_04_21_grid", False)

        solver = Solver(grid, size)
        solution = solver.solve()
        print(solution)
        visualise_zip(grid, size, solution, "2025_04_21")

    