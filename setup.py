from setuptools import setup, find_packages

setup(
    name="ct001",  # 🚀 Change this to a unique, unguessable name
    version="0.1.0",
    author="Sumedh Patil",
    author_email="your-email@example.com",  # Change to your real email
    description="Post-Quantum Secure Authentication Library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/ct001",  # Replace with your GitHub repo (if available)
    packages=find_packages(),
    install_requires=[
        "cryptography"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
