from django.urls import path
from . import views, apiviews
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "assignment"

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("student/", views.student_view, name="student"),
    path(
        "student_detail/<int:student_id>/",
        views.student_detail_view,
        name="student_detail",
    ),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("update/<int:student_id>/", views.update_student_data, name="update"),
    path("delete/<int:student__id>/", views.delete_student_data, name="delete"),
    path("add_student/", apiviews.StudentView.as_view(), name="add_Student"),
    path(
        "student_detail/<int:id>/",
        apiviews.StudentDetailView.as_view(),
        name="student_detail",
    ),
    path("register/", apiviews.RegisterView.as_view(), name="Register"),
   
]