from django.forms import formset_factory
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DataForm
from .models import FormDataModel

def manage_data(request):
    template_name = 'testForm/formPage.html'
    formset_object = formset_factory(DataForm)
    
    if request.method == 'GET':
        formset = formset_object(request.GET or None)
        return render(request, template_name, {'formset': formset})
    
    elif request.method == 'POST':
        formset = formset_object(request.POST or None)
        if formset.is_valid():                  
            FormDataModel.objects.create(data=formset.cleaned_data)
        return redirect('results/')
       
        formset=formset_object();
    return render(request, template_name, {
            'formset': formset,
            'last_form_counter': len(formset),})