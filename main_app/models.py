from django.db import models

# Create your models here.


class StudentRecord(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.DateField()
    graduation_year = models.IntegerField()
    gender = models.CharField(
        max_length=20,
        choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    city = models.CharField(max_length=200)

    class Meta:
        db_table = 'Student Records'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def get(self, name):
        return self.__getattribute__(name)
    
    def __repr__(self) -> str:
        return super().__repr__()
