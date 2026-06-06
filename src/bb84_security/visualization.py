import matplotlib.pyplot as plt


def plot_qber(
    attack_probabilities,
    qber_values
):

    plt.figure(
        figsize=(8, 5)
    )

    plt.plot(
        attack_probabilities,
        qber_values,
        marker="o"
    )

    plt.xlabel(
        "Attack Probability"
    )

    plt.ylabel(
        "QBER"
    )

    plt.title(
        "QBER vs Attack Probability"
    )

    plt.grid(True)

    plt.show()