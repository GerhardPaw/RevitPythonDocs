import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

try:
	selection_ids = uidoc.Selection.GetElementIds()
	selection = [doc.GetElement(id) for id in selection_ids]
	OUT = selection if selection else 'No elements selected'

except Exception as e:
	OUT = str(e)