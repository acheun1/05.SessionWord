from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request): 
    if 'word_list' not in request.session:
        request.session['word_list'] =[]
    context= {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'app_01/index.html',context)

def add_word(request):
    if request.method != 'POST':
        return redirect('/')

    word = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'big_font': request.POST['big_font']
    }
    request.session['word_list'].append(word)
    request.session.modified=True
    return redirect ('/')

def reset(request):
    pass
    # del request.session['cnt']
    # return redirect('/')
