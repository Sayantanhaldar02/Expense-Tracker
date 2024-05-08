from django.urls import path
from expence_tracker.views import *

urlpatterns = [
    path("", create_expence, name="create_expence"),
    # path("", create_category, name="create_category"),
    # path("", get_all_expence_and_category, name="get_all_expence_and_category"),
    # path("update/<id>/", update_expence, name="update_expence"),
    path("delete/<id>/", delete_expence, name="delete_expence"),
    path("login/", user_login, name="user_login"),
    path("register/", user_register, name="user_register"),
    path("logout/", user_logout, name="user_logout"),
]
