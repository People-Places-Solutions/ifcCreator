@echo off
set /p input_path="Enter the path to the IFC file: "
"C:\ProgramData\Bentley\PowerPlatformPython\python\python.exe" ifc_to_openroads\main.py %input_path%
pause
