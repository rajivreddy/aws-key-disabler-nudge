import os
import boto3
from iam_users import key_disabler
from ses_notification import notification

ses_client = boto3.client("ses", region_name="us-west-2", aws_access_key_id=os.environ['ACCESS_KEY'], aws_secret_access_key=os.environ['SECRET_ACCESS_KEY'])

users_list = key_disabler.get_iam_user()
print("Warning List")
warn_list = key_disabler.get_warning_users_list(users_list)

print("Danger List")
dang_list = key_disabler.get_disable_users_list(users_list)

users_data = warn_list + dang_list


def ses_mail(source="admin@example.com",to="admin@example.com"):
    response = ses_client.send_email(
        Source=source,
        Destination={
            'ToAddresses': [
                to,
            ]
        },
        Message=notification.compose_mail_for_admins(users_data)
    )
    print(response)


ses_mail(source=os.getenv("SOURCE_ADDR", default="admin@example.com"),to=os.getenv("TO_ADDR",default="admin@example.com"))
