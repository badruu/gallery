from django.db import models

class Photo(models.Model):
    image_name = models.CharField(default = 'IMG', max_length = 30)
    image = models.ImageField(default = 'default.jpg', upload_to = 'images')
    image_desc = models.CharField(max_length = 70)
    # location = models.ManyToManyField(location)
    # pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.image_desc

    def save_photo(self):
        self.save()

# class Location(models.Model):
#     place = models.CharField(max_length = 70)
#     def __str__(self):
#         return self.place