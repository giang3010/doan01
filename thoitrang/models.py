from django.db import models

# Create your models here.
class NHOM_SP(models.Model):
    MaNhom = models.CharField(max_length= 10, primary_key=True)
    TenNhom = models.CharField(max_length= 100)
    Hinhanh = models.ImageField()

    def __str__(self):
        return self.MaNhom

class DANHMUC_SP(models.Model):
    MaDM = models.CharField(max_length= 10, primary_key=True)
    TenDM = models.CharField(max_length= 100)
    MaNhom = models.ForeignKey(NHOM_SP, on_delete=models.CASCADE)

    def __str__(self):
        return self.MaDM

class SANPHAM(models.Model):
    MASP= models.CharField(max_length= 10, primary_key=True)
    TenSP = models.CharField(max_length= 100)
    Mota = models.TextField()
    Thuonghieu = models.CharField(max_length= 50)
    GiaBan = models.FloatField()
    Soluong = models.IntegerField()
    Hinhanh = models.ImageField()
    Kichco = models.CharField(max_length= 5)
    Mausac = models.CharField(max_length= 50)
    Hdsd = models.TextField()

    def __str__(self):
        return self.MASP





