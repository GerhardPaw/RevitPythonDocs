# RevitPythonDocs
Collection of Python Scripts for Dynamo and pyRevit

Welcome to our repository dedicated to providing Python scripts for Revit, focusing on Dynamo and PyRevit extensions. This repository aims to foster a community-driven collection of scripts to enhance productivity and extend functionality within Revit through Python scripting.

Short Introduction
This repository hosts Python scripts tailored for Revit, supporting both Dynamo and PyRevit platforms. Whether you're automating repetitive tasks, extending Revit's capabilities, or exploring the vast possibilities of computational design within Revit, you'll find a growing library of scripts contributed by professionals and enthusiasts alike.

General Coding Guidelines
To maintain a high standard of quality and ensure consistency across contributions, we ask that all contributors adhere to the following guidelines:

Coding Style
Naming Conventions:
Use snake_case for variable names and function names.
Use camelCase only if you're contributing to an existing script that predominantly uses camelCase, to maintain consistency within the script.
Comments and Docstrings:
Provide comments and explanations as needed to clarify complex logic or decisions made in your code. Avoid over-commenting by explaining only where necessary.
Use # for comments. Start with a single-line comment at the top if you wish to include the author's name, webpage, or email.
For scripts where the title might not sufficiently explain the purpose, include a docstring at the beginning of your script with a brief explanation of its functionality.
File Naming Rules
Method or Task Representation: Scripts that encapsulate methods or tasks should be categorized into one of four versions: basic, advanced, function, example. Each version addresses a different level of complexity or use-case scenario.

Basic code represents the most simple but working code that demonstrates the use of the task.
A basic code must not handle errors or varying inputs what is why it will not work for every scenario. Also it will not give user feedback and might fail silently.
See the following basic code for getting the active sheet.

<pre lang="python"><code>
import clr
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

active_view = doc.ActiveView

if active_view.Category.Id == ElementId(BuiltInCategory.OST_Sheets):
    active_sheet = active_view

OUT = active_sheet
</code></pre>

Advanced code raises errors where necessary to give proper feedback to users.
Keep in mind that Dynamo already handles pretty much all exceptions itself what is why an excessive error handling is not necessary.
The error handling should focus on raising exceptions for null values to nprevent the code from failing silently.
If the script uses node inputs these have to be correctly handled for single elements and lists.
This code should work for all possible input scenarios and give user feedback in any possible case.
See the following advanced code for getting the active sheet.

<pre lang="python"><code>
import clr
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

active_view = doc.ActiveView

if active_view.Category.Id != ElementId(BuiltInCategory.OST_Sheets):
    raise TypeError("Active view is not of category Sheets")

OUT = active_view
</code></pre>

Function code encapsulates the whole task into a function and calls it accordingly.
This code should handle errors and work for single element and list inputs.

<pre lang="python"><code>
import clr
clr.AddReference("RevitServices")

from RevitServices.Persistence import DocumentManager
from Autodesk.Revit.DB import BuiltInCategory, ElementId

doc = DocumentManager.Instance.CurrentDBDocument

def get_active_sheet():

    active_view = doc.ActiveView
    if active_view.Category.Id != ElementId(BuiltInCategory.OST_Sheets):
        raise TypeError("Active view is not of category Sheets")

    return active_view

active_sheet = get_active_sheet()

OUT = active_sheet
</code></pre>

example: Provides fully-fledged examples demonstrating practical applications.
Larger, Multi-Task Scripts: Scripts encompassing multiple tasks or complex functionalities should be tagged as tool in their filename. Include a docstring at the beginning of the script, briefly explaining its purpose and any necessary background information.

Contributing to the Repository
We welcome contributions from everyone! To contribute your script:

Fork the Repository: Start by forking this repository to your GitHub account.
Add Your Script: Place your script in the appropriate directory (Dynamo or pyRevit). Ensure it adheres to the naming rules and guidelines mentioned above.
Document Your Code: Include comments, a docstring if necessary, and ensure your code follows the prescribed coding style.
Create a Pull Request (PR): Once you've added your script, create a pull request to the main repository. In your PR, provide a brief overview of your script and its purpose.
Review: Your PR will be reviewed by the community. This process ensures that contributions align with the project's goals and quality standards. You may be asked to make revisions based on feedback.
By following these guidelines, we can together build a valuable resource for all Revit users looking to leverage Python for automation and customization. Your contributions not only help grow this repository but also support the broader Revit community in exploring new possibilities.

Thank you for contributing and happy scripting!
