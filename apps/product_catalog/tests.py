from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.text import slugify
from django.test import SimpleTestCase
from django.urls import reverse

from apps.product_catalog.models import Category, Country, Image, Product, ImageAssociation

class CategoryModelTest(TestCase):
    def test_create_category(self):
        # Test the creation of a category
        category = Category.objects.create(name="Test Category")
        self.assertIsNotNone(category)
        self.assertEqual(category.name, "Test Category")

    def test_slug_creation(self):
        # Test that the slug is correctly created based on the name
        category = Category.objects.create(name="Test Category")
        expected_slug = slugify(category.name)
        print(category.slug, expected_slug)
        self.assertEqual(category.slug, expected_slug)

    def test_str_representation(self):
        # Test the string representation of the category
        category = Category.objects.create(name="Test Category")
        self.assertEqual(str(category), "Test Category")

class CountryModelTest(TestCase):
    def test_create_country(self):
        # Test the creation of a country
        country = Country.objects.create(name="Test Country")
        self.assertIsNotNone(country)
        self.assertEqual(country.name, "Test Country")

    def test_str_representation(self):
        # Test the string representation of the country
        country = Country.objects.create(name="Test Country")
        self.assertEqual(str(country), "Test Country")

class ImageModelTest(TestCase):
    def test_create_image(self):
        # Test the creation of an image
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        img_instance = Image.objects.create(image=image)
        self.assertIsNotNone(img_instance)
        self.assertTrue('test_image' in img_instance.image.name and img_instance.image.name.endswith('.jpg'))

    def test_str_representation(self):
        # Test the string representation of the image
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        img_instance = Image.objects.create(image=image)
        self.assertEqual(str(img_instance), img_instance.image.name)

class ProductModelTest(TestCase):
    def test_create_product(self):
        # Create necessary foreign key objects
        category = Category.objects.create(name="Test Category")
        country = Country.objects.create(name="Test Country")

        # Test the creation of a product
        product = Product.objects.create(
            category=category,
            name="Test Product",
            description="This is a test product",
            price=10.00,
            country=country
        )
        self.assertIsNotNone(product)
        self.assertEqual(product.name, "Test Product")

    def test_str_representation(self):
        # Test the string representation of the product
        category = Category.objects.create(name="Test Category")
        country = Country.objects.create(name="Test Country")
        product = Product.objects.create(
            category=category,
            name="Test Product",
            description="This is a test product",
            price=10.00,
            country=country
        )
        self.assertEqual(str(product), f"{category}: {product.name}")

class ImageAssociationModelTest(TestCase):
    def test_create_image_association(self):
        # Create necessary objects
        category = Category.objects.create(name="Test Category")
        country = Country.objects.create(name="Test Country")
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        img_instance = Image.objects.create(image=image)
        product = Product.objects.create(
            category=category,
            name="Test Product",
            description="This is a test product",
            price=10.00,
            country=country
        )
        # Test the creation of an image association
        image_association = ImageAssociation.objects.create(
            product=product,
            image=img_instance
        )
        self.assertIsNotNone(image_association)

    def test_str_representation(self):
        # Test the string representation of the image association
        category = Category.objects.create(name="Test Category")
        country = Country.objects.create(name="Test Country")
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        img_instance = Image.objects.create(image=image)
        product = Product.objects.create(
            category=category,
            name="Test Product",
            description="This is a test product",
            price=10.00,
            country=country
        )
        image_association = ImageAssociation.objects.create(
            product=product,
            image=img_instance
        )
        self.assertEqual(str(image_association), f"{product} - {img_instance}")
