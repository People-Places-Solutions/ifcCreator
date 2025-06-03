import pandas as pd

def merge_excel_tables(ifc_table, excel_tables):
    out_tables = {}
    for key, value_table in excel_tables.items():
        out_tables[key] = pd.merge(ifc_table,value_table, on="ElementId", how="outer")
    return out_tables

def merge_ifc_excel(merged_excel_tables, ifc_table):
    out_tables = {}
    for key, value_table in merged_excel_tables.items():
        out_tables[key] = pd.merge(ifc_table,value_table, on="GlobalId", how="outer")
    return out_tables

