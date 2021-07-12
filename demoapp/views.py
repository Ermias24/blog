from django.utils import timezone
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Post
from .forms import PostForm

def save_post(request):
    form = PostForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        product = form.save()
        return HttpResponseRedirect(reverse("demoapp:save_post"))
    context = {'form' : form}
    return render(request, 'add_post.html', context)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


