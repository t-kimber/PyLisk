"""
Utility functions.

"""

import getpass
import argparse
import hashlib
from nacl.signing import SigningKey
import base64


def addressToBinary(address):
    """

    # TODO: check checksum

    Notes
    -----
    Thankful for https://github.com/dakk/lisk-pool3 for this code
    Taken from :
    https://github.com/dakk/lisk-pool3/blob/a9179f6f059bf2e578a5b8cd582d197d2cbac6a0/liskpool3.py#L54
    """
    B32_STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    B32_DICT = "zxvcpmbn3465o978uyrtkqew2adsjhfg"

    # Check lsk
    if address[0:3] != "lsk":
        raise ValueError("Address must start with 'lsk'.")

    # Checksum
    # sum(address[3:])

    s = ""
    for x in address[3::][:-6]:
        s += B32_STD[B32_DICT.index(x)]
    s = base64.b32decode(s)

    return s


def compute_publickey_from_seed(seed):
    """
    # TODO
    """
    public_key = SigningKey(seed).verify_key._key
    return public_key


def compute_seed_from_passphrase(passphrase):
    """
    # TODO
    """

    return hashlib.sha256(passphrase.encode()).digest()


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
    # TODO
    """
    value = float(numeric_input)
    if value <= 0:
        raise argparse.ArgumentTypeError(f"{numeric_input} must be positive.")
    return value
