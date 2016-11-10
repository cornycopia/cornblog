from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Entry, Comment

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_entry_list'

    def get_queryset(self):
        """Return the last five published blog entries."""
        return Entry.objects.order_by('-pub_date')[:5]
"""
    def upvote(self, request, entry_id):
        entry = get_object_or_404(Entry, pk=entry_id)
        entry.score = entry.score + 1
        entry.save()
        return HttpResponseRedirect(reverse('blog:entry', args=(entry.id,)))
"""

def entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/entry.html', {'entry' : entry})

def post_comment(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    try:
        i_commenter = request.POST['commenter']
        i_comment_text = request.POST['comment_text']
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'blog/post_comment.html', {
            'entry' : entry,
            'error_message': "There is an error during the comment creation",
        })
    else:
        entry.save()
        entry.comment_set.create(pub_time=timezone.now(), commenter=i_commenter, comment_text=i_comment_text)
        return HttpResponseRedirect(reverse('blog:entry', args=(entry.id,)))

