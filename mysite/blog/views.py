from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
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



#################################################
#################################################


#publish blog post 
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)



#add comment
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    #if form is filled in
    if request.method == 'POST':
        form = CommentForm(request.POST)
        #if all fields are valid 
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})




#approve comments 
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)




#DELETE COMMENT
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)