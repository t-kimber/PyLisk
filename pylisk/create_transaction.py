"""
Script to create a transaction.

"""
from hashlib import sha256
from pylisk.transaction import BalanceTransferTransaction
from pylisk.account import Account


def main():

    address = "lskjks9w7v7wd6kg5gkt9eq5tvzu2w5vwfdc3ptkw"
    acc = Account.from_info({"address": address})

    bal_trs = BalanceTransferTransaction(
        nonce=acc.nonce,
        sender_public_key=acc.public_key,
        recipient_bin_add=acc.bin_address,
        amount=100000000,
    )

    NETWORK_ID = {
        "testnet": bytes.fromhex(
            "15f0dacc1060e91818224a94286b13aa04279c640bd5d6f193182031d133df7c"
        ),
    }

    seed_phrase_1 = (
        "slight decline reward exist rib zebra multiply anger display alpha raccoon sing"
    )
    seed_1 = sha256(seed_phrase_1.encode()).digest()

    bal_trs.sign(seed=seed_1, net_id=NETWORK_ID["testnet"])
    hex_trs = bal_trs.serialize().hex()
    print(f"{hex_trs=}")


if __name__ == "__main__":
    main()
