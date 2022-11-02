from django.urls import path,include
from . import views

urlpatterns = [

    path('', views.articles, name= 'allarticles'),
    path('<int:pk>/<slug:slug>/',views.article, name='article_details'),
    path('filter/<slug:slug>', views.tagfilter, name= 'tagfilter'),
    path('createpost/', views.createpost, name='createpost'),
    path('prompts/', views.prompts, name='prompts'),
    path('prompts/<slug:slug>', views.prompt_details, name='prompt_details'),
    path('editpost/<slug:slug>', views.edit_post, name='editpost'),
    path('deletepost/<slug:slug>', views.delete_post, name='deletepost'),
]