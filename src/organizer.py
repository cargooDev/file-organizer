from pathlib import Path

def scan_directory(directory:Path):
    for item in directory.iterdir():
        if item.is_file():
            print(item.name)