import pandas as pd

def merge_excel_tables(ifc_item_type_excel_table, item_type_excel_table):
    out_tables = []
    for excel_table in item_type_excel_table:
        table = {}
        merged_table = pd.merge(ifc_item_type_excel_table, excel_table["df"], on="ElementId", how="outer")
        table["Item Type Name"] = excel_table["Item Type Name"]
        table["Library"] = excel_table["Library"]
        table["df"] = merged_table
        out_tables.append(table)
    return out_tables

def merge_ifc_excel(merged_excel_dataframes, ifc_dataframes):
    out_tables = []
    for table in merged_excel_dataframes:
        item_type_name = table["Item Type Name"]
        if item_type_name in ifc_dataframes:
            merged_df = pd.merge(table["df"], ifc_dataframes[item_type_name], on="GlobalId", how="outer")
            out_tables.append({"Item Type Name": item_type_name, "Library": table["Library"], "df": merged_df})
    return out_tables

def write_merged_tables_to_excel(merged_dataframes, data_path):
    for item_type, df in merged_dataframes.items():
        excel_workbook_path = f"{data_path}\\{item_type['Library']}.xlsx"
        df.to_excel(excel_workbook_path, sheet_name=item_type['Item Type Name'], index=False)
