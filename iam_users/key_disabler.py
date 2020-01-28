import os
import boto3
from datetime import datetime, tzinfo

iam_client = boto3.client('iam', aws_access_key_id=os.environ['ACCESS_KEY'],
                          aws_secret_access_key=os.environ['SECRET_ACCESS_KEY'])


def get_iam_user():
    users_list = iam_client.list_users()
    # print(users_list["Users"][0])
    # print("\n\n")
    users_data = []
    for i in users_list["Users"]:
        user_data = {"user_name": i["UserName"], "access_key": i["UserId"], "create_date": i["CreateDate"]}
        users_data.append(user_data)
    # print(users_data)
    return users_data


def key_age(create_date):
    age = datetime.now(create_date.tzinfo) - create_date
    if "days" in str(age):
        return int(str(age).split(" ")[0])


def get_warning_users_list(user_list):
    users_list = []
    for i in user_list:
        user_data = {}
        if 90 > key_age(i["create_date"]) >= 75:
            user_data = {"user_name": i["user_name"], "status": "Warning", "key_age": key_age(i["create_date"]),
                         "expire_due": 90 - key_age(i["create_date"])}
            users_list.append(user_data)
    return users_list


def get_disable_users_list(user_list):
    users_list = []
    for i in user_list:
        if key_age(i["create_date"]) >= 90:
            user_data = {"user_name": i["user_name"], "status": "Danger", "key_age": key_age(i["create_date"])}
            users_list.append(user_data)

    return users_list
