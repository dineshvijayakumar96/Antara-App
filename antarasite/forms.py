from django import forms
from .models import AntaraEscapesInquiry, Inquiry, AboutusInquiry, ContactusInquiry, ServiceDCInquiry, ServiceDPInquiry, ServiceHHInquiry, ServiceKWInquiry, ServiceNCInquiry, ServiceNDCInquiry, ServiceSCInquiry, ServiceWWInquiry, ServiceYTInquiry
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class InquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'mobile', 'gender', 'country', 'city', 'nationality', 'comment', 'aboutus']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['name'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Name*', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['mobile'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Mobile No*', 'required': 'True'})
        self.fields['gender'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'Select Gender*', 'required': 'True'})
        self.fields['country'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'Select Country*', 'required': 'True'})
        self.fields['city'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'City*', 'required': 'True'})
        self.fields['nationality'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Nationality*', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Your Message', 'rows': 4})
        self.fields['aboutus'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'How did you hear about us? *', 'required': 'True'})

class AboutusInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = AboutusInquiry
        fields = ['name', 'email', 'mobile', 'gender', 'country', 'city', 'nationality', 'comment', 'aboutus']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['name'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Name*', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['mobile'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Mobile No*', 'required': 'True'})
        self.fields['gender'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'Select Gender*', 'required': 'True'})
        self.fields['country'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'Select Country*', 'required': 'True'})
        self.fields['city'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'City*', 'required': 'True'})
        self.fields['nationality'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Nationality*', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Your Message', 'rows': 4})
        self.fields['aboutus'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'How did you hear about us? *', 'required': 'True'})

class ContactusInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ContactusInquiry
        fields = ['name', 'email', 'mobile', 'gender', 'country', 'city', 'nationality', 'comment', 'aboutus']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['name'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Name*', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['mobile'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Mobile No*', 'required': 'True'})
        self.fields['gender'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'Select Gender*', 'required': 'True'})
        self.fields['country'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'Select Country*', 'required': 'True'})
        self.fields['city'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'City*', 'required': 'True'})
        self.fields['nationality'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Nationality*', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Your Message', 'rows': 4})
        self.fields['aboutus'].widget.attrs.update({'class': 'form-select home-enq-input', 'placeholder': 'How did you hear about us? *', 'required': 'True'})

class ServiceDCInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ServiceDCInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class ServiceDPInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ServiceDPInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class ServiceHHInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ServiceHHInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class ServiceKWInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ServiceKWInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class ServiceNCInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ServiceNCInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class ServiceNDCInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ServiceNDCInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class ServiceSCInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ServiceSCInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class ServiceWWInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = ServiceWWInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class ServiceYTInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    
    class Meta:
        model = ServiceYTInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})

class AntaraEscapesInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    
    class Meta:
        model = AntaraEscapesInquiry
        fields = ['firstname', 'lastname', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom attributes, placeholders, or additional styling if needed
        self.fields['firstname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'First Name', 'required': 'True'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Last Name', 'required': 'True'})
        self.fields['email'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Email', 'required': 'True'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control home-enq-input', 'placeholder': 'Add Comment', 'rows': 7})