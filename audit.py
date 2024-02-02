import os
import shutil
import time
import argparse
import logging
import hashlib
import zipfile
from cryptography.fernet import Fernet
import pandas as pd

def calculate_hash(filename, algorithm="sha256"):
    """
    Calcula o hash de um arquivo.
 """
    hasher = hashlib.new(algorithm)
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def compress_directory(directory):
    """
    Comprime um diretório em um arquivo ZIP.
    """
    archive_name = f"{directory}.zip"
    with zipfile.ZipFile(archive_name, "w") as archive:
        for root, dirs, files in os.walk(directory):
            for file in files:
                archive.write(os.path.join(root, file))
    return archive_name

def encrypt_file(filename, key):
    """
    Criptografa um arquivo usando o algoritmo Fernet.
    """
    cipher = Fernet(key)
    with open(filename, "rb") as f:
        data = f.read()
    ciphertext = cipher.encrypt(data)
    encrypted_filename = f"{filename}.enc"
    with open(encrypted_filename, "wb") as f:
        f.write(ciphertext)
    return encrypted_filename

def create_report(evidence_files):
    """
    Cria um relatório em CSV com informações sobre os arquivos coletados.

    """
    report = pd.DataFrame(evidence_files)
    report_name = "evidence_report.csv"
    report.to_csv(report_name)
    return report_name

def main():
    """
    Função principal que coleta as evidências, calcula hashes, comprime, criptografa e gera um relatório.
    """
    # Argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Script de Coleta de Evidências em Máquinas Windows")
    parser.add_argument("machine_name", help="Nome da máquina")
    parser.add_argument("evidence_dir", help="Diretório de destino das evidências")
    args = parser.parse_args()

    if not os.path.exists(args.evidence_dir):
        raise ValueError(f"Diretório de destino das evidências não encontrado: {args.evidence_dir}")
    
    logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s", level=logging.INFO)

    evidence_files = []
    for root, dirs, files in os.walk("C:\\Evidence"):
        for file in files:
            filename = os.path.join(root, file)
            size = os.path.getsize(filename)
            timestamp = os.path.getmtime(filename)
            file_hash = calculate_hash(filename)
            evidence_files.append({
                "filename": filename,
                "size": size,
                "timestamp": timestamp,
                "hash": file_hash,
            })

    compressed_file = compress_directory("C:\\Evidence")

    key = Fernet
