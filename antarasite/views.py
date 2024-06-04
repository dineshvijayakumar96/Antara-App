from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import AntaraEscapesInquiryForm, InquiryForm, AboutusInquiryForm, ContactusInquiryForm, ServiceDCInquiryForm, ServiceDPInquiryForm, ServiceHHInquiryForm, ServiceKWInquiryForm, ServiceNCInquiryForm, ServiceNDCInquiryForm, ServiceSCInquiryForm, ServiceWWInquiryForm, ServiceYTInquiryForm
from .models import AntaraEscapesInquiry, Inquiry, AboutusInquiry, ContactusInquiry, ServiceDCInquiry, ServiceDPInquiry, ServiceHHInquiry, ServiceKWInquiry, ServiceNCInquiry, ServiceNDCInquiry, ServiceSCInquiry, ServiceWWInquiry, ServiceYTInquiry

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Home Page - Inquiry from ' + form.cleaned_data['name']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'home.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'home.html', {'form': form})

    else:
        form = InquiryForm()
        return render(request, 'home.html', {'form': form})

def aboutus(request):
    if request.method == 'POST':
        form = AboutusInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'About Us - Inquiry from ' + form.cleaned_data['name']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'about-us.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'about-us.html', {'form': form})

    else:
        form = AboutusInquiryForm()
        return render(request, 'about-us.html', {'form': form})

# def servicedc(request):
#     if request.method == 'POST':
#         form = ServiceDCInquiryForm(request.POST)
#         if form.is_valid():
#             # Save form submission to the database
#             inquiry_instance = form.save()

#             # Email Setup
#             subject = 'Service Diabetes Consultation - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
#             from_email = 'antaracares@gmail.com'  # Set your email address here
#             to_email = ['antaracares@gmail.com']  # Set your to email address here

#             # Load the HTML template
#             html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

#             # Create an EmailMultiAlternatives object to send both HTML and plain text emails
#             email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
#             email.attach_alternative(html_message, "text/html")

#             try:
#                 # Send the email
#                 email.send()

#                 # Set a session variable to indicate that the form has been submitted
#                 request.session['form_submitted'] = True

#                 # Redirect to a thank you page or use render if you want to display a thank you message on the same page
#                 return redirect('thankyou')

#             except Exception as e:
#                 # Handle email sending error
#                 return render(request, 'service-dc.html', {'error': str(e), 'form': form})

#         else:
#             # Form is not valid, render the form with validation errors
#             return render(request, 'service-dc.html', {'form': form})

#     else:
#         form = ServiceDCInquiryForm()
#         return render(request, 'service-dc.html', {'form': form})

def servicehh(request):
    if request.method == 'POST':
        form = ServiceHHInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Service Men Health - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'service-hh.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'service-hh.html', {'form': form})

    else:
        form = ServiceHHInquiryForm()
        return render(request, 'service-hh.html', {'form': form})

def serviceww(request):
    if request.method == 'POST':
        form = ServiceWWInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Service Women Wellness - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'service-ww.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'service-ww.html', {'form': form})

    else:
        form = ServiceWWInquiryForm()
        return render(request, 'service-ww.html', {'form': form})

def servicekw(request):
    if request.method == 'POST':
        form = ServiceKWInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Service Weight Management & Obesity - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'service-kw.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'service-kw.html', {'form': form})

    else:
        form = ServiceKWInquiryForm()
        return render(request, 'service-kw.html', {'form': form})

def servicenc(request):
    if request.method == 'POST':
        form = ServiceNCInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Service Naturopathic Consultations - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'service-nc.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'service-nc.html', {'form': form})

    else:
        form = ServiceNCInquiryForm()
        return render(request, 'service-nc.html', {'form': form})

def servicendc(request):
    if request.method == 'POST':
        form = ServiceNDCInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Service Nutrition and Diet Consultations - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'service-ndc.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'service-ndc.html', {'form': form})

    else:
        form = ServiceNDCInquiryForm()
        return render(request, 'service-ndc.html', {'form': form})

