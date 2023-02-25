from django.shortcuts import render

# Create your views here.

def index(request):
    content = ""
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            if '사랑해' in content:
                content = "나도 사랑해 ㅎㅎ"
            if '보고싶' in content:
                content = "그럼 빨리 와야지ㅋ"
            else:
                content = "듣고 싶은 말이 아님ㅋ"
        else:
            content = "아무것도 안쓰네 ㅋ"

    context = {
        'content': content
    }
    return render(request, 'myapp/index.html', context)