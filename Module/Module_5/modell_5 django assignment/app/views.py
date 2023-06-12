from django.shortcuts import render,redirect
from .models import *
import re
# Create your views here.

def home(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email']) 
        if uid.role == 'admin':
            aid =adminn.objects.get(user_id=uid)

            context={
                'uid':uid,
                'aid':aid,
            }
            return render(request,'index.html',context)


def login(request):
    if 'email' in request.session:
        return redirect('home')
    else:    
        if request.POST:
            email=request.POST['emailname']
            password=request.POST['passwordname']

            uid=User.objects.get(email=email)

            if uid.password ==password:
                if uid.role== "admin":
                    aid=adminn.objects.get(user_id=uid)
                    request.session['email'] = uid.email
                    return redirect('home')
            else:
                pass

    return render(request,'login.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('login')
    else:
        return redirect('login')    

def profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == 'admin':
            aid = adminn.objects.get(user_id=uid)
            context={
                'uid':uid,
                'aid':aid
            }
            return render(request,'profile.html',context)
    else:
        return redirect('login')        


def adminPassChange(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if request.POST:
            if uid.role == 'admin':
                aid=adminn.objects.get(user_id=uid)
                currentPassword = request.POST['currentPassword']
                newPassword = request.POST['newPassword']
                confirmPassword = request.POST['confirmPassword']
                if uid.password==currentPassword:
                    if newPassword ==confirmPassword:
                        uid.password =newPassword
                        uid.save()
                        return redirect('logout')
                    else:
                        return redirect('logout')
                else:
                    return redirect('logout')
            context = {
            'uid': uid,
            'aid': aid,
            }
            return render(request, 'app/profile.html', context)    


def adminProfileChange(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if request.method == 'POST':
            if uid.role =='admin':
                aid=adminn.objects.get(user_id=uid)
                name = request.POST['name']
                shopName = request.POST['shopName']
                contact = request.POST['contact']
                shopAddress = request.POST['shopAddress']
                pattern = re.compile('[-\s]?[6-9]\d{9}')
                if pattern.match(contact):
                    aid = adminn.objects.get(user_id=uid)
                    aid.name = name
                    aid.shopName = shopName
                    aid.contact = contact
                    aid.shopAddress = shopAddress
                    aid.save()
                    return redirect('profile')

                else:
                    aid = adminn.objects.get(user_id=uid)
                    msg = 'Invalid mobile number'
                    context = {
                        'uid': uid,
                        'aid': aid,
                        'msg': msg,
                    }
                    return render(request, 'app\profile.html', context)

                return redirect('profile')

def adminPicChange(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if request.POST:
            if uid.role=='admin':
                aid=adminn.objects.get(user_id=uid)
                if 'pic' in request.FILES:
                    pic=request.FILES['pic']
                    aid.pic = pic
                    aid.save()

                    return redirect('profile')
    else:
        return redirect('login')                    


def addProduct(request):
    if 'email' in request.session:
        uid=User.objects.get(email = request.session['email'] )
        aid=adminn.objects.get(user_id=uid)
        if request.POST:
            brand = request.POST['brand']
            productName= request.POST['productName']
            ram=request.POST['ram']
            screenSize =request.POST['screenSize']
            batteryCapacity=request.POST['batteryCapacity']
            cpu=request.POST['cpu']
            price=request.POST['price']
            sim=request.POST['sim']
            
            if 'pic' in request.FILES:
                pid=product.objects.create(
                    user_id = uid,
                    productName=productName,
                    brand=brand,
                    price=price,
                    ram=ram,
                    screenSize=screenSize,
                    batteryCapacity=batteryCapacity,
                    CPU=cpu,
                    sim=sim,
                    pic=request.FILES['pic']
                )
            else:
                pid=product.objects.create(
                    user_id = uid,
                    productName=productName,
                    brand=brand,
                    price=price,
                    ram=ram,
                    screenSize=screenSize,
                    batteryCapacity=batteryCapacity,
                    CPU=cpu,
                    sim=sim
                )
            return redirect('allProduct')
        else:        
            context={
                    'uid':uid,
                    'aid':aid, 
                }
            return render(request,'addProduct.html',context)
    return redirect('login')
             


def allProduct(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=='admin':
            aid=adminn.objects.get(user_id=uid)
            pall=product.objects.filter(user_id=uid)

            context={
                'uid':uid,
                'aid':aid,
                'pall':pall
            }

            return render(request,'allproduct.html',context)

    else:
        return redirect('login') 


def searchProduct(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role =='admin':
            aid=adminn.objects.get(user_id=uid)
            category_id_search=request.POST['category_id_search']
            pall=product.objects.filter(user_id = uid, brand=category_id_search)

            context={
                'uid':uid,
                'aid':aid,
                'pall':pall,
            }
            return render(request,'allProduct.html',context)


def editProduct(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        pid = product.objects.get(id=pk)
        aid=adminn.objects.get(user_id=uid)
        pall=product.objects.filter(user_id=uid)
        context = {
            'uid': uid,
            'aid': aid,
            'pid': pid,
            'pall': pall,
        }
        return render(request, 'editProduct.html', context)
    else:
        return redirect('login')

def updateProduct(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role=='admin':
            aid=adminn.objects.get(user_id=uid)
            pall=product.objects.filter(user_id=uid)

            if request.POST:
                if 'category_id' in request.POST:
                    pid = product.objects.get(id=request.POST['id'])
                    category_name = request.POST['category_id']
                    pid.productName = request.POST['productName']
                    pid.price = request.POST['price']
                    pid.ram = request.POST['ram']
                    pid.screenSize = request.POST['screenSize']
                    pid.batteryCapacity = request.POST['batteryCapacity']
                    pid.CPU = request.POST['CPU']
                    pid.sim = request.POST['sim']

                if 'pic' in request.FILES:
                    pid.pic = request.FILES['pic']

                pid.save()
                context = {
                'uid': uid,
                'aid': aid,
                'pall': pall,
            }
            return render(request, 'allProduct.html', context)



def deleteProduct(request,pk):
    if 'email' in request.session:
        pid=product.objects.get(id=pk)
        pid.delete()
        return redirect('allProduct')
    else:
        return redirect('login')    



















