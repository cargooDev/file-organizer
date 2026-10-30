from pathlib import Path
from src.classifier import classify_file

def scan_directory(directory:Path):
    for item in directory.iterdir():
        if item.is_file():
            category = classify_file(item)
            destination_dir = directory / category
            destination = destination_dir / item.name
            if destination.exists():
                print(f"[SKIP] {item.name} - destination already exists")
                continue
            print(f"[DRY RUN] {item.name} -> {destination}")