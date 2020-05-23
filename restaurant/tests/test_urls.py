from django.test import SimpleTestCase
from django.urls import reverse, resolve
from restaurant.views import index, addItemView, addCategoryView, addBranchView, addTableView, dashboardView, registerView, profile, edit_profile, change_password
from django.contrib.auth.views import LoginView, LogoutView

class TestUrls(SimpleTestCase):

	def test_index_url(self):
		url = reverse('index')
		self.assertEquals('/', url);
		self.assertEquals(resolve(url).func, index)

	def test_addItem_url(self):
		url = reverse('addItem')
		self.assertEquals('/addItem', url);
		self.assertEquals(resolve(url).func.view_class, addItemView)

	def test_addCategory_url(self):
		url = reverse('addCategory')
		self.assertEquals('/addCategory', url);
		self.assertEquals(resolve(url).func.view_class, addCategoryView)

	def test_addBranch_url(self):
		url = reverse('addBranch')
		self.assertEquals('/addBranch', url);
		self.assertEquals(resolve(url).func.view_class, addBranchView)

	def test_dashboard_url(self):
		url = reverse('dashboard')
		self.assertEquals('/dashboard/', url);
		self.assertEquals(resolve(url).func, dashboardView)

	def test_login_url_url(self):
		url = reverse('login_url')
		self.assertEquals('/login/', url);
		self.assertEquals(resolve(url).func.view_class, LoginView)

	def test_logout_url_url(self):
		url = reverse('logout_url')
		self.assertEquals('/logout/', url);
		self.assertEquals(resolve(url).func.view_class, LogoutView)

	def test_register_url_url(self):
		url = reverse('register_url')
		self.assertEquals('/register/', url);
		self.assertEquals(resolve(url).func, registerView)

	def test_profile_url(self):
		url = reverse('profile')
		self.assertEquals('/profile/', url);
		self.assertEquals(resolve(url).func, profile)

	def test_edit_profile_url(self):
		url = reverse('edit_profile')
		self.assertEquals('/profile/edit/', url);
		self.assertEquals(resolve(url).func, edit_profile)

	def test_change_password_url(self):
		url = reverse('change_password')
		self.assertEquals('/change_password/', url);
		self.assertEquals(resolve(url).func, change_password)

	