from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("about/",views.about,name="about"),
    path("category/<slug:value>",views.category.as_view(),name="category"),
    path("add_to_cart/",views.add_to_cart,name="add_to_cart"),
    path("cart/",views.cart,name="showcart")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)