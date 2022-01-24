"""
pylisk.cli.py

Main command line interface for PyLisk.

"""
import argparse
import subprocess

from .utils.user_input import (
    ask_passphrase,
    ask_confirmation,
    check_passphrase_validity,
    check_positivity,
)


def main():

    # Parse arguments
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Subcommand send
    send_subparser = subparsers.add_parser("send")

    send_subparser.add_argument(
        "--receiver",
        dest="receiver",
        type=str,
        help="The receiver of the transaction",
        required=True,
    )
    send_subparser.add_argument(
        "--amount",
        dest="amount",
        help="The amount [in Lisk] the receiver of the transaction is getting",
        required=True,
        type=check_positivity,
    )
    send_subparser.add_argument(
        "--net",
        dest="net",
        type=str,
        choices=["test", "main"],
        help="The net to apply the transaction, testnet or mainnet.",
        default="test",
    )
    send_subparser.set_defaults(func=main_send)

    # Subcommand vote
    vote_subparser = subparsers.add_parser("vote")

    vote_subparser.add_argument(
        "--delegate",
        dest="delegate",
        type=str,
        help="The delegate to vote for",
        required=True,
    )
    vote_subparser.add_argument(
        "--amount",
        dest="amount",
        help="The amount the delegate will receive",
        required=True,
        type=check_positivity,
    )
    vote_subparser.add_argument(
        "--net",
        dest="net",
        type=str,
        help="The net to apply the transaction, testnet or mainnet.",
        choices=["test", "main"],
        default="test",
    )
    vote_subparser.set_defaults(func=main_vote)

    # Set as variables
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        # Run help if no arguments were given
        subprocess.run(["pylisk", "-h"])


def main_send(args):
    """
    # TODO
    """

    passphrase = ask_passphrase()
    validity_passphrase = check_passphrase_validity(passphrase)
    while validity_passphrase:
        print(f"Starting session on {args.net} net...")
        print("To log out of your session, press CTRL + C")
        print(
            f"\nSummary of transaction on the {args.net} net:\n"
            f"=======================================\n"
            f"{'Receiver of the transaction:' : <30}{args.receiver}\n"
            f"{'Amount the receiver will get:' : <30}{args.amount} Lisk\n"
        )

        confirmation = ask_confirmation("send")
        # create_sending_transaction(net, receiver, holder, amount)
        validity_passphrase = False


def main_vote(args):
    """
    # TODO
    """

    passphrase = ask_passphrase()
    validity_passphrase = check_passphrase_validity(passphrase)
    while validity_passphrase:
        print(f"Starting session on {args.net} net...")
        print("To log out of your session, press CTRL + C")
        print(
            f"\nSummary of transaction on the {args.net} net:\n"
            f"=======================================\n"
            f"{'Delegate address:' : <30}{args.delegate}\n"
            f"{'Amount for the delegate:' : <30}{args.amount} Lisk\n"
        )

        confirmation = ask_confirmation("vote")
        # create_voting_transaction(net, receiver, holder, amount)
        validity_passphrase = False
