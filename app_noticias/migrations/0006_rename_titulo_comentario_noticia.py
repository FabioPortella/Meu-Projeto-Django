# Generated by Django 4.2 on 2023-06-09 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0005_rename_data_publicacao_noticia_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='titulo',
            new_name='noticia',
        ),
    ]