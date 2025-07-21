from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Medicine, Category
from django.shortcuts import render, get_object_or_404


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import Medicine, CartItem

from django.db.models import Q

def medicine_search(request):
    query = request.GET.get('q', '')
    medicines = Medicine.objects.filter(
        Q(name__icontains=query) | Q(brand__icontains=query)
    ) if query else []

    return render(request, 'inventory/pages/medicine_search.html', {
        'query': query,
        'medicines': medicines
    })



# 🏠 Home Page
def index(request):
    return render(request, 'inventory/pages/index.html')


def about(request):
    return render(request, 'inventory/pages/about.html')

def blog(request):
    return render(request, 'inventory/pages/blog.html')


# 🛒 Shop Page - Category-wise medicine listing
def shop_view(request):
    categories = Category.objects.prefetch_related('medicine_set').all()
    return render(request, 'inventory/pages/shop.html', {'categories': categories})




from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'inventory/pages/doctor_list.html', {'doctors': doctors})




def category(request):
    categories = Category.objects.all()
    return render(request, 'inventory/pages/category.html', {
        'categories': categories
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    medicines = Medicine.objects.filter(category=category)
    return render(request, 'inventory/pages/category_detail.html', {
        'category': category,
        'medicines': medicines,
    })




@login_required
def add_to_cart(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, medicine=medicine,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'inventory/pages/cart.html', {
        'cart_items': cart_items,
        'total': total
    })



from django.shortcuts import redirect

@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('view_cart')

@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('view_cart')

@login_required
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')









def protinestore(request):
    return render(request, 'inventory/pages/protinestore.html')

def beauty(request):
    return render(request, 'inventory/pages/beauty.html')

def medicine(request):
    return render(request, 'inventory/pages/medicine.html')

def categaris(request):
    return render(request, 'inventory/pages/categoiry.html')


# def contact(request):
#     return render(request, 'inventory/pages/contact.html')


from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

        # Display a success message to the user
        messages.success(request, "Thank you for your message. We will get back to you soon.")

        return redirect('contact')  # Redirect back to the contact page

    return render(request, 'inventory/pages/contact.html')



# 📦 Get Medicines by Category (AJAX)
def get_medicines_by_category(request, category_id):
    medicines = Medicine.objects.filter(category_id=category_id)
    data = []
    for med in medicines:
        data.append({
            'name': med.name,
            'brand': med.brand,
            'description': med.description,
            'price': float(med.price),
            'quantity': med.quantity,
            'image': request.build_absolute_uri(med.image.url) if med.image else '',
        })
    return JsonResponse({'medicines': data})


# 🔐 Login Page
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'inventory/pages/login.html', {
                'error': 'Invalid username or password'
            })
    return render(request, 'inventory/pages/login.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dummy_payment(request):
    return render(request, 'inventory/pages/payment_success.html')


