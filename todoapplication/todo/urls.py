from django.urls import path
from todo import views


urlpatterns = [
    path('todos',views.TodoMixinList.as_view()),
    path('todos/<int:id>',views.TodoDetailsMixin.as_view()),
    path('todos/accounts/signup',views.UserCreationView.as_view())
]