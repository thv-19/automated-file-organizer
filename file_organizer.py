import os
import shutil
file_catagories = {"Image":[".jpg",".png",".jpeg",".gif",".bmp",".webp"],
                   "Document": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
                   "Audios":[".mp3",".wav", ".aac",".flac", ".m4a"],
                    "video":[".mp4", ".avi", ".mkv", ".mov", ".wmv"],
                     "Installer": [".exe", ".msi", ".deb", ".dmg"] }
#Return the category for a given file extension
def get_category(file_extension):
    for category, extensions in file_catagories.items():
        if file_extension.lower() in extensions:
            return category
    return "others"
#Organize files in the selected folder.
def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: The folder doesnot exist.")
        return
    moved_files = 0
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            continue
        _, extension = os.path.splitext(file_name)
        category = get_category(extension)
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)
        destination = os.path.join(category_folder, file_name)
        if os.path.exists(destination):
            base_name, file_extension= os.path.splitext(file_name)
            counter = 1
            while os.path.exists(destination):
                new_name = f"{base_name}_{counter}{file_extension}"
                destination = os.path.join(category_folder, new_name)
                counter +=1
        shutil.move(file_path, destination)
        print(f"Moved: {file_name}-> {category}/")
        moved_files +=1
    print("\nOrganization complete!")
    print(f"Total files moved: {moved_files}")
def main():
    folder_path = input("Enter the folder path to organize:").strip()
    organize_files(folder_path)
if __name__ =="__main__":
    main()