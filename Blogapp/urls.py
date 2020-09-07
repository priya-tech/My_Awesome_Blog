from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryViewList,LikeView,AddCommentView


urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_categories/', AddCategoryView.as_view(), name='add_category'),
    path('article_edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article_remove/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category_list', CategoryViewList, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
