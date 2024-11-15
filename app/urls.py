from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    IndexView,
    RegisterView,
    LoginUserView,
    LogoutView,
    AddToCartView,
    ViewCartView,
    RemoveFromCartView,
    CategoryView,
    ProductDetailView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('view-cart/', ViewCartView.as_view(), name='view_cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),

    path('category/<str:category_name>/', CategoryView.as_view(), name='category_page'), 
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
