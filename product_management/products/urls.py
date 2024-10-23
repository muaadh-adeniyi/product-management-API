from django.urls import path
from . import views


from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_handler, name='product_handler'),  # Handle all operations at the same path
]





