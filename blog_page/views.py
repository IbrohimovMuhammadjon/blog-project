from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm 

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'object_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html' 
    context_object_name = 'post'

class BlogPageView(CreateView):
    model = Post
    form_class = PostForm  
    template_name = 'post_new.html'

class BlogUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('home')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')