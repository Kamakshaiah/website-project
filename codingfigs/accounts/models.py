
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, phone, image, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            firstname = firstname, 
            lastname = lastname,
            email=self.normalize_email(email),
            phone=phone,
            image=image
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, email, phone, image, password=None):
        """
        Creates and saves a superuser with the given email, phone and password.
        """
        user = self.create_user(
            firstname = firstname, 
            lastname = lastname,
            email=email,
            password=password,
            phone=phone,
            image=image
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = PhoneNumberField()
    image = models.ImageField(blank=True, null=True, upload_to='profile_images/', default='default.jpg')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phone', 'image']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def profile_name(self):
        return f'{self.firstname}, {self.lastname[0]}' 

    # @property
    # def imageURL(self):
    #     if self.image:
    #         return self.image.url
    #     else:
    #         return 'default.jpg'