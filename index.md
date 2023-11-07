---
layout: default
title: Home
---

# Welcome to My Python Scripts

Here you can find a list of my Python projects hosted on GitHub.

{% for file in site.static_files %}
  {% if file.path contains '.py' %}
- [{{ file.name }}]({{ file.path }})
  {% endif %}
{% endfor %}
