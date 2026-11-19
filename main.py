
import shutil
from organiser import organize_files

source_folder = input("Enter source folder path: ")

destination_folder = "Organized_Files"

try:

    organize_files(source_folder, destination_folder)

    print("\nFile organization completed successfully!")

except (OSError, shutil.Error) as error:

    print(f"Error: {error}")
