from django.db import models
from apps.accounts.models import Account

subjects = ["Math", "Pyhsics", "Algebra", "English"]


class Subject(models.Model):
    subject = models.CharField(max_length=20, choices=list(map(lambda x: (x, x), subjects)), null=True)


class Questions(models.Model):
    subject = models.CharField(max_length=20, choices=list(map(lambda x: (x, x), subjects)), null=True)
    title = models.CharField(max_length=211)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


OPTIONS = ['A', 'B', 'C', 'D']


class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_a = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option A')
    option_b = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option B')
    option_c = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option C')
    option_d = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option D')
    correct_answer = models.CharField(max_length=2, blank=False, null=False,
                                      choices=list(map(lambda x: (x, x), OPTIONS)))

    def __str__(self) -> str:
        return self.question.title


class Quiz(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    true_count = models.PositiveIntegerField(default=0)


class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=2, blank=False, null=False, choices=list(map(lambda x: (x, x), OPTIONS)))
    created_at = models.DateTimeField(auto_now_add=True)
    correctness = models.BooleanField(default=False)

    def __str__(self):
        return self.answer



