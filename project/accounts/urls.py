from django.urls import path
from .views import *

urlpatterns = [
    path("login/",login_page,name="login"),
    path("register/",register_page,name="register"),
    path("activate/<email_token>/",activate_email_account , name="activate_email"),
    path("password_reset/",password_reset,name="password_reset"),
    # path("order_history/",order_history,name="order_history"),
    # path("product_reviews/",product_reviews,name="product_reviews"),
    # path("contact/",contact,name="contact"),
    # path("about/",about,name="about"),
    # path("privacy_policy/",privacy_policy,name="privacy_policy"),
    # path("terms_and_conditions/",terms_and_conditions,name="terms_and_conditions"),
    # path("shipping_address/",shipping_address,name="shipping_address"),
    # path("product_search/",product_search,name="product_search"),
    # path("cart/",cart,name="cart"),
]