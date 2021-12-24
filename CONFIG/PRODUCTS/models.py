from django.db import models



class ProductCategorieModel(models.Model):
    categorieTitle = models.CharField(max_length=50,verbose_name="Kategori İsmi")
    def __str__(self):
        return self.categorieTitle

class ProductModel(models.Model):
    productTitle = models.CharField(max_length=50, verbose_name="Ürün İsmi")
    productPrice = models.FloatField(verbose_name="Ürün Fiyatı")
    productDescription = models.TextField(max_length=500, verbose_name="Ürün Açıklaması")
    productImage = models.ImageField(verbose_name="Ürün Görseli", upload_to="products/",blank=True,null=True)
    productShipping = models.BooleanField(default=False,verbose_name="Ücretsiz Kargo Mu",blank=False,null=False)
    productCategorie = models.ManyToManyField(ProductCategorieModel,verbose_name="Kategori")
    def __str__(self):
        return self.productTitle

class ProductCommentsModel(models.Model):
    customer    = models.ForeignKey("USERAPP.CustomUserModel",verbose_name="Müşteri İsmi",on_delete=models.CASCADE,default="")
    createdDate  = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    product      = models.ForeignKey(ProductModel,verbose_name="Ürün adı",on_delete=models.CASCADE)
    commentText  = models.TextField(max_length=250,verbose_name="Yorum",default=None)

    def __str__(self):
        return self.commentText











# class ShippingAddress(models.Model):
#    customer = models.ForeignKey(CustomerModel,on_delete=models.SET_NULL,verbose_name="Müşteri")
#    order    = models.ForeignKey(OrderModel,on_delete=models.SET_NULL,null=True)
#    address  =
