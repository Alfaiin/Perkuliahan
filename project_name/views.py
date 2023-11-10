from django.shortcuts import render
def index(request):
    context={
        'Judul':'Kuliah',
        'Kontributor':'Aam',
    }
    return render(request,'index.html',context)