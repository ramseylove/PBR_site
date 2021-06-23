from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True, label='Email Address')
    # subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': "4"}))

    class Meta:
        fields = ('from_email', 'name', 'message',)
