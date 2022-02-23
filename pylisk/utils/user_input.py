"""
Utility functions for user input.

"""

import getpass
import argparse


def ask_passphrase():
    """
    Asks the user for their passphrase.

    Parameters
    ----------
    None

    Returns
    -------
    str :
        The passphrase of the user.
    """

    print("Please enter passphrase")
    passphrase_1 = getpass.getpass(prompt="Passphrase: ")

    print("Please re-enter passphrase")
    passphrase_2 = getpass.getpass(prompt="Passphrase: ")

    if passphrase_1 != passphrase_2:
        raise Exception(f"Passphrases do not match. Aborting")

    else:
        return passphrase_1


def check_passphrase_validity(passphrase):
    """
    Checks whether the passphrase is valid or not.

    Parameters
    ----------
    passphrase : str
        The passphrase to be checked.

    Returns
    -------
    bool :
        Whether the passphrase is valid or not.
    """
    print("By default, the passphrase is valid.\n")
    return True


def ask_confirmation(action):
    """
    Asks the user for confirmation of action.

    Parameters
    ----------
    action : str
        The action to take place if confirmed.

    Returns
    -------
    str :
        The action to be executed if confirmed, aborts otherwise.
    """

    confirmation = str(input("Please confirm the transaction [y]/n: "))

    if confirmation in ["y", "yes", "Y", "Yes", "YES"]:
        print(f"Creating action: {action}")
        return action

    elif confirmation in ["n", "no", "N", "No", "NO"]:
        raise Exception(f"Confirmation of {action} failed. Aborting")

    else:
        print(f"Please choose either 'y' or 'n' for {action} confirmation: ")
        ask_confirmation(action)


def check_positivity(numeric_input):
    """
    Verifies if an input is greater or equal than zero.

    Parameters
    ----------
    numeric_input : int or float
        Any numeric value.

    Returns
    -------
    value : float
        The positive numeric value.
    """

    value = float(numeric_input)
    if value <= 0:
        raise argparse.ArgumentTypeError(f"{numeric_input} must be positive.")
    return value
