from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View
from django.contrib import messages

from .models import Product, OrderCard


class Index(ListView):
    template_name = 'shop/index.html'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all().order_by('id')


class Detail(DetailView):
    template_name = 'shop/detail.html'
    model = Product


class Cart(LoginRequiredMixin, ListView):
    template_name = 'shop/cart.html'

    def get_queryset(self):
        return self.request.user.shoppingcart.product.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Cart, self).get_context_data()
        object_list = context['object_list']
        num = 0
        for i in object_list:
            num += i.product.price * i.amount
        context['total'] = num
        return context


class AddCart(View):
    def post(self, request):
        # 获取产品， 购物车
        product = self.request.POST.get('product')
        product_obj = Product.objects.get(pk=product)
        shopping_card = request.user.shoppingcart
        try:
            order_card = OrderCard.objects.get(cardorders=shopping_card, product=product)
        except OrderCard.DoesNotExist:
            order_card = OrderCard.objects.create(product=product_obj)
            shopping_card.product.add(order_card)
            shopping_card.save()

        # 数量加1
        order_card.amount += 1
        order_card.save()

        messages.success(request, 'Product %s AddToCart Successfully' % product_obj.name)
        return redirect(reverse('shop:detail', kwargs={'pk': product}))


class Check(View):
    def post(self, request):
        user = request.user
        total = user.shoppingcart.product.aggregate(Sum('price'))
        if not user.shoppingcart.product.all().exists():
            messages.error(request, '无商品')
            return redirect('shop:cart')
        if user.wallet.amount >= total['price__sum']:
            user.wallet.amount -= total['price__sum']
            user.shoppingcart.product.all().delete()
            messages.success(request, '结账成功')
        else:
            messages.error(request, '结账失败， 钱包余额不足!')
        return redirect('shop:cart')
