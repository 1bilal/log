import django.db.models.deletion
from django.db import migrations, models


def create_default_category(apps, schema_editor):
    Category = apps.get_model("blog", "Category")
    default_category = Category.objects.create(name="Uncategorized")

    Article = apps.get_model("blog", "Article")
    for article in Article.objects.filter(category__isnull=True):
        article.category = default_category
        article.save()


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="articles",
                to="blog.category",
            ),
        ),
        migrations.RunPython(create_default_category),
    ]
