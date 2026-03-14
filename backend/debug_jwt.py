
import os
import django
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biteroute_backend.settings')
django.setup()

import jwt
import datetime
from core.auth_utils import generate_token

try:
    print("Checking settings.SECRET_KEY...")
    print(f"SECRET_KEY length: {len(settings.SECRET_KEY)}")
    
    print("Testing jwt.encode directly...")
    payload = {
        "user_id": 999,
        "role": "admin",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
        "iat": datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    print(f"Direct JWT encode successful: {token[:20]}...")

    print("Testing generate_token function...")
    token = generate_token(999, "admin")
    print(f"generate_token successful: {token[:20]}...")

except Exception as e:
    import traceback
    print("❌ EXCEPTION CAUGHT:")
    traceback.print_exc()
