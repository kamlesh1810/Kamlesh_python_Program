from django.db import models

# Create your models here.

class User(models.Model):
    email=models.EmailField(unique=True,max_length=30)
    password=models.CharField(max_length=30)
    role=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.email 

class adminn(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)        
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)    
    shopName=models.CharField(max_length=30)
    shopAddress=models.CharField(max_length=30)
    pic =models.FileField(upload_to='media/images',default='media/myPic.png')

    def __str__(self) -> str:   
        return self.name

# class category(models.Model):
#     brand_name=models.CharField(max_length=20)        

#     def __str__(self) -> str:
#         return self.brand_name

class product(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # category_id=models.ForeignKey(category,on_delete=models.CASCADE)
    productName=models.CharField(max_length=30)
    brand=models.CharField(max_length=100)
    price=models.CharField(max_length=20)   
    ram=models.CharField(max_length=30)
    screenSize=models.CharField(max_length=20)
    batteryCapacity=models.CharField(max_length=30)
    CPU=models.CharField(max_length=30)
    sim=models.CharField(max_length=30)
    pic =models.FileField(upload_to='media/images', default='media/mobile.png   ', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.productName
