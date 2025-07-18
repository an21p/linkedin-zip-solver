import unittest
from point import Point
from solver import Solver
from visualiser import visualise_zip, grid_dict_to_list

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
        grid = {
            (0,2): Point(value=2),
            (2,0): Point(value=1),
        }

        solver = Solver(grid, size)
        assert [(2,0), (1,0), (0,0), (0,1), (1,1), (2,1), (2,2), (1,2), (0,2)] == solver.solve()

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
        grid = {
            (0,1): Point(bottom=True),
            (0,2): Point(value=2),
            (1,1): Point(top=True, bottom=True),
            (2,0): Point(value=1),
            (2,1): Point(top=True),
        }

        solver = Solver(grid, size)
        assert [(2, 0), (2, 1), (2, 2), (1, 2), (1, 1), (1, 0), (0, 0), (0, 1), (0, 2)] == solver.solve()

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
        visualise_zip(grid, size, solution, "2025_04_21_sample_solution")
        assert solution == [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (0, 3), (0, 2), (1, 2), (2, 2), (2, 1)]

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
        visualise_zip(grid, size, solution, "2025_04_21_open_solution")
        assert solution == [(4, 1), (4, 0), (5, 0), (5, 1), (5, 2), (4, 2), (3, 2), (3, 1), (3, 0), (2, 0), (2, 1), (1, 1), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (4, 3), (3, 3), (2, 3), (2, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]

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
        visualise_zip(grid, size, solution, "2025_04_21_step_solution")
        assert solution == [(4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (1, 2), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (4, 2), (4, 3), (4, 4)]

    def test_can_solve_grid_2025_04_21_full(self):
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
        visualise_zip(grid, size, grid_list, "2025_04_21_full_grid", False)

        solver = Solver(grid, size)
        solution = solver.solve()
        visualise_zip(grid, size, solution, "2025_04_21_full_solution")
        assert solution == [(4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (1, 2), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (4, 2), (4, 3), (4, 4)]


    def test_can_solve_grid_2025_0_full(self):
        size = 8
        grid = {
            (0,2): Point(8),
            (0,5): Point(9),
            (1,2): Point(18),
            (1,5): Point(17),
            (2,0): Point(6),
            (2,1): Point(7),
            (2,2): Point(19),
            (2,5): Point(20),
            (2,6): Point(16),
            (2,7): Point(10),
            (5,0): Point(5),
            (5,1): Point(2),
            (5,2): Point(13),
            (5,5): Point(1),
            (5,6): Point(15),
            (5,7): Point(11),
            (6,2): Point(3),
            (6,5): Point(14),
            (7,2): Point(4),
            (7,5): Point(12),
        }

        grid_list = grid_dict_to_list(grid, size)
        visualise_zip(grid, size, grid_list, "2025_06_26_full_grid", False)

        solver = Solver(grid, size)
        solution = solver.solve()
        visualise_zip(grid, size, solution, "2025_06_26_full_solution")
