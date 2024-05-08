from django.shortcuts import render,redirect
from expence_tracker.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



# create expence
@login_required(login_url="/login/")
def create_expence(request):
    
    # create category
    if request.method=="POST":
        if "category_submit" in request.POST:
            print(True)
            category_data=request.POST.get("category_name")
            category_obj=Category(
                category=category_data,
                user=request.user
            )
            category_obj.save()
            print(category_obj.id)
            return redirect("/")
        
        
    # create expence
    if request.method=="POST":
        
        if "expense_submit" in request.POST:
            expence_name = request.POST.get("expence_name")
            amount = request.POST.get("amount")
            category_id = request.POST.get("category")
            category = Category.objects.get(pk=category_id)
            date = request.POST.get("date")
            user = request.user
            
            expence = Expence(
                expence_name=expence_name,
                amount=amount,
                category=category,
                date=date,
                user=user
            )
            expence.save()
            print(expence_name,amount,category,date,user)
            return redirect("/")
        
    
    # update expence
    if request.method=="POST":
        if "expense_update" in request.POST:
            expence_id = request.POST.get("expence_id")
            
            expence = Expence.objects.get(id=expence_id)
            
            if not expence:
                return redirect("/")
            
            expence.expence_name = request.POST.get("expence_name")
            expence.amount = request.POST.get("amount")
            category_id = request.POST.get("category")
            expence.category = Category.objects.get(pk=category_id)
            expence.date = request.POST.get("date")
            
            expence.save()
            return redirect("/")
    
        
        
    # all category and expences
    categories = Category.objects.filter(user=request.user)
    expences = Expence.objects.filter(user=request.user)
    
    return render(
        request,
        "create_expence.html", 
        context={
            "categories":categories,
            "expences":expences
        }
    )



# delete expence
@login_required(login_url="/login/")
def delete_expence(request,id):
    expence = Expence.objects.get(id=id)
    if not expence:
        return redirect("/")
    
    expence.delete()
    return redirect("/")
    






# creating user registration method 
def user_register(request):
    
    if request.user.is_authenticated:
        return redirect("/")
    
    # check the method is post or not
    if request.method=="POST":
        
        # getting data from form
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # get the user from the database based on username
        user = User.objects.filter(username = username)

        # if user is exist, show an error message
        if user.exists():
            messages.info(request, "Username Already Taken")
            return redirect("/register/")
        
        # if user is not exist, then create a user object
        user = User(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        # using set_password method to convert the user given password to non-understandable password
        user.set_password(password)
        # save the user model
        user.save()
        
        # send a message
        messages.info(request,"Account Created Successfully")
        # return the response
        return redirect("/login/")
    
    return render(request, "register.html")




# creating a user login method
def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    # check the method is post or not
    if request.method == "POST":
        
        # getting data from form
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        
        # get user from database based on username
        user = User.objects.filter(username=username)

        # check user exists or not
        # if not exist
        if not user.exists():
            messages.error(request, "Invalid Username")
            return redirect("/login/")
        
        # if exist
        user = authenticate(username = username, password=password)

        # check user is given correct password or not
        if user is None:
            messages.info(request, "Incorrect Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")
    
    return render(request, "login.html")



# user logout method
def user_logout(request):
    logout(request)
    return redirect("/login/")