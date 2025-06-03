# The first item in this list should always be the IFC Item Type, which references the GlobalId of the IFC element.
from pathlib import Path


IFC_ITEM_TYPE = {"Library":"IFC", "Item Type Name":"IFC_sign"}
ITEM_TYPES= [{"Library":"WSDOT_Item_Types", "Item Type Name":"Signs"}]

IFC_ELEMENT_TYPE = "IfcBuildingElementProxy"

current_file_path = Path(__file__).resolve()

DATA_DIRECTORY = current_file_path.parent / "data"

print(DATA_DIRECTORY)