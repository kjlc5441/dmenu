from django.db import models
from user.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField('顯示區位', max_length=10)
    name=models.TextField('產品名稱', null=True)
    plu=models.TextField('POS編碼', null=True)
    content = models.TextField('圖片名稱')
    price = models.DecimalField('價格', max_digits=7, decimal_places=0,default=0)
    saleout = models.BooleanField('是否售完', null=True,default=False)
    created_time = models.DateTimeField('創建时間', auto_now_add=True)
    updated_time = models.DateTimeField('更新时間', auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_active = models.BooleanField('是否活躍', default=True)

    # 增加類方法 ：for查詢,列印時可看到明細
    def __str__(self):
        return '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' % (self.id,self.title,self.name,self.plu, self.content, self.price, self.saleout, self.created_time, self.updated_time,self.is_active)

class NoteB(models.Model):
    title = models.CharField('顯示區位', max_length=10)
    name=models.TextField('產品名稱', null=True)
    plu=models.TextField('POS編碼', null=True)
    content = models.TextField('圖片名稱')
    price = models.DecimalField('價格', max_digits=7, decimal_places=0,default=0)
    saleout = models.BooleanField('是否售完', null=True,default=False)
    created_time = models.DateTimeField('創建时間', auto_now_add=True)
    updated_time = models.DateTimeField('更新时間', auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_active = models.BooleanField('是否活躍', default=True)

    # 增加類方法 ：for查詢,列印時可看到明細
    def __str__(self):
      return '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' % (self.id,self.title,self.name,self.plu, self.content, self.price, self.saleout, self.created_time, self.updated_time,self.is_active)

class NoteC(models.Model):
    title = models.CharField('顯示區位', max_length=10)
    name=models.TextField('產品名稱', null=True)
    plu=models.TextField('POS編碼', null=True)
    content = models.TextField('圖片名稱')
    price = models.DecimalField('價格', max_digits=7, decimal_places=0,default=0)
    saleout = models.BooleanField('是否售完', null=True,default=False)
    created_time = models.DateTimeField('創建时間', auto_now_add=True)
    updated_time = models.DateTimeField('更新时間', auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_active = models.BooleanField('是否活躍', default=True)

    # 增加類方法 ：for查詢,列印時可看到明細
    def __str__(self):
       return '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' % (self.id,self.title,self.name,self.plu, self.content, self.price, self.saleout, self.created_time, self.updated_time,self.is_active)


class Store(models.Model):
    store_name=models.TextField('店名', null=True)
    store_tel=models.TextField('電話', null=True)
    store_pre1=models.TextField('電話', null=True)

    def __str__(self):
        return '%s|%s|%s' % (self.store_name,self.store_tel,self.store_pre1)
