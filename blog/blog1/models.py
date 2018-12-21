from django.db import models
from django.utils.timezone import now
from django.core.urlresolvers import reverse
def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)


class Posts(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(null=True,blank=True,upload_to=upload_location)
    content=models.TextField(max_length=5000)
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog1:detail",kwargs={"id":self.id})
    class Meta:
        ordering=["-id","-timestamp","-updated"]



