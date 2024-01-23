from django.shortcuts import render, redirect
from .models import InventoryData
from Networkwireapp.ansibleinventory import ansibleinventory
from .forms import GetData
from Networkwireapp.ansibleplaybookupdate import ansibleplaybookupdate

def networkwire(request):
    data = InventoryData.objects.all()
    if request.method == 'POST':
        InventoryData.objects.all().delete()
        databaseload = ansibleinventory()
          # Fetch all data from the database
        return render(request, 'updateinventory.html', {'data': data})
    else:
        return render(request, 'updateinventory.html', {'data': data})

def get_data(request):
    if request.method == 'POST':
        form = GetData(request.POST)
        if form.is_valid():
            command = form.cleaned_data['Task']
            device_selected = form.cleaned_data['Device']
            output=ansibleplaybookupdate(command,device_selected)
    
            # print(output)
            form.fields['Output'].widget.attrs['value'] = '\n'.join(output)
            form = GetData(initial={'Output': output})
        
            return render(request,'Getdata.html',{"form":form})     
    return render(request,'Getdata.html',{"form":GetData})
    


          

