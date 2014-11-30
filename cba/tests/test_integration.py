"""
User stories of the admin system.

'As an admin, I want to...'
"""
from unittest import expectedFailure

from django.contrib.messages import get_messages
from django.core.urlresolvers import reverse
from django.test import TestCase

from .factories import PersonFactory
from .models import Person


class AdminMainIndexTest(TestCase):
    @expectedFailure
    def test_index(self):
        """See a list of managed apps so I can find my content."""
        # GET the main admin index
        url = reverse('cba:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Ensure there is a link to the app index
        app_index_url = reverse('cba:tests:index')
        self.assertContains(response, app_index_url)

        # Ensure there is a link to the model list
        model_list_url = reverse('cba:tests:person_list')
        self.assertContains(response, model_list_url)


class AdminAppIndexTest(TestCase):
    @expectedFailure
    def test_app_index(self):
        """See the list of models in an app so I can find content in the app."""
        # GET the inxex of the app
        url = reverse('cba:tests:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # There should be a link back to main index
        app_index_url = reverse('cba:index')
        self.assertContains(response, app_index_url)

        # Ensure there is a link to the model list
        model_list_url = reverse('cba:tests:person_list')
        self.assertContains(response, model_list_url)


class AdminModelListTest(TestCase):
    @expectedFailure
    def test_object_list(self):
        """See a list of instances of a model so I can find the one I need."""
        # Get a model list
        url = reverse('cba:tests:person_list')
        instance = PersonFactory.create()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # The str representation of the object should be visible
        self.assertContains(response, str(instance))

        # There should be a link to the object on the site
        self.assertContains(response, instance.get_absolute_url())

        # There should be a link to the update view
        update_url = reverse('cba:tests:person_update', kwargs={'pk': instance.pk})
        self.assertContains(response, update_url)

        # Link to delete
        delete_url = reverse('cba:tests:person_delete', kwargs={'pk': instance.pk})
        self.assertContains(response, delete_url)


class AdminModelCreateTest(TestCase):
    @expectedFailure
    def test_create(self):
        """Create new instances of a model so that there is new content."""
        # GET a create view
        url = reverse('cba:tests:person_create')
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)

        # Ensure there is a form on the page
        # TODO: This could be a better test of the form
        expected = '<form action="{}" method="POST">'.format(url)
        self.assertContains(response_get, expected, html=True)

        # POST the form
        data = {'name': 'Homer Simpson'}
        response_post = self.client.post(url, data=data)

        # Ensure redirected as expected
        self.assertEqual(response_post.status_code, 302)
        self.assertEqual(response_post['Location'], url)

        # Ensure object modified as expected
        instance = Person.objects.get()
        self.assertEqual(instance.name, data['name'])

        # Ensure "created" message visible to user
        messages = get_messages(response_post.request)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0], 'Person created.')


class AdminModelUpdateTest(TestCase):
    @expectedFailure
    def test_update(self):
        """Update instances of a model so that it is up to date."""
        # To update, we need an existing instance
        instance = PersonFactory.create(name='Homer Simpson')
        # Get the update page for it
        url = reverse('cba:tests:person_update', kwargs={'pk': instance.pk})
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)

        # Ensure the form is on the page
        # TODO: This could be a better test of the form
        expected = '<form action="{}" method="POST">'.format(url)
        self.assertContains(response_get, expected, html=True)

        # We POST the form with new data
        data = {'name': 'Max Power'}
        response_post = self.client.post(url, data=data)

        # Ensure we have been redirected as expected
        self.assertEqual(response_post.status_code, 302)
        self.assertEqual(response_post['Location'], url)

        # Ensure the object was  modified correctly
        instance = Person.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, data['name'])

        # Ensure an "updated" message is displayed to the user
        messages = get_messages(response_post.request)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0], 'Person updated.')


class AdminModelDeleteTest(TestCase):
    @expectedFailure
    def test_delete(self):
        """Delete instances of a model to clear away useless data."""
        # To delete, we need an existing instance
        instance = PersonFactory.create()
        # Get the delete page for it
        url = reverse('cba:tests:person_delete', kwargs={'pk': instance.pk})
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)

        # TODO: Show list of related models that will also be deleted
        # (Will this need to be validated?)

        # Ensure form is on page
        # TODO: This could be a better test of the form
        expected = '<form action="{}" method="POST">'.format(url)
        self.assertContains(response_get, expected, html=True)

        # POST the form to confirm the delete
        response_post = self.client.post(url)

        # Ensure redirect is correct
        self.assertEqual(response_post.status_code, 302)
        expected = reverse('cba:tests:person_list')
        self.assertEqual(response_post['Location'], expected)

        # Ensure object has gone
        self.assertFalse(Person.objects.exists())

        # Ensure "deleted" message visible to user
        messages = get_messages(response_post.request)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0], 'Person deleted.')
