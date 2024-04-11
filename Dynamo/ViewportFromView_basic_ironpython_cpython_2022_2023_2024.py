import clr
clr.AddReference("RevitNodes")
clr.AddReference("RevitServices")

import Revit
clr.ImportExtensions(Revit.Elements)

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

# Create dictionary of all viewports and their id
viewport_dict = {vp.ViewId: vp for vp in FilteredElementCollector(doc)
                 .OfCategory(BuiltInCategory.OST_Viewports)
                 .WhereElementIsNotElementType()
                 .ToElements()}

views = UnwrapElement(IN[0]) if isinstance(IN[0], list) else [UnwrapElement(IN[0])]

matching_viewports = [viewport_dict.get(view.Id) for view in views if view.Id in viewport_dict]

OUT = matching_viewports
