from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Item
from django.views.generic import CreateView, DetailView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'cart/home.html')

def DisplayItems(request):
    context = {
    'items' : Item.objects.all()
    }
    return render(request, 'cart/display_items.html', context)

class ItemsAddView(CreateView):
    model = Item
    fields = ['name', 'price']

    success_url = '/cartitems'

class ItemDetailView(DetailView):
    model = Item

class ItemDeleteView(DeleteView):
    model = Item
    success_url = '/cartitems'
