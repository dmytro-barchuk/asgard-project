from django.db import models
from pytils.translit import slugify
from django.core.validators import MinLengthValidator


class Category(models.Model):
	title = models.CharField(max_length=30)
	slug = models.SlugField(max_length=30, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.title
	# Делаем уникальный SLUG
	def save(self, *args, **kwargs):
		if self.slug == None:
			slug = slugify(self.title)
			has_slug = Category.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.title) + '-' + str(count) 
				has_slug = Category.objects.filter(slug=slug).exists()
			self.slug = slug
		super(Category, self).save(*args, **kwargs)

class Service(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	service_name = models.CharField(max_length=100)
	image = models.ImageField(null=True, blank=True, upload_to="%Y/%M/")
	body = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	slug = models.SlugField(max_length=100, null = True, blank=True, verbose_name ="Slug (не заповнювати): ")

	def __str__(self):
		return self.service_name

	# Делаем уникальный SLUG
	def save(self, *args, **kwargs):
		if self.slug == None:
			slug = slugify(self.service_name)
			has_slug = Service.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.service_name) + '-' + str(count) 
				has_slug = Service.objects.filter(slug=slug).exists()
			self.slug = slug
		super(Service, self).save(*args, **kwargs)

class Comment(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254, blank=True)
	comment_text = models.TextField(
		validators=[MinLengthValidator(2, message="Не меньше 2 символов")]
	)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

