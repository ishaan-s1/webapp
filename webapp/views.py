# I have created this file - Ishaan
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get("removepunc", "off")
    fullcap = request.POST.get("fullcap", "off")
    nlremove = request.POST.get("nlremove", "off")
    spremove = request.POST.get("spremove", "off")

    ss = ''
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        ss += ' | Removed Punctuations | '
        params = {'purpose': ss, 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcap == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        ss += ' | Changed to Uppercase |'
        params = {'purpose': ss, 'analyzed_text': analyzed}
        djtext = analyzed

    if (spremove == "on"):
        analyzed = ""
        ss += ' | Removed Spaces |'
        ll = len(djtext)
        for index, char in enumerate(djtext):
            if index + 1 < ll and not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': ss, 'analyzed_text': analyzed}
        djtext = analyzed

    if (nlremove == "on"):
        analyzed = ""
        ss += ' | Removed NewLines | '
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': ss, 'analyzed_text': analyzed}

    if (removepunc != "on" and nlremove != "on" and spremove != "on" and fullcap != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
