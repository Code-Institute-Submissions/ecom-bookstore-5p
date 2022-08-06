from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from postoffice.forms import NewsletterForm, NotifySignUpForm
from django.core.mail import EmailMessage
from postoffice.models import Newsletter, BookNotify
from django.contrib.auth.models import Group
from django.contrib import messages
from books.models import Book
from django.contrib.sites.models import Site
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
            form = NewsletterForm(request.POST)
            if form.is_valid():
                emails = Newsletter.objects.all()
                current_site = Site.objects.get_current()

                # TODO: By making it cancel via id anyone could just type in numbers and cancel random peoples newsletters, get around this by sending a confirmation email?
                for e in emails:
                    email = EmailMessage(
                        subject=form.cleaned_data['subject'],
                        body=form.cleaned_data['body']+f'\n{current_site.domain}/cancel_newsletter/{e.id}',
                        from_email=os.environ.get('EMAIL_HOST_USER'),
                        bcc=[e.email]
                    )
                    email.send()

                return redirect('index_bookstore')
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


class cancel_newsletter(View):
    def get(self, request, id):
        if Newsletter.objects.filter(id=id).exists():
            email = Newsletter.objects.get(id=id)
            email.delete()
            email = EmailMessage(
                subject='Newsletter Cancellation',
                body='Sorry to see you go! As requested you have been removed from the sites newsletter list.',
                from_email=os.environ.get('EMAIL_HOST_USER'),
                bcc=[email.email]
            )
            email.send()
            messages.success(request, 'You have been removed from the newsletter list.')
        return redirect('index_bookstore')
