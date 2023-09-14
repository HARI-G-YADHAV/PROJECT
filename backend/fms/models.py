from django.db import models

# Create your models here.

class newfile(models.Model):
    file_no=models.IntegerField(default=10,unique=True)
    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is being created (not updated)
            max_value = newfile.objects.aggregate(models.Max('file_no')) 
            self.file_no = max_value + 1  # Increment the field
        super().save(*args, **kwargs)
    newfile_date=models.DateTimeField(auto_now_add=True)
    newfile_reciver=models.CharField(max_length=20)


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


    
