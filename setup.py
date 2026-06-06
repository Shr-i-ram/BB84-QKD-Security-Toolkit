from setuptools import setup, find_packages

setup(
    name="bb84-security",
    version="0.1.0",
    description="BB84 Quantum Key Distribution security analysis and eavesdropping attack simulations",
    author="Shriram",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.24",
        "matplotlib>=3.8",
        "qiskit>=1.2",
        "qiskit-aer>=0.15",
    ],
    python_requires=">=3.10",
)