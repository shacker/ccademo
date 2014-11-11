from django.template import Library
from dashboard.widget_functions import WidgetFunctions

register = Library()

@register.inclusion_tag("dashboard/widget_instance.html")
def render_widget(widget_instance, user):

	# We have the name of the function *as a string*  but need to call that func.
	# Call getattr() to get the function by string name
    get_data = getattr(WidgetFunctions, widget_instance.widget.func)
    data = get_data(widget_instance, user)

    # Return both the metadata (UserWidget instance) and the retrieved data for this instance
    return {
        'meta': widget_instance.widget,
        'data': data,
    }
