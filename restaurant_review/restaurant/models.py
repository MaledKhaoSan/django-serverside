from django.db import models

class RestaurantType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('NO_STOREFRONT', 'No Storefront'),
        ('STOREFRONT', 'Storefront'),
        ('DELIVERY', 'Delivery'),
        ('PICKUP', 'Pickup'),
    ]

    PRICE_RANGE_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('PREMIUM', 'Premium'),
    ]

    name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    price_range = models.CharField(max_length=20, choices=PRICE_RANGE_CHOICES)
    province = models.CharField(max_length=100, default='Unknown')
    district = models.CharField(max_length=100, default='Unknown')
    subdistrict = models.CharField(max_length=100, default='Unknown')
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)  # Keeping ForeignKey for relational integrity
    restaurant_types = models.ManyToManyField(RestaurantType, through='RestaurantRestaurantType')

    def __str__(self):
        return self.name


class RestaurantRestaurantType(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    restaurant_type = models.ForeignKey(RestaurantType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('restaurant', 'restaurant_type')



class OperatingHour(models.Model):
    DAY_OF_WEEK_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    TIME_CHOICES = [
        ('00:00', '00:00'), ('00:30', '00:30'),
        ('01:00', '01:00'), ('01:30', '01:30'),
        ('02:00', '02:00'), ('02:30', '02:30'),
        ('03:00', '03:00'), ('03:30', '03:30'),
        ('04:00', '04:00'), ('04:30', '04:30'),
        ('05:00', '05:00'), ('05:30', '05:30'),
        ('06:00', '06:00'), ('06:30', '06:30'),
        ('07:00', '07:00'), ('07:30', '07:30'),
        ('08:00', '08:00'), ('08:30', '08:30'),
        ('09:00', '09:00'), ('09:30', '09:30'),
        ('10:00', '10:00'), ('10:30', '10:30'),
        ('11:00', '11:00'), ('11:30', '11:30'),
        ('12:00', '12:00'), ('12:30', '12:30'),
        ('13:00', '13:00'), ('13:30', '13:30'),
        ('14:00', '14:00'), ('14:30', '14:30'),
        ('15:00', '15:00'), ('15:30', '15:30'),
        ('16:00', '16:00'), ('16:30', '16:30'),
        ('17:00', '17:00'), ('17:30', '17:30'),
        ('18:00', '18:00'), ('18:30', '18:30'),
        ('19:00', '19:00'), ('19:30', '19:30'),
        ('20:00', '20:00'), ('20:30', '20:30'),
        ('21:00', '21:00'), ('21:30', '21:30'),
        ('22:00', '22:00'), ('22:30', '22:30'),
        ('23:00', '23:00'), ('23:30', '23:30'),
        ('23:59', '23:59'),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAY_OF_WEEK_CHOICES)
    opening_time = models.CharField(max_length=5, choices=TIME_CHOICES)  # Changed to CharField with choices
    closing_time = models.CharField(max_length=5, choices=TIME_CHOICES)  # Changed to CharField with choices

    def __str__(self):
        return f"{self.restaurant.name} - {self.day_of_week}"