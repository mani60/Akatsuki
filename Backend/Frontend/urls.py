from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("about/",views.about,name="about"),
    path("category/<slug:value>",views.category.as_view(),name="category"),
    path("productDetail/<int:pk>",views.productDetail.as_view(),name="product-detail"),
    path("add_to_cart/",views.add_to_cart,name="add_to_cart"),
    path("cart/",views.cart,name="showcart"),
    path("IncCart/",views.IncCart),
    path("DecCart/",views.DecCart),
    path("RemoveItem/",views.RemoveItem),
    path("add_to_Order/",views.add_to_Order,name="add_to_Order"),
    path("Orders/",views.Orders,name="Orders"),
    path("search/",views.search,name="search"),
    path("Incwish/",views.Incwish),
    path("Decwish/",views.Decwish),
    path("wishList/",views.wishList,name="wishList")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)