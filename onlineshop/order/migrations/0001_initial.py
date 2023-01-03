# Generated by Django 4.1.4 on 2022-12-22 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('DENIED', 'DENIED'), ('IN WORK', 'IN WORK')], default='IN WORK', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Work_shedule',
            fields=[
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='order.order')),
                ('TIME', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.animal')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(to='order.orderitem'),
        ),
    ]