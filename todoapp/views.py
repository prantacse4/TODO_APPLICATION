from django.shortcuts import render,HttpResponseRedirect
from .forms import NoteRegistration
from .forms import NoteRegistrationArchive
from .models import Notes
from django.db.models import Count



# Create your views here.

def home(request):
    if request.method == 'POST':
        myform = NoteRegistration(request.POST)
        if myform.is_valid():
            myform.save(commit=True)
            myform = NoteRegistration()
            return HttpResponseRedirect('/')
    else:
        myform = NoteRegistration()
    notesdata = Notes.objects.all()
    count = Notes.objects.all().count()
    all_work_count = Notes.objects.filter(archive=0).count()
    diction = {'form':myform, 'notesdata':notesdata,  'count':count, 'all_work_count':all_work_count}
    return render(request, 'todoapp/index.html', context=diction)


#Delete
def delete(request,id):
    if request.method == 'POST':
        del_id = Notes.objects.get(pk=id)
        del_id.delete()
        return HttpResponseRedirect('/')


#UpdateArchive

def archive(request, id):
    diction={}
    if request.method=='POST':
        u_id = Notes.objects.get(pk=id)
        myform = NoteRegistrationArchive(request.POST, instance=u_id)
        if myform.is_valid():
            myform.save(commit=True)
            return HttpResponseRedirect('/')
        else:
         return render(request, 'todoapp/index.html', context=diction)

    else:
         return render(request, 'todoapp/index.html', context=diction)


def add_note(request):
    if request.method == 'POST':
        myform = NoteRegistration(request.POST)
        if myform.is_valid():
            myform.save(commit=True)
            myform = NoteRegistration()
            success_msg = "আপনার নোট ডাটাবেজ এ যুক্ত হয়েছে।"
            diction = {'form':myform, 'success_msg':success_msg}
            return render(request, 'todoapp/add_note.html', context=diction)

            # return HttpResponseRedirect('/')
    else:
        myform = NoteRegistration()
    # notesdata = Notes.objects.all()
    # count = Notes.objects.all().count()
    # all_work_count = Notes.objects.filter(archive=0).count()
    diction = {'form':myform}
    return render(request, 'todoapp/add_note.html', context=diction)