"""validate_input.

This function will validate input.
"""


def validate_input(prompt, options):
    """Validate the input from the user.

    :param options: a list of eligible options.
    """
    while True:
        option = input(prompt).lower()

        if option in options:
            return option

        print("Sorry, I didn't understand! Try Again!")
