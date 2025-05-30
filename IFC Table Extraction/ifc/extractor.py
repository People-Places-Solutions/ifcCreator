import ifcopenshell
import sys
import ifcopenshell.util
import ifcopenshell.util.element
import pandas as pd

def get_property_sets(in_file, element_type):
    """Extracts property sets from IFC elements of a specified type and saves them to a DataFrame.
    Args:
        in_file (str): Path to the IFC file.
        element_type (str): Type of IFC element to extract (e.g., IfcGeographicElement, IfcCivilElement).
        pset_name (str): Name of the property set to extract.
        
        Returns:
        pandas.DataFrame: DataFrame containing the GlobalId and properties of the specified property set."""

    ifc_file = ifcopenshell.open(in_file)
    elements = ifc_file.by_type(element_type)

    if not elements:
        print(f"No elements of type {element_type} found in the IFC file.")
        sys.exit()

    dataframes = {}
    for elem in elements:
        psets = ifcopenshell.util.element.get_psets(elem)

        for pset in psets:
            if pset not in dataframes:
                dataframes[pset] = pd.DataFrame()
            pset["GlobalId"] = elem.GlobalId
            dataframes[pset] = dataframes[pset].append(psets[pset], ignore_index=True)

    return dataframes

if __name__ == "__main__":
    element_type = "IfcBuildingElementProxy"  # Change this to the desired element type
    in_file = r"C:\Users\SMITHS4\Python Projects\ifcCreator\IFC Table Extraction\data\ifc_data.ifc"
    get_property_sets(in_file, element_type)