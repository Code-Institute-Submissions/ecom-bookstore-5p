from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from postoffice.forms import NewsletterForm, NotifySignUpForm
from django.core.mail import EmailMessage
from postoffice.models import Newsletter, BookNotify
from django.contrib.auth.models import Group
from django.contrib import messages
from books.models import Book
import os

class write_newsletter(View):
    def get(self, request):
        if Group.objects.filter(user=request.user, name='newsletter_writer').exists():
            form = NewsletterForm()
            return render(
                request,
                'postoffice/newsletter.html',
                {
                    'form': form
                }
            )
        messages.error(request, 'You dont have permission to be here!')
        return redirect('index_bookstore')

    def post(self, request):
        if Group.objects.filter(user=request.user, name='newsletter_writer').exists():
            print("huruhr")
            form = NewsletterForm(request.POST)
            if form.is_valid():

                emails = Newsletter.objects.all()

                email = EmailMessage(
                    subject=form.cleaned_data['subject'],
                    body=form.cleaned_data['body'],
                    from_email=os.environ.get('EMAIL_HOST_USER'),
                    bcc=[e.email for e in emails]
                )

                email.send()

        messages.error(request, 'You dont have permission to be here!')
        return redirect('index_bookstore')

class signup_newsletter(View):
    def get(self, request):
        form = NotifySignUpForm()

        return render(
            request,
            'postoffice/newsletter_signup.html',
            {
                'form': form
            }
        )
        pass

    def post(self, request):
        form = NotifySignUpForm(request.POST)
        if form.is_valid():
            if Newsletter.objects.filter(email=form.cleaned_data['email']).exists():
                messages.warning(request, 'This email is already signed up for the newsletter!')
                return redirect('signup_newsletter')
            new = Newsletter()
            new.email = form.cleaned_data['email']
            new.save()
            messages.success(request, 'Thank you for signing up for the newsletter!')
        else:
            messages.error(request, 'Something went wrong with the form!')
        return redirect('signup_newsletter')