def servicesc(request):
    if request.method == 'POST':
        form = ServiceSCInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Service Senior Care - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'service-sc.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'service-sc.html', {'form': form})

    else:
        form = ServiceSCInquiryForm()
        return render(request, 'service-sc.html', {'form': form})

def serviceyt(request):
    if request.method == 'POST':
        form = ServiceYTInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Service Yoga Sessions - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'service-yt.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'service-yt.html', {'form': form})

    else:
        form = ServiceYTInquiryForm()
        return render(request, 'service-yt.html', {'form': form})

def servicedp(request):
    if request.method == 'POST':
        form = ServiceDPInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Service Detoxification Programs - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'service-dp.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'service-dp.html', {'form': form})

    else:
        form = ServiceDPInquiryForm()
        return render(request, 'service-dp.html', {'form': form})
    
# def antaraescapes(request):
#     if request.method == 'POST':
#         form = AntaraEscapesInquiryForm(request.POST)
#         if form.is_valid():
#             # Save form submission to the database
#             inquiry_instance = form.save()

#             # Email Setup
#             subject = 'Service Yoga Sessions - Inquiry from ' + form.cleaned_data['firstname'] + ' ' + form.cleaned_data['lastname']
#             from_email = 'antaracares@gmail.com'  # Set your email address here
#             to_email = ['antaracares@gmail.com']  # Set your to email address here

#             # Load the HTML template
#             html_message = render_to_string('inquiry_email_template_2.html', {'inquiry_instance': inquiry_instance})

#             # Create an EmailMultiAlternatives object to send both HTML and plain text emails
#             email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
#             email.attach_alternative(html_message, "text/html")

#             try:
#                 # Send the email
#                 email.send()

#                 # Set a session variable to indicate that the form has been submitted
#                 request.session['form_submitted'] = True

#                 # Redirect to a thank you page or use render if you want to display a thank you message on the same page
#                 return redirect('thankyou')

#             except Exception as e:
#                 # Handle email sending error
#                 return render(request, 'antara-escapes.html', {'error': str(e), 'form': form})

#         else:
#             # Form is not valid, render the form with validation errors
#             return render(request, 'antara-escapes.html', {'form': form})

#     else:
#         form = AntaraEscapesInquiryForm()
#         return render(request, 'antara-escapes.html', {'form': form})
    
def antaraescapes(request):
    return render(request, 'antara-escapes.html', {})

def yogaclub(request):
    return render(request, 'yoga-club.html', {})

def contactus(request):
    if request.method == 'POST':
        form = ContactusInquiryForm(request.POST)
        if form.is_valid():
            # Save form submission to the database
            inquiry_instance = form.save()

            # Email Setup
            subject = 'Contact Us - Inquiry from ' + form.cleaned_data['name']
            from_email = 'antaracares@gmail.com'  # Set your email address here
            to_email = ['antaracares@gmail.com']  # Set your to email address here

            # Load the HTML template
            html_message = render_to_string('inquiry_email_template.html', {'form': form})

            # Create an EmailMultiAlternatives object to send both HTML and plain text emails
            email = EmailMultiAlternatives(subject, 'This is the plaintext message', from_email, to_email)
            email.attach_alternative(html_message, "text/html")

            try:
                # Send the email
                email.send()

                # Set a session variable to indicate that the form has been submitted
                request.session['form_submitted'] = True

                # Redirect to a thank you page or use render if you want to display a thank you message on the same page
                return redirect('thankyou')

            except Exception as e:
                # Handle email sending error
                return render(request, 'contact-us.html', {'error': str(e), 'form': form})

        else:
            # Form is not valid, render the form with validation errors
            return render(request, 'contact-us.html', {'form': form})

    else:
        form = ContactusInquiryForm()
        return render(request, 'contact-us.html', {'form': form})
    
def thankyou(request):
    # Check if the form has been submitted before allowing access to the thank-you page
    if not request.session.get('form_submitted', False):
        # If not, redirect to another page, for example, the home page
        return redirect('home')

    # Clear the session variable to ensure that the user can't access the thank-you page again
    request.session['form_submitted'] = False

    return render(request, 'thank-you.html', {})