"""
pylisk.cli.py

Main command line interface for PyLisk.

"""
import argparse
import subprocess


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
        type=int,
        help="The amount [in Lisk] the receiver of the transaction is getting",
        required=True,
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
        type=int,
        help="The amount the delegate will receive",
        required=True,
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
    print(args)


def main_vote(args):
    print(args)
