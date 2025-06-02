
import config
from ifc_to_openroads import extractor
if __name__ == "__main__":
    element_type = "IfcBuildingElementProxy"  # Change this to the desired element type
    in_file = r"ifc_to_openroads\data\ifc_data.ifc"
    dfs = extractor.get_property_sets(in_file, element_type, config)
    print(dfs)

