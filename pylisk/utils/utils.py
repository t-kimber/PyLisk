"""
Utility functions.

"""
import hashlib
from nacl.signing import SigningKey
import base64


def addressToBinary(address):
    """
    Converts an address into bytes.

    Parameters
    ----------
    address : str
        A Lisk address.

    Returns
    -------
    bin_address : bytes
        The Lisk address in bytes.

    Notes
    -----
    Thankful for https://github.com/dakk/lisk-pool3 for his code,
    Taken from:
    https://github.com/dakk/lisk-pool3/blob/a9179f6f059bf2e578a5b8cd582d197d2cbac6a0/liskpool3.py#L54
    """

    # Available characters
    B32_STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    B32_DICT = "zxvcpmbn3465o978uyrtkqew2adsjhfg"

    # Check if address start with "lsk"
    if address[0:3] != "lsk":
        raise ValueError("Address must start with 'lsk'.")

    # TODO: verify checksum

    bin_address = ""
    for x in address[3::][:-6]:
        bin_address += B32_STD[B32_DICT.index(x)]
    bin_address = base64.b32decode(bin_address)

    return bin_address


def net_to_net_id(network):
    """
    Converts the string network (test or main) to the official network identifier.

    Parameters
    ----------
    network : str
        The network to consider for a transaction, "test" or "main".s

    Returns
    -------
    network_id : bytes
        The network ID

    Notes
    -----
    See https://testnet-service.lisk.com/api/v2/network/status .

    """
    if network == "test":
        network_id = bytes.fromhex(
            "15f0dacc1060e91818224a94286b13aa04279c640bd5d6f193182031d133df7c"
        )
    else:
        raise NotImplementedError("Transaction on the main net no implemented yet.")

    return network_id


def lisk_to_beddows(amount):
    """
    Converts an amount from Lisk to Beddows.

    Parameters
    ----------
    amount : float
        A numerical value in Lisk.

    Returns
    -------
    int :
        The amount in Beddows.
    """

    return int(amount * 10**8)


def compute_publickey_from_seed(seed):
    """
    Computes the public key from a seed.

    Parameters
    ----------
    seed : bytes
        The seed.

    Returns
    -------
    public_key : bytes
        The public key associated to the seed.
    """

    public_key = SigningKey(seed).verify_key._key
    return public_key


def compute_seed_from_passphrase(passphrase):
    """
    Computes the seed from a passphrase.

    Parameters
    ----------
    passphrase : str
        A passphrase known by the user.

    Returns
    -------
    seed : bytes
        The seed from the passphrase.

    """
    seed = hashlib.sha256(passphrase.encode()).digest()
    return seed
