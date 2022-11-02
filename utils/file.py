from pathlib import Path

INPUT_FILES_PATH = Path('./inputs/')
DAY_FILES_PATH = Path('./days/')


def create_day_input_file_path(day_number):
    path = Path(INPUT_FILES_PATH / f'day_{day_number}.txt')
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def create_day_folder_path(day_number):
    return Path(DAY_FILES_PATH / f'day_{day_number}')
