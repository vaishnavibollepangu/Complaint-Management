from django import forms

from complaint_managementapp.models import Contact,Customer,Administration,AddCatagory,Solvers,Update_Status,Send_Query,Replay
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
class AdministrationForm(forms.ModelForm):
    class Meta:
        model = Administration
        fields = "__all__"
class AddCatagoryForm(forms.ModelForm):
    class Meta:
        model = AddCatagory
        fields = ["title","descreption","catagory","priority"]
class SolversForm(forms.ModelForm):
    class Meta:
        model = Solvers
        fields = "__all__"
class Update_StatusForm(forms.ModelForm):
    class Meta:
        model = Update_Status
        fields = "__all__"
class Send_QueryForm(forms.ModelForm):
    class Meta:
        model = Send_Query
        fields = "__all__"

class ReplayForm(forms.ModelForm):
    class Meta:
        model = Replay
        fields = "__all__"
