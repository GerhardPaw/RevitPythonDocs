import clr
clr.AddReference("RevitNodes")
clr.AddReference("RevitServices")

import Revit
clr.ImportExtensions(Revit.Elements)

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = DocumentManager.Instance.CurrentDBDocument

viewport_dict = {vp.ViewId: vp for vp in FilteredElementCollector(doc)
                 .OfCategory(BuiltInCategory.OST_Viewports)
                 .WhereElementIsNotElementType()
                 .ToElements()}

if not viewport_dict:
    raise Exception("No viewports found in the project")
  
views = UnwrapElement(IN[0]) if isinstance(IN[0], list) else [UnwrapElement(IN[0])]

if not views:
    raise Exception("The view input is empty")

matching_viewports = [viewport_dict.get(view.Id) for view in views if view.Id in viewport_dict]

if not matching_viewports:
    raise Exception("No viewports found, the views are not placed on a sheet.")

OUT = matching_viewports
