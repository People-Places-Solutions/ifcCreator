import os
import win32com.client


class MicroStationImporter:
    """
    Handles the automation of importing item type instances into MicroStation/OpenRoads
    using COM automation and key-ins.
    """

    def __init__(self, app_name="MicroStationDGN.Application"):
        """
        Initializes the COM connection to MicroStation/OpenRoads.
        """
        try:
            self.app = win32com.client.GetActiveObject(app_name)
            print(f"Connected to {app_name} successfully.")
        except Exception as e:
            raise RuntimeError(f"Failed to connect to MicroStation: {e}")

    def import_itemtypes_from_excel(self, excel_path: str):
        """
        Sends a key-in command to import item type instances from an Excel file.

        Parameters:
            excel_path (str): Full path to the Excel file.
        """
        if not os.path.exists(excel_path):
            raise FileNotFoundError(f"Excel file not found: {excel_path}")

        keyin = f'ITEMTYPE INSTANCES IMPORT EXCEL "{excel_path}"'
        try:
            self.app.CadInputQueue.SendKeyin(keyin)
            print(f"Import command sent for: {excel_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to send key-in to MicroStation: {e}")
