from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("signout", views.signout, name="signout"),
    path("courses/all", views.courses, name="courses"),
    path("course/view/<int:id>", views.course, name="course"),
    path("courses/search", views.search, name="search"),
    path("courses/<str:param>", views.filter, name="filter"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("course/new", views.new_course, name="new_course"),
    path("course/view/<int:id>/enrolled", views.enrolled_course, name="enrolled_course"),
    path("course/view/<int:id>/chapters", views.chapters, name="chapters"),
]
