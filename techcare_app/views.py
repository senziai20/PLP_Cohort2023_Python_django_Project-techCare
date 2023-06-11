from django.shortcuts import render, redirect
from .forms import RepairRequestForm
from .models import RepairRequest

# techcare_app/views.py
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about_us(request):
    return render(request, 'about.html', {})

def create_repair_request(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair_requests')
    else:
        form = RepairRequestForm()

    return render(request, 'create_repair_request.html', {'form': form})


def repair_requests(request):
    repair_requests = RepairRequest.objects.all()
    return render(request, 'repair_requests.html', {'repair_requests': repair_requests})
