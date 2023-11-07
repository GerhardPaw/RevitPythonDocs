import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

selection_ids = uidoc.Selection.GetElementIds()

selection = [element for id in selection_ids]
OUT = selection
