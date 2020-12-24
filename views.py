from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


def post_list(request):
    
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) #3 posts in each page

    #Get the current page number
    page = request.GET.get('page')

    # Get the content of the page (posts)
    try:
         posts = paginator.page(page)
    
    #if page is not an integer, return first page
    except PageNotAnInteger:
        posts = paginator.page(1)
    
    #if page number is above the last page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
   

    #pass the page number and retrieved objects to the template.
    return render(request, 'blog/post/list.html', {
                                            'page': page,
                                            'posts': posts})

class PostListView(ListView):
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'
    queryset = Post.published.all()
    paginate_by = 3
    


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                                slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    
    return render(request, 'blog/post/detail.html', {'post': post})
