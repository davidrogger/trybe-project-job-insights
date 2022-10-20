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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    jobs = read(path)
    jobs_industries_types = get_unique_values_from(jobs, "industry")
    return jobs_industries_types


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
