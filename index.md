---
layout: default
title: Home
---

# Welcome to My Python Scripts

Here you can find a list of my Python projects hosted on GitHub.

{% for file in site.static_files %}
  {% if file.path contains '.py' %}
- [{{ file.name | remove: '_ironpython_2023.py' }}]({{ file.path }})
  {% endif %}
{% endfor %}
