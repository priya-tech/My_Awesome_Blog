from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
#def home(request):
#    return render(request, 'Blogapp/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'Blogapp/home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request,cats):
    category_list = Post.objects.filter(category=cats.title().replace('-', ' '))
    return render(request, 'Blogapp/category.html', {'cats':cats.title().replace('-', ' '), 'category_list':category_list})

def CategoryViewList(request):
    cats_list = Category.objects.all()
    return render(request, 'Blogapp/category_list.html', {'cats_list':cats_list})

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Blogapp/article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Blogapp/add_post.html'
    #fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'Blogapp/add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'Blogapp/update_post.html'
    fields = ('title','title_tag','content','snippet')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'Blogapp/delete_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'Blogapp/add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
