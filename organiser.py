import os
import shutil
from pathlib import Path
from logger import logger
from config import FILE_CATEGORIES
from logging import error


def get_categories(file_extension):
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "others"


get_categories("txt")


def create_folder(folder_path):

    os.makedirs(folder_path, exist_ok=True)


def organize_files(source_folder, destination_folder):

    source_path = Path(source_folder)
    destination_path = Path(destination_folder)

    if not source_path.is_dir():
        raise NotADirectoryError(
            f"Source folder does not exist: {source_folder}"
        )

    destination_path.mkdir(parents=True, exist_ok=True)

    for file in source_path.iterdir():

        # Skip directories
        if not file.is_file():
            continue

        # Get file extension
        extension = file.suffix.lower()

        # Identify category
        category = get_categories(extension)

        # Create destination folder
        category_folder = destination_path / category
        category_folder.mkdir(exist_ok=True)

        # Avoid overwriting duplicate filenames
        destination_file = category_folder / file.name

        counter = 1

        while destination_file.exists():

            destination_file = category_folder / (
                f"{file.stem}_{counter}{file.suffix}"
            )

            counter += 1

        # Move file
        shutil.move(str(file), str(destination_file))
        logger.info(f"Moved {file.name} to {category}")

        try:
            shutil.move(str(file), str(destination_file))
            logger.info(f"Moved {file.name} to {category}")
        except OSError as error:
            logger.exception(f"Could not move {file.name}: {error}")
