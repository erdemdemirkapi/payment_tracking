from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from payment_tracking.settings import EMAIL_HOST_USER

class Mails(APIView):
    def post(self, request, *args, **kwargs):
        email_to = self.request.data.get('email_to')

        send_mail(
            'Payment Reminder',
            'It seems you have debt someone to the system. We kindly ask you to make your payment as soon as possible.',
            EMAIL_HOST_USER,
            [email_to],
            fail_silently=False,
        )

        if success:
            response = {'data': 'success'}
        else:
            response = {'data': 'failed'}

        return Response(response)