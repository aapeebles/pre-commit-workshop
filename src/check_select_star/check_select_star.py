"""Trying to build a pre-commit check."""

from pathlib import Path

import sqlparse


def check_select_star(filename: str) -> bool:
    """Doc string to make it happy."""
    string_to_search = 'select *'
    # file_path = Path(filename.lower())
    # file_extension = file_path.suffix
    # if file_extension != "sql":
    #     print(f"{filename} skipped")
    # else:
    content = Path(filename).read_text()
    print(content)
    try:
        sql_statements = sqlparse.parse(content)
        print(sql_statements)
        item_num = 1
        error_list = [
            f"'Select *' test failed in statement {item_num}. Be better."
            for snippet in sql_statements
            if string_to_search in str(snippet)
        ]
        print('\n'.join(error_list))
        return any(error_list)
    # todo: fix error check to be relevant
    # TODO: consider if I want it to return TRUE because of no errors or sql files, etc
    except FileNotFoundError:
        return False
