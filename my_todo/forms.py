from django import  forms

from my_todo.models import Todo


class TodoForm(forms.ModelForm):
    check = forms.BooleanField(widget=forms.CheckboxInput)
    title = forms.CharField(min_length=2)
    time = forms.IntegerField(widget=forms.NumberInput, min_value=5)
    class Meta:
        model = Todo
        fields = '__all__'
