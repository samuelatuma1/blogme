from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

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
                                            'posts': posts})

class PostListView(ListView):
    
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                                slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
                        
    comments = post.comments.all().filter(active=True)
    new_comment = None

    if request.method == 'POST':
        #Get comment
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #Commit,but dont save
            new_comment = comment_form.save(commit=False)

            #Assign the current post to the comment
            new_comment.post = post
            comment_form.save()
        
    else:
        comment_form = CommentForm()
            
    return render(request, 'blog/post/detail.html', {'post': post,
                                                'comments': comments,
                                                'comment_form': comment_form,
                                                'new_comment': new_comment})

#Shares post via mail
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent=False
    if request.method == 'POST':
        
        # Get form details
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            #Create form messages
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} recommends you read {post.title}'
            message = f"Read {post.title} at {post_url} \n {cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, 'atumasaake@gmail.com', [cd['to']])
            sent=True

    else:
        #present form
        form = EmailPostForm()
        
    return render(request, 'blog/post/share.html', {'post':post,
                                                'sent': sent,
                                                'form': form
                                                    })
