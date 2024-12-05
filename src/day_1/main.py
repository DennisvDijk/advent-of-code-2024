import os

from pathlib import Path
from loguru import logger
from collections import Counter


class inputfileHandler:
    
    def __init__(self, file_path):

        self.file_path = file_path
        self.left_list = []
        self.right_list = []

    def create_lists(self):
        logger.info("Reading input file....")
        with open(self.file_path, 'r') as file:
            logger.info("Generating left and rights lists...")
            left_list, right_list = zip(*(map(int, line.split()) for line in file))
            logger.success("Generation succesful.")
        return sorted(list(left_list)), sorted(list(right_list))


class SolutionP1(inputfileHandler):
    
    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__(self.file_path)
    
    def compare_lists(self):
        left_list, right_list = self.create_lists()
        total = [abs(r - l) for r, l in zip(right_list, left_list)]

        total_sum = sum(total)
        return total_sum

class SolutionP2(inputfileHandler):
    
    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__(self.file_path)
    
    def similarity_score(self):
        left_list, right_list = self.create_lists()
        score = sum(num * Counter(right_list)[num] for num in Counter(left_list))
        return score


if __name__ == "__main__":

    input_path = Path(os.getcwd()) / "files" / "input.txt"

    # part 1
    total_p1 = SolutionP1(input_path).compare_lists()
    logger.success(f"Part 1: {total_p1}")


    # part 2

    total_p2 = SolutionP2(input_path).similarity_score()
    logger.success(f"Part 2: {total_p2}")