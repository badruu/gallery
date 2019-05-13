from django.db import models
import datetime as dt



class Location(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(default = 'Nairobi', max_length = 70)
    country = models.CharField(default = 'Kenya', max_length = 70)
    
    def __str__(self):
        return self.city+" "+self.country

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Photo(models.Model):
    image_name = models.CharField(default = 'Image', max_length = 30)
    image = models.ImageField(default = 'default.jpg', upload_to = 'images')
    image_desc = models.CharField(max_length = 70)
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.image_desc

    def save_photo(self):
        self.save()

    @classmethod
    def search_by_image_name(cls,search_term):
        photo = cls.objects.filter(image_name__icontains=search_term)
        return photo
