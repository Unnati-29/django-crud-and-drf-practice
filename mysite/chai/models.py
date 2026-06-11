from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML' , 'Masala Chai'),
        ('GR' , 'Green Chai'),  
        ('HR' , 'Herbal Chai'),
        ('EL' , 'Elachi Chai'),
        ('KL' , 'Kiwi Chai'),
        ('PL' , 'Plain Chai'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/',blank=True,null=True)
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(default=' ')
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)

    def __str__(self):
        return self.name
    
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review for {self.chai.name} - Rating: {self.rating}'
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200) 
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')
    def __str__(self):
        return self.name    

class ChaiOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chai_variety = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Order of {self.quantity} {self.chai_variety.name} by {self.user.username}'