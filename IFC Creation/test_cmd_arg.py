import argparse
import ifcopenshell  # Assuming you're using ifcopenshell to read IFC files
import pandas as pd



def get_input():
    """
    Parses command line arguments for IFC file path, IFC type, and property set name.
    Returns:
        str: Path to the IFC file.
    """
    parser = argparse.ArgumentParser(description="Extract attributes from an IFC file and export as a table.")
    parser.add_argument("ifc_path", help="Path to the IFC file")
    parser.add_argument(
        "ifc_type",
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

    print(f"Extracting from IFC at {args.ifc_path}, type: {args.ifc_type}")
    return args.ifc_path


if __name__ == "__main__":
    get_input()
