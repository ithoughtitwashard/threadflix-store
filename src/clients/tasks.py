from celery import shared_task

from clients.account_services import code_and_expiration_for_email_verification
from clients.models import EmailVerification, User


@shared_task
def send_email(user_id):
    user = User.objects.get(id=user_id)
    code, expiration = code_and_expiration_for_email_verification()
    record = EmailVerification.objects.create(code=code, user=user, expiration=expiration)
    record.send_verification_email()
