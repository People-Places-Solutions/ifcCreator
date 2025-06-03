import ifcopenshell
import sys
import ifcopenshell.util
import ifcopenshell.util.element
import pandas as pd


def get_property_sets(in_file, ifc_element_type, item_types):
    """Extracts property sets from IFC elements of a specified type and saves them to a DataFrame.
    Args:
        in_file (str): Path to the IFC file.
        element_type (str): Type of IFC element to extract, which is definied in the config file.
        pset_name (str): Name of the property set to extract.
        config (module): Configuration module containing variables like ITEM_TYPES.

        Returns:
        pandas.DataFrame: DataFrame containing the GlobalId and properties of the specified property set.

        Description:
            This function extracts property sets from IFC elements of a specified type and saves them to a DataFrame.
            The property sets are nested dictionaries and must be flattened and formatted to comply with the OpenRoads
            Item Types Excel workbook structure.
    """

    ifc_file = ifcopenshell.open(in_file)
    elements = ifc_file.by_type(ifc_element_type)

    if not elements:
        print(f"No elements of type {ifc_element_type} found in the IFC file.")
        sys.exit()

    dataframes = {}
    for elem in elements:
        psets = ifcopenshell.util.element.get_psets(elem)

        for item_type in item_types:
            item_type_name = item_type["Item Type Name"]
            if item_type_name not in dataframes:
                dataframes[item_type_name] = pd.DataFrame()

            item_type_dict = psets[item_type_name]

            item_type_dict["GlobalId"] = elem.GlobalId
            item_type_dict = format_pset_dictionaries(item_type_dict)

            dataframes[item_type_name] = pd.concat(
                [dataframes[item_type_name], pd.DataFrame([item_type_dict])],
                ignore_index=True,
            )
    return dataframes


def format_pset_dictionaries(item_type_dict, formatted_dict={}, prefix=""):
    """
    Args:
        item_type_dict (dict): The original item type dictionary to format.
        formatted_dict (dict, optional): The formatted dictionary to populate. Defaults to an empty dict.
        prefix (str, optional): The prefix to use for nested keys. Defaults to an empty string.

    Returns:
        dict: The formatted dictionary with flattened keys.

    Description:
        This function is meant to be internal to this file and is used to format the property set dictionaries
        created by OpenRoads' method of exporting Item Types to .ifc files.
    """
    unused_keys = ["type", "id", "UsageName"]
    for key, value in item_type_dict.items():
        if isinstance(value, dict):
            # If the value is a dictionary, format it recursively with the prefix
            format_pset_dictionaries(value, formatted_dict, f"{prefix}{key}.")
            # Recursively format nested dictionaries
        else:
            if key in unused_keys:
                continue
            prefix = prefix.removesuffix("properties.")
            formatted_dict[f"{prefix}{key}"] = value

    return formatted_dict
