import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import Material

doc = DocumentManager.Instance.CurrentDBDocument

material_name = 'material_01'

try:
	TransactionManager.Instance.EnsureInTransaction(doc)
	material_id = Material.Create(doc, material_name)
	material = doc.GetElement(material_id)

	TransactionManager.Instance.TransactionTaskDone()
	OUT = material
except Exception as e:
	TransactionManager.Instance.ForceCloseTransaction()
	OUT = str(e)