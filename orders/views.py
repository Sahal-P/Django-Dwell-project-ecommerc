from django.shortcuts import render,redirect
from django.http import JsonResponse
from accounts.models import Address
from cart.models import CartItem,OldCart
from orders.models import Orders
from category.models import Products
# Create your views here.
def admin_order_detailes(request):
    orders = Orders.objects.all().order_by('-orderd_date')
    return render(request,"admin/orders.html", {"orders": orders})

def add_address(request):
    user = request.user
    if request.POST:
        first_name = request.POST.get('first_name')
        
        if request.POST['last_name']:
            last_name = request.POST.get('last_name')
    
        phone1 = request.POST.get('phone1')
        if request.POST['phone2']:
            phone2 = request.POST.get('phone2')
        
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        if request.POST['address2']:
            address2 = request.POST.get('address2')

        country = request.POST.get('country')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        payment = request.POST.get('paymentMethod')
        
        address = Address.objects.create(user= user, first_name=first_name,
                                         last_name=last_name ,phone_number_1=phone1, 
                                         phone_number_2= phone2, address_1 = address1, 
                                         address_2 = address2, country=country,State=state ,
                                         zip_code = zip_code , email=email
                                         )
        address.save()
        
        return redirect("checkout")
    return render(request, "add_address.html")

def order_place(request,total=0,quantity=0,
                cart_items=None,tax=0,delv=0,
                g_total=0):
    user = request.user
    try : 
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user,is_active=True)
            for i in cart_items :
                product = Products.objects.get(id = i.product.id)
                get_minus_prod = i.Quantity  
                minus =i.product.quantity-get_minus_prod  
                product.quantity = minus
                product.save()   
        for cart_item in cart_items:
            total += (cart_item.product.selling_price * cart_item.Quantity)
            quantity += cart_item.Quantity
            tax = (5*total)/100
            delv = 5
            g_total = total+ tax+delv
    except  :
        pass
    if request.POST:
        payment = request.POST.get('flexRadioDefault')
        adrs_id = request.POST.get('address')
        if payment and adrs_id is not None:
            for item in cart_items:
                Orders(product = item.product ,user = request.user , 
                       address= adrs_id ,total_price = item.sub_total(),
                       payment=payment, status = "placed" ,
                       price = item.product.selling_price , 
                       quantity = item.Quantity).save()
                
                OldCart(product = item.product,user = request.user , Quantity = item.Quantity).save()
            CartItem.objects.filter(user=request.user,is_active=True).delete()
            return render(request , "order_success.html" ,{"user":user,"g_total":g_total})
    return redirect("checkout")

def order_status(request):
    try:
        orders = Orders.objects.filter(user = request.user).order_by('-orderd_date')
    except:
        return render(request, "order_status.html" )
    return render(request, "order_status.html" ,{"orders":orders})


def order_details(request, id):
    order = Orders.objects.get(id=id)
    return render(request, "order_details.html",{"order":order})

def admin_orderedit(request):
    
    order_id = request.GET.get('oid')
    value = request.GET.get('value')
    obj = Orders.objects.get(id = order_id)
    obj.status = value
    obj.save()
    return JsonResponse({"order":order_id})

def ordercancell(request ,id):
    order = Orders.objects.get(id=id)
    order.status = "cancelled"
    order.save()
    return render(request, "order_details.html",{"order":order})

def admin_order_cancell(request):
    id = request.GET.get('id')
    orders = Orders.objects.get(id=id)
    orders.status = "cancelled"
    orders.save()
    orders = Orders.objects.all().order_by('id')
    return JsonResponse({"id":id})

def return_order(request,id):
    order = Orders.objects.get(id=id)
    order.status="Return Requested waiting for approval"
    order.save()
    return render(request, "order_details.html",{"order":order})
    
def approve_return(request):
    id = request.GET.get('id')
    orders = Orders.objects.get(id=id)
    orders.status="Return Aproved"
    orders.save()
    orders = Orders.objects.all().order_by('id')
    return JsonResponse({"id":id})