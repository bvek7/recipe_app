
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse

def dish(request):
    if request.method== "POST":
     data=request.POST
     dish_name=data.get("dish_name")
     dish_description=data.get("dish_description")
     dish_image=request.FILES.get("dish_image")
      

    
     print(dish_name)
     print(dish_description)
     print(dish_image)

     Dish.objects.create(
            dish_name=dish_name,
            dish_description=dish_description,
            dish_image=dish_image,
        )



     return redirect("/recipe/")
    
    queryset=Dish.objects.all()
    context={"dish":queryset}
    
    return render(request, "recipe.html",context)

def dish_delete(request,id):
    queryset=get_object_or_404(Dish,id=id)
    queryset.delete()
    

    return redirect("/recipe/")

def dish_update(request, id):
    queryset = get_object_or_404(Dish, id=id)
    
    if request.method == "POST":
        data = request.POST
        dish_name = data.get("dish_name")
        dish_description = data.get("dish_description")
        dish_image = request.FILES.get("dish_image")

        queryset.dish_name = dish_name
        queryset.dish_description = dish_description
        
        if dish_image:
            queryset.dish_image = dish_image

        queryset.save()  # Save the updated dish object
        
        return redirect("/recipe/") 
    
    context = {"dish": queryset} 
    return render(request, "update.html", context)

def register(request):
    if request.method=="POST":
        data=request.POST
        email=data.get("email")
        Username=data.get("Username")
        password=data.get("password")
        password1=data.get("password1")

        if User.objects.create_user(username=Username, password=password):
            messages(request,"registerd in sucessfully")
            return redirect(request,"recipe.html")
        
        else :
         User.objects.filter(Username=Username, email=email).exist()
         messages.error(request,"Credintals already exist")
        

            
    return render(request, 'recipe.html')