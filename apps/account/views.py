from django.conf import settings
from django.views.generic import TemplateView, CreateView

from .forms import SubscriberAddForm

from mailchimp3 import MailChimp
import hashlib


class ThanksSignupView(TemplateView):
    template_name = 'account/thanks.html'


class SubscribeAddView(CreateView):
    template_name = 'account/subscription.html'
    success_url = '/thanks/'
    form_class = SubscriberAddForm

    def form_valid(self, form):
        # add to mailchimp

        email = form.cleaned_data.get('email')

        if settings.MAILCHIMP_ENABLE and email:
            email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
            try:
                mailchimp_client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY, mc_user=settings.MAILCHIMP_USERNAME)

                data = {
                    'email_address': email,
                    'status': 'subscribed',
                    'status_if_new': 'subscribed'
                }

                mailchimp_client.lists.members.create_or_update(
                    list_id=settings.MAILCHIMP_LIST_ID,
                    subscriber_hash=email_hash,
                    data=data
                )
            except Exception as e:
                pass

        return super().form_valid(form)
