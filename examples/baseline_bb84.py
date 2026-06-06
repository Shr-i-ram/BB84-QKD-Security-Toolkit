from bb84_security.protocol import (
    BB84Protocol
)

protocol = BB84Protocol(
    num_bits=1000
)

results = protocol.run()

print(
    "\n=== BB84 BASELINE ==="
)

print(
    f"QBER: {results['qber']:.4f}"
)