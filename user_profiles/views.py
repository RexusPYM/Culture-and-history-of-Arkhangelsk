from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Comment
from .models import Profile
from .forms import CommentForm


class MakeComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    success_url = reverse_lazy("home")
    # подключить редис
    redis_cache = Profile.objects.all()

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.profile = self.redis_cache.get(user=self.request.user)
        comment.hist_object_id = self.kwargs['historical_object_id']
        self.success_url = reverse_lazy(f"historical_object:detail_object",
                                        kwargs={'pk': (self.kwargs['historical_object_id'])})
        comment.save()
        return super().form_valid(form)
