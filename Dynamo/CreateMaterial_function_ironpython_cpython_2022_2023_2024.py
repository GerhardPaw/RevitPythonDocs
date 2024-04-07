import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from Autodesk.Revit.DB import Material

doc = DocumentManager.Instance.CurrentDBDocument

def create_material(name):

    material_id = Material.Create(doc, name)
    material = doc.GetElement(material_id)
    if not material:
        raise ValueError('No material created')

    return material

TransactionManager.Instance.EnsureInTransaction(doc)

material_name = 'material_01'
material = create_material(material_name)

TransactionManager.Instance.TransactionTaskDone()

OUT = material
