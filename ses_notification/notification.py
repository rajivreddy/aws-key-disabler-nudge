def compose_mail_for_user(data):
    message = {}
    if data["status"] == "warning":
        message["Subject"] = {
            'Charset': 'UTF-8',
            'Data': "Warning: " + "IAM AccessKey AGE status",
        }
        message["Body"] = {
            'Html': {
                'Charset': 'UTF-8',
                'Data': 'Your AWS access key (User ID is:' + data["user_name"] + ') is about to expire in ' + str(
                    data["expire_due"]) + ' days once it crosses 90 days, your access key will be disabled.',
            },
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is the message body in text format.',
            },
        }
    else:
        message["Subject"] = {
            'Charset': 'UTF-8',
            'Data': "Disabled: " + "IAM AccessKey AGE status",
        }
        message["Body"] = {
            'Html': {
                'Charset': 'UTF-8',
                'Data': 'Your AWS access key (User ID is:' + data[
                    "user_name"] + ') is  has been disabled because of your access key age is ' + str(
                    data["key_age"]) + ', which is exceeded 90 days.',
            },
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is the message body in text format.',
            },
        }
    return message


def compose_mail_for_admins(data):
    message = {}
    message["Subject"] = {
        'Charset': 'UTF-8',
        'Data': "IAM AccessKey Status Report",
    }
    message_data = ""
    for i in data:
        message_data += "<br>Username is : " + i["user_name"] + " , the Account Age is : " + str(i["key_age"]) + " And state of Key is in :" + i["status"]
    print(message_data)
    message["Body"] = {
        'Html': {
            'Charset': 'UTF-8',
            'Data': "Hi <br>" + message_data,
        },
        'Text': {
            'Charset': 'UTF-8',
            'Data': 'This is the message body in text format.',
        },
    }
    return message




#compose_mail_for_admins([{'user_name': 'akhil.desai@srijan.net', 'status': 'Danger', 'key_age': 403}, {'user_name': 'alistair@oncorps.io', 'status': 'Danger', 'key_age': 250}, {'user_name': 'ashish.thakur', 'status': 'Danger', 'key_age': 511}, {'user_name': 'auth0.machineuser', 'status': 'Danger', 'key_age': 445}, {'user_name': 'dom@oncorps.io', 'status': 'Danger', 'key_age': 510}, {'user_name': 'james@oncorps.io', 'status': 'Danger', 'key_age': 244}, {'user_name': 'jeson', 'status': 'Danger', 'key_age': 544}, {'user_name': 'jomon.johny@srijan.net', 'status': 'Danger', 'key_age': 249}, {'user_name': 'mark@oncorps.io', 'status': 'Danger', 'key_age': 150}, {'user_name': 'nathan@oncorps.io', 'status': 'Danger', 'key_age': 368}, {'user_name': 'navya.n@srijan.net', 'status': 'Danger', 'key_age': 321}, {'user_name': 'nigel@oncorps.io', 'status': 'Danger', 'key_age': 510}, {'user_name': 'parv.jain@srijan.net', 'status': 'Danger', 'key_age': 372}, {'user_name': 'peter+aws@oncorps.io', 'status': 'Danger', 'key_age': 416}, {'user_name': 'philroy.pereira@srijan.net', 'status': 'Danger', 'key_age': 329}, {'user_name': 'rajeev.jaggavarapu', 'status': 'Danger', 'key_age': 567}, {'user_name': 'ramnivas.yadav@srijan.net', 'status': 'Danger', 'key_age': 262}, {'user_name': 'ses-smtp-user.gitlab', 'status': 'Danger', 'key_age': 278}, {'user_name': 'ses-stage', 'status': 'Danger', 'key_age': 102}, {'user_name': 'surabhi.gokte@srijan.net', 'status': 'Danger', 'key_age': 256}, {'user_name': 'udit.verma@srijan.net', 'status': 'Danger', 'key_age': 480}, {'user_name': 'vaughan.po@srijan.net', 'status': 'Danger', 'key_age': 199}, {'user_name': 'vikash.choudhary@srijan.net', 'status': 'Danger', 'key_age': 262}, {'user_name': 'vishwa.chikate@srijan.net', 'status': 'Danger', 'key_age': 504}])
