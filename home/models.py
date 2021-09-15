from django.db import models
from django.contrib import admin


class Sneaker(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    @admin.display(
        boolean=True,
        description='Sold out?'
    )
    def sold_out(self):
        sizes = self.sneakersize_set.all()
        if sizes:
            return False
        return True

    @admin.display(
        description='Available pieces',
    )
    def available_pieces(self):
        sizes = self.sneakersize_set.all()
        pieces = 0
        for piece in sizes:
            pieces += 1
        return pieces

    @property
    def lunghezzanome(self):
        return len(self.name)


    @property
    def get_first_img(self):
        images = self.sneakerimage_set.all()
        list_urls = []
        for url in images:
            list_urls.append(url)
        if len(list_urls):
            return list_urls[0].image
        else:
            result = '/static/images/placeholder.png'
        return result


class SneakerImage(models.Model):
    sneaker = models.ForeignKey(Sneaker,
                                on_delete=models.CASCADE)
    image = models.URLField(max_length=300, blank=True, null=True)


class SneakerSize(models.Model):
    sneaker = models.ForeignKey(Sneaker,
                                on_delete=models.CASCADE)
    size_number = models.CharField(null=True, max_length=8)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return str(self.size_number)
