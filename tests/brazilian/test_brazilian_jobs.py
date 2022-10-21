from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs_dict_english = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    columns = [
        {"en": "title", "pt": "titulo"},
        {"en": "salary", "pt": "salario"},
        {"en": "type", "pt": "tipo"},
    ]

    for job in jobs_dict_english:
        for column in columns:
            should_be_true = column["en"] in job
            should_be_false = column["pt"] in job

            assert should_be_true is True
            assert should_be_false is False
