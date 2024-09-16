import os
import random
import time
from datetime import datetime, timedelta

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    delta = end - start
    int_delta = delta.total_seconds()
    random_second = random.uniform(0, int_delta)
    return start + timedelta(seconds=random_second)

def change_file_modification_date(file_path, new_date):
    """Change the modification date of a file to `new_date`"""
    mod_time = time.mktime(new_date.timetuple())
    os.utime(file_path, (mod_time, mod_time))

def modify_files_in_directory(directory_path, start_date, end_date):
    """Change the modification date of all files in `directory_path`"""
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            new_mod_date = random_date(start_date, end_date)
            change_file_modification_date(file_path, new_mod_date)
            print(f"Changed {file_path} to {new_mod_date}")

if __name__ == "__main__":
    # Define the directory path and date range
    directory_path = R"D:\Scan T4"
    start_date = datetime(2024, 4, 29, 8, 0, 0)
    end_date = datetime(2024, 4, 28, 20, 0, 0)

    modify_files_in_directory(directory_path, start_date, end_date)
