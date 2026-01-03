from pathlib import Path
from zipfile import ZipFile

import gdown


def download_and_extract(google_id, file, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    file = Path(output_dir) / file

    if not file.exists():
        print(f"{file} downloading...")
        gdown.download(
            id=google_id,
            output=str(file),
            quiet=True
        )
    
    if not file.with_suffix("").is_dir():
        print("Extracting...")
        with ZipFile(file, "r") as fp:
            fp.extractall(path=output_dir)