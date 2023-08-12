from django.db import models
from django.contrib.auth.models import User

import random
import string


class BasicForm(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    blood_group = models.CharField(max_length=4)
    slug = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_random_code(self):
        length = 6  # You can adjust the length of the code as needed
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def save(self, *args, **kwargs):
        if not self.code:  # Generate code only if it's not already set
            self.code = self.generate_random_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"BasicForm #{self.id}"
