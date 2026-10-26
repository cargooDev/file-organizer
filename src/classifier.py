from pathlib import Path

FILE_CATEGORIES = {
    "Images": {'.jpeg', '.jpg', '.png'},
    "Documents": {'.pdf', '.docx', '.txt'},
    "Videos": {'.mp4'},
    "Audios": {'.mp3'},
    "Archives": {'.zip'}
}

def classify_file(file_path: Path) -> str:
    extension = file_path.suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"