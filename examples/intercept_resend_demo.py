from bb84_security.protocol import (
    BB84Protocol
)

from bb84_security.attacks import (
    InterceptResendAttack
)

protocol = BB84Protocol(
    num_bits=1000
)

protocol.generate_data()

attack = InterceptResendAttack()

protocol.bob_bits = attack.apply(
    protocol.alice_bits,
    protocol.alice_bases,
    protocol.bob_bases
)

print(
    "QBER:",
    protocol.compute_qber()
)