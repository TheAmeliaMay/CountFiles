@echo off
set /p Input=Directory: 
python3 count_files.py -d %Input%