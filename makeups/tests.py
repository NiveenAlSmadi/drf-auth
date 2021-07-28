from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import product

# Create your tests here.
class makeupsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='Maybelline', password='password')
        test_user.save()

        test_makeups = product.objects.create(
            brand = test_user,
            name = 'Maybelline Dream Bouncy Blush',
            description = 'New bouncy texture is formulated with silicone elastomers• Lightweight like a powder, yet melts seamlessly into skin like a cream giving you a fresh flush• Dermatologist tested• Allergy tested• Non-comedogenic',
            price=15,
            rating=5,
        )
        test_makeups.save()

    def test_makeup_content(self):
        products = product.objects.get(id=1)
        actual_brand = str(products.brand)
        actual_name = str(products.name)
        actual_description = str(products.description)
        actual_price = str(products.price)
        actual_rating = str(products.rating)
        self.assertEqual(actual_brand, 'Maybelline')
        self.assertEqual( actual_name, 'Maybelline Dream Bouncy Blush')
        self.assertEqual(actual_description, 'New bouncy texture is formulated with silicone elastomers• Lightweight like a powder, yet melts seamlessly into skin like a cream giving you a fresh flush• Dermatologist tested• Allergy tested• Non-comedogenic')
        self.assertEqual( actual_price, '15')
        self.assertEqual( actual_rating, '5')