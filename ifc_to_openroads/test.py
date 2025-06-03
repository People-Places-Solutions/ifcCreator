import config
import extractor
import pytest
import merger
import helpers
import pandas as pd
import os

data_path = os.path.abspath(config.DATA_DIRECTORY)

def test_extractor():
    in_file = r"ifc_to_openroads\data\ifc_data.ifc"
    dict_of_dataframes = extractor.get_property_sets(in_file, config.IFC_ELEMENT_TYPE, config.ITEM_TYPES)
    assert type(dict_of_dataframes) == dict
    assert len(dict_of_dataframes) > 0
    return dict_of_dataframes

def test_get_excel_tables():
    excel_tables = helpers.get_excel_tables(config.ITEM_TYPES, config.DATA_DIRECTORY)
    assert type(excel_tables) == dict
    assert len(excel_tables) > 0
    return excel_tables


def test_get_ifc_excel_table():
    ifc_item_type = config.IFC_ITEM_TYPE
    ifc_dataframe = helpers.get_ifc_excel_table(ifc_item_type, config.DATA_DIRECTORY)
    assert type(ifc_dataframe) == pd.DataFrame
    assert not ifc_dataframe.empty
    return ifc_dataframe


def test_merge_tables(test_get_ifc_excel_table, test_get_excel_tables):
    merged_tables = merger.merge_excel_tables(test_get_ifc_excel_table, test_get_excel_tables)
    assert type(merged_tables) == dict
    assert len(merged_tables) > 0
    print("Merged tables:")
    for key, value in merged_tables.items():
        print(f"Table for {key}:")
        print(value)
        value.to_csv(f"{data_path}\\merged_{key}.csv", index=False)
    return merged_tables

def test_merge_ifc_excel(test_merge_tables, test_get_ifc_excel_table):
    merged_tables = merger.merge_ifc_excel(test_merge_tables, test_get_ifc_excel_table)
    assert type(merged_tables) == dict
    assert len(merged_tables) > 0
    print("Merged tables with IFC:")
    for key, value in merged_tables.items():
        print(f"Table for {key}:")
        print(value)
        value.to_csv(f"{data_path}\\merged_{key}_ifc.csv", index=False)

if __name__ == "__main__":
    # test_extractor()
    # test_get_excel_tables()
    # test_get_ifc_excel_table()
    # test_merge_tables(test_get_ifc_excel_table(), test_get_excel_tables())
    test_merge_ifc_excel(test_merge_tables(), test_get_ifc_excel_table())
