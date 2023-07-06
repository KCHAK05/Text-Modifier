from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    text_new = request.POST.get('word','no text given')
    remove_punc = request.POST.get('removepunc', 'off')
    capitalise = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    purpose = ""

    if (remove_punc=='on'):
        punctuations = '''":;{}[]()*&^%$'#@!/.,?+~<>'''
        analysed_text = ""
        for char in text_new:
            if char not in punctuations:
                analysed_text = analysed_text + char
        if (purpose==""):
            purpose = purpose + 'remove punctuations'
        else:
            purpose = purpose + ', remove punctuations'
        params = {'purpose': purpose, 'analysed_text': analysed_text}
        text_new = analysed_text

    if (capitalise=='on'):
        analysed_text = ""
        for char in text_new:
            analysed_text = analysed_text + char.upper()
        if (purpose==""):
            purpose = purpose + 'capitalise the text'
        else:
            purpose = purpose + ', capitalise the text'
        params = {'purpose': purpose, 'analysed_text': analysed_text}
        text_new = analysed_text

    if (newlineremove == 'on'):
        analysed_text = ""
        for char in text_new:
            if (char!='\n' and char!='\r'):
                analysed_text = analysed_text + char
        if (purpose==""):
            purpose = purpose + 'remove new lines from the text'
        else:
            purpose = purpose + ', remove new lines from the text'
        params = {'purpose': purpose, 'analysed_text': analysed_text}
        text_new = analysed_text

    if (spaceremover=='on'):
        analysed_text = ""
        for char in text_new:
            if (char != ' '):
                analysed_text = analysed_text + char
        if (purpose== ""):
            purpose = purpose + 'remove whitespaces'
        else:
            purpose = purpose + ', remove whitespaces'
        params = {'purpose': purpose, 'analysed_text': analysed_text}
        text_new = analysed_text

    if (charcount == 'on'):
        punctuations = '''":;{}[]()*&^%$'#@!/.,?+~<> '''
        analysed_text = "The number of characters in the string are : "
        number = 0
        for char in text_new:
            if (char not in punctuations):
                number = number + 1
        analysed_text = str(number)
        if (purpose == ""):
            purpose = purpose + 'count the characters'
        else:
            purpose = purpose + ', count the characters'
        params = {'purpose': purpose, 'analysed_text': "The number of characters are "+analysed_text}
        text_new = analysed_text

    if (charcount!='on' and remove_punc!='on' and spaceremover!='on' and capitalise!='on' and newlineremove!='on'):
        return render(request,'error_handle.html')

    return render(request, 'analyse.html', params)


