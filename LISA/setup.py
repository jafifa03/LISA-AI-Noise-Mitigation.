from setuptools import setup, find_packages

setup(
    name="lisa_ai_mitigation",
    version="0.1.0",
    author="Afifa Jamal",
    description="Multi-Agent RL for Active Noise Mitigation in LISA",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch",
        "gymnasium",
        "scipy",
        "matplotlib",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics",
        "Intended Audience :: Science/Research",
    ],
)