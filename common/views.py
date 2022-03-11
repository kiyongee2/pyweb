from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from common.forms import UserForm

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)  # db와 비교 인증 처리
        if user is not None:  # 일치한다면
            login(request, user)  # 접속이 됨(로그인 성공)
            return redirect('board:index')
        else:
            error = "아이디나 비밀번호가 일치하지 않습니다."
            return render(request, 'common/login.html', {'error':error})
    else:
        return render(request, 'common/login.html')

def logout_view(request):
    #로그 아웃 - 함수형 view(FBV)
    logout(request)
    return redirect('board:index')  #로그아웃 후 인덱스 페이지로 이동

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)  # 입력된 데이터와 폼 가져오기
        if form.is_valid():  # 유효성 검사를 통과하면
            form.save()      # db에 저장
            return redirect('board:index')
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'common/signup.html', context)
