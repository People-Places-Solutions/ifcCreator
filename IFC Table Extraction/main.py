import utils.helpers
from itemtypes.microstation_importer import MicroStationImporter

if __name__ == "__main__":
    # Get command line input for the Excel file path, IFC file path, element type, and property set name
    excel_file, input_ifc, element_type, pset_name = utils.helpers.get_command_line_input()

    open_roads = MicroStationImporter()
    open_roads.create_dump_file()

