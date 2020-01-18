from django.db import models

class Transaction(models.Model):
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now_add = True)
    note = models.TextField()
    user = models.ForeignKey('users.CustomUser', related_name='user', on_delete = models.CASCADE)
    amount_cents = models.IntegerField(default = 0, null = False)
    amount_currency = models.CharField(default = 'TRY', max_length = 10, null = False)
    state = models.CharField(max_length = 50, default = 'pending', editable = False)
    to_whom = models.ForeignKey('users.CustomUser', related_name='to_whom', on_delete = models.CASCADE)

    def __str__(self):
        return self.note