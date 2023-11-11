import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

view_family_types = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.ViewFamilyType).WhereElementIsElementType().ToElements()

OUT = view_family_types