@echo off
set /p input_path="Enter the path to the IFC file: "
python ifc_to_openroads\main.py %input_path%
pause
