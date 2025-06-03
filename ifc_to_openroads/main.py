
import config
import extractor
import helpers
import merger
from microstation_importer import MicroStationImporter
import pandas as pd
from pathlib import Path

if __name__ == "__main__":

    input_ifc_file = helpers.get_command_line_input()

    input_ifc_file_dir = Path(input_ifc_file).parent

    helpers.copy_xlsx_files(input_ifc_file_dir, config.DATA_DIRECTORY)

    extracted_ifc_data = extractor.get_property_sets(input_ifc_file, config.IFC_ELEMENT_TYPE, config.ITEM_TYPES)
    item_type_excel_tables = helpers.get_excel_tables(config.ITEM_TYPES, config.DATA_DIRECTORY)
    ifc_item_type_excel_table = helpers.get_ifc_excel_table(config.IFC_ITEM_TYPE, config.DATA_DIRECTORY)
    merged_tables = merger.merge_excel_tables(ifc_item_type_excel_table, item_type_excel_tables)
    data_tables_merged = merger.merge_ifc_excel(merged_tables, extracted_ifc_data)


    merger.write_merged_tables_to_excel(data_tables_merged, config.DATA_DIRECTORY)

    for table in data_tables_merged:
        excel_workbook_path = f"{config.DATA_DIRECTORY}\\{table['Library']}.xlsx"
        importer = MicroStationImporter()
        importer.import_itemtypes_from_excel(excel_workbook_path)

