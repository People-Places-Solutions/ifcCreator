"""Main entry point for the IFC to OpenRoads Item Types Importer."""

# IFC to OpenRoads Item Types Importer v1.0from pathlib import Path
from pathlib import Path
import config
import extractor
import helpers
import merger
import microstation_importer

if __name__ == "__main__":
    # Please refer to the README.md for usage instructions.

    # Get the input IFC file from command line arguments
    input_ifc_file = helpers.get_command_line_input()

    # Copy the Item Type Excel files to the data directory
    input_ifc_file_dir = Path(input_ifc_file).parent
    helpers.copy_xlsx_files(input_ifc_file_dir, config.DATA_DIRECTORY)

    # Pull Item Type data from the .ifc file
    extracted_ifc_data = extractor.get_property_sets(
        input_ifc_file, config.IFC_ELEMENT_TYPE, config.ITEM_TYPES
    )

    # Pull the Item Type Excel files from the data directory to
    # create table with correct columns and rows
    # including the ElementId
    item_type_excel_tables = helpers.get_excel_tables(
        config.ITEM_TYPES, config.DATA_DIRECTORY
    )

    # Pull the the ElementId and GlobalId info from the IFC Item Type Excel file
    ifc_item_type_excel_table = helpers.get_ifc_excel_table(
        config.IFC_ITEM_TYPE, config.DATA_DIRECTORY
    )

    # Merge the IFC Item Type Excel table with the Item Type Excel tables
    merged_tables = merger.merge_excel_tables(
        ifc_item_type_excel_table, item_type_excel_tables
    )

    # Merge the extracted IFC data with the merged Excel tables
    data_tables_merged = merger.merge_ifc_excel(merged_tables, extracted_ifc_data)

    # Write the merged tables to the Excel files in the data directory
    merger.write_merged_tables_to_excel(data_tables_merged, config.DATA_DIRECTORY)

    # For each Item Type Excel file, import the Item Types into OpenRoads
    for table in data_tables_merged:
        excel_workbook_path = f"{config.DATA_DIRECTORY}\\{table['Library']}.xlsx"
        importer = microstation_importer.MicroStationImporter()
        importer.import_itemtypes_from_excel(excel_workbook_path)
