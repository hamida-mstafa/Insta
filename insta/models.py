from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name="yg")
    title = models.CharField(max_length=60, null=True)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    likes = models.IntegerField(default=0, null=True)
    caption = models.CharField(max_length=140, default="")
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
    def save_image(self):
        self.save()

    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item;
