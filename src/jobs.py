import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(f'../{path}', "r") as file:
        dict_jobs = csv.DictReader(file)
        list_jobs = [*dict_jobs]

    return list_jobs
