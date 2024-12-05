from pathlib import Path
from loguru import logger

# getting env vars.
from envs import PREFIX_INPUT_FILE_PATH



class inputReader:
    
    def __init__(self, day: int):
        self.prefix_file_path = PREFIX_INPUT_FILE_PATH
        self.day = day

    def _construct_input_file_path(self):
        return f"{self.prefix_file_path}{str(self.day)}.txt"

    def read_input(self, split=False):

        input_path = Path(self._construct_input_file_path())
        logger.info(f"Currently trying to read input for day {str(self.day)} at filepath: {input_path}")
        with open(input_path, 'r') as file:
            return file.read()
        
