import os
import django
import sys
from collections import Counter

# Setup Django environment
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biteroute_backend.settings')
django.setup()

from core.models import User, HotelOwner

def check_duplicates():
    print("Checking for duplicate contacts in User model...")
    users = User.objects.all()
    user_contacts = [u.contact.lower() for u in users]
    user_counts = Counter(user_contacts)
    
    found_duplicates = False
    for contact, count in user_counts.items():
        if count > 1:
            print(f"❌ Duplicate User contact found: '{contact}' (Count: {count})")
            found_duplicates = True
            
    if not found_duplicates:
        print("✅ No duplicate User contacts found.")

    print("\nChecking for duplicate contacts in HotelOwner model...")
    owners = HotelOwner.objects.all()
    owner_contacts = [o.contact.lower() for o in owners]
    owner_counts = Counter(owner_contacts)
    
    found_duplicates = False
    for contact, count in owner_counts.items():
        if count > 1:
            print(f"❌ Duplicate HotelOwner contact found: '{contact}' (Count: {count})")
            found_duplicates = True

    if not found_duplicates:
        print("✅ No duplicate HotelOwner contacts found.")

if __name__ == "__main__":
    try:
        check_duplicates()
    except Exception as e:
        print(f"An error occurred: {e}")
