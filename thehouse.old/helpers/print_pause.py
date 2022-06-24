import time


def print_pause(string, sleep=1):
    """Print a message and pause the terminal
    :param sleep: the amount of seconds the terminal should sleep as integer
    """
    print(string)
    time.sleep(sleep)
