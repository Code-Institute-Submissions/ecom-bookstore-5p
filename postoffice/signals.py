from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from books.models import Book
from postoffice.models import Newsletter, BookNotify
from django.core.mail import EmailMessage
import os


@receiver(pre_save, sender=Book)
def email_before_change(sender, instance, **kwargs):
    id = instance.id
    old_value = Book.objects.get(id=id)

    if old_value.stock == 0 and instance.stock > 0:
        emails = BookNotify.objects.filter(book__id=id)

        email = EmailMessage(
            subject=f'{instance.name} Is Now Back In Stock!',
            body=f'{instance.name} is back in stock, you can purchase it here from this link: <a href="https://bookstore-5p.herokuapp.com/books/view/{id}">Buy Me!</a>',
            from_email=os.environ.get('EMAIL_HOST_USER'),
            bcc=[e.email for e in emails]
        )

        email.send()

    elif not old_value.available and instance.available:
        emails = BookNotify.objects.filter(book__id=id)

        email = EmailMessage(
            subject=f'{instance.name} Is Now Available For Purchase!',
            body=f'{instance.name} is ready for you to buy, you can purchase it here from this link: <a href="https://bookstore-5p.herokuapp.com/books/view/{id}">Buy Me!</a>',
            from_email=os.environ.get('EMAIL_HOST_USER'),
            bcc=[e.email for e in emails]
        )

        email.send()