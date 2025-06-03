import argparse
import pandas as pd

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



def get_excel_tables(item_types, data_path):
    """
    Loads Excel tables into pandas DataFrames.
    Args:
        item_types (list): A list of item types to load.
        data_path (str): The path to the data directory.
    Returns:
        dict: A dictionary of DataFrames, keyed by item type name.
    """
    excel_tables = {}
    for item_type in item_types:
        item_type_name = item_type["Item Type Name"]
        excel_workbook_path = f"{data_path}\\{item_type['Library']}.xlsx"
        excel_tables[item_type_name] = pd.read_excel(excel_workbook_path, sheet_name=item_type_name)
    return excel_tables

def get_ifc_excel_table(ifc_item_type, data_path):
    """
    Loads the Excel table for a specific IFC item type into a pandas DataFrame.
    Args:
        ifc_item_type (dict): The IFC item type information.
        data_path (str): The path to the data directory.
    Returns:
        pandas.DataFrame: The DataFrame containing the Excel table for the specified IFC item type.
    """
    item_type_name = ifc_item_type["Item Type Name"]
    excel_workbook_path = f"{data_path}\\{ifc_item_type['Library']}.xlsx"
    ifc_dataframe = pd.read_excel(excel_workbook_path, sheet_name=item_type_name)
    return ifc_dataframe