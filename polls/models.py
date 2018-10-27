import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=200, verbose_name='質問')
    pub_date = models.DateTimeField('公開日時')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """ 1日以内に公開された？ """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近の記事'


class Choice(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='回答')
    votes = models.IntegerField(default=0, verbose_name='得票数')

    def __str__(self):
        return self.choice_text
