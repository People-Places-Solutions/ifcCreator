
import config
import extractor
import helpers
import merger
from microstation_importer import MicroStationImporter
import pandas as pd

if __name__ == "__main__":

    # input_ifc_file = helpers.get_command_line_input()
    input_ifc_file = r"C:\Users\SMITHS4\Python Projects\ifcCreator\ifc_to_openroads\data\ifc_data.ifc"
    extracted_ifc_data = extractor.get_property_sets(input_ifc_file, config.IFC_ELEMENT_TYPE, config.ITEM_TYPES)
    item_type_excel_tables = helpers.get_excel_tables(config.ITEM_TYPES, config.DATA_DIRECTORY)
    ifc_item_type_excel_table = helpers.get_ifc_excel_table(config.IFC_ITEM_TYPE, config.DATA_DIRECTORY)
    merged_tables = merger.merge_excel_tables(ifc_item_type_excel_table, item_type_excel_tables)
    data_tables_merged = merger.merge_ifc_excel(merged_tables, extracted_ifc_data)

    data_tables_merged[0]["df"].to_csv(f"{config.DATA_DIRECTORY}\\merged_data.csv", index=False)

    # merger.write_merged_tables_to_excel(merged_tables, config.DATA_DIRECTORY)

    # for table in merged_tables:
    #     excel_workbook_path = f"{config.DATA_DIRECTORY}\\{table['Library']}.xlsx"
    #     MicroStationImporter.import_to_microstation(excel_workbook_path)
