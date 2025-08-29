from pathlib import Path
import shutil

directory_name = input(f'Enter location of directory: ')

src = Path(directory_name)

for item in src.iterdir():
    print(item)


