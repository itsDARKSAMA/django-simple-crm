from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddNewRecordForm,UpdateRecordForm
from django.contrib import messages
from datetime import datetime
from .models import Record
from django.db.models import Q
import logging
# Create your views here.

#--(a.almajayda) : main index view  
def index(request):
    return render(request,'index.html')


#--(a.almajayda) : new record screen 
@login_required
def dashboard(request):
    
    records = Record.objects.all()

    return render(request,"dashboard.html",{"records":records})




#--(a.almajayda) : add new record view 
@login_required
def new_record(request):

    form = AddNewRecordForm()

    if request.method == "POST":
        form = AddNewRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Record added successfully')
            return redirect('dashboard')
    else:
        form = AddNewRecordForm()
    return render(request,'new_record.html',{'form':form})



@login_required
def view_record(request,id):
    record = get_object_or_404(Record,pk=id)
    return render(request,'view_record.html',{'record':record})

@login_required
def edit_record(request,id):
    record = get_object_or_404(Record,pk=id)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Record updated successfully')
            return redirect('view-record',id=id)

    return render(request,'edit_record.html',{'record':record,'form':form})

@login_required
def delete_record(request,id):
    record = get_object_or_404(Record,pk=id)

    if request.method == 'POST':

        if 'cancel' in request.POST:

            return redirect('edit-record',id=id)

        elif 'delete' in request.POST:

            record.delete()
            messages.success(request,'Record Deleted Success')


            return redirect('dashboard')



    return render(request,'delete_record.html',{'record':record})


logger = logging.getLogger(__name__)

@login_required
def search(request):
    query = request.GET.get('query')

    # if not query:  # Check if query is empty or None

        
    
    results = []

    try:
        if query:
            #--(a.almajayda) we need to fix this with any data structure to fix the performance 
            results = Record.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(mobile__icontains=query))
        else:
            return redirect('dashboard')
    except Exception as e:
        log = logger.error(f'error during search : {e}')
    
    return render(request,'search.html' , {'query':query,'results':results})