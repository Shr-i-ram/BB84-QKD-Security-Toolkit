from qiskit_aer.noise import (
    NoiseModel,
    depolarizing_error
)


def depolarizing_noise(
    probability=0.02
):

    noise_model = NoiseModel()

    error = depolarizing_error(
        probability,
        1
    )

    noise_model.add_all_qubit_quantum_error(
        error,
        ["h", "x"]
    )

    return noise_model