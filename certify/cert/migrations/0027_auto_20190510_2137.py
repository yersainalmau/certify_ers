# Generated by Django 2.2 on 2019-05-10 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0026_assignment_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedquestion',
            name='assignment',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='cert.Assignment'),
        ),
        migrations.AlterField(
            model_name='assignedquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cert.Question'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assigned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assgn_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assgn_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='certificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cert.Certificate'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='current_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cert.Question'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cert.Person'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='quiz_structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cert.QuizStructure'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub1', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub10', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject11',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub11', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject12',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub12', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub2', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub3', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub4', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub5', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub6', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub7', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub8', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='quizstructure',
            name='subject9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub9', to='cert.Subject'),
        ),
        migrations.AlterField(
            model_name='sendemail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]