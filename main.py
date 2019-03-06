import sys
import pygame as pg

import application

def main():
    """Create an App and start the program."""
    app = application.App()
    app.main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
