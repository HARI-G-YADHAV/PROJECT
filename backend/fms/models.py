from django.db import models

# Create your models here.

class newfile(models.Model):
    file_no = models.IntegerField(default=10, unique=True)
    newfile_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is being created (not updated)
            max_value_dict = newfile.objects.aggregate(models.Max('file_no'))
            max_value = max_value_dict['file_no__max']  # Extract the max value from the dictionary
            if max_value is not None:  # Check if there are any existing records
                self.file_no = max_value + 1  # Increment the field
        super().save(*args, **kwargs)


class v_file(models.Model):
    vf_computer_no=models.IntegerField(primary_key=True)
    vf_file_no=models.ForeignKey(newfile,on_delete=models.CASCADE,to_field='file_no',null=True)
    vf_description=models.TextField()
    vf_file_opned=models.DateField()
    vf_file_closed=models.DateField()


class section(models.Model):    
    sec_id=models.IntegerField(primary_key=True)
    sec_user=models.CharField(max_length=10)

class user(models.Model):
    user_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    role=models.CharField(max_length=20)


    
