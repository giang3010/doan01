from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Quanly(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError("Tài khoản phải có email")
        if not username:
            raise ValueError("Tài khoản phải có tên đăng nhập")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(user=self._db)
        return user

    def create_superuser(self,email,username , password,first_name,last_name):
        user = self.models(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Taikhoan(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=100, unique= True)
    username = models.CharField(max_length= 50, unique= True)
    ngaytao = models.DateTimeField(verbose_name='ngaytao', auto_now_add= True)
    dangnhaplancuoi = models.DateTimeField(verbose_name='dangnhaplancuoi', auto_now= True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    object = Quanly()

    def __str__(self):
        return self.email + ", " + self.username

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True