import numpy as np


class InterceptResendAttack:

    def apply(
        self,
        alice_bits,
        alice_bases,
        bob_bases
    ):

        eve_bases = np.random.randint(
            0, 2, len(alice_bits)
        )

        bob_bits = np.zeros_like(
            alice_bits
        )

        for i in range(len(alice_bits)):

            if eve_bases[i] == alice_bases[i]:

                measured = alice_bits[i]

            else:

                measured = np.random.randint(
                    0, 2
                )

            if bob_bases[i] == eve_bases[i]:

                bob_bits[i] = measured

            else:

                bob_bits[i] = np.random.randint(
                    0, 2
                )

        return bob_bits


class RandomBasisAttack:

    def __init__(
        self,
        attack_probability=0.5
    ):

        self.attack_probability = (
            attack_probability
        )

    def apply(
        self,
        alice_bits,
        alice_bases,
        bob_bases
    ):

        bob_bits = np.copy(
            alice_bits
        )

        for i in range(len(alice_bits)):

            if (
                np.random.rand()
                < self.attack_probability
            ):

                bob_bits[i] = np.random.randint(
                    0, 2
                )

        return bob_bits