from pathlib import Path
from utils.input_handler import inputReader

class inputHandler(inputReader):

    def __init__(self, day: int) -> None:
        super().__init__(day)
        self.input = self.read_input(split=True)
        self.day = day

    def handle_input(self, split: bool = False) -> list:
        formatted_input = self.input.split("\n")
        return formatted_input


class SolutionP2(inputHandler):

    def __init__(self, day: int) -> None:
        super().__init__(day)
        self.input = [line.strip() for line in self.handle_input() if line.strip()]

    def flip_horizontal(self, grid):
        return [row[::-1] for row in grid]

    def flip_vertical(self, grid):
        # Convert tuples back to strings after transposing
        return [''.join(col) for col in zip(*grid)]

    def find_pattern(self, grid):
        total = 0
        for row in grid:
            for i in range(len(row)-4):
                if row[i] == 'X' and row[i+2] == 'M' and row[i+3] == 'A' and row[i+4] == 'S':
                    total += 1
        return total

    def search_word(self, word: str) -> int:
        grid = self.input
        total = 0
        
        # Check horizontal patterns (right and left)
        total += self.find_pattern(grid)
        total += self.find_pattern(self.flip_horizontal(grid))
        
        # Check vertical patterns (up and down)
        vertical_grid = self.flip_vertical(grid)
        total += self.find_pattern(vertical_grid)
        total += self.find_pattern(self.flip_horizontal(vertical_grid))
        
        # Check diagonal patterns by rotating grid 45 degrees
        diagonal_grid = [''.join(row[i] for row in grid if i < len(row)) 
                        for i in range(max(len(row) for row in grid))]
        total += self.find_pattern(diagonal_grid)
        total += self.find_pattern(self.flip_horizontal(diagonal_grid))
        
        return total
    


if __name__ == "__main__":
    day = Path(__file__).parent.stem.split('_')[-1]

    count = SolutionP2(day).search_word("X-MAS")

    print(count)



