from django.db import models
from pytils.translit import slugify


class News(models.Model):
	news_title = models.CharField(verbose_name = "Заголовок:", max_length=100)
	image = models.ImageField(verbose_name = "Фото:", null=True, blank=True, upload_to="news/%Y/%M/")
	body = models.TextField(verbose_name ="Текст новости:", null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	slug = models.SlugField(max_length=100, null = True, blank=True, verbose_name ="Slug (не заповнювати): ")

	def __str__(self):
		return self.news_title

	# Делаем уникальный SLUG
	def save(self, *args, **kwargs):
		if self.slug == None:
			slug = slugify(self.news_title)
			has_slug = News.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.news_title) + '-' + str(count) 
				has_slug = News.objects.filter(slug=slug).exists()
			self.slug = slug
		super(News, self).save(*args, **kwargs)