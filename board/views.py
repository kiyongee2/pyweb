from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm

def index(request):
    #질문 목록
    question_list = Question.objects.order_by('-create_date')  #'-'내림 차순, -pk도 가능
    # question_list = Question.objects.all()  #db에서 전체 검색
    return render(request, 'board/question_list.html',
                  {'question_list':question_list})
    # return HttpResponse("<h2>Hello~ Django!!</h2>")

def detail(request, question_id):
    #상세 페이지
    question = get_object_or_404(Question, pk=question_id)  #url경로 오류 처리
    #question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request, 'board/detail.html', context)

def question_create(request):
    #질문 등록
    if request.method == "POST":
        form = QuestionForm(request.POST)  # 내용이 작성된 폼
        if form.is_valid():
            question = form.save(commit=False)  #가저장
            question.create_date = timezone.now()
            question.save()  #실제 저장
            return redirect('board:index')  # 질문 목록 페이지 강제 이동
    else: #request.method == "GET":
        form = QuestionForm()  #질문 등록 폼 객체 변수 생성(비어있는 폼)
    context = {'form':form}
    return render(request, 'board/question_form.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)  # 해당 질문 1개 가져옴
    if request.method == "POST":
        form = AnswerForm(request.POST)  #데이터가 채워진 폼
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question_id)
    else:
        form = AnswerForm()   # 비어있는 폼
    context = {'form':form}
    return render(request, 'board/detail.html', context)
