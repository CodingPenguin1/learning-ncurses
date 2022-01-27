#!/usr/bin/env python

import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 10, "Hello World!")
    stdscr.addstr(15, 25, "another string")
    stdscr.refresh()
    stdscr.getch()


if __name__ == '__main__':
    wrapper(main)