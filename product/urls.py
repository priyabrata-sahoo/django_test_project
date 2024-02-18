from django.urls import path
from . import views


urlpatterns = [
    # path("register/", UserRegistrationView.as_view(), name="user-registration"),
   path('product/',views.ProductApi.as_view(),name='product')
]
