import clr
clr.AddReference('RevitServices')

from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

views = UnwrapElement(IN[0]) if isinstance(IN[0],list) else [UnwrapElement(IN[0])]
view_templates = UnwrapElement(IN[1]) if isinstance(IN[0],list) else [UnwrapElement(IN[1])]
successful_views = []

TransactionManager.Instance.EnsureInTransaction(doc)

for view, view_template in zip(views, view_templates):
	view.ViewTemplateId = view_template.Id
	if view.ViewTemplateId == view_template.Id:
		successful_views.append(view)

TransactionManager.Instance.TransactionTaskDone()

OUT = successful_views