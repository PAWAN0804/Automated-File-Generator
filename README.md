# Automated-File-Generator
A Python-based Automated File Organizer that automatically sorts files into categorized folders based on their file extensions. Built using Python's OS, Pathlib, and Shutil modules, with duplicate filename handling and logging for efficient file management.


# Automated File Organizer using Python 

## 📌 Project Overview
The **Automated File Organizer** is a Python-based application designed to simplify file management by automatically organizing files into separate folders based on their extensions.

Instead of manually sorting files, this application identifies file types and moves them into appropriate directories, making file management easier, faster, and more efficient.

## 🚀 Features
- Automatically organizes files based on file extensions.
- Creates folders dynamically for different file categories.
- Supports Images, Documents, Videos, Audio, Spreadsheets, Python files, and Archives.
- Handles duplicate filenames without overwriting existing files.
- Uses exception handling to manage runtime errors.
- Maintains activity logs for tracking file movements.
- Supports unknown file extensions through an Others category.

## 🛠️ Technologies Used
- Python 3
- OS Module
- Shutil Module
- Pathlib Module
- Logging Module

## 📂 Project Structure
```text
Automated_File_Organizer/
│
├── main.py
├── organizer.py
├── config.py
├── logger.py
├── Organized_Files/
├── logs/
└── README.md
```

## ⚙️ Installation and Setup

**Step 1: Clone the repository**
```bash
git clone YOUR_REPOSITORY_URL
```

**Step 2: Navigate to the project directory**
```bash
cd Automated_File_Organizer
```

**Step 3: Create a virtual environment**
```bash
python -m venv my_env
```

**Step 4: Activate the environment**

Windows PowerShell:
```powershell
.\my_env\Scripts\Activate.ps1
```

**Step 5: Run the application**
```bash
python main.py
```

## 💻 How It Works
1. The user provides the source folder path.
2. The application scans files in the selected directory.
3. Python identifies each file's extension.
4. Files are categorized according to predefined extension mappings.
5. Required destination folders are created automatically.
6. Files are moved into their respective folders.
7. Duplicate filenames are renamed to prevent overwriting.

## 🎯 Learning Outcomes
- Practical implementation of Python file handling.
- Understanding directory and path management.
- Working with Python built-in modules.
- Implementing exception handling.
- Understanding modular programming.
- Developing real-world automation applications.

## 🔮 Future Enhancements
- Graphical User Interface using Tkinter.
- Automatic file organization scheduling.
- File statistics dashboard.
- File backup and restore functionality.
- Dry-run mode to preview file movements.

## 👨‍💻 Author
Developed as a Python programming project to demonstrate practical skills in automation, file handling, and application development.

**If you find this project useful, feel free to ⭐ the repository!**
