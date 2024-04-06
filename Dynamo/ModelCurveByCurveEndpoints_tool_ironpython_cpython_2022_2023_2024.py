import clr
import math
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import XYZ

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI.Selection import ObjectType

# Import ProtoGeometry with alias to avoid conflicts
clr.AddReference("ProtoGeometry")
import Autodesk.DesignScript.Geometry as DS

# Import ToDSType (bool) extension method
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

"""
    This script creates a model curve by the end points of two model curves
    - Run
    - Select point on first model curve near the desired end
    - Select point on second model curve near the desired end
    - Finish selection
    - Model curve will be created with the same line style as selected model curve
"""

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
sel = uiapp.ActiveUIDocument.Selection

# Function to get the line style of a Revit model curve
def get_line_style(curve_element):

    line_style_id = curve_element.LineStyle.Id
    line_style = doc.GetElement(line_style_id)
    # Raise error if element is null
    if line_style is None:
        raise Exception("Can´t get line style from line.")

    return line_style


# Function to apply a line style to a Revit model curve
def apply_line_style(dynamo_model_curve, graphics_style):

    # Retrieve the underlying Revit element
    revit_model_curve = dynamo_model_curve.InternalElement

    # Start a transaction
    TransactionManager.Instance.EnsureInTransaction(doc)

    # Access and set the line style parameter using the ElementId of the GraphicsStyle
    line_style_parameter = revit_model_curve.LookupParameter("Line Style")  # Revit parameter name
    if line_style_parameter and not line_style_parameter.IsReadOnly:
        # Use the ElementId of the GraphicsStyle object
        line_style_parameter.Set(graphics_style.Id)
    else:
        raise Exception("Line style parameter is not available or read-only.")

    TransactionManager.Instance.TransactionTaskDone()


def distance_between_points(pt1, pt2):
    return math.sqrt((pt2.X - pt1.X)**2 + (pt2.Y - pt1.Y)**2 + (pt2.Z - pt1.Z)**2)

def create_dynamo_line(start_point, end_point):
    # Convert Revit XYZ points to Dynamo Points and create a line
    return DS.Line.ByStartPointEndPoint(start_point.ToPoint(), end_point.ToPoint())

closest_endpoints = []
model_curves = []

# Start selection mode for multiple elements
refs = sel.PickObjects(ObjectType.Element, "Select multiple Model Curves")
for ref in refs:
    element = doc.GetElement(ref.ElementId)
    if hasattr(element, "GeometryCurve"):
        curve = element.GeometryCurve
        graphics_style = get_line_style(element)
        startPoint = curve.GetEndPoint(0)
        endPoint = curve.GetEndPoint(1)

        # Determine which endpoint is closer to the clicked point
        pickedPoint = ref.GlobalPoint
        if distance_between_points(startPoint, pickedPoint) < distance_between_points(endPoint, pickedPoint):
            closest_endpoints.append(startPoint)
        else:
            closest_endpoints.append(endPoint)

if not closest_endpoints:
    raise Exception("Error at calculating the endpoints of the lines")

# Create Dynamo lines and use them to create Revit model curves
TransactionManager.Instance.EnsureInTransaction(doc)
for i in range(0, len(closest_endpoints), 2):
    dynamo_line = create_dynamo_line(closest_endpoints[i], closest_endpoints[i + 1])
    model_curve = Revit.Elements.ModelCurve.ByCurve(dynamo_line)
    apply_line_style(model_curve, graphics_style)
    model_curves.append(model_curve)
TransactionManager.Instance.TransactionTaskDone()

if not model_curves:
    raise Exception("Error at creating the model curve")

OUT = model_curves