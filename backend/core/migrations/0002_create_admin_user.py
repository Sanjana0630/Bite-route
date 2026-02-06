from django.db import migrations


def create_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    if not User.objects.filter(username='admin').exists():
        user = User.objects.create(
            username='admin',
            email='admin@example.com',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('Admin@123')
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]