"""Utility script that fetches CIFAR-10 dataset from web."""

import urllib.request
import tarfile
import os

# URL of the .tar.gz file
CIFAR_10_DATASET_DOWNLOAD_URL: str = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"

# Path where you want to save the downloaded file
CIFAR_10_DATASET_PATH: str = "artifacts/cifar-10-python.tar.gz"

# Download the file
urllib.request.urlretrieve(
    url=CIFAR_10_DATASET_DOWNLOAD_URL,
    filename=CIFAR_10_DATASET_PATH,
)

# Extract the contents
with tarfile.open(CIFAR_10_DATASET_PATH, "r:gz") as tar:
    tar.extractall()

# Delete the downloaded .tar.gz file if needed
os.remove(download_path)