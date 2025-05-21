import ifcopenshell.api.pset
import ifcopenshell.api.root
import ifcopenshell.api.unit
import ifcopenshell.api.context
import ifcopenshell.api.project
import ifcopenshell.api.geometry
import numpy as np
import pandas as pd

def add_property_set(file, product):
    pset = ifcopenshell.api.pset.add_pset(file, product=product, name="Signs")
    ifcopenshell.api.pset.edit_pset(file, pset=pset, properties={"sign_int": 37})

def create_sign(file, body, x, y, z):
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
    add_property_set(file, sign)

def create_point(file, body, x, y, z):
    matrix = np.array([[0, -1, 0, x], 
                   [1, 0, 0, y], 
                   [0, 0, 1, z],
                   [0, 0, 0, 1]])
    sign = ifcopenshell.api.root.create_entity(file, ifc_class = "IfcAnnotation", predefined_type="SurveyPoint")
    ifcopenshell.api.geometry.edit_object_placement(file, product=sign, matrix=matrix,is_si=True)

    # vertices = [[(0.,0.,0.), (0.,0.,0.), (0.,0.,0.), (0.,0.,0.), (0.,0.,0.)]]
    # faces = [[(0,1,2,3), (0,4,1), (1,4,2), (2,4,3), (3,4,0)]]
    # sign_representation = ifcopenshell.api.geometry.add_mesh_representation(file, context=body, vertices=vertices, faces=faces)
    # ifcopenshell.api.geometry.assign_representation(file,product=sign,representation=sign_representation)
    add_property_set(file, sign)

def import_signs(csv_in, unit):
    df = pd.read_csv(csv_in)
    unit_dict = {
        "US_SURVEY_FOOT": 1200/3937,
        "INTERNATIONAL_FOOT" : 0.3048,
        "METER" : 1
    }
    df['X_2011NAD83'] = df['X_2011NAD83']*unit_dict[unit]
    df['Y_2011NAD83'] = df['Y_2011NAD83']*unit_dict[unit]
    df['Z'] = df['Z']*unit_dict[unit]
    return df


if __name__ == "__main__":
    import_signs(r"data\Finalsets_merged_XYZ.csv", "US_SURVEY_FOOT")

