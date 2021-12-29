from django.test import TestCase
import random,string


x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(20))


# Create your tests here.
