from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Entry, Comment
from .forms import EntryForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_entry_list'

    def get_queryset(self):
        """Return the last five published blog entries."""
        return Entry.objects.order_by('-score')[:5]

def entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    form = EntryForm()
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'upvote':
            entry.score += 1
            entry.save()
        elif action == 'downvote':
            entry.score -= 1
            entry.save()
        else:
            form = EntryForm(request.POST)
            if form.is_valid():
                i_commenter = form.cleaned_data['commenter']
                i_comment_text = form.cleaned_data['comment']
                entry.save()
                entry.comment_set.create(pub_time=timezone.now(), commenter=i_commenter, comment_text=i_comment_text)
        return HttpResponseRedirect(reverse('blog:entry', args=(entry.id,)))
    return render(request, 'blog/entry.html', {'entry' : entry, 'form' : form})
