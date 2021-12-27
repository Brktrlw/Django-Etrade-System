from django.shortcuts import render,HttpResponse
from USERAPP.models import CartModel
from ORDERS.models import OrderItemModel,OrderModel


def v_payment(request):
    orderItems = CartModel.objects.filter(customer_id=request.user.id)
    ORDER      = OrderModel.objects.create(customer_id=request.user.id,complete=False,orderAddress_id=4)
    #ORDER.save()
    for item in orderItems:
        print(item.product.id)
        ITEM=OrderItemModel.objects.create(product_id=item.product.id,quantity=item.amount,order_id=ORDER.id)
        #ITEM.save()
    #orderItems.delete()

    return render(request,"cart.html")