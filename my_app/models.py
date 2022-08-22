
from django.db import models
from django.urls import reverse


class Mebel(models.Model):
	Name = models.CharField(max_length=250,null=False,blank=False,db_index=True)
	Info = models.TextField(max_length=10000,null=False,blank=False,db_index=True)
	Malumot = models.TextField(max_length=10000,null=False,blank=False,db_index=True)
	image = models.ImageField(upload_to="images/",blank=True,db_index=True)
	created_at = models.DateTimeField(auto_now_add=True)
	data_pub = models.DateTimeField(auto_now_add=True)



	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse('product', args=[str(self.id)])


class Comments(models.Model):
	Ism = models.CharField(max_length=250,null=False,blank=False,db_index=True)
	Tel = models.TextField(max_length=10000,null=False,blank=False,db_index=True)
	Pochta = models.TextField(max_length=10000,null=False,blank=False,db_index=True)
	Xabar = models.TextField(max_length=10000,null=False,blank=False,db_index=True)


	def __str__(self):
		return self.Ism





