from django.urls import path 

from .views import   makeupsListView ,makeupsDetailsView 

urlpatterns = [
    path('products', makeupsListView.as_view(), name='products'), 
    path('<int:pk>', makeupsDetailsView.as_view(), name='products_details'), 
]
