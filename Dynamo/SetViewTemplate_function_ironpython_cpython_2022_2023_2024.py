import clr
clr.AddReference("RevitServices")

import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

views = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
view_templates = UnwrapElement(IN[1]) if isinstance(IN[0],list) else [UnwrapElement(IN[1])]

def set_view_template():

    successful_views = []

    TransactionManager.Instance.EnsureInTransaction(doc)

    for view, view_template in zip(views, view_templates):
        view.ViewTemplateId = view_template.Id
        if view.ViewTemplateId == view_template.Id:
            successful_views.append(view)

    TransactionManager.Instance.TransactionTaskDone()

    if not successful_views:
        raise ValueError("No view templates have been applied")
    return successful_views


successful_views = set_view_template()

OUT = successful_views