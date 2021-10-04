from django.urls import path
from todo import views


urlpatterns = [
    path('todos',views.TodoDetailsMixin.as_view()),
    path('todos/<int:id>',views.TodoDetailsMixin.as_view())
]