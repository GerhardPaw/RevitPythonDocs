---
layout: default
title:
---

# IronPython Code for Revit 2023

Hyperlinks lead to file on GitHub

{% for file in site.static_files %}
  {% if file.path contains '.py' %}
- [{{ file.name | remove: '_ironpython_2023.py' }}](https://github.com/GerhardPaw/RevitPythonDatabase/blob/main/{{ file.path }})
  {% endif %}
{% endfor %}
