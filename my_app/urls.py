from django.urls import path 
from .views import BlogListView,IndexListView,BlogDetailView,ContactListView,DoctorsListView,Doctors1ListView
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
	path('product/',DoctorsListView.as_view(),name="product"),
	path('',IndexListView.as_view(),name="index"),
	path('cart/',BlogDetailView.as_view(),name="cart"),
	path('catalog/', BlogListView.as_view(), name='catalog'),
	path('compare/',Doctors1ListView.as_view(),name="compare"),
	path('contact/',ContactListView.as_view(),name="contact"),
	
	


]

