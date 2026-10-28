from pathlib import Path
from src.classifier import classify_file

def scan_directory(directory:Path):
    for item in directory.iterdir():
        if item.is_file():
            category = classify_file(item)
            print(f"{item.name} -> {category}")