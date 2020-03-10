from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# import the logging library
import logging

from simplemooc.core import SomeUtils

# Get an instance of a logger
logger = logging.getLogger(__name__)
logger.addHandler(SomeUtils.null_handler)


def send_mail_template(subject, template_name, context, recipient_list,
    from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=False):
       	logger.info("Enviando email")
        message_html = render_to_string(template_name, context)
        message_txt = striptags(message_html)   
        email = EmailMultiAlternatives(
            subject=subject, body=message_txt, from_email=from_email, 
            to=recipient_list
    )
        email.attach_alternative(message_html, "text/html")
        email.send(fail_silently=fail_silently)
        logger.info("Email enviado com sucesso") 