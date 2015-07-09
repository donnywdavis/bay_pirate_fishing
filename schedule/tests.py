import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Event

def create_event(name, location, days_to_event):
    start_date = timezone.now() + datetime.timedelta(days=days_to_event)
    end_date = timezone.now() + datetime.timedelta(days=(days_to_event + 2))
    return Event.objects.create(name=name, location=location, start_date=start_date, end_date=end_date)

class ScheduleTests(TestCase):
    def test_home_page_with_no_events(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events")

    def test_home_page_with_event(self):
        create_event('Event 1', 'This location', 2)
        events = Event.objects.filter(end_date__gte=datetime.date.today())[:3]
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['events'],
            ['<Event: Event 1>']
        )

    def test_schedule_index_with_no_events(self):
        response = self.client.get(reverse('schedule:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events")

    def test_schedule_index_with_events(self):
        create_event('Event 1', 'This location', 2)
        events = Event.objects.all()
        response = self.client.get(reverse('schedule:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['events'],
            ['<Event: Event 1>']
        )
