from django.shortcuts import render

# Create your views here.

def index(request):
    content = request.POST.get('content')
    if content:
        if '사랑해' in content:
            content = "나도 사랑해 ㅎㅎ"
    else:
        content = "아무것도 안쓰네 ㅋ"
    context = {
        'content': content
    }
    return render(request, 'myapp/index.html', context)