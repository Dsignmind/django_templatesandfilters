from django.shortcuts import render

# Create your views here.
def index(request):
    #filter example
    context_dict = {'text': 'practicing django filters!','number':100}
    return render(request, 'basic_app/index.html', context_dict)


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')