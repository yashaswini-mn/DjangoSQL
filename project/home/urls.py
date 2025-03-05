from django.urls import path
from home.views import *

urlpatterns = [
    path("index/",index,name="index"),
    path("wishlist/",wishlist,name="wishlist"),
    path("order_history/",order_history,name="order_history"),
    path("product_reviews/",product_reviews,name="product_reviews"),
    path("contact/",contact,name="contact"),
    path("about/",about,name="about"),
    path("privacypolicy/",privacypolicy,name="privacy-policy"),
    path("trems_and_conditions/",trems_and_conditions,name="terms-and-conditions"),
    path("shipping_address/",shipping_address,name="shipping-address"),
    path("product_search/",product_search,name="product_search"),
    path("cart/",cart,name="cart"),
]