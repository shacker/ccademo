ccademo
=======

CCA intranet demo

Course with many students and instructors
http://127.0.0.1:8000/courses/offering/20356/participants
API:
http://127.0.0.1:8000/api/offerings/5606/

Rendering forms with bootstrap: Two custom libs installed:

django-bootstrap-form
django-widget-tweaks

When we render an entire {{form}} at once, best path is:

{% load bootstrap %}
...
{{ search_form|bootstrap }}

But when we need per-field granularity, apply the classes Bootstrap needs individually via widget-tweaks:

{% load widget_tweaks %}
...
{% render_field form.title class+="form-control" %}

Fork of django_messages - special URL identifier
http://127.0.0.1:8000/messages/compose/group-offering-20356/

