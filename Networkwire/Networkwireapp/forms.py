from django import forms
from .models import InventoryData


class GetData(forms.Form):
    # updateText = forms.TextInput()
    devices = list(InventoryData.objects.values_list('Hostname',flat=True))
    CHOICES =[(item.strip(),item.strip()) for item in devices]
    # print(CHOICES)
    Device = forms.ChoiceField(widget=forms.Select(), choices=CHOICES,required=False)
    Task =forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea', 'rows': 2, 'cols': 25}),required=False)
    Output = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea', 'rows': 25, 'cols': 100}),required=False)