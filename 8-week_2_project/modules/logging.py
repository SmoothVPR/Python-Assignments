#!/usr/bin/env python3

"""
Author:    Malik R Booker
Created:   November 11, 2021
Completed: November 12, 2021
Modified:  November 14, 2021

Brief:
    Custom logger module for a Logger object that prioritizes readability
    and manually logs events with various specified commands.
"""

import termcolor
import colorama
import pathlib
import sys
import os

from datetime import datetime
from typing import NoReturn

class Logger(object):
    """
    Logger object that prioritizes readability and manually logs
    events with various specified commands.
    """
    def __init__(self, filename: str) -> None:
        self.filename   = filename
        self.dir_path   = "logs"
        self.log_file   = f"{self.dir_path}/{self.filename}"

        self.write_mode = 'w'
        self.prefix     = lambda: f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]:"

    def _create_log_file(self) -> None:
        """
        Creates a log directory if it doesn't exist then proceeds to
        create a log file if it doesn't exist.
        """
        if not pathlib.Path(self.dir_path).is_dir():
            os.makedirs(self.dir_path)

        with open(self.log_file, self.write_mode) as f:
            f.write(f"{self.prefix()} Log file created.\n")

    def init(self) -> None:
        """
        Creates specified log file if it does not already exist. Otherwise,
        it appends a separator to the existing log file. Finally, the write 
        mode is changed to append.
        """
        colorama.init()

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

    def log(self, message: str) -> None:
        """
        Prints to standard output stream.

        User should aim to have the message start with a capital letter and end with a period.
        """
        formatted_message = f"{self.prefix()} {message}\n"

        sys.stdout.write(formatted_message)
        with open(self.log_file, self.write_mode) as f:
            f.write(formatted_message)

    def err(self, message: str, exit_code: int=1) -> NoReturn:
        """
        Prints to standard error stream and exits.

        User should aim to have the message start with a capital letter and end with a period.
        """
        formatted_message = f"{self.prefix()} FATAL ERROR - {message}\n"

        sys.stderr.write(termcolor.colored(formatted_message, "red"))
        with open(self.log_file, self.write_mode) as f:
            f.write(formatted_message)

        sys.exit(exit_code)

    def warn(self, message: str) -> None:
        """
        Prints to standard error stream without exiting.

        User should aim to have the message start with a capital letter and end with a period.
        """
        formatted_message = f"{self.prefix()} WARNING - {message}\n"

        sys.stdout.write(termcolor.colored(formatted_message, "yellow"))
        with open(self.log_file, self.write_mode) as f:
            f.write(formatted_message)

    def destroy(self) -> None:
        """
        Formality for denoting end of log.
        """
        self.log("Logger destroyed.")

        sys.stdout.write(f"\nLog saved to '{self.log_file}'.\n")

if __name__ == "__main__":
    logger = Logger("test.log")

    logger.init()
    logger.log("Test log.")
    logger.warn("Test warning!")
    logger.destroy()

    logger.init()
    logger.err("Test error.")
    # logger.destroy() # Will not be reached
