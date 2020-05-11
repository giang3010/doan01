from django.db import models

# Create your models here.
class KhachHang(models.Model):
    Username = models.CharField(max_length= 10, primary_key=True)
    Email = models.CharField(max_length= 100)
    Password = models.CharField(max_length= 100)
    Ho = models.CharField(max_length= 100)
    Ten = models.CharField(max_length= 100)
    GioiTinh = models.CharField(max_length= 100)
    QuyenDangNhap = models.BooleanField(default= True)
    def __str__(self):
        return self.Username

