from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Blog.models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Blog.forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Count, F
from datetime import datetime
import uuid
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string

# def print_friendly_blog(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)
#     context = {'blog': blog}
#     html_content = render_to_string('App_Blog/print_friendly_blog.html', context)

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename="{blog.slug}.pdf"'

#     pdfkit.from_string(html_content, False, options={'encoding': 'UTF-8'}, output_path=response)

#     return response


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

# class BlogList(ListView):
#     context_object_name = 'blogs'
#     model = Blog
#     template_name = 'App_Blog/blog_list.html'
def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)  # Display 5 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    recent_posts = Blog.objects.order_by('-publish_date')[:5]

    return render(request, 'App_Blog/blog_list.html', {'page_obj': page_obj,'recent_posts':recent_posts})



@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog, user= request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':slug}))
    return render(request, 'App_Blog/blog_details.html', context={'blog':blog, 'comment_form':comment_form, 'liked':liked,})

@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user
    if not already_liked:
        liked_post = Likes(blog=blog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':blog.slug}))

@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':blog.slug}))

class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'App_Blog/my_blogs.html'


class UpdateBlog(LoginRequiredMixin,UpdateView):
    model=Blog
    fields=('blog_title','blog_content','blog_image')
    template_name='App_Blog/edit_blog.html'

    def get_success_url(self,**kwargs):
        return reverse_lazy('App_Blog:blog_details',kwargs={'slug':self.object.slug})




def search_blog(request):
    query = request.GET.get('q')

    if query:
        blogs = Blog.objects.filter(blog_title__icontains=query)
    else:
        blogs = Blog.objects.all()

    return render(request, 'App_Blog/blog_list.html', {'blogs': blogs})


def listish(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)  # Display 5 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'App_Blog/blog_list.html', {'page_obj': page_obj})

