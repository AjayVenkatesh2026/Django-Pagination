from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import StudentRecord
from .forms import StudentRecordForm

# Create your views here.


def index(request):
    records = StudentRecord.objects.order_by("-id")
    paginator = Paginator(records, 50)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main_app/index.html', {"page_obj": page_obj})


def student(request, id):
    student_record = get_object_or_404(StudentRecord, pk=id)
    return render(request, 'main_app/student.html', {"student": student_record})


def edit(request, id):
    student_record = get_object_or_404(StudentRecord, pk=id)
    if(request.method == "POST"):
        form = StudentRecordForm(request.POST, instance=student_record)
        if(form.is_valid()):
            form.save()
            return redirect("index")
    form = StudentRecordForm(instance=student_record)
    return render(request, 'main_app/edit.html', {"form": form})

def create(request):
    if(request.method == "POST"):
        form = StudentRecordForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("index")
    else:
        form = StudentRecordForm()
        return render(request, 'main_app/create.html', {'form': form})

def delete(request, id):
    student_record = StudentRecord.objects.get(pk=id)
    student_record.delete()
    return redirect("index")
