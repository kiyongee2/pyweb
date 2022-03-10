from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from board.models import Question, Answer
from board.forms import QuestionForm, AnswerForm

def index(request):
    #인덱스 페이지
    question_list = Question.objects.order_by('-pk')[:3]
    context = {'question_list':question_list}
    return render(request, 'board/index.html', context)

def boardlist(request):
    #질문 목록
    question_list = Question.objects.order_by('-create_date')  #'-'내림 차순, -pk도 가능
    # question_list = Question.objects.all()  #db에서 전체 검색

    # 페이징 처리
    page = request.GET.get('page', '1')  #페이지
    paginator = Paginator(question_list, 10)  #페이지당 10개 자료
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj}
    return render(request, 'board/question_list.html', context)
    # return HttpResponse("<h2>Hello~ Django!!</h2>")

def detail(request, question_id):
    #상세 페이지
    question = get_object_or_404(Question, pk=question_id)  #url경로 오류 처리
    #question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request, 'board/detail.html', context)

@login_required(login_url='common:login')
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

@login_required(login_url='common:login')
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

@login_required(login_url='common:login')
def question_modify(request, question_id):
    # 질문 수정
    question = Question.objects.get(id=question_id)
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

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    #답변 수정
    answer = Answer.objects.get(id=answer_id)
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

@login_required(login_url='common:login')
def question_delete(request, question_id):
    #질문 삭제
    question = Question.objects.get(id=question_id)
    question.delete()     #해당 질문 삭제
    return redirect('board:boardlist')  # 질문 목록

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    # 답변 삭제
    answer = Answer.objects.get(id=answer_id)
    answer.delete()
    return redirect('board:detail', question_id=answer.question.id)  # 상세페이지