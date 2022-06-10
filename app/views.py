from django.shortcuts import render ,redirect
from django.contrib import messages
from app.models import Todo 
from app.forms import TodoForm

# Create your views here.
def index(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            if Todo.objects.filter(item=f.item).exists():
                messages.error(request,"Todo Item Already Exists")
            else:
                f.save()    
            return redirect('/')

    context = {
        "form": form,
        'items': Todo.objects.all(),
        }        
    
    return render(request,'index.html',context)



def updateitem(request,pk):
    todo_item = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo_item)
    if request.method == 'POST':
        form = TodoForm(request.POST or None,instance=todo_item)
        if form.is_valid():
            f = form.save(commit=False)
            todo_item.item = f.item
            todo_item.status = f.status
            form.save()
            return redirect('index')
    context = {
        "form": form,
        }        
    
    return render(request,'update.html',context)     
           
def deleteitem(request,pk):
    item = Todo.objects.get(id=pk).delete()
    return redirect("/")       