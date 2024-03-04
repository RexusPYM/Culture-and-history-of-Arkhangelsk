from django import template
from user_profiles.forms import CommentForm
from user_profiles.models import Comment

register = template.Library()


@register.inclusion_tag("tags/comment_form.html")
def comment_form(historical_object_id):
    return {"comment_form": CommentForm,
            "historical_object_id": historical_object_id}


@register.simple_tag
def comments_show(historical_object_id):
    comments = Comment.objects.filter(hist_object_id=historical_object_id)
    return comments
