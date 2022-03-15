from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm

@login_required(login_url='common:login_view')
def answer_create(request, question_id):
    # 답변 등록
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)  # 해당 질문 1개 가져옴
    if request.method == "POST":
        form = AnswerForm(request.POST)  #데이터가 채워진 폼
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user   #인증된 사용자(글쓴이)
            answer.save()
            return redirect('board:detail', question_id=question_id)
            # return render(request, 'board:detail.html', question_id=question_id)
    else:
        form = AnswerForm()   # 비어있는 폼
    context = {'question':question, 'form':form}
    return render(request, 'board/detail.html', context)

@login_required(login_url='common:login_view')
def answer_modify(request, answer_id):
    #답변 수정
    answer = get_object_or_404(Answer, pk=answer_id)
    # answer = Answer.objects.get(id=answer_id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.author = request.user
            answer.save()   #db에 저장
            return redirect('board:detail', question_id = answer.question.id)
    else:
        form = AnswerForm(instance=answer)   # 수정할 답변 폼
    context = {'form':form}
    return render(request, 'board/answer_form.html', context)

@login_required(login_url='common:login_view')
def answer_delete(request, answer_id):
    # 답변 삭제
    answer = get_object_or_404(Answer, pk=answer_id)
    # answer = Answer.objects.get(id=answer_id)
    answer.delete()
    return redirect('board:detail', question_id=answer.question.id)  # 상세페이지

