from django.db import models

# Create your models here.
class Restaurant():
    def __init__(self, email, password):
        # self.id = id
        self.email = email
        self.password = password
