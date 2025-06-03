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
            # merged_df = pd.merge(table["df"], ifc_dataframes[item_type_name], on="GlobalId", how="outer")
            updated_excel_df = table["df"].set_index("GlobalId", drop=True)
            updated_ifc_df = ifc_dataframes[item_type_name].set_index("GlobalId", drop=True)
            
            for col in updated_ifc_df.columns:
                if col in updated_excel_df.columns:
                    updated_excel_df[col] = updated_excel_df[col].astype(object)

            updated_excel_df.update(updated_ifc_df, overwrite=True)
            out_tables.append({"Item Type Name": item_type_name, "Library": table["Library"], "df": updated_excel_df})
    return out_tables

def write_merged_tables_to_excel(merged_dataframes, data_path):
    for table in merged_dataframes:
        excel_workbook_path = f"{data_path}\\{table['Library']}.xlsx"
        # table["df"].to_excel(excel_workbook_path, sheet_name=table['Item Type Name'], index=False)
        with pd.ExcelWriter(excel_workbook_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            # Write the new DataFrame to a new sheet
            table["df"].to_excel(writer, sheet_name=table['Item Type Name'], index=False)

