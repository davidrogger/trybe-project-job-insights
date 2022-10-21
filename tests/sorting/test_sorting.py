from src.sorting import sort_by
import pytest


@pytest.fixture
def fake_jobs():
    return [
        {
            "job_title": "Marketing",
            "min_salary": "",
            "max_salary": "",
            "date_posted": "2020-06-07",
        },
        {
            "job_title": "Senior Sales Force Developer",
            "min_salary": "44587",
            "max_salary": "82162",
            "date_posted": "2020-06-07",
        },
        {
            "job_title": "Diesel Mechanic",
            "min_salary": "46298",
            "max_salary": "55893",
            "date_posted": "2020-05-01",
        },
        {
            "job_title": "Plumber",
            "min_salary": "",
            "max_salary": "",
            "date_posted": "2020-04-29",
        },
        {
            "job_title": "Full stack end developer",
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2022-10-21",
        },
        {
            "job_title": "Web developer",
            "min_salary": "2000",
            "max_salary": "4000",
            "date_posted": "2021-10-01",
        },
    ]


def test_sort_by_criteria(fake_jobs):
    jobs = fake_jobs

    criteria_valid_orders = [
        {
            "criteria": "max_salary",
            "first_job": 'Senior Sales Force Developer',
            "last_job": 'Plumber',
        },
        {
            "criteria": "min_salary",
            "first_job": 'Web developer',
            "last_job": 'Plumber',
        },
        {
            "criteria": "date_posted",
            "first_job": 'Full stack end developer',
            "last_job": 'Plumber',
        },
    ]

    for valid in criteria_valid_orders:
        sort_by(jobs, valid["criteria"])
        first_job_by_method = jobs[0]["job_title"]
        last_job_by_method = jobs[-1]["job_title"]

        assert first_job_by_method == valid["first_job"]
        assert last_job_by_method == valid["last_job"]
