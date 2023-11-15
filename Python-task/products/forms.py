from django.forms import ModelForm
from django import forms
from .models import Product, PC, Laptop, Printer, Promotion


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['maker', 'model']
        exclude = ()


class PCForm(ModelForm):
    class Meta:
        model = PC
        fields = ['code', 'speed', 'ram', 'hd', 'cd', 'price']


class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        fields = ['code', 'speed', 'ram', 'hd', 'price', 'screen']


class PrinterForm(ModelForm):
    class Meta:
        model = Printer
        fields = ['code', 'color', 'type', 'price']


class PromotionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PromotionForm, self).__init__(*args, **kwargs)

        pc_records = PC.objects.all()
        laptop_records = Laptop.objects.all()
        printer_records = Printer.objects.all()

        pc_related_products = Product.objects.filter(pc__in=pc_records)
        laptop_related_products = Product.objects.filter(laptop__in=laptop_records)
        printer_related_products = Product.objects.filter(printer__in=printer_records)

        computers = pc_related_products | laptop_related_products

        self.fields['computer'].queryset = computers
        self.fields['printer'].queryset = printer_related_products

    class Meta:
        model = Promotion
        fields = ['computer', 'printer']
        exclude = ('price',)
