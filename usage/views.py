from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import UseCase
from ConvertToText import pdfConvertor, docConvertor
from django.conf import settings
from os import path
# Create your views here.
def index(request):
	return render(request, 'usage/index.html')

def usage(request):
	return render(request, "usage/usage.html")

def installation(request):
	return render(request, "usage/installation.html")

def contact(request):
	return render(request,"usage/contact.html")

class convert(CreateView):
	model = UseCase
	fields = ['file_to_convert']


def convertor(request, file_id):
	file = str(UseCase.objects.get(pk=file_id))
	file = settings.BASE_DIR+file
	ConvertedText = ""
	if file[-4:] == ".pdf":
		ConvertedText = pdfConvertor.extract_text(file)
	elif file[-4:] == ".doc":
		ConvertedText = docConvertor.extract_text(file)
	else:
		ConvertedText = "Cannot Convert or unknown file type."
	context = {
		'file' : path.basename(file),
		'text' : ConvertedText,
	}
	return render(request, "usage/convertedView.html", context)
