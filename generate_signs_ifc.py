import ifcopenshell.api.pset
import ifcopenshell.api.root
import ifcopenshell.api.unit
import ifcopenshell.api.context
import ifcopenshell.api.project
import ifcopenshell.api.geometry
import helpers
import numpy as np

model = ifcopenshell.api.project.create_file()


project = ifcopenshell.api.root.create_entity(model, ifc_class="IfcProject", name="My Project")

ifcopenshell.api.unit.assign_unit(model)

context = ifcopenshell.api.context.add_context(model, context_type="Model")

body = ifcopenshell.api.context.add_context(model, context_type="Model",
    context_identifier="Body", target_view="MODEL_VIEW", parent=context)

data = helpers.import_signs(r"data\Finalsets_merged_XYZ.csv", "US_SURVEY_FOOT")

# create_point(model, -3, -3, 0)
for index, row in data.iterrows():
    helpers.create_point(model, body, row['X_2011NAD83'], row['Y_2011NAD83'], row['Z'])


model.write("ifc_out/points_signs.ifc")