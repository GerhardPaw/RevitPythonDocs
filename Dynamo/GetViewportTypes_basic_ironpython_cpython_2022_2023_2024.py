import clr
clr.AddReference("RevitNodes")
clr.AddReference("RevitServices")
clr.AddReference("RevitAPI")

import Revit
clr.ImportExtensions(Revit.Elements)

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, ElementType

doc = DocumentManager.Instance.CurrentDBDocument

viewport_types = []
element_types = FilteredElementCollector(doc).OfClass(ElementType).ToElements()

for element_type in element_types:
    if hasattr(element_type, "FamilyName") and element_type.FamilyName == "Viewport":
        viewport_types.append(element_type)

OUT = viewport_types