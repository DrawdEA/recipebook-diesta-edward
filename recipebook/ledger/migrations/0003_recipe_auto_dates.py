from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ledger", "0002_profile_and_recipe_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
