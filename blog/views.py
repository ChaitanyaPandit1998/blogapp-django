from django.shortcuts import render,Http404,get_object_or_404
from .models import Post
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


def index(request):
  object_list=Post.objects.all()
  context={'object_list':object_list}
  return render(request,'blog/home.html',context)

def detail(request,blog_id):
  blog=get_object_or_404(Post,pk=blog_id)
  return render(request,'blog/detail.html',{'blog':blog})


class BlogCreateView(CreateView):
  model=Post
  template_name='blog/add.html'
  fields='__all__'

class BlogUpdateView(UpdateView):
  model=Post
  template_name='blog/edit.html'
  fields=['title','body']

class BlogDeleteView(DeleteView):
  model=Post
  template_name='blog/delete.html'
  success_url=reverse_lazy('blog:index')
  
  
