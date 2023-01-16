from django.shortcuts import render
from blog.models import Post,Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView, DeleteView)

# Create your views here.



class AboutView(TemplateView):
    template_name = 'about.html'



class PostListView(ListView):
    model = Post 

    def get_queryset(self):
        #__lte is less than or equal to. 
        # the -published_date posts them in reverse order / so the most recent one is at the top
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')



#blog post deatils 
class PostDetailView(DetailView):
    model = Post



#create new blog post
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post



#update a blog post 
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post



#delete a blog post
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')




#draft a blog post 
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

