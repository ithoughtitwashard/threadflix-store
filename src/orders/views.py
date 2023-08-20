from django.urls import reverse_lazy
from django.views.generic import CreateView

from default.views import TitleMixin
from orders.forms import OrderCreateForm
from orders.models import Order


class OrderCreateView(TitleMixin, CreateView):
    title = 'Make an order'
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('orders:create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OrderCreateView, self).form_valid(form)
