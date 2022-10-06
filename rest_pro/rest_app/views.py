from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserForm, chefForm, waiterForm, customerForm, foodForm
from .models import chef, food, customer, payment


def index(request):
    return render(request, 'index.html')


def admhome(request):
    return render(request, 'adm/index.html')


def login(request):
    return render(request, 'registration/login.html')


def cxhome(request):
    return render(request, 'cx/index.html')


def userview(request):
    user = request.user
    if user.is_staff:
        return redirect('admhome')
    elif user.is_customer:
        return redirect('cxhome')
    else:
        return redirect('index')


def add_chef(request):
    form = UserForm()
    n_form = chefForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = chefForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_chef = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('add_chef')
    return render(request, 'adm/add_chef.html', {'form': form, 'n_form': n_form})


def add_waiter(request):
    form = UserForm()
    n_form = waiterForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = waiterForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_waiter = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('add_waiter')
    return render(request, 'adm/add_waiter.html', {'form': form, 'n_form': n_form})


def signup(request):
    form = UserForm()
    n_form = customerForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = customerForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('signup')
    return render(request, 'register.html', {'form': form, 'n_form': n_form})


def view_chef(request):
    dataset = chef.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'adm/view_chef.html', context)


def update_chef(request, id=None):
    data = chef.objects.get(id=id)
    m_form = chefForm(instance=data)
    if request.method == 'POST':
        m_form = chefForm(request.POST, instance=data)
        if m_form.is_valid():
            m_form.save()
            # messages.info(request, ' updated Successfully')
            return redirect('view_chef')

    return render(request, 'adm/update_chef.html', {'m_form': m_form})


def add_food(request):
    v_form = foodForm()
    if request.method == 'POST':
        v_form = foodForm(request.POST, request.FILES)
        if v_form.is_valid():
            vc = v_form.save(commit=False)
            vc.save()
            messages.info(request, ' Successfully')
            return redirect('add_food')
    return render(request, 'adm/add_food.html', {'v_form': v_form})


def view_food(request):
    dataset = food.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'adm/view_food.html', context)


def cx_food(request):
    dataset = food.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'cx/view_food.html', context)


def add_order(request, id):
    u = customer.objects.get(user=request.user)
    accessory = food.objects.get(id=id)
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        food_price = request.POST.get('food_price')
        food_type = request.POST.get('food_type')
        food_image = request.POST.get('food_image')
        card_number = request.POST.get('card_number')
        cvv = request.POST.get('cvv')
        date = request.POST.get('date')
        ob = payment()
        ob.food_name = food_name
        ob.food_price = food_price
        ob.food_type = food_type
        ob.food_image = food_image
        ob.card_number = card_number
        ob.cvv = cvv
        ob.date = date
        ob.custom = u
        ob.payment_status = 1
        ob.save()
        messages.info(request, 'Requested')
        return redirect('view_order')

    return render(request, 'cx/payment.html', {'key': accessory})

def view_order(request):
    dataset = payment.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'cx/view_order.html', context)

def view_foodorder(request):
    dataset = payment.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'adm/view_foodorder.html', context)


def confirm_order(request, id):
    req = payment.objects.get(id=id)
    req.order_status = 1

    req.save()

    messages.info(request, 'Approved  Application')
    return redirect('view_foodorder')


def rej_order(request, id):
    req = payment.objects.get(id=id)
    req.order_status = 2
    req.save()
    return redirect('view_foodorder')
