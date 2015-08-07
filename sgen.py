#!/usr/bin/env python3

COMMENT_INDICATOR = '#'

import os
from pathlib import Path
from random import choice, random

def is_real_line(line: str) -> bool:
    return line and not line.startswith(COMMENT_INDICATOR)

def read_real_lines(fp: Path) -> [str]:
    with fp.open('r') as f:
        all_lines = (x.strip() for x in f.readlines())
        real_lines = filter(is_real_line, all_lines)
        return list(real_lines)

sources = Path(os.path.dirname(os.path.realpath(__file__)))

domains        = read_real_lines(sources / 'domains.txt')
past_projects  = read_real_lines(sources / 'past_projects.txt')
target_markets = read_real_lines(sources / 'target_markets.txt')

def the_x_of_y():
    m = "Startup idea: the {} of {}"
    return m.format(choice(past_projects), choice(domains))

def x_for_y():
    m = "Startup idea: {} for {}"
    return m.format(choice(past_projects + domains), choice(target_markets))

def xaas():
    return "Startup idea: {} as a service".format(choice(domains))

def generate_startup():
    fs = [the_x_of_y, x_for_y, xaas]
    return choice(fs)()

if __name__ == "__main__":
    try:
        while True:
            print(generate_startup(), end='')
            input()
    except:
        print()
