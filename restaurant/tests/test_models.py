from django.test import TestCase
from restaurant.models import Branch, BranchItem, Category, Customer, Employee, Item, Order, OrderItem, Receipt, Reservation, Table, User
from restaurant.models import create_customer_profile, create_employee_profile
import os

class TestModels(TestCase):

	def test_create_customer_profile(self):
		if os.getenv("hideAmnesties") == 'yes':
			return;
		self.assertEquals(User.objects.count(), 0)
		user = User.objects.create_user("username", "test@test.com", "password");
		create_customer_profile(user, created=True, instance=user);