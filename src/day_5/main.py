from utils.input_handler import inputReader
from typing import List

class inputHandler(inputReader):
    def __init__(self, day) -> None:
        super().__init__(day)


    def split_file(self) -> list:

        splitted_input = self.read_input().split("\n\n")
        return splitted_input



class SolutionP1(inputHandler):
    def __init__(self, day) -> None:
        super().__init__(day)
        self.input: List[str] = self.split_file()


if __name__ == "__main__":
    day = 5
    file = inputHandler(day)

    files = file._split_file()
