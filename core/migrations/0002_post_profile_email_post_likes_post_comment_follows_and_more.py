# Generated by Django 4.2 on 2023-04-18 14:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("content", models.TextField(max_length=300)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 4, 18, 17, 22, 27, 271154)
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.CreateModel(
            name="Post_Likes",
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
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.post"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post_Comment",
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
                ("content", models.TextField(max_length=300)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 4, 18, 17, 22, 27, 272154)
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.post"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Follows",
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
                (
                    "follower_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follower_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "leader_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leader_id",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment_Likes",
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
                (
                    "comment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.post"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment_Comment",
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
                ("content", models.TextField(max_length=300)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 4, 18, 17, 22, 27, 272154)
                    ),
                ),
                (
                    "comment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.post_comment",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="post_likes",
            constraint=models.UniqueConstraint(
                fields=("user_id", "post_id"), name="UQ_Core_Post_Likes_user_id_post_id"
            ),
        ),
        migrations.AddConstraint(
            model_name="follows",
            constraint=models.UniqueConstraint(
                fields=("follower_id", "leader_id"),
                name="UQ_Core_Follows_follower_id_leader_id",
            ),
        ),
        migrations.AddConstraint(
            model_name="comment_likes",
            constraint=models.UniqueConstraint(
                fields=("user_id", "comment_id"),
                name="UQ_Core_Comment_Likes_user_id_comment_id",
            ),
        ),
        migrations.AddConstraint(
            model_name="comment_comment",
            constraint=models.UniqueConstraint(
                fields=("user_id", "comment_id"),
                name="UQ_Core_Comment_Comment_user_id_comment_id",
            ),
        ),
    ]