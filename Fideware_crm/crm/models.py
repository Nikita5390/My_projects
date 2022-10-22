from django.db import models
from django.utils import timezone
from enum import Enum
from uuid import uuid4
from datetime import timedelta, datetime, tzinfo
from field_history.tracker import FieldHistoryTracker


class Status(Enum):
    Request_send = "Запрос отправлен"
    Request_cancel = "Отмена запроса"
    Repeated_request = "Повторный запрос"
    In_contacts = "В контактах"
    Not_now = "Не сейчас"
    More_info = "Хочет узнать больше"
    Ready_call = "Готов созвониться"
    Call_assigned = "Назначен звонок"
    Phoned = "Состоялся звонок"
    Converted = "Сконвертирован"
    Not_target_audience = "Не целевая аудитория"
    Not_write = "Не пишите мне больше"
    Removed = "Удалил"

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class LeadStep(Enum):
    Thank_connect = "Поблагодарили за коннект"
    Useful_content = "Отправили полезный контект"
    Poll_deleted = "Отправили опрос"
    Sent_our_case = "Отправили наш кейс"
    Suggested_call = "Предложили созвониться"
    Kicked_1 = "Пнули раз"
    Kicked_2 = "Пнули два"
    Kicked_3_mail = "Пнули на почту"
    Kicked_4_mail = "Повторно пнули на почту"

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class User(models.Model):
    class Meta:
        db_table = "users"

    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    linkedin = models.CharField(max_length=256)
    add_contact = models.TextField()
    group = models.CharField(max_length=20)

    last_contact = models.DateField(null=False)
    next_contact = models.DateField(null=False)
    status = models.CharField(max_length=50, choices=Status.choices(), default=Status.Request_send)
    step = models.CharField(max_length=50, choices=LeadStep.choices(), default=LeadStep.Thank_connect)
    comment = models.TextField()
    history = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    field_history1 = FieldHistoryTracker(['status'])
    field_history2 = FieldHistoryTracker(['step'])

    def __str__(self):
        return '%s' % self.name

# IMPORT EXCEL:
# CREATE TABLE fw_crm (User_name VARCHAR (255) NOT NULL, Last_name VARCHAR (255) NOT NULL,
# Linked VARCHAR (255) NOT NULL, Email VARCHAR (255) NOT NULL,
# Job VARCHAR (255) NOT NULL, Company VARCHAR (255) NOT NULL,
# Group_user VARCHAR (255) NOT NULL, Next_contact TIMESTAMP NOT NULL,
# Status VARCHAR (255) NOT NULL, Last_contact TIMESTAMP NOT NULL)

# COPY fw_crm FROM 'D:\Fideware\Table_CRM_UTF8.csv' DELIMITER ';' CSV HEADER;
