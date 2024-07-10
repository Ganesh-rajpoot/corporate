from django.test import TestCase
from .models import *
from django.utils import timezone
# Create your tests here.
class JobModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Job.objects.create(
            title='Senior Developer',
            description='Seeking experienced Django developers',
            company_name='Tech Solutions',
            location='New York',
            salary=90000.00,
        )

    def test_job_title(self):
        job = Job.objects.get(id=1)
        expected_object_name = f'{job.title}'
        self.assertEqual(expected_object_name, 'Senior Developer')

    def test_job_company_name(self):
        job = Job.objects.get(id=1)
        expected_object_name = f'{job.company_name}'
        self.assertEqual(expected_object_name, 'Tech Solutions')

    def test_job_salary(self):
        job = Job.objects.get(id=1)
        expected_salary = job.salary
        self.assertEqual(expected_salary, 90000.00)

    # Add more test cases as needed
class BlogPostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BlogPost.objects.create(
            title='First Blog Post',
            content='This is the content of the first blog post.',
        )

    def test_title_content(self):
        blog_post = BlogPost.objects.get(id=1)
        expected_object_name = f'{blog_post.title}'
        self.assertEqual(expected_object_name, 'First Blog Post')

    def test_content(self):
        blog_post = BlogPost.objects.get(id=1)
        expected_object_name = f'{blog_post.content}'
        self.assertEqual(expected_object_name, 'This is the content of the first blog post.')

    def test_created_at(self):
        blog_post = BlogPost.objects.get(id=1)
        self.assertTrue(blog_post.created_at <= timezone.now())

    def test_updated_at(self):
        blog_post = BlogPost.objects.get(id=1)
        initial_updated_at = blog_post.updated_at
        blog_post.title = 'Updated Title'
        blog_post.save()
        self.assertTrue(blog_post.updated_at > initial_updated_at)

    # Add more test cases as needed

