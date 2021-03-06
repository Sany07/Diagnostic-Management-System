from django.shortcuts import render , redirect
from departments.models import Doctor,Department
from services.models import Test
from .models import Appointment,Contact

# Create your views here.
def contact(request):

    if request.method=='POST':
        u_name= request.POST['name']
        phone_no= request.POST['phone']
        message= request.POST['message']
        department= request.POST['info_form_dep']
        doctor= request.POST['info_form_doc']
        
        appointment = Appointment(name=u_name, phone_no=phone_no, message=message, department=department, doctor=doctor )
        appointment.save()


        return redirect('contact')

    departments=Department.objects.all()
    doctor=Doctor.objects.all()
    context={

        'departments':departments,
        'doctors':doctor
    }

    return render(request ,'contact.html',context) 

