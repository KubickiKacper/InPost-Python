from django.shortcuts import render, redirect
from .forms import ProductForm, PCForm, LaptopForm, PrinterForm, PromotionForm
from .models import Product, PC, Laptop, Printer, Promotion
from .utils import profitability_ratio, type_check, export_products_to_csv, export_promos_to_csv, printer_code_check
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    products = Product.objects.all()

    context = {"products": products}
    return render(request, 'home.html', context)


def pc_create_view(request, *args, **kwargs):
    product_form = ProductForm(request.POST or None)
    pc_form = PCForm(request.POST or None)

    if product_form.is_valid() and pc_form.is_valid():
        product = product_form.save(commit=False)
        product.type = 'PC'
        product.save()

        pc = pc_form.save(commit=False)
        pc.model = product
        pc.save()

        return redirect(home_view)

    context = {'product_form': product_form, 'pc_form': pc_form}

    return render(request, 'pc_create.html', context)


def laptop_create_view(request, *args, **kwargs):
    product_form = ProductForm(request.POST or None)
    laptop_form = LaptopForm(request.POST or None)

    if product_form.is_valid() and laptop_form.is_valid():
        product = product_form.save(commit=False)
        product.type = 'Laptop'
        product.save()

        laptop = laptop_form.save(commit=False)
        laptop.model = product
        laptop.save()

        return redirect(home_view)

    context = {'product_form': product_form, 'laptop_form': laptop_form}

    return render(request, 'laptop_create.html', context)


def printer_create_view(request, *args, **kwargs):
    product_form = ProductForm(request.POST or None)
    printer_form = PrinterForm(request.POST or None)

    if product_form.is_valid() and printer_form.is_valid():
        product = product_form.save(commit=False)
        product.type = 'Printer'
        product.save()

        printer = printer_form.save(commit=False)
        printer.model = product
        printer.save()

        return redirect(home_view)

    context = {'product_form': product_form, 'printer_form': printer_form}

    return render(request, 'printer_create.html', context)


def type_check_route(request, model_name, *args, **kwargs):
    result = type_check(model_name, code=True)

    if not result:
        return redirect(printer_code_check_route, model_name=model_name)
    else:
        product_type, product_code = result[0], result[1]
        if product_type == "PC":
            return redirect(product_pc_view, code=product_code)
        elif product_type == "Laptop":
            return redirect(product_laptop_view, code=product_code)
        else:
            return redirect(home_view)


def printer_code_check_route(request, model_name, *args, **kwargs):
    printer_code = printer_code_check(model_name)

    return redirect(product_printer_view, code=printer_code)


def product_pc_view(request, code, *args, **kwargs):
    pc = PC.objects.get(code=code)
    profit_ratio = profitability_ratio(pc)

    context = {"pc_object": pc, "profitability_ratio": profit_ratio}

    return render(request, 'pc.html', context)


def product_pc_list_view(request, *args, **kwargs):
    pc_list = PC.objects.all()
    context = {"pc_list": pc_list}

    return render(request, 'pc_list.html', context)


def product_laptop_view(request, code, *args, **kwargs):
    laptop = Laptop.objects.get(code=code)
    profit_ratio = profitability_ratio(laptop)

    context = {"laptop_object": laptop, "profitability_ratio": profit_ratio}

    return render(request, 'laptop.html', context)


def product_printer_view(request, code, *args, **kwargs):
    printer = Printer.objects.get(code=code)

    context = {"printer_object": printer}

    return render(request, 'printer.html', context)


def product_laptop_list_view(request, *args, **kwargs):
    laptop_list = Laptop.objects.all()
    context = {"laptop_list": laptop_list}

    return render(request, 'laptop_list.html', context)


def promo_create_view(request, *args, **kwargs):
    promotion_form = PromotionForm(request.POST or None)

    if promotion_form.is_valid():
        promo = promotion_form.save(commit=False)
        product_type, product_price = type_check(promo.computer.model, price=True)
        printer_price = Printer.objects.get(model=promo.printer.model).price

        promo.price = 0.9 * (float(printer_price) + float(product_price))

        promo.save()

        return redirect(home_view)

    context = {'promotion_form': promotion_form}

    return render(request, 'promo_create.html', context)


def promo_list_view(request, *args, **kwargs):
    promo_list = Promotion.objects.all()

    context = {"promo_list": promo_list}

    return render(request, 'promo_list.html', context)


def product_create_select(request, *args, **kwargs):
    context = {}
    return render(request, 'product_create_select.html', context)


def pc_csv(*args, **kwargs):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="pc.csv"'},
    )

    pc_list = PC.objects.all()
    response = export_products_to_csv(response, pc_list)

    return response


def laptop_csv(*args, **kwargs):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="laptops.csv"'},
    )

    laptop_list = Laptop.objects.all()
    response = export_products_to_csv(response, laptop_list)

    return response


def promo_csv(*args, **kwargs):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="promotions.csv"'},
    )

    promo_list = Promotion.objects.all()
    response = export_promos_to_csv(response, promo_list)

    return response
