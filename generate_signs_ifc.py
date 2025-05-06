import ifcopenshell
import ifcopenshell.api
import csv
import ifcopenshell.api.root
import ifcopenshell.api.unit
import ifcopenshell.api.context
import ifcopenshell.api.project
import ifcopenshell.api.spatial
import ifcopenshell.api.geometry
import ifcopenshell.api.aggregate

def to_ifc_value(val):
    if val is None or val == "":
        return None
    elif isinstance(val, (int, float)):
        return ifcopenshell.entity_instance("IFCREAL", val)
    elif isinstance(val, str):
        return ifcopenshell.entity_instance("IFCTEXT", val)
    else:
        return ifcopenshell.entity_instance("IFCTEXT", str(val))


# --- Data dictionary defines which attributes to attach ---
data_dictionary = [
    {"name": "SignHeight", "type": "IfcLengthMeasure"},
    {"name": "SignText", "type": "IfcLabel"},
    {"name": "Condition", "type": "IfcLabel"},
    {"name": "InstalledDate", "type": "IfcDate"},
]

# --- Load sign data from CSV ---
def load_signs_from_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        signs = []
        for row in reader:
            # Convert numeric fields from strings
            row["x"] = float(row["x"])
            row["y"] = float(row["y"])
            row["z"] = float(row["z"])
            if "SignHeight" in row and row["SignHeight"]:
                row["SignHeight"] = float(row["SignHeight"])
            signs.append(row)
        return signs

signs = load_signs_from_csv("signs.csv")



# Create a blank model
model = ifcopenshell.api.project.create_file()

# All projects must have one IFC Project element
project = ifcopenshell.api.root.create_entity(model, ifc_class="IfcProject", name="My Project")

# Geometry is optional in IFC, but because we want to use geometry in this example, let's define units
# Assigning without arguments defaults to metric units
ifcopenshell.api.unit.assign_unit(model)

# Let's create a modeling geometry context, so we can store 3D geometry (note: IFC supports 2D too!)
context = ifcopenshell.api.context.add_context(model, context_type="Model")

# In particular, in this example we want to store the 3D "body" geometry of objects, i.e. the body shape
body = ifcopenshell.api.context.add_context(model, context_type="Model",
    context_identifier="Body", target_view="MODEL_VIEW", parent=context)

# Create a site, building, and storey. Many hierarchies are possible.
site = ifcopenshell.api.root.create_entity(model, ifc_class="IfcSite", name="My Site")

ifc = model

# --- PropertySet helper ---
def create_property_set(ifc, sign, dictionary):
    props = []
    for field in dictionary:
        key = field["name"]
        val = sign.get(key)
        prop = ifc.create_entity(
            "IfcPropertySingleValue",
            Name=key,
            NominalValue=to_ifc_value(val) if val else None
        )
        props.append(prop)
    return ifc.create_entity(
        "IfcPropertySet",
        GlobalId=ifcopenshell.guid.new(),
        Name="SignProperties",
        HasProperties=props
    )

# --- Create IFC elements for each sign ---
for sign in signs:
    proxy = ifcopenshell.api.run("root.create_entity", ifc, ifc_class="IfcBuildingElementProxy", name=sign["id"])

    # Place the sign at its coordinates
    placement_matrix = [
        [1, 0, 0, sign["x"]],
        [0, 1, 0, sign["y"]],
        [0, 0, 1, sign["z"]],
        [0, 0, 0, 1],
    ]
    ifcopenshell.api.run("geometry.edit_object_placement", ifc, product=proxy, matrix=placement_matrix)

    ifcopenshell.api.run("spatial.assign_container", ifc, relating_structure=site, product=proxy)

    # Add property set
    pset = create_property_set(ifc, sign, data_dictionary)
    ifc.create_entity(
        "IfcRelDefinesByProperties",
        GlobalId=ifcopenshell.guid.new(),
        RelatingPropertyDefinition=pset,
        RelatedObjects=[proxy]
    )

# --- Write IFC file ---
ifc.write("road_signs_from_csv.ifc")
print("✅ IFC file saved as 'road_signs_from_csv.ifc'")
