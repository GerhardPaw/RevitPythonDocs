import clr
clr.AddReference("RevitServices")
clr.AddReference("RevitAPI")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from Autodesk.Revit.DB import Material

doc = DocumentManager.Instance.CurrentDBDocument

material_name = "material_01"

TransactionManager.Instance.EnsureInTransaction(doc)
material_id = Material.Create(doc, material_name)
material = doc.GetElement(material_id)

TransactionManager.Instance.TransactionTaskDone()

if not material:
    raise ValueError("No material created")

OUT = material