from django.db import models



class ProductMainModel(models.Model):

    size_choices = (
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
    )
    quality_choices = (
        ('High', 'high'),
        ('Medium', 'medium'),
        ('Low', 'low'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    unique_code = models.CharField(max_length=10, unique=True)
    size = models.CharField(max_length=10, choices=size_choices)
    quality = models.CharField(max_length=20, choices=quality_choices)

    def colors(self):
        if not hasattr(self, '_colors'):
            self._colors = self.productcolourmodel_set.all()
        return self._colors

    def images(self):
        if not hasattr(self, '_images'):
            self._images = self.productimagemodel_set.all()
        return self._images

    def __str__(self) -> str:
        return self.title


class ProductColourModel(models.Model):
    color_choices = (
        ('Red', 'red'),
        ('Blue', 'blue'),
        ('Green', 'green'),
        ('Black', 'black'),
    )

    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, choices=color_choices)


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_img/')