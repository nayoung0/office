# Generated by Django 4.2.9 on 2024-01-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_remove_answer_content_answer_select_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='select_question',
            field=models.IntegerField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_a',
            field=models.CharField(default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_b',
            field=models.CharField(default='1', max_length=1, null=True),
        ),
    ]
