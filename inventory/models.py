



from django.db import models
from django.contrib.auth.models import User  # ✅ add at the top if not already




from django.db import models
from django.utils.text import slugify



class Doctor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)
    specialization = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15)  # in international format e.g., +919876543210

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='medicine_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name





from django.contrib.auth.models import User
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.medicine.price

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}"




class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.medicine.price

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}"



class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100,)  # ✅ Set default
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.medicine.price
        self.medicine.quantity -= self.quantity
        self.medicine.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order: {self.customer_name} - {self.medicine.name}"




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)  # For the user's name
    email = models.EmailField()  # For the user's email address
    subject = models.CharField(max_length=200)  # For the subject of the message
    message = models.TextField()  # For the content of the message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the message was created

    def __str__(self):
        return f"Message from {self.name} ({self.email})"




