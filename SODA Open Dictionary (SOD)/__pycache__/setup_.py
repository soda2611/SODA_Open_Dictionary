import os
import zipfile
import io
import shutil
import subprocess
import requests
import winshell

def download_file(url, filename):
    response = requests.get(url)
    open(filename, 'wb').write(response.content)

def install_python(exe_path):
    subprocess.run([exe_path, "/quiet", "InstallAllUsers=0", "PrependPath=1"])

url = "https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe"

filename = "python_installer.exe"

download_file(url, filename)

install_python(os.path.join(os.getcwd(), filename))

os.system(f"del /S /Q {filename}")

os.system("pip install pywin32 winshell requests kivymd==1.2.0 kivy googletrans==4.0.0rc1 eng-to-ipa pyttsx3 notify-py")
os.system("python.exe -m pip install --upgrade pip")

try:
    repo_url = "https://github.com/soda2611/SODA_Open_Dictionary/archive/refs/heads/main.zip"

    repo_dir = "SODA_Open_Dictionary-main"

    sod_dir = "SODA Open Dictionary (SOD)"

    response = requests.get(repo_url)

    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    zip_file.extractall()

    shutil.move(os.path.join(repo_dir, sod_dir), sod_dir)

    os.system(f"rmdir /S /Q {repo_dir}")

    python_file = os.path.abspath(f"{sod_dir}/UI.py")

    icon_file = os.path.abspath(f"{sod_dir}/func/Logo.ico")

    desktop = winshell.desktop()

    shortcut_name = "SODA Open Dictionary"

    shortcut = os.path.join(desktop, shortcut_name + ".lnk")

    with winshell.shortcut(shortcut) as link:
        link.path = python_file
        link.description = "An open dictionary for everyone"
        link.arguments = python_file
        link.icon_location = (icon_file, 0)
        link.working_directory = os.path.abspath(sod_dir)
    
except Exception as ex:
    print(ex)

