from django import forms


def order_form_fields():
    first_name = _create_input('Thread', 'TextInput')
    last_name = _create_input('Flix', 'TextInput')
    email = _create_input('you@example.com', 'EmailInput')
    address = _create_input('Ukraine, Kyiv, Kovalsky provulok, 5', 'TextInput')
    return first_name, last_name, email, address


def _create_input(placeholder: str, input_type: str, readonly: bool = False):
    attrs = {
        'class': 'form-control',
        'placeholder': placeholder,
        'readonly': readonly
    }
    if input_type == 'TextInput':
        return forms.CharField(widget=forms.TextInput(attrs=attrs))
    elif input_type == 'EmailInput':
        return forms.CharField(widget=forms.EmailInput(attrs=attrs))
