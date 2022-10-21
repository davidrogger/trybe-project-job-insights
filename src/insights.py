from src.jobs import read


def get_unique_values_from(source, key):
    unique_value = set()
    for column in source:
        empty = 0
        if len(column[key]) != empty:
            unique_value.add(column[key])
    unique_value_list = [*unique_value]
    return unique_value_list


def get_unique_job_types(path):
    jobs = read(path)
    jobs_type_list = get_unique_values_from(jobs, "job_type")

    return jobs_type_list


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs = read(path)
    jobs_industries_types = get_unique_values_from(jobs, "industry")
    return jobs_industries_types


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def is_bigger_than_current_salary(source_salary, current_salary):
    return source_salary > current_salary


def is_smaller_than_currenty_salary(source_salary, current_salary):
    return source_salary < current_salary


def get_salary_from(source, key, initial_salary):
    salary_types = {
        "min_salary": is_smaller_than_currenty_salary,
        "max_salary": is_bigger_than_current_salary,
    }
    filtered_salary = initial_salary

    for job in source:
        if job[key].isnumeric():
            salary_converted_int = int(job[key])
            if salary_types[key](salary_converted_int, filtered_salary):
                filtered_salary = salary_converted_int

    return filtered_salary


def get_max_salary(path):
    jobs = read(path)
    initial_salary = 0
    max_salary = get_salary_from(jobs, "max_salary", initial_salary)

    return max_salary


def get_min_salary(path):
    jobs = read(path)
    initial_salary = float("inf")
    min_salary = get_salary_from(jobs, "min_salary", initial_salary)

    return min_salary


def are_integer(list):
    for value in list:
        if isinstance(value, int):
            return True

    raise ValueError


def check_input_validation(job: dict):
    input_keys = [*job.keys()]
    valid_keys = ["max_salary", "min_salary"]
    if input_keys == valid_keys:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]
        are_integer([min_salary, max_salary])
        if min_salary < max_salary:
            return True

    raise ValueError


def matches_salary_range(job, salary):
    check_input_validation(job)
    are_integer([salary])
    return job["max_salary"] >= salary >= job["min_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtered.append(job)
        except ValueError:
            pass

    return jobs_filtered
