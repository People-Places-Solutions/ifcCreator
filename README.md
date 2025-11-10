# IFC Item Types Importer

## Description

This package is intended to address a shortcoming in Bentley Systems OpenRoads' ability to import .ifc files. By default, when an IFC is imported into OpenRoads only the geometry comes through, not any property sets and their properties. 
This package circumvents that by reading the properties directly from the IFC and then using the exported Item Types tables from OpenRoads to then populate those tables and reimport them into OpenRoads.
It is important to note that the schema between the IFC and OpenRoads must match exactly, so IFC files created outside of OpenRoads will not work with this method. Also, one of the exported Item Types tables must contain the GlobalId for each element imported into OpenRoads, which requires a custom expression inside OpenRoads to make that GlobalId accessible.


### Dependencies

* Windows Operating System
* Bentley Systems OpenRoads 24.00.00.205
* Python 3.12.10

### Installing

* Keep all files and folders in this program together
* The Python version MUST be Python 3.12.10. Download here https://www.python.org/downloads/release/python-31210/
* Python must be added as part of your PATH variable.
* Once python has been installed run the "Install Requirements.bat". This just runs the command below to install all required packages.
```
pip install -r requirements.txt
```

### Executing program

* Import your .ifc file into OpenRoads and attach the required Item Types and the IFC specific Item Type.
* Use the Export Item Types tool to export your Item Types to an empty folder only containing your .ifc file.
* Execute the Run.bat file in this directory and when prompted give it the full path to your .ifc file in the same foder as the exported Item Types files.
* For this to work the drawing with the .ifc files must be open in OpenRoads when the script is executed.

## Help

If you run into issues make sure that you are using the correct Item Types and that they match the properties contained in the .ifc file.

## Authors

Samuel Smith with Jacobs (smith.samuel@jacobs.com)

## Version History

* 0.1
    * Initial Release
