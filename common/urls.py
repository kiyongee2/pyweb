from django.urls import path
from django.contrib.auth import views

app_name = 'common'

urlpatterns = [
    # LoginView 클래스 - 제네릭 뷰
    path('login/', views.LoginView.as_view(template_name='common/login.html'),
         name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]