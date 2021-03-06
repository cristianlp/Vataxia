from django.conf.urls import url
from .views.login import LoginView
from .views.logout import LogoutView
from .views.profile import ProfileView
from .views.reset_password import ResetPasswordView
from .views.update_password import UpdatePasswordView
from .views.user import UserView, UserDetail


urlpatterns = [

    # Login / logout
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),

    # Password management
    url(r'^reset_password$', ResetPasswordView.as_view()),
    url(r'^update_password$', UpdatePasswordView.as_view()),

    # Profiles
    url(r'^profiles$', ProfileView.as_view()),

    # Users
    url(r'^users$', UserView.as_view()),
    url(r'^users/(?P<user_id>[\d]+)$', UserDetail.as_view()),

]
