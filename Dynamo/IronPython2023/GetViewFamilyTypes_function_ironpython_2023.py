import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

def get_view_family_types():
	types = FilteredElementCollector(doc).OfClass(Autodesk.Revit.DB.ViewFamilyType).WhereElementIsElementType().ToElements()
	return types

view_family_types = get_view_family_types()

OUT = view_family_types