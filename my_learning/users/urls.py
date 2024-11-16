from django.urls import path
from django.contrib.auth.views import LoginView
from .views import MyLogoutView, RegisterView, AboutMeView, print_receipt


app_name = "users"


urlpatterns = [
    path("login/", LoginView.as_view(
        redirect_authenticated_user=True,
        template_name="users/login.html"
    )
         , name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    # path("create/", AboutMeView.as_view(), name="create-profile"),
    path("profile/", AboutMeView.as_view(), name="profile"),
    path('print_receipt/', print_receipt, name='print_receipt'),
]
