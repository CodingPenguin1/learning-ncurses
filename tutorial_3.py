#!/usr/bin/env python

import curses
from curses import wrapper
from time import sleep


def main(stdscr):
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_BLUE, -1)

    counter_win = curses.newwin(1, 10, 10, 10)

    for i in range(100):
        color = curses.color_pair(i % 3 + 1)
        counter_win.addstr(0, 0, str(i), color)
        counter_win.refresh()
        sleep(0.1)


if __name__ == '__main__':
    wrapper(main)