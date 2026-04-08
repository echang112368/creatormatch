from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountsFlowTests(TestCase):
    def test_signup_creates_user_and_logs_them_in(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "MyStrongPass123!",
                "password2": "MyStrongPass123!",
            },
        )

        self.assertRedirects(response, reverse("landing"), fetch_redirect_response=False)
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertIn("_auth_user_id", self.client.session)

    def test_landing_and_auth_routes_are_wired(self):
        self.assertEqual(reverse("landing"), "/")
        self.assertEqual(reverse("signup"), "/accounts/signup/")
        self.assertEqual(reverse("login"), "/accounts/login/")
        self.assertEqual(reverse("logout"), "/accounts/logout/")
