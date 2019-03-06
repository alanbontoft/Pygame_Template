import sys
import pygame as pg

import application

def main():
    """Create an App and start the main loop."""
    app = application.App()
    app.main_loop()
    
    """ clean up when main loop exits """
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
