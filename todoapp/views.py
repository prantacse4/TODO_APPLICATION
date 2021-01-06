from django.shortcuts import render, HttpResponseRedirect
from .forms import NoteRegistration
from .forms import NoteRegistrationArchive
from .forms import NoteRegistrationUpdate
from .models import Notes
from django.db.models import Count


#For LoginSignup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from  django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


#loginSignup

def registerpage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    else:

        myform = UserCreationForm()
        
        if request.method == 'POST':
            myform = UserCreationForm(request.POST)
            if myform.is_valid():
                myform.save(commit=True)
                user = myform.cleaned_data.get('username')
                messages.success(request, 'একয়াউন্ট তৈরি হয়েছে '+ user)
                return HttpResponseRedirect('/login')


        diction = {'myform':myform}
        return render(request, 'todoapp/register.html', context=diction)




def loginpage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

            else:
                messages.info(request, 'ইউজারনেম অথবা পাসওয়ার্ড এ কোনো ভুল আছে।')

        diction = {}
        return render(request, 'todoapp/login.html', context=diction)



@login_required(login_url='loginpage')
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/login')


@login_required(login_url='loginpage')
def delete_my_account(request):
    if request.method == 'POST':
        userdata = request.user.id
        del_id = User.objects.get(id=userdata)
        del_id.delete()
        logout(request)
        return HttpResponseRedirect('/')


#Copyright
@login_required(login_url='loginpage')
def copyright(request):
    diction={}
    return render(request, 'todoapp/copyright.html', context=diction)


@login_required(login_url='loginpage')
def home(request):
    if request.method == 'POST':
        myform = NoteRegistration(request.POST)
        if myform.is_valid():
            user = request.user
            title = myform.cleaned_data['title']
            note = myform.cleaned_data['note']
            archive = myform.cleaned_data['archive']
            date = myform.cleaned_data['date']
            reg = Notes(user=user, title=title, note=note, archive=archive,date=date)
            reg.save()
            myform = NoteRegistration()
            return HttpResponseRedirect('/')
    else:
        myform = NoteRegistration()

    userdata = request.user
    if request.user.is_authenticated:
        notesdata = Notes.objects.filter(user=userdata)

    count = Notes.objects.filter(user=userdata).count()
    all_work_count = Notes.objects.filter(archive=0,user=userdata).count()
    diction = {'form':myform, 'notesdata':notesdata,  'count':count, 'all_work_count':all_work_count}
    return render(request, 'todoapp/index.html', context=diction)


#Delete
@login_required(login_url='loginpage')
def delete(request,id):
    if request.method == 'POST':
        del_id = Notes.objects.get(pk=id)
        del_id.delete()
        return HttpResponseRedirect('/')


#UpdateArchive
@login_required(login_url='loginpage')
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


@login_required(login_url='loginpage')
def add_note(request):
    if request.method == 'POST':
        myform = NoteRegistration(request.POST)
        if myform.is_valid():
            user = request.user 
            title = myform.cleaned_data['title']
            note = myform.cleaned_data['note']
            archive = myform.cleaned_data['archive']
            date = myform.cleaned_data['date']
            reg = Notes(user=user, title=title, note=note, archive=archive,date=date)
            reg.save()
            myform = NoteRegistration()
            success_msg = "আপনার নোট ডাটাবেজ এ যুক্ত হয়েছে।"
            diction = {'form':myform, 'success_msg':success_msg}
            return render(request, 'todoapp/add_note.html', context=diction)
    else:
        myform = NoteRegistration()
    diction = {'form':myform}
    return render(request, 'todoapp/add_note.html', context=diction)


#archivepage
@login_required(login_url='loginpage')
def archivepage(request):
    userdata = request.user
    if request.user.is_authenticated:
        notesdata = Notes.objects.filter(user=userdata)

    all_work_count = Notes.objects.filter(archive=1,user=userdata).count()
    diction = {'notesdata':notesdata, 'all_work_count':all_work_count}
    return render(request, 'todoapp/archive.html', context=diction)


#unarchive
@login_required(login_url='loginpage')
def unarchive(request, id):
    diction={}
    if request.method=='POST':
        u_id = Notes.objects.get(pk=id)
        myform = NoteRegistrationArchive(request.POST, instance=u_id)
        if myform.is_valid():
            myform.save(commit=True)
            return HttpResponseRedirect('/archive')
        else:
         return render(request, 'todoapp/archive.html', context=diction)

    else:
         return render(request, 'todoapp/archive.html', context=diction)

#delete From Archive
@login_required(login_url='loginpage')
def deletefromarchive(request,id):
    if request.method == 'POST':
        del_id = Notes.objects.get(pk=id)
        del_id.delete()
        return HttpResponseRedirect('/archive')



#all  Notes

@login_required(login_url='loginpage')
def all(request):
    userdata = request.user
    if request.user.is_authenticated:
        notesdata = Notes.objects.filter(user=userdata)
    count = Notes.objects.filter(user=userdata).count()
    diction = {'notesdata':notesdata,  'count':count}
    return render(request, 'todoapp/all.html', context=diction)


#Delete
@login_required(login_url='loginpage')
def all_delete(request,id):
    if request.method == 'POST':
        del_id = Notes.objects.get(pk=id)
        del_id.delete()
        return HttpResponseRedirect('/all')




#View Update/Delete
@login_required(login_url='loginpage')
def view_update(request, id):
    userdata = request.user
    notesdata = Notes.objects.get(pk=id, user=userdata)
    diction={'notesdata':notesdata}
    sid = str(id)
    if request.method=='POST':
        u_id = Notes.objects.get(pk=id)
        myform = NoteRegistrationUpdate(request.POST, instance=u_id)
        if myform.is_valid():
            myform.save(commit=True)
            return HttpResponseRedirect('/view/'+sid)

        
    else:
        u_id = Notes.objects.get(pk=id)
        myform = NoteRegistrationUpdate(instance=u_id)
    return render(request, 'todoapp/view.html', context=diction)


