# restaurant_review/restaurant/models.py
from django.db import models
from django.contrib.auth.models import User


# UserProfile model to add extra user info
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    phone_number = models.CharField(default='Unknown', max_length=15)
    about_me = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.user.username


# RestaurantType remains unchanged
class RestaurantType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# Restaurant model
class Restaurant(models.Model):
    no_storefront = models.BooleanField(default=False)
    storefront = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    pickup = models.BooleanField(default=False)

    PRICE_RANGE_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('PREMIUM', 'Premium'),
    ]

    name = models.CharField(max_length=255)
    price_range = models.CharField(max_length=20, choices=PRICE_RANGE_CHOICES)
    province = models.CharField(max_length=100, default='Unknown')
    district = models.CharField(max_length=100, default='Unknown')
    subdistrict = models.CharField(max_length=100, default='Unknown')

    # Allow latitude and longitude to be nullable
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the owner of the restaurant
    restaurant_types = models.ManyToManyField(RestaurantType, through='RestaurantRestaurantType')

    def __str__(self):
        return self.name


# Many-to-Many relationship between Restaurant and RestaurantType
class RestaurantRestaurantType(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    restaurant_type = models.ForeignKey(RestaurantType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('restaurant', 'restaurant_type')


# Operating Hours for a restaurant
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
    opening_time = models.CharField(max_length=5, choices=TIME_CHOICES)
    closing_time = models.CharField(max_length=5, choices=TIME_CHOICES)

    def __str__(self):
        return f"{self.restaurant.name} - {self.day_of_week}"


# Reviews of a restaurant
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # Link to Restaurant
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User who wrote the review
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.restaurant.name}"


# Favorite restaurants for a user
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # Link to the Restaurant
    favorited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} favorited {self.restaurant.name}"


# Images associated with a review
class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)  # Link to Review
    image_file = models.ImageField(upload_to='review_images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Who uploaded the image
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.review.restaurant.name} by {self.review.user.username}"


# Images associated with a restaurant
class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # Link to Restaurant
    image_file = models.ImageField(upload_to='restaurant_images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Who uploaded the image
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.restaurant.name}, uploaded by {self.uploaded_by.username}"
