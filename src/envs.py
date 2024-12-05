import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
FILES_DIR = os.path.join(ROOT_DIR, 'files')
PREFIX_INPUT_FILE_PATH = os.path.join(FILES_DIR, 'input_day_')