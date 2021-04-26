#I have created this file - Namkha
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("HOME")
def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == "on":
    #analyzed = djtext
        punctuations = '''[[\]{}.,^$|#s],"$&"'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        print(analyzed)
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="/r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra spaces', 'analyzed_text': analyzed}
        djtext=analyzed
    if(removepunc != "on" and fullcaps !="on" and newlineremover != "on" and extraspaceremover != "on") :
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)




