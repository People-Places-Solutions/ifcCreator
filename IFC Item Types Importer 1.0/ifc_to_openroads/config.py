# The first item in this list should always be the IFC Item Type, which references the GlobalId of the IFC element.
from pathlib import Path

# There must only be one IFC Item Type and it must only contain the GlobalId
IFC_ITEM_TYPE = {"Library": "IFC", "Item Type Name": "IFC_sign"}
# Any additional Item Types should be included in this list. This format mirrors the format seen
# when exporting item types from OpenRoads into excel
ITEM_TYPES = [{"Library": "WSDOT_Item_Types", "Item Type Name": "Signs"}]

# This is the default IFC element type exported by OpenRoads
IFC_ELEMENT_TYPE = "IfcBuildingElementProxy"

current_file_path = Path(__file__).resolve()

DATA_DIRECTORY = current_file_path.parent / "data"
