"""
Utility functions.

"""


def ask_passphrase():
    """
    Asks the user for their passphrase

    Parameters
    ----------
    None

    Returns
    -------
    str :
        The passphrase of the user.
    """
    return str(input("Please give your passphrase: "))


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
