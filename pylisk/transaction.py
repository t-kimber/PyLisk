import pylisk.schema.balanceTransfer_pb2 as balanceTrs
from nacl.signing import SigningKey
import requests


class BalanceTransferTransaction:
    """
    Creates a transfer transaction between two accounts.
    """

    def __init__(
        self, nonce, sender_public_key, recipient_bin_add, amount, fee=210000, data=""
    ):
        if (
            not isinstance(nonce, int)
            or not isinstance(sender_public_key, bytes)
            or not isinstance(recipient_bin_add, bytes)
            or not isinstance(amount, int)
            or not isinstance(fee, int)
            or not isinstance(data, str)
        ):
            raise TypeError("Respect argument types.")

        if (
            len(data) > 64
            or len(recipient_bin_add) != 20
            or len(sender_public_key) != 32
        ):
            raise ValueError("Argument has inappropriate value.")

        self.moduleID = 2
        self.assetID = 0
        self.nonce = nonce
        self.fee = fee
        self.senderPublicKey = sender_public_key
        self.amount = amount
        self.recipientAddress = recipient_bin_add
        self.data = data
        self.signatures = []

    def serialize(self, include_signatures=True):
        """
        Serializes a transaction.

        Parameters
        ----------
        include_signatures : bool
            Whether or not to include the signature(s) of the transaction.

        Returns
        -------
        bytes :
            The serialized transaction.
        """
        trs = balanceTrs.BalanceTransfer()
        trs.moduleID = self.moduleID
        trs.assetID = self.assetID
        trs.nonce = self.nonce
        trs.fee = self.fee
        trs.senderPublicKey = self.senderPublicKey
        trs.asset.amount = self.amount
        trs.asset.recipientAddress = self.recipientAddress
        trs.asset.data = self.data

        if include_signatures:
            for signature in self.signatures:
                trs.signatures.extend([signature])

        return trs.SerializeToString()

    def get_signing_bytes(self, net_id):
        """
        Prepends the required tags.

        Parameters
        ----------
        net_id : 32 bytes
            Network identifier to avoid transaction replay.

        Returns
        -------
        bytes :
            Bytes to be signed.
        """
        return net_id + self.serialize(include_signatures=False)

    def sign(self, seed, net_id):
        """
        Signs a transaction given an account seed and network identifier.

        Parameters
        ----------
        seed : 32 bytes
            The seed associated to the account.
        net_id : 32 bytes
            Network identifier.

        Returns
        -------
        None
        """
        signing_key = SigningKey(seed)
        signing_bytes = self.get_signing_bytes(net_id)
        signature = signing_key.sign(signing_bytes).signature
        self.signatures.append(signature)

    def send(self, net):
        """
        #TODO
        """
        if net == "test":
            ans = requests.post(
                f"https://testnet-service.lisk.com/api/v2/transactions?transaction={self.serialize().hex()}"
            )
            print(ans.json())
