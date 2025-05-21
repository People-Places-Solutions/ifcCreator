import ifcopenshell
from ifccsv import IfcCsv
import sys
import pandas
in_file = r"ifc_out\placed_sign_meshes.ifc"

# Load your IFC file
ifc_file = ifcopenshell.open(in_file)

# Get an entity (example with getting the first wall)
signs = ifc_file.by_type('IfcGeographicElement')
if not signs:
    print("No walls found in the IFC file.")
    sys.exit() 

element_data = []
for sign in signs:
    psets = ifcopenshell.util.element.get_psets(sign)
    psets["Signs"]["GlobalId"] = sign.GlobalId
    print(psets)
    element_data.append(psets["Signs"])

df = pandas.DataFrame(element_data)
df.to_csv("ifc_out/psets_out.csv",index=False)


# Method 1: Using get_info() - returns attributes as a dictionary

