from django.views.generic import ListView,DetailView
from .models import Mebel



class IndexListView(ListView):
    model = Mebel
    template_name = 'index.html'


class BlogDetailView(ListView):
    model = Mebel
    template_name = 'cart.html'

class BlogListView(ListView):
    model = Mebel
    template_name = 'catalog.html'
  

class ContactListView(ListView):
    model = Mebel
    template_name = 'contacts.html'

class DoctorsListView(ListView):
    model = Mebel
    template_name = 'product.html'

class Doctors1ListView(ListView):
    model = Mebel
    template_name = 'compare.html'





