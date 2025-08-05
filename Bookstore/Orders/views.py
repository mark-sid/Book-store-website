from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import OrderCreateForm
from Cart.cart import Cart
from . models import OrderItem
# Create your views here.


class OrderCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'Orders/order_create.html'
        form = OrderCreateForm()
        cart = Cart(request)

        return render(request, template_name,{'cart': cart, 'form': form})

    def post(self, request, *args, **kwargs):
        form = OrderCreateForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         book=item['book'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            return render(request,'orders/order_created.html', {'order': order})
        return render(request, 'Orders/order_create.html',{'cart': cart, 'form': form})