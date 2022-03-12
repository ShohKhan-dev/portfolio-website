from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('about/', views.about, name="about"),
	path('blogs/', views.blogs, name="blogs"),
	path('projects/', views.projects, name="projects"),
    path('resume/', views.resume, name="resume"),
	path('contact/', views.contact, name="contact"),
	path('article/', views.article, name="article"),
	
]

