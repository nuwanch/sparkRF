# Generated by Django 4.2.7 on 2024-02-13 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_antennatable_rfreportdatacommon_rfreportdataspecific'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antennatable',
            name='band1800_gain',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band1800_vbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band2100_gain',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band2100_vbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band2300_gain',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band2300_vbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band2600_gain',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band2600_vbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band3500_gain',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band3500_vbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band600_gain',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band600_vbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band700_gain',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band700_vbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band850_gain',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='band850_vbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='bracket_weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='freq_high',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='freq_low',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='hbw',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='num_high_ports',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='num_low_ports',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='antennatable',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='rfreportdataspecific',
            name='sector_azimuth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rfreportdataspecific',
            name='sector_carrier_power',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='rfreportdataspecific',
            name='sector_combiner_loss',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='rfreportdataspecific',
            name='sector_feeder_loss',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='rfreportdataspecific',
            name='sector_num_of_carriers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rfreportdataspecific',
            name='sector_tx_filter_loss',
            field=models.FloatField(null=True),
        ),
    ]
