from django.urls import path

from polls import views

app_name = "polls"
urlpatterns = [
    path("", views.get_index, name="index"),
    path("<int:question_id>/", views.get_detail, name="detail"),
    path("<int:question_id>/results/", views.get_results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
