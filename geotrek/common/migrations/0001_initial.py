# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geotrek.authent.models


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0001_initial'),
        ('cirkwi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=128, verbose_name='File type')),
                ('structure', models.ForeignKey(db_column=b'structure', default=geotrek.authent.models.default_structure, verbose_name='Related structure', to='authent.Structure')),
            ],
            options={
                'ordering': ['type'],
                'abstract': False,
                'db_table': 'fl_b_fichier',
                'verbose_name': 'File type',
                'verbose_name_plural': 'File types',
            },
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organism', models.CharField(max_length=128, verbose_name='Organism', db_column=b'organisme')),
                ('structure', models.ForeignKey(db_column=b'structure', default=geotrek.authent.models.default_structure, verbose_name='Related structure', to='authent.Structure')),
            ],
            options={
                'ordering': ['organism'],
                'db_table': 'm_b_organisme',
                'verbose_name': 'Organism',
                'verbose_name_plural': 'Organisms',
            },
        ),
        migrations.CreateModel(
            name='RecordSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pictogram', models.FileField(db_column=b'picto', upload_to=b'upload', max_length=512, blank=True, null=True, verbose_name='Pictogram')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('website', models.URLField(max_length=256, null=True, verbose_name='Website', db_column=b'website', blank=True)),
                ('structure', models.ForeignKey(db_column=b'structure', default=geotrek.authent.models.default_structure, verbose_name='Related structure', to='authent.Structure')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'o_b_source_fiche',
                'verbose_name': 'Record source',
                'verbose_name_plural': 'Record sources',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pictogram', models.FileField(max_length=512, null=True, verbose_name='Pictogram', db_column=b'picto', upload_to=b'upload')),
                ('label', models.CharField(max_length=128, verbose_name='Label', db_column=b'theme')),
                ('label_en', models.CharField(max_length=128, null=True, verbose_name='Label', db_column=b'theme_en')),
                ('label_es', models.CharField(max_length=128, null=True, verbose_name='Label', db_column=b'theme_es')),
                ('label_fr', models.CharField(max_length=128, null=True, verbose_name='Label', db_column=b'theme_fr')),
                ('label_it', models.CharField(max_length=128, null=True, verbose_name='Label', db_column=b'theme_it')),
                ('cirkwi', models.ForeignKey(verbose_name='Cirkwi tag', blank=True, to='cirkwi.CirkwiTag', null=True)),
            ],
            options={
                'ordering': ['label'],
                'db_table': 'o_b_theme',
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
    ]
