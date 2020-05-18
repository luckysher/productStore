from django.db import models
from datetime import timedelta
from django.core.validators import MinLengthValidator, MaxLengthValidator


class News(models.Model):
    # news Id
    news_id = models.AutoField(db_column='id', primary_key=True)

    # Description of the news
    description = models.CharField(verbose_name='news',  max_length=100, help_text= "Latest News", unique="True",
                                   validators=[MinLengthValidator(limit_value=10, message="News description should be atleast 10 chars"),
                                               MaxLengthValidator(limit_value=100, message="News description can not be > 100 chars")])
    # date of the news
    arrival_date = models.DateField(auto_now_add=True)

    expired = models.BooleanField(db_column='News Expired', default=False, help_text="Has this news expired")

    # The news will expire after this date
    expire_date = models.DateField()

    def _is_news_expired(self):
        return self.expired or self.arrival_date > self.expire_date

    def _get_expiration_date(self):
        if self.expire_date:
            return self.expire_date
        return self.arrival_date + timedelta(7)

    def __str__(self):
        return """News(id={id}, description={description}, date={date}, expire_date={expire_date})""".format(id=self.id,
                                                                                                                 description=self.description,
                                                                                                                 date=self.arrival_date,
                                                                                                                 expire_date=self.expire_date)

    class meta:
        db_table = 'news'


class Product(models.Model):

    Percent = 'PR'
    Amount = 'Amt'

    DISCOUNT_TYPE_CHOICE = [
        (Percent, 'Percent'),
        (Amount, 'Amount')
    ]

    id = models.AutoField(db_column='product_id', primary_key=True)
    name = models.CharField(max_length=50, null=False,
                            verbose_name='product Name',
                            help_text="Name of the product")
    details = models.CharField(max_length=50, null=False,
                               verbose_name='Product Detail',
                               help_text="Details of the product")
    cost = models.FloatField(verbose_name="Product Cost", blank=False,
                               help_text="Product cost per unit",
                               unique=False)
    discount_type = models.CharField(max_length=3,
                                     choices=DISCOUNT_TYPE_CHOICE,
                                     verbose_name='Discount Type',
                                     help_text="Discount on this product e.g Amount, Percent")

    discount = models.FloatField(verbose_name="Discount Price", default=0.0,
                                   help_text="Discount of for the product in amount",
                                   unique=False)
    percent = models.FloatField(verbose_name="Discount Percent", default=0.0,
                                  help_text="Discount of for the product in percent",
                                  unique=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return """Product(id={id}, name={name}, details={details}, cost={cost}, discount_amount={discount}, 
        discount_type={discount_type}, discount_percent={discount_percent})""".format(
            id=self.id,
            details=self.details,
            cost=self.cost,
            name=self.name,
            discount=self.discount,
            discount_type=self.discount_type,
            discount_percent=self.percent)

    class meta:
        db_table = 'product'