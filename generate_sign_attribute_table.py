import ifcopenshell
from ifccsv import IfcCsv
import sys
in_file = r"ifc_out\placed_sign_meshes.ifc"

# Load your IFC file
ifc_file = ifcopenshell.open(in_file)

# Get an entity (example with getting the first wall)
signs = ifc_file.by_type('IfcGeographicElement')
if not signs:
    print("No walls found in the IFC file.")
    sys.exit() 

sign = signs[0]

# Method 1: Using get_info() - returns attributes as a dictionary
attributes = sign.get_info()
attributes_list = list(attributes.keys())


model = ifcopenshell.open(r"C:\Users\SMITHS4\Python Projects\ifcCreator\ifc_out\placed_sign_meshes.ifc")
# Using the selector is optional. You may specify elements as a list manually if you prefer.
# e.g. elements = model.by_type("IfcElement")
elements = ifcopenshell.util.selector.filter_elements(model, "IfcElement")


attributes = attributes_list

# Export our model's elements and their attributes to a CSV.
ifc_csv = IfcCsv()
ifc_csv.export(model, elements, attributes, output="ifc_out/out.csv", format="csv", delimiter=",", null="-")
