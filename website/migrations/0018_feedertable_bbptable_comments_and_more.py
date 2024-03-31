# Generated by Django 4.2.7 on 2024-03-31 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_bbptable_combinertable_filtertable_mpttable_rhtable_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeederTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, null=True)),
                ('vendor', models.CharField(max_length=100, null=True)),
                ('feeder_dimension', models.CharField(max_length=100, null=True)),
                ('L7_loss_per_meter', models.CharField(max_length=50, null=True)),
                ('L18_loss_per_meter', models.CharField(max_length=50, null=True)),
                ('L21_loss_per_meter', models.CharField(max_length=50, null=True)),
                ('L23_loss_per_meter', models.CharField(max_length=50, null=True)),
                ('L26_loss_per_meter', models.CharField(max_length=50, null=True)),
                ('U85_loss_per_meter', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('quantity_in_hand', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bbptable',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bbptable',
            name='lte_cell_capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bbptable',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bbptable',
            name='nr_cell_capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bbptable',
            name='quantity_in_hand',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bbptable',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bbptable',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bbptable',
            name='usage',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bbptable',
            name='vendor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='combinertable',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='combinertable',
            name='insertion_loss',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='combinertable',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='combinertable',
            name='quantity_in_hand',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='combinertable',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='combinertable',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='combinertable',
            name='usage',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='combinertable',
            name='vendor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='filtertable',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='filtertable',
            name='insertion_loss',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='filtertable',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='filtertable',
            name='quantity_in_hand',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='filtertable',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='filtertable',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='filtertable',
            name='usage',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='filtertable',
            name='vendor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='lte_cell_capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='nr_cell_capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='quantity_in_hand',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='usage',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='vendor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mpttable',
            name='ype',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='dimesons',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='frequency_range',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='num_rx_ports',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='num_tx_ports',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='pa_power',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='quantity_in_hand',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='usage',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='vendor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rhtable',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]