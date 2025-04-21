from datetime import datetime
from point import Point
from visualiser import visualise_zip

import sys

class Solver():
    def __init__(self,grid,size):
        self.size = size
        self.spaces = size*size
        self.grid = grid

    def valid_moves(self, r, c, moves, left):
        # need to check for grid borders
        # and point / cell borders
        next_moves = []
        coordinate = tuple([r,c])
        point = Point() if not coordinate in self.grid else self.grid[coordinate]
        next_value = left[0]

        # right
        if r+1 < self.size and not point.right:
            next_moves.append(tuple([r+1, c]))
        # down
        if c+1 < self.size and not point.bottom:
            next_moves.append(tuple([r, c+1]))
        # left
        if 0 <= r-1 and not point.left:
            next_moves.append(tuple([r-1, c]))
        # up
        if 0 <= c-1 and not point.top:
            next_moves.append(tuple([r, c-1]))


        valid = []
        for move in next_moves:
            if move in moves:
                continue
            if move in self.grid and next_value is not None and next_value != self.grid[move].value and self.grid[move].value is not None:
                continue
            valid.append(move)

        return valid


    def solve(self):
        points_with_values = filter(lambda k: self.grid[k].value != None, self.grid.keys())
        sorted_pwv = sorted(points_with_values, key=lambda x: self.grid[x].value)
        # print(list(map(lambda x: self.grid[x], sorted_pwv)))

        start = sorted_pwv.pop(0)
        left = list(map(lambda x: self.grid[x].value, sorted_pwv))
        row = start[0]
        col = start[1]
        moves = [start]

        _, solution =  self.do_solve(row,col,moves,left)
        return solution

    def do_solve(self, r, c, moves, left):
        has_points_left = len(left) > 0
        has_unused_spaces = len(moves) < self.spaces

        if not has_points_left and has_unused_spaces: return False, []
        if not has_points_left and not has_unused_spaces: return True, moves

        # print(r,c, moves, left, has_points_left, has_unused_spaces)

        for next_valid_coordinate in self.valid_moves(r,c,moves,left):
            r_next, c_next = next_valid_coordinate
            v_next = Point() if not next_valid_coordinate in self.grid else self.grid[next_valid_coordinate]
            if v_next is not None:
                new_left = list(filter(lambda x:x != v_next.value, left))
                new_moves = [x for x in moves]
                new_moves.append(tuple([r_next, c_next]))
            solved, solution = self.do_solve(r_next, c_next, new_moves, new_left)  
            if solved:
                return True, solution
        return False, []


if __name__ == "__main__":
    # if len( sys.argv ) != 2:
    #     print("Requires image input")
    #     exit()
    # solver = Solver(sys.argv[1])
    # solved_at = datetime.strftime(datetime.now(), "%Y-%m-%d-%H:%M:%S.%f")

    # solution, _ = solver.solve(f"{solved_at}")

    # if solution is not None:
    #     print("solved")
    # else:
    #     print("failed")

    size = 3
    grid = {}
    grid[tuple([2,0])] = Point(1)
    grid[tuple([0,2])] = Point(2)
    grid[tuple([1,1])] = Point(top=True, bottom=True)

    solver = Solver(grid, size)
    print("input")
    print(solver.grid, solver.size, end="\n\n")
    solution = solver.solve()
    print("solution")
    print(solution, end="\n\n")

    solved_at = datetime.strftime(datetime.now(), "%Y-%m-%d-%H:%M:%S.%f")
    visualise_zip(grid, size, solution, f"{solved_at}")
