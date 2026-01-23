from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from .forms import OrderCreateForm
from Cart.cart import Cart
from . models import OrderItem


class OrderCreateView(TemplateView):
    template_name = 'Orders/order_create.html'

    def get(self, *args, **kwargs):
        form = OrderCreateForm()
        cart = Cart(self.request)

        return TemplateResponse(self.request, self.template_name, {'cart': cart, 'form': form})

    def post(self, *args, **kwargs):
        form = OrderCreateForm(self.request.POST)
        cart = Cart(self.request)

        if form.is_valid():
            order = form.save()

            for book in cart:
                OrderItem.objects.create(
                    order=order,
                    book=book['book'],
                    price=book['price'],
                    quantity=book['quantity']
                )

            cart.clear()

            return TemplateResponse(
                self.request,
                'orders/order_created.html',
                {'order': order}
            )

        return TemplateResponse(self.request, self.template_name, {'cart': cart, 'form': form})

