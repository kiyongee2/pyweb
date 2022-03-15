from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm

@login_required(login_url='common:login_view')
def question_create(request):
    #질문 등록
    if request.method == "POST":
        form = QuestionForm(request.POST)  # 내용이 작성된 폼
        if form.is_valid():
            question = form.save(commit=False)  #가저장
            question.create_date = timezone.now()  #작성일
            question.author = request.user  #인증된 사용자(글쓴이)
            question.save()  #실제 저장(db에 저장)
            return redirect('board:boardlist')  # 질문 목록 페이지 강제 이동
    else: #request.method == "GET":
        form = QuestionForm()  #질문 등록 폼 객체 변수 생성(비어있는 폼)
    context = {'form':form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login_view')
def question_modify(request, question_id):
    # 질문 수정
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)  #새로 작성한 폼
        if form.is_valid():
            question = form.save(commit=False)     #가저장
            question.modify_date = timezone.now()  # 수정일
            question.author = request.user         # 글쓴이
            question.save()                        # db에 저장
            return redirect('board:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)    #이미 작성된 폼
    context = {'form':form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login_view')
def question_delete(request, question_id):
    #질문 삭제
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    question.delete()     #해당 질문 삭제
    return redirect('board:boardlist')  # 질문 목록