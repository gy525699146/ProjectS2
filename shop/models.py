from django.db import models
from django.contrib.auth.views import get_user_model
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254)
    price = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to='product_img')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={'pk': self.pk})


class ShoppingCart(models.Model):
    product = models.ManyToManyField('shop.OrderCard', null=True, related_name='cardorders')
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    order_cards = models.ManyToManyField('shop.OrderCard', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class OrderCard(models.Model):
    product = models.ForeignKey(Product, verbose_name='产品', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='数量', default=0)


# OrderCard.objects.filter(shoppingcart=)