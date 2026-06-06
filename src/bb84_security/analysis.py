import numpy as np


def qber(
    alice_key,
    bob_key
):

    return np.mean(
        alice_key != bob_key
    )


def information_leakage(
    alice_key,
    eve_key
):

    return np.mean(
        alice_key == eve_key
    )