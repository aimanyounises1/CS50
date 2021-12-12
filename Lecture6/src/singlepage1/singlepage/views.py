from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'singlepage/index.html')

texts = ["This course picks up where Harvard University's CS50 leaves off",
", diving more deeply into the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap. Topics include database design, scalability, security, and user experience.",
" Through hands-on projects, students learn to write and use APIs, create interactive UIs, and leverage cloud services like GitHub and Heroku. ",
"By semester’s end, students emerge with knowledge and experience in principles, languages, and tools that empower them to design and deploy applications on the Internet."
]
def section(request , num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No Such Section")