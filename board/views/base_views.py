from django.contrib import messages
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