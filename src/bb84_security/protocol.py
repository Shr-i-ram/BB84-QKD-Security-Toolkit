import numpy as np


class BB84Protocol:

    def __init__(self, num_bits=1000):

        self.num_bits = num_bits

        self.alice_bits = None
        self.alice_bases = None

        self.bob_bits = None
        self.bob_bases = None

    def generate_data(self):

        self.alice_bits = np.random.randint(
            0, 2, self.num_bits
        )

        self.alice_bases = np.random.randint(
            0, 2, self.num_bits
        )

        self.bob_bases = np.random.randint(
            0, 2, self.num_bits
        )

    def transmit_without_attack(self):

        self.bob_bits = np.copy(
            self.alice_bits
        )

        mismatch = (
            self.alice_bases != self.bob_bases
        )

        random_results = np.random.randint(
            0, 2, np.sum(mismatch)
        )

        self.bob_bits[mismatch] = random_results

    def sift_keys(self):

        mask = (
            self.alice_bases ==
            self.bob_bases
        )

        return (
            self.alice_bits[mask],
            self.bob_bits[mask]
        )

    def compute_qber(self):

        alice_key, bob_key = self.sift_keys()

        if len(alice_key) == 0:
            return 0

        return np.mean(
            alice_key != bob_key
        )

    def run(self):

        self.generate_data()

        self.transmit_without_attack()

        return {
            "qber": self.compute_qber()
        }