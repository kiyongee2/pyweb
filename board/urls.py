from django.urls import path
from . import views

app_name = 'board'  #네임 스페이스(소속) - url경로 이름

urlpatterns = [
    # 인덱스 페이지
    path('', views.index, name='index'),  #127.0.0.1:8000/board/
    # 질문 목록
    path('boardlist/', views.boardlist, name='boardlist'),  #127.0.0.1:8000/board/
    # 상세 페이지
    path('<int:question_id>/', views.detail, name='detail'), #127.0.0.1:8000/board/1/
    # 질문 등록 - 127.0.0.1:8000/board/question/create/
    path('question/create/', views.question_create, name='question_create'),
    # 답변 등록 - 127.0.0.1:8000/board/answer/create/1/
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # 질문 수정
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # 답변 수정
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    # 질문 삭제
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # 답변 삭제
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]