import requests


def request(apiEndpoint, query):
    """
    Return the information from a List network for the queried information.

    Parameters
    ----------
    apiEndpoint: str
        An url that links to the Lisk net of choice (mainnet, testnet, ...),
        see https://lisk.com/documentation/lisk-service/index.html#public-lisk-service-apis.

    query: str
        The information wanted from the api, ususally composed of an number of queries,
        such as transaction and the associated height.

    Returns
    -------
    list:
        A list made of the information coming from the chosen network.

    Notes
    -----
    See the Lisk Service documentation for more details at
    https://lisk.com/documentation/lisk-service/index.html.
    """

    uri = apiEndpoint + query
    try:
        response = requests.get(uri)
        response.raise_for_status()
        response = response.json()
        if "data" in response:
            return response["data"]
        else:
            print("Empty data entry.")
            return None
    except requests.exceptions.HTTPError as err:
        print("Failed request...")
        raise
