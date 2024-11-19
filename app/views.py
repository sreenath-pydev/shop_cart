from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import DeleteView
from .forms import UserRegistrationForm, AddressForm
from .models import Product, CartItem, UserAddress
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.http import JsonResponse

class IndexView(View):
    def get(self, request):
        """Displays the home page with men's and women's products."""
        men_products = Product.objects.filter(category='men')  
        women_products = Product.objects.filter(category='women')  
        return render(request, 'app/index.html', {
            'men_products': men_products,
            'women_products': women_products
        })

class CategoryView(View):
    def get(self, request, category_name):
        """Displays products filtered by category."""
        products = Product.objects.filter(category=category_name)
        return render(request, 'app/product_by_category.html', {'products': products, 'category_name': category_name})
    

class ProductDetailView(View):
    def get(self, request, product_id):
        """Displays detailed information for a specific product."""
        product = get_object_or_404(Product, id=product_id)
        all_products = Product.objects.all()  # Display all products for recommendations
        return render(request, 'app/product_details.html', {'product': product, 'all_products': all_products})
    

class RegisterView(View):
    def get(self, request):
        """Displays the registration form."""
        form = UserRegistrationForm()
        return render(request, 'app/register.html', {'form': form})

    def post(self, request):
        """Handles the registration form submission."""
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if password != confirm_password:
                form.add_error('confirm_password', 'Passwords do not match.')
                messages.error(request, "Passwords do not match.")
                return render(request, 'app/register.html', {'form': form})
            
            user = form.save(commit=False)
            user.set_password(password) 
            user.save()
            messages.success(request, "User registered successfully.")
            return redirect('login')
        else:
            messages.warning(request, "Invalid input, please correct the errors.")
        
        return render(request, 'app/register.html', {'form': form})
    

class LoginUserView(View):
    def get(self, request):
        """Displays the login form."""
        return render(request, 'app/login.html')

    def post(self, request):
        """Handles the login form submission."""
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
        return render(request, 'app/login.html')


class LogoutView(View):
    def get(self, request):
        """Logs out the user and redirects to the home page."""
        logout(request)
        return redirect('index')


@method_decorator(login_required, name='dispatch')  
class AddToCartView(View):
    def post(self, request, product_id):
        """Adds a product to the cart."""
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1  # Increment quantity if the item is already in the cart
        cart_item.save()
        return redirect('view_cart')


@method_decorator(login_required, name='dispatch')  
class ViewCartView(View):
    def get(self, request):
        """Displays the current user's cart."""
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.get_total_price() for item in cart_items)  # Assuming CartItem has a method to calculate the total price
        return render(request, 'app/view_cart.html', {'cart_items': cart_items, 'total_amount': total_amount})


class RemoveFromCartView(DeleteView):
    model = CartItem

    def get(self, request, *args, **kwargs):
        """Removes a product from the cart."""
        self.object = self.get_object()
        self.object.delete()
        return redirect('view_cart')
    
@method_decorator(login_required, name='dispatch')
class CheckoutView(View):
    def get(self, request):
        # Fetch cart items for the logged-in user
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.get_total_price() for item in cart_items)

        # Fetch the user's address
        try:
            user_address = UserAddress.objects.get(user=request.user)
            print(user_address.customer_name)
        except UserAddress.DoesNotExist:
            user_address = None

        return render(request, 'app/checkout.html', {
            'cart_items': cart_items,
            'total_price': total_price,
            'user_address': user_address
        })

    def post(self, request):
        # Perform checkout operations
        cart_items = CartItem.objects.filter(user=request.user)

        if cart_items.exists():
            # Clear the cart
            cart_items.delete()

            # Add success message
            messages.success(request, "Checkout completed successfully!")
        else:
            messages.error(request, "Your cart is empty.")

        # Redirect to the cart page
        return redirect('order_success')

@method_decorator(login_required, name='dispatch')
class UpdateAddressView(View):
    def get(self, request):
        # Fetch the user's current address or initialize a blank form
        try:
            address_instance = UserAddress.objects.get(user=request.user)
        except UserAddress.DoesNotExist:
            address_instance = None

        form = AddressForm(instance=address_instance)
        return render(request, 'app/update_address.html', {'form': form})

    def post(self, request):
        # Handle form submission
        try:
            address_instance = UserAddress.objects.get(user=request.user)
        except UserAddress.DoesNotExist:
            address_instance = None

        form = AddressForm(request.POST, instance=address_instance)

        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, "Address updated successfully!")
            return redirect('checkout')  # Redirect to the checkout page
        else:
            messages.error(request, "Failed to update address. Please correct the errors.")
        
        return render(request, 'app/update_address.html', {'form': form})
    
def order_success(request):
    return render(request, 'app/order_success.html')

class SearchView(View):
    def get(self, request):
        """Displays search results based on the query."""
        query = request.GET.get("q")
        if query:
            products = Product.objects.filter(name__icontains=query)
        else:
            products = Product.objects.all()
        return JsonResponse({"products": list(products.values())}, safe=False) 

    