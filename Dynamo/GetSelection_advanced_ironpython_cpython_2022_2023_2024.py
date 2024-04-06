import clr
clr.AddReference("RevitNodes")
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

selection_ids = uidoc.Selection.GetElementIds()
selection = []

for id in selection_ids:
    element = doc.GetElement(id)
    selection.append(element)

if not selection:
    raise ValueError("No elements selected")

OUT = selection