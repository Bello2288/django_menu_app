from django.urls import path, include

urlpatterns = [
    path('', include('menuitems.urls')),
    # path('orders/', include('orders.urls')),
]
