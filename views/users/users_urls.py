from __future__ import unicode_literals
from .users_views import (
    RegisterHandle,
    LoginHandle,
)

urls = [
    (r'register', RegisterHandle),
    (r'login', LoginHandle)
]
