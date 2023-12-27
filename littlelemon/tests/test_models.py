from django.test import TestCase
from django.utils import timezone
from .models import Booking, Menu


class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            name="Test Booking", no_of_guests=5, booking_date=timezone.now()
        )
        self.assertEqual(booking.name, "Test Booking")
        self.assertEqual(booking.no_of_guests, 5)
        self.assertIsNotNone(booking.booking_date)


class MenuModelTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(title="Test Menu", price=9.99, inventory=10)
        self.assertEqual(menu.title, "Test Menu")
        self.assertEqual(menu.price, 9.99)
        self.assertEqual(menu.inventory, 10)

    def test_menu_str_method(self):
        menu = Menu.objects.create(title="Test Menu", price=9.99, inventory=10)
        self.assertEqual(str(menu), "Test Menu : 9.99")
