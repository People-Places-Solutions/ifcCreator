import config
import extractor
import pytest
import merger
import helpers
import pandas as pd
import os


data_path = os.path.abspath(config.DATA_DIRECTORY)

@pytest.fixture(scope="session")
def data_path():
    return os.path.abspath(config.DATA_DIRECTORY)

@pytest.fixture(scope="session")
def ifc_file():
    return r"data\ifc_data.ifc"

@pytest.fixture(scope="session")
def dict_of_dataframes(ifc_file):
    return extractor.get_property_sets(ifc_file, config.IFC_ELEMENT_TYPE, config.ITEM_TYPES)

@pytest.fixture(scope="session")
def excel_tables():
    return helpers.get_excel_tables(config.ITEM_TYPES, config.DATA_DIRECTORY)

@pytest.fixture(scope="session")
def ifc_dataframe():
    return helpers.get_ifc_excel_table(config.IFC_ITEM_TYPE, config.DATA_DIRECTORY)

@pytest.fixture(scope="session")
def merged_tables(ifc_dataframe, excel_tables):
    return merger.merge_excel_tables(ifc_dataframe, excel_tables)

def test_extractor(dict_of_dataframes):
    assert type(dict_of_dataframes) == dict
    assert len(dict_of_dataframes) > 0

def test_get_excel_tables(excel_tables):
    assert type(excel_tables) == list
    assert len(excel_tables) > 0
    assert all(isinstance(table, dict) for table in excel_tables)
    assert all("df" in table for table in excel_tables)

def test_get_ifc_excel_table(ifc_dataframe):
    assert type(ifc_dataframe) == pd.DataFrame
    assert not ifc_dataframe.empty

def test_merge_tables(merged_tables):
    assert type(merged_tables) == list
    assert len(merged_tables) > 0

def test_merge_ifc_excel(merged_tables, dict_of_dataframes):
    merged_tables = merger.merge_ifc_excel(merged_tables, dict_of_dataframes)
    assert type(merged_tables) == list
    assert len(merged_tables) > 0
