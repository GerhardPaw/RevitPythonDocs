import clr
clr.AddReference("RevitNodes")
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

def get_selection():
    selection_ids = uidoc.Selection.GetElementIds()
    selection = [doc.GetElement(id) for id in selection_ids]

    if not selection:
        raise ValueError("No elements selected")

    return selection

selection = get_selection()

OUT = selection