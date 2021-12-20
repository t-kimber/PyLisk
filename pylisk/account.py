from hashlib import sha256
from pylisk.lisk_request import request


class Account:
    """
    # TODO
    """

    def __init__(self, address, public_key, available_balance, nonce, keys, name=None):
        self.address = address
        self.public_key = public_key
        self.bin_address = sha256(public_key).digest()[:20]
        self.available_balance = available_balance
        self.nonce = nonce
        self.keys = keys
        self.name = name

    @classmethod
    def from_info(cls, info):
        """
        # TODO

        Parameters
        ----------
        info :

        Returns
        -------
        """
        if "address" in info:
            ans = request(
                "https://testnet-service.lisk.com/api/v2/",
                f"accounts?address={info['address']}",
            )[0]
        elif "name" in info:
            ans = request(
                "https://testnet-service.lisk.com/api/v2/",
                f"accounts?username={info['name']}",
            )[0]
        elif "public_key" in info:
            ans = request(
                "https://testnet-service.lisk.com/api/v2/",
                f"accounts?publicKey={info['public_key']}",
            )[0]
        else:
            return

        return cls(
            address=ans["summary"]["address"],
            public_key=bytes.fromhex(ans["summary"]["publicKey"]),
            available_balance=int(ans["token"]["balance"]),
            nonce=int(ans["sequence"]["nonce"]),
            keys=ans["keys"],
            name=ans["dpos"]["delegate"]["username"],
        )

    def __str__(self):
        """
        # TODO
        """
        return (
            f"address = {self.address} \n"
            f"public key = {self.public_key.hex()} \n"
            f"nonce = {self.nonce} \n"
            f"keys : number of signature = {self.keys['numberOfSignatures']} \n"
            f"keys : mandatory keys = {self.keys['mandatoryKeys']}"
        )
