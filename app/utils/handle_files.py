#!/usr/bin/env python
"""
TODO
"""

from csv import reader, writer
from datetime import datetime
from json import dump, load
from os import mkdir
from os.path import dirname, join, realpath, exists


def open_json(path: str, name: str) -> dict:
    """
    TODO
    """
    try:
        with open(join(path, name), "r") as lineobj:
            return load(lineobj)
    except Exception as e:
        return e


def open_csv_to_dict(path: str, name: str) -> object:
    """
    TODO
    """
    companies = {}
    try:
        with open(join(path, name), "r") as lineobj:
            csv_reader = reader(lineobj)
            headers = next(csv_reader)
            # TODO refactor repetition into dictcomp?
            for row in csv_reader:
                companies[row[0]] = {
                    headers[1]: row[1],
                    headers[2]: row[2],
                    headers[3]: row[3],
                }
        return companies
    except Exception as e:
        return e


def save_json(input: dict, save_file: str):
    """
    TODO
    """
    path = dirname(realpath(save_file))
    try:
        if not test_path(path):
            create_path(path)
        with open(save_file, "w") as outfile:
            dump(input, outfile, indent=2)
    except Exception as e:
        return e


def save_csv(headers: list[str], rows: list, save_file: str):
    """
    TODO
    """
    path = dirname(realpath(save_file))
    try:
        if not test_path(path):
            create_path(path)
        with open(save_file, "w", newline="") as outfile:
            w = writer(outfile)
            w.writerow(headers)
            w.writerows(rows)
    except Exception as e:
        return e


def get_save_file_name(provider: str, mode: str, save_path: str, save_filename: str):
    """
    TODO
    """

    date = datetime.now().strftime("%G-%m-%d_%H-%M")
    name = save_filename.replace("<PROVIDER>", provider)

    return join(save_path, f"{date}_{mode}_{name}")


def test_path(path: str):
    """
    TODO
    """
    try:
        return exists(path)
    except Exception as e:
        return e


def create_path(path: str):
    """
    TODO
    """
    try:
        mkdir(path)
    except Exception as e:
        return e