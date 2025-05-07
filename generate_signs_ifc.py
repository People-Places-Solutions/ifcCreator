import ifcopenshell.api.pset
import ifcopenshell.api.root
import ifcopenshell.api.unit
import ifcopenshell.api.context
import ifcopenshell.api.project
import ifcopenshell.api.geometry

import numpy as np

model = ifcopenshell.api.project.create_file()


project = ifcopenshell.api.root.create_entity(model, ifc_class="IfcProject", name="My Project")

ifcopenshell.api.unit.assign_unit(model)

context = ifcopenshell.api.context.add_context(model, context_type="Model")

body = ifcopenshell.api.context.add_context(model, context_type="Model",
    context_identifier="Body", target_view="MODEL_VIEW", parent=context)

def add_property_set(file, product):
    pset = ifcopenshell.api.pset.add_pset(file, product=product, name="Signs")
    ifcopenshell.api.pset.edit_pset(file, pset=pset, properties={"sign_int": 37})

def create_sign(file, x, y, z):
    matrix = np.array([[0, -1, 0, x], 
                   [1, 0, 0, y], 
                   [0, 0, 1, z],
                   [0, 0, 0, 1]])
    sign = ifcopenshell.api.root.create_entity(file, ifc_class = "IfcGeographicElement", predefined_type="Sign")
    ifcopenshell.api.geometry.edit_object_placement(file, product=sign, matrix=matrix,is_si=True)

    vertices = [[(-1.,-1.,0.), (-1.,1.,0.), (1.,1.,0.), (1.,-1.,0.), (0.,0.,1.)]]
    faces = [[(0,1,2,3), (0,4,1), (1,4,2), (2,4,3), (3,4,0)]]
    sign_representation = ifcopenshell.api.geometry.add_mesh_representation(file, context=body, vertices=vertices, faces=faces)
    ifcopenshell.api.geometry.assign_representation(file,product=sign,representation=sign_representation)
    add_property_set(model, sign)

def create_point(file, x, y, z):
    matrix = np.array([[0, -1, 0, x], 
                   [1, 0, 0, y], 
                   [0, 0, 1, z],
                   [0, 0, 0, 1]])
    sign = ifcopenshell.api.root.create_entity(file, ifc_class = "IfcAnnotation", predefined_type="SurveyPoint")
    ifcopenshell.api.geometry.edit_object_placement(file, product=sign, matrix=matrix,is_si=True)

    # vertices = [[(-1.,-1.,0.), (-1.,1.,0.), (1.,1.,0.), (1.,-1.,0.), (0.,0.,0.)]]
    # faces = [[(0,1,2,3), (0,4,1), (1,4,2), (2,4,3), (3,4,0)]]
    # sign_representation = ifcopenshell.api.geometry.add_mesh_representation(file, context=body, vertices=vertices, faces=faces)
    # ifcopenshell.api.geometry.assign_representation(file,product=sign,representation=sign_representation)
    add_property_set(model, sign)


create_point(model, -3, -3, 0)
create_sign(model, 3, 3, 0)


model.write("ifc_out/element_model.ifc")