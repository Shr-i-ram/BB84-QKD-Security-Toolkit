import numpy as np

from bb84_security.protocol import (
    BB84Protocol
)

from bb84_security.visualization import (
    plot_qber
)

noise_levels = np.linspace(
    0,
    0.20,
    10
)

qber_values = []

for noise in noise_levels:

    protocol = BB84Protocol(
        num_bits=1000
    )

    protocol.generate_data()

    protocol.transmit_without_attack()

    flip_mask = (
        np.random.rand(
            len(protocol.bob_bits)
        ) < noise
    )

    protocol.bob_bits[flip_mask] = (
        1 - protocol.bob_bits[flip_mask]
    )

    qber_values.append(
        protocol.compute_qber()
    )

print(
    "\nNoise Levels:"
)

print(noise_levels)

print(
    "\nQBER Values:"
)

print(qber_values)

plot_qber(
    noise_levels,
    qber_values
)