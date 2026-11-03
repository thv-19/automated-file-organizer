# 📂 Automated File Organizer

**Keep your files organized, clean, and easy to find!** ✨

## 📌 About the Project

Automated File Organizer is a Python script that automatically organizes files into separate folders based on their file extensions.

Instead of manually sorting files, this tool does the work for you! 🚀

## ✨ Features

- 🖼️ **Images:** Organizes `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, and `.webp` files.
- 📄 **Documents:** Organizes `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, and `.pptx` files.
- 🎵 **Audio:** Organizes `.mp3`, `.wav`, `.aac`, `.flac`, and `.m4a` files.
- 🎬 **Videos:** Organizes `.mp4`, `.avi`, `.mkv`, `.mov`, and `.wmv` files.
- 💿 **Installers:** Organizes `.exe`, `.msi`, `.deb`, and `.dmg` files.
- 📦 **Others:** Stores files with unrecognized extensions.
- 📁 Automatically creates category folders.
- 🛡️ Prevents existing files from being overwritten by renaming duplicates.
- 📊 Displays a summary of the files moved.

## 🛠️ Technologies Used

- 🐍 Python 3
- `os` — for file and folder operations.
- `shutil` — for moving files.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/thv-19/automated-file-organizer.git
```

### 2. Open the project folder

```bash
cd automated-file-organizer
```

### 3. Run the program

```bash
python file_organizer.py
```

### 4. Enter a folder path

When prompted, enter the full path of the folder you want to organize.

## 💻 Example

**Before organizing:**

```text
MyFiles/
├── photo.jpg
├── report.pdf
├── song.mp3
├── movie.mp4
└── notes.xyz
```

**After organizing:**

```text
MyFiles/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audios/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
└── Others/
    └── notes.xyz
```

## 📊 Example Output

```text
Moved: photo.jpg -> Images/
Moved: report.pdf -> Documents/
Moved: song.mp3 -> Audios/
Moved: movie.mp4 -> Videos/
Moved: notes.xyz -> Others/

Organization complete!
Total files moved: 5
```

## 📂 Project Structure

```text
automated-file-organizer/
│
├── file_organizer.py
├── README.md
└── requirements.txt
```

## 📦 Requirements

This project uses Python's built-in modules (`os` and `shutil`), so no additional packages are required.

## 🎯 Project Goal

The goal of this project is to practice Python fundamentals, including:

- Functions
- Dictionaries and lists
- Loops and conditional statements
- File handling
- Working with Python modules

## 👩‍💻 Author

**Trainlyze Week 1 Project**

⭐ If you find this project useful, consider giving the repository a star!

---

