import pandas as pd


def merge_excel_tables(ifc_item_type_excel_table, item_type_excel_table):
    """
    Args:
        ifc_item_type_excel_table (pd.DataFrame): The IFC item type Excel table.
        item_type_excel_table (list): A list of item type Excel tables.

    Returns:
        list: A list of merged Excel tables.

    Description:
        This is run after all data has been retrieved by helper functions.
        The purpose is to combine the tables from the Item Types files with the IFC table,
        so that the new table will have all the correct Item Type rows and columns, but with the
        IFC GlobalId added in.
    """
    out_tables = []
    for excel_table in item_type_excel_table:
        table = {}
        merged_table = pd.merge(
            ifc_item_type_excel_table, excel_table["df"], on="ElementId", how="outer"
        )
        table["Item Type Name"] = excel_table["Item Type Name"]
        table["Library"] = excel_table["Library"]
        table["df"] = merged_table
        out_tables.append(table)
    return out_tables


def merge_ifc_excel(merged_excel_dataframes, ifc_dataframes):
    """
    Args: merged_excel_dataframes (list): A list of merged Excel DataFrames.
          ifc_dataframes (dict): A dictionary of IFC DataFrames keyed by item type name.

    Returns:
        list: A list of merged tables.

    Description:
        This function is run after the Item Type Excel file tables have been merged.
        The purpose of this function is to populate the data extracted from the .ifc file
        into the table that was created from the Item Type Excel file and has been correctly formatted.
    """
    out_tables = []
    for table in merged_excel_dataframes:
        item_type_name = table["Item Type Name"]
        if item_type_name in ifc_dataframes:
            updated_excel_df = table["df"].set_index("GlobalId", drop=True)
            updated_ifc_df = ifc_dataframes[item_type_name].set_index(
                "GlobalId", drop=True
            )

            for col in updated_ifc_df.columns:
                if col in updated_excel_df.columns:
                    updated_excel_df[col] = updated_excel_df[col].astype(object)

            updated_excel_df.update(updated_ifc_df, overwrite=True)
            out_tables.append(
                {
                    "Item Type Name": item_type_name,
                    "Library": table["Library"],
                    "df": updated_excel_df,
                }
            )
    return out_tables


def write_merged_tables_to_excel(merged_dataframes, data_path):
    """
    Args:
        merged_dataframes (list): A list of merged DataFrames to write to Excel.
        data_path (str): The path to the data directory.

    Description:
        This function writes the merged DataFrames to Excel files in the specified data directory.
    """
    for table in merged_dataframes:
        excel_workbook_path = f"{data_path}\\{table['Library']}.xlsx"
        with pd.ExcelWriter(
            excel_workbook_path, engine="openpyxl", mode="a", if_sheet_exists="replace"
        ) as writer:
            # Write the new DataFrame to a new sheet
            table["df"].to_excel(
                writer, sheet_name=table["Item Type Name"], index=False
            )
