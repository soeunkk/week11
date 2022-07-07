from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:  # 비밀번호와 비밀번호 확인이 일치하는가
            try:    # 이미 존재하는 username인가
                user = User.objects.get(username=request.POST['userId'])
                return render(request, 'accounts/signup.html', {'error': '이미 존재하는 아이디입니다.'})
            except User.DoesNotExist:   # 존재하지 않은 유저라면 회원가입 진행
                user = User.objects.create_user(
                    username=request.POST['userId'], password=request.POST['password1']
                )
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'accounts/signup.html')

def signin(request):
    if request.method == 'POST':
        id = request.POST['userId']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=id, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/signin.html', {'error': '잘못된 아이디 또는 비밀번호입니다.'})
    else:
        return render(request, 'accounts/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
