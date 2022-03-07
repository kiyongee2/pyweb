from django.shortcuts import render, redirect

from common.forms import UserForm

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
