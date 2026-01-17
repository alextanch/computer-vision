from pathlib import Path
from zipfile import ZipFile

import gdown
import torch


def set_seed(seed):
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

        # что бы все операции на GPU были детерменированными
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


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

    print("Done!")