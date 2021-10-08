from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        self.category=Category(category_name='Travel')
        self.category.save_category()

    def test_instance(self):
            self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0) 

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)

class LocationTestCase(TestCase):
    def setUp(self):
        self.location=Location(location_name='Bomet')
        self.location.save_location()
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))


    def test_save_location(self):
        self.location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        category = Location.objects.all()
        self.assertTrue(len(category) == 0)
    
    
    def test_get_location(self):
        location = Location.get_locations()
        self.assertTrue(location)


class ImageTestcase(TestCase):
    def setUp(self):

        self.category=Category(category_name='Beach')
        self.category.save_category()

        self.location = Location(location_name='Bomet')
        self.location.save_location()

        self.beach= Image(id=1,image_name = 'Beaches', description ='Beaches Test',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.beach,Image))


    def test_save_image(self):
        self.beach.save_image()
        img = Image.objects.all()
        self.assertTrue(len(img) > 0)

    def test_delete_image(self):
        self.beach.delete_image()
        image= Image.objects.all()
        self.assertTrue(len(image)== 0)
    
    def test_update_image(self):
        self.beach.save_image()
        # self.beach.update_image(self.beach.id, 'images/img.jpg')
        # new_image = Image.objects.filter(image='images/img1.jpg')
        # self.assertFalse(len(new_image) > 0)

    def test_get_image_by_id(self):
        self.beach.save_image()
        img = self.beach.get_image_by_id(self.beach.id)
        images = Image.objects.filter(id=self.beach.id)
        self.assertTrue(img, images)


    def test_search_category(self):
        category = 'Travel'
        found_img = self.beach.search_category(category)
        self.assertFalse(len(found_img) > 1)  
    
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()  