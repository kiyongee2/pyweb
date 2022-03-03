from django.urls import path
from . import views

app_name = 'board'  #네임 스페이스(소속) - url경로 이름

urlpatterns = [
    # 질문 목록
    path('', views.index, name='index'),  #127.0.0.1:8000/board/
    # 상세 페이지
    path('<int:question_id>/', views.detail, name='detail'), #127.0.0.1:8000/board/1/
    # 질문 등록 - 127.0.0.1:8000/board/question/create/
    path('question/create/', views.question_create, name='question_create'),
    # 답변 등록 - 127.0.0.1:8000/board/answer/create/1/
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]