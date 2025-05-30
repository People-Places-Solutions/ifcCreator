import argparse

def get_command_line_input():
    """
    Parses command line arguments for IFC file path, IFC type, and property set name.
    Returns:
        str: Path to the IFC file.
    """
    parser = argparse.ArgumentParser(description="Extract attributes from an IFC file and export as a table.")
    parser.add_argument("excel_woorkbook_path", help="Path to the exported Item Types Excel workbook")
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

    print(f"Extracting from IFC at {args.ifc_path}, type: {args.element_type}, property set: {args.pset_name}")
    print(f"Exporting to Excel workbook at {args.excel_woorkbook_path}")

    if not args.ifc_path.endswith('.ifc'):
        raise ValueError("The provided IFC file path must end with '.ifc'.")
    
    return args.excel_woorkbook_path ,args.ifc_path, args.element_type, args.pset_name