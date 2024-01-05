import os
import shutil
import time
import argparse
import logging
import hashlib
import zipfile
import cryptography.fernet
import pandas as pd


def calculate_hash(filename):
    hash_algorithm = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_algorithm.update(chunk)
    return hash_algorithm.hexdigest()


def compress_directory(directory):
    archive = zipfile.ZipFile(f"{directory}.zip", "w")
    for root, dirs, files in os.walk(directory):
        for file in files:
            archive.write(os.path.join(root, file))
    archive.close()


def encrypt_file(filename, key):
    cipher = cryptography.fernet.Fernet(key)
    with open(filename, "rb") as f:
        data = f.read()
    ciphertext = cipher.encrypt(data)
    with open(filename + ".enc", "wb") as f:
        f.write(ciphertext)


def create_report():
    evidence_files = []
    for root, dirs, files in os.walk("C:\\Evidence"):
        for file in files:
            filename = os.path.join(root, file)
            size = os.path.getsize(filename)
            timestamp = os.path.getmtime(filename)
            evidence_files.append({
                "filename": filename,
                "size": size,
                "timestamp": timestamp,
            })

    report = pd.DataFrame(evidence_files)
    report.to_csv("evidence_report.csv")


def main():
    parser = argparse.ArgumentParser(description="Windows Machine Evidence Collection Script")
    parser.add_argument("machine_name", help="Machine name")
    parser.add_argument("evidence_dir", help="Evidence destination directory")
    args = parser.parse_args()

    machine_name = args.machine_name
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    evidence_dir = os.path.join(args.evidence_dir, f"{machine_name}_{timestamp}")

    # Validate arguments

    if not os.path.exists(args.evidence_dir):
        raise ValueError(f"Evidence destination directory not found: {args.evidence_dir}")

    # Start logging

    logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s", level=logging.INFO)

    # Collect evidence

    collect_log_files()
    collect_configuration_files()
    collect_application_data()

    # Calculate hashes of collected files

    for root, dirs, files in os.walk(evidence_dir):
        for file in files:
            filename = os.path.join(root, file)
            hash = calculate_hash(filename)
            logging.info(f"Hash of {filename}: {hash}")

    # Compress collected files

    compress_directory(evidence_dir)

    # Encrypt collected files

    key = cryptography.fernet.generate_key()
    for root, dirs, files in os.walk(evidence_dir):
        for file in files:
            filename = os.path.join(root, file)
            encrypt_file(filename, key)

    # Create report of collected evidence

    create_report()

    logging.info("Evidence collection complete")


if __name__ == "__main__":
    main()
