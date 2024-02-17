from django.shortcuts import render
from store.models import Product
import locale
def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {"products": products}
    return render(request, "home.html", context)



# En algún lugar de tu vista antes de pasar el contexto al template

