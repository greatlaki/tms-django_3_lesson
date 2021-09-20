from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

'''
Read:
    Women.objects
        Women.objects.create()
    Women.objects.all()
    Women.objects.filter()
    Women.objects.exlude()
    Women.objects.get()
    Women.objects.order_by()
    
Update:
    wu = Women.objects.get(pk=2)
    wu.title = ''
    wu.content = ''
    wu.save()

Delete:
    wd.delete()
'''