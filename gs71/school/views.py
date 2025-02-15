from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponse
from .forms import ContactForm


#returning a html content from function based View
def myview(request):
    return HttpResponse('<h1>Function based view</h1>') 


#returning a html content from Class based View
class MyView(View):
    name = "rahim"  #if i want to pass var name from url then iw ill write here name = "" else will raise error
    def get(self,request):
        # return HttpResponse('<h1>Class based view</h1>')      
        return HttpResponse(self.name)      #returning a variable 

# making child class of above

class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)
    

# rendering template from function based view
def RenderTemplatesByFuncView(request):
    return render(request,'school/home.html',{"method":"Function_based"})


# rendering template from Class based view
class RenderTemplatesByClassView(View):
    def get(self,request):
        return render(request,'school/home.html',{"method":"class_based"})


# form using function based view
def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you, your form was submitted by function based view method')
    else:
        form = ContactForm()  # Empty form for GET request

    return render(request, 'school/contact.html', {'form': form})


# form using Class based view
class ContactClassView(View):
    def get(self,request):

        form = ContactForm()  # Empty form for GET request
        return render(request, 'school/contact.html', {'form': form})
    def post(self,request):

        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you, your form was submitted by Class based view method.')


# Rendering different templates from one view using Function based view

def DifferentTemplateByOneFuncView(request,templatename):
    template_name = templatename
    context = {"name":"Rahim"}
    return render(request,template_name,context)


class DifferentTemplateByOneClassView(View):
    templatename = ""
    def get(self,request):
        context = {"name":"Rahim"}
        return render(request,self.templatename,context)
