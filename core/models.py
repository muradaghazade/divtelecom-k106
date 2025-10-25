from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    cover_image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    ram = models.IntegerField()
    camera = models.IntegerField()
    battery = models.IntegerField()
    storage = models.IntegerField()
    ip_rating = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    display_type = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    cpu = models.CharField(max_length=50)
    
    


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return f"Slider {self.id}"
    
class Brand(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='brands/')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.IntegerField()

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f"Cart {self.id}"
    
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_payment = models.IntegerField()
    payment_type = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.id}"


class Favorite_product(models.Model):
     product = models.ForeignKey(Product, on_delete=models.CASCADE)

     class Meta:
        verbose_name = 'Favorite_product'
        verbose_name_plural = 'Favorite_products'

     def __str__(self):
        return f"Favorite_product {self.id}"
     
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"Comment {self.id}"
    
class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f"Image {self.id}"