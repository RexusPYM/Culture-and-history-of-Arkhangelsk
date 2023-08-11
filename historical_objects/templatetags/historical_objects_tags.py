from django import template
from historical_objects.forms import EmailForm

register = template.Library()


@register.inclusion_tag("tags/email_form.html")
def email_form():
    return {"email_form": EmailForm}
