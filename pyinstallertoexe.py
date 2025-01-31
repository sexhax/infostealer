import os
import subprocess

files = [f for f in os.listdir() if f.endswith('.py')]
if not files:
    print("No Python files found in the current directory.")
    exit(1)

for idx, file in enumerate(files, 1):
    print(f"{idx}. {file}")

while True:
    try:
        file_index = int(input("Enter the number of the file you want to convert to .exe: ")) - 1
        if 0 <= file_index < len(files):
            break
        else:
            print(f"Invalid number, please enter a number between 1 and {len(files)}.")
    except ValueError:
        print("Please enter a valid number.")

selected_file = files[file_index]

pyinstaller_path = r"C:\Users\0\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\pyinstaller.exe"

if not os.path.exists(pyinstaller_path):
    print(f"PyInstaller not found at {pyinstaller_path}. Please check the path.")
    exit(1)

try:
    subprocess.run([pyinstaller_path, '--onefile', selected_file], check=True)
    print(f"{selected_file} has been successfully converted to .exe.")
except subprocess.CalledProcessError:
    print(f"An error occurred while converting {selected_file} to .exe.")
