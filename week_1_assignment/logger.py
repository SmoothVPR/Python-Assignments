#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 11, 2021
Modified: November 11, 2021

Brief:
    Custom logger module
"""

import pathlib
import sys

from datetime import datetime

class Logger(object):
    """
    Logger object that
    """
    def __init__(self, log_file):
        self.log_file   = log_file

        self.write_mode = 'w'
        self.prefix     = lambda: f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: "

    def _create_log_file(self):
        """
        Creates a log file if it doesn't exist.
        """
        with open(self.log_file, self.write_mode) as f:
            f.write(self.prefix() + "Log file created.\n")

    def init(self):
        """
        Creates specified log file if it does not already exist. Otherwise,
        it does nothing. Finally, the write mode is changed to append.
        """
        if not pathlib.Path(self.log_file).is_file():
            sys.stdout.write(f"Log file not found. Creating '{self.log_file}'.\n\n")
            self._create_log_file()
        else:
            sys.stdout.write(f"Log file found. Appending to '{self.log_file}'.\n\n")

            # Add dash separator in between previous and current logs
            with open(self.log_file, 'a') as f:
                f.write(f"\n{'-' * 80}\n\n")

        # Change write_mode to append
        self.write_mode = 'a'
        self.log("Logger initiated.")

    def log(self, text):
        """
        User should aim to have the text start with a Capital letter and end with a period.
        """
        formatted_text = self.prefix() + text + "\n"

        print(formatted_text[:-1])
        with open(self.log_file, self.write_mode) as f:
            f.write(formatted_text)

    def destroy(self):
        """
        Formality to denoting end of log.
        """
        self.log(f"Logger destroyed.")

        sys.stdout.write(f"Log saved to '{self.log_file}'.\n")

if __name__ == "__main__":
    logger = Logger("test.log")

    logger.init()
    logger.log("Test incident.")
    logger.destroy()
