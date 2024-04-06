import clr
clr.AddReference("RevitAPI")
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, ViewSheet

doc = DocumentManager.Instance.CurrentDBDocument

def get_sheets():
    sheets = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()
    if not sheets:
        raise ValueError("No sheets found")
    return sheets

sheets = get_sheets()

OUT = sheets