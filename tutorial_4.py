#!/usr/bin/env python

import curses
from curses import wrapper
from time import sleep
from curses.textpad import Textbox, rectangle


def config(stdscr):
    curses.use_default_colors()
    # stdscr.nodelay(True)  # Enable for part 2


def main(stdscr):
    config(stdscr)
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_BLUE, -1)

    # === Part 1 === #
    # key = stdscr.getkey()
    # stdscr.addstr(5, 5, f'Key: {key}')
    # stdscr.refresh()
    # stdscr.getch()

    # === Part 2 === #
    # x, y = 0, 0
    # string_x, dx = 1, 1
    # while True:
    #     try:
    #         key = stdscr.getkey()
    #     except curses.error:
    #         key = None

    #     if key == 'KEY_DOWN':
    #         y += 1
    #     elif key == 'KEY_LEFT':
    #         x -= 1
    #     elif key == 'KEY_RIGHT':
    #         x += 1
    #     elif key == 'KEY_UP':
    #         y -= 1

    #     if string_x in {0, stdscr.getmaxyx()[1] - len('string')}:
    #         dx *= -1
    #     string_x += dx

    #     stdscr.erase()
    #     stdscr.addstr(0, string_x, 'string')
    #     stdscr.addstr(y, x, '0')
    #     stdscr.refresh()

    # === Part 3 === #
    win = curses.newwin(3, 18, 2, 2)
    box = Textbox(win)

    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.refresh()
    box.edit()
    text = box.gather().replace('\n', '').strip()

    stdscr.addstr(10, 40, text)

    stdscr.getch()


if __name__ == '__main__':
    wrapper(main)
