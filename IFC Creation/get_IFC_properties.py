import argparse
import ifcopenshell
import sys
import pandas
import argparse

def get_command_line_input():
    """
    Parses command line arguments for IFC file path, IFC type, and property set name.
    Returns:
        str: Path to the IFC file.
    """
    parser = argparse.ArgumentParser(description="Extract attributes from an IFC file and export as a table.")
    parser.add_argument("ifc_path", help="Path to the IFC file")
    parser.add_argument(
        "element_type",
        nargs="?",
        default="IfcCivilElement",
        help="Type of IFC element (e.g., IfcGeographicElement, IfcCivilElement). Optional."
    )
    parser.add_argument(
        "pset_name",
        nargs="?",
        default="Signs",
        help="Name of the property set to extract. Must be the same name as the Item Type library. Optional."
    )

    args = parser.parse_args()

    print(f"Extracting from IFC at {args.ifc_path}, type: {args.element_type}")
    return args.ifc_path, args.element_type, args.pset_name

def get_property_sets(in_file, element_type, pset_name):
    """Extracts property sets from IFC elements of a specified type and saves them to a DataFrame.
    Args:
        in_file (str): Path to the IFC file.
        element_type (str): Type of IFC element to extract (e.g., IfcGeographicElement, IfcCivilElement).
        pset_name (str): Name of the property set to extract.
        
        Returns:
        pandas.DataFrame: DataFrame containing the GlobalId and properties of the specified property set."""

    ifc_file = ifcopenshell.open(in_file)
    signs = ifc_file.by_type(element_type)

    if not signs:
        print(f"No elements of type {element_type} found in the IFC file.")
        sys.exit()

    element_data = []
    for sign in signs:
        psets = ifcopenshell.util.element.get_psets(sign)
        if pset_name not in psets:
            print(f"Property set '{pset_name}' not found in element {sign.GlobalId}.")
            continue

        psets[pset_name]["GlobalId"] = sign.GlobalId
        element_data.append(psets[pset_name])

    df = pandas.DataFrame(element_data)
    return df
