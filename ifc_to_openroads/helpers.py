import argparse
import pandas as pd
import os
import shutil


def get_command_line_input():
    """
    Parses command line arguments for IFC file path, IFC type, and property set name.
    Returns:
        str: Path to the IFC file.
    """
    parser = argparse.ArgumentParser(description="Extract attributes from an IFC file and export as a table.")
    parser.add_argument("ifc_path", help="Path to the IFC file")

    args = parser.parse_args()

    print(f"Extracting from IFC at {args.ifc_path}")

    if not args.ifc_path.endswith('.ifc'):
        raise ValueError("The provided IFC file path must end with '.ifc'.")

    return args.ifc_path



def get_excel_tables(item_types, data_path):
    """
    Loads Excel tables into pandas DataFrames.
    Args:
        item_types (list): A list of item types to load.
        data_path (str): The path to the data directory.
    Returns:
        dict: A dictionary of DataFrames, keyed by item type name.
    """
    excel_tables = []
    for item_type in item_types:
        table = {}
        item_type_name = item_type["Item Type Name"]
        excel_workbook_path = f"{data_path}\\{item_type['Library']}.xlsx"
        table["Item Type Name"] = item_type["Item Type Name"]
        table["Library"] = item_type["Library"]
        table["df"] = pd.read_excel(excel_workbook_path, sheet_name=item_type_name)
        excel_tables.append(table)
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

def copy_xlsx_files(source_dir, dest_dir):
    # Ensure destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    
    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.xlsx'):
            source_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            shutil.copy2(source_file, dest_file)
            print(f"Copied {filename} to {dest_dir}")

