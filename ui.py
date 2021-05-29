import curses

class UserInterface():

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()

        self.begin_x = 0
        self.begin_y = 0
        self.height = 200
        self.width = 200

        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)      

        self.win = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)        
        
    def terminate(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def displayText(self, text, x, y, length=30, color=1):
        spaces = " " * length

        self.win.addstr(y, x, spaces)
        self.win.addstr(y, x, text, curses.color_pair(color))
        self.win.refresh()
