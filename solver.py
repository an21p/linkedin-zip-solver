from datetime import datetime
from typing import Dict, Tuple, List, Optional
from point import Point
from visualiser import visualise_zip


class Solver:
    def __init__(self, grid: Dict[Tuple[int, int], Point], size: int) -> None:
        self.size: int = size
        self.spaces: int = size * size
        self.grid: Dict[Tuple[int, int], Point] = grid

    def valid_moves(self, r: int, c: int, moves: List[Tuple[int, int]], left: List[Optional[int]]) -> List[Tuple[int, int]]:
        next_moves: List[Tuple[int, int]] = []
        coordinate: Tuple[int, int] = (r, c)
        point: Point = self.grid[coordinate] if coordinate in self.grid else Point()
        next_value: Optional[int] = left[0]

        if 0 <= c - 1 and not point.left:
            next_moves.append((r, c - 1))
        if 0 <= r - 1 and not point.top:
            next_moves.append((r - 1, c))
        if c + 1 < self.size and not point.right:
            next_moves.append((r, c + 1))
        if r + 1 < self.size and not point.bottom:
            next_moves.append((r + 1, c))

        valid: List[Tuple[int, int]] = []
        for move in next_moves:
            if move in moves:
                continue
            if move in self.grid and next_value is not None and next_value != self.grid[move].value and self.grid[move].value is not None:
                continue
            valid.append(move)

        return valid

    def solve(self) -> List[Tuple[int, int]]:
        points_with_values = filter(lambda k: self.grid[k].value is not None, self.grid.keys())
        sorted_pwv = sorted(points_with_values, key=lambda x: self.grid[x].value) # type: ignore
        start: Tuple[int, int] = sorted_pwv.pop(0)
        left: List[Optional[int]] = list(map(lambda x: self.grid[x].value, sorted_pwv))
        row: int = start[0]
        col: int = start[1]
        moves: List[Tuple[int, int]] = [start]

        _, solution = self.do_solve(row, col, moves, left)
        return solution

    def do_solve(
        self, 
        r: int, 
        c: int, 
        moves: List[Tuple[int, int]], 
        left: List[Optional[int]]
    ) -> Tuple[bool, List[Tuple[int, int]]]:
        has_points_left: bool = len(left) > 0
        has_unused_spaces: bool = len(moves) < self.spaces

        if not has_points_left and has_unused_spaces:
            return False, []
        if not has_points_left and not has_unused_spaces:
            return True, moves

        for next_valid_coordinate in self.valid_moves(r, c, moves, left):
            r_next, c_next = next_valid_coordinate
            v_next: Point = self.grid[next_valid_coordinate] if next_valid_coordinate in self.grid else Point()
            new_left: List[Optional[int]] = list(filter(lambda x: x != v_next.value, left))
            new_moves: List[Tuple[int, int]] = moves.copy()
            new_moves.append((r_next, c_next))
            solved, solution = self.do_solve(r_next, c_next, new_moves, new_left)
            if solved:
                return True, solution
        return False, []


if __name__ == "__main__":
    size: int = 3
    grid: Dict[Tuple[int, int], Point] = {}
    grid[(2, 0)] = Point(1)
    grid[(0, 2)] = Point(2)
    grid[(1, 1)] = Point(top=True, bottom=True)

    solver = Solver(grid, size)
    print("input")
    print(solver.grid, solver.size, end="\n\n")
    solution = solver.solve()
    print("solution")
    print(solution, end="\n\n")

    solved_at: str = datetime.strftime(datetime.now(), "%Y-%m-%d-%H:%M:%S.%f")
    visualise_zip(grid, size, solution, solved_at)
