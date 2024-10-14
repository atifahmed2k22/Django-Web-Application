from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    capitalize = request.GET.get('capitalize', 'off')

    analyzed = djtext  # Start with the original text
    purpose = []

    # Remove punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''.join(char for char in analyzed if char not in punctuations)
        purpose.append('Removed Punctuations')

    # Change to uppercase
    if fullcaps == "on":
        analyzed = analyzed.upper()
        purpose.append('Changed to Uppercase')

    # Remove new lines
    if newlineremover == "on":
        analyzed = analyzed.replace('\n', '').replace('\r', '')
        purpose.append('Removed New Lines')

    # Capitalize each word
    if capitalize == "on":
        analyzed = analyzed.title()
        purpose.append('Capitalized Each Word')

    # If no operation was selected
    if not purpose:
        return HttpResponse("Please select at least one operation.")

    params = {'purpose': ', '.join(purpose), 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
