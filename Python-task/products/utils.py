from .models import PC, Laptop, Product, Printer
import csv


def profitability_ratio(object):
    return round(((object.ram + object.hd) / object.price) * object.speed, 2)


def type_check(model_name, code=False, price=False):
    """ Check if product with given name is PC or laptop.
        This structure of if statement prevents calling .objects.filter()
        many times, in the best scenario will be executed 1 time, in worst 2.
        Extended by flags, returning additional values.
    """

    result = []
    obj = PC.objects.filter(model=model_name).first()

    if not obj:
        obj = Laptop.objects.filter(model=model_name).first()
        if not obj:
            return None

        result.append("Laptop")
    else:
        result.append("PC")

    if code:
        result.append(obj.code)
    if price:
        result.append(obj.price)

    return result


def printer_code_check(model_name):
    printer = Printer.objects.get(model=model_name)

    return printer.code


def export_products_to_csv(response, obj_list):
    writer = csv.writer(response)

    product_fields = [field.name for field in Product._meta.fields]
    obj_fields = [field.name for field in obj_list.model._meta.fields]
    same_fields = list(set(product_fields) & set(obj_fields))

    for value in same_fields:
        obj_fields.remove(value)

    writer.writerow(['profitability_ratio'] + product_fields + obj_fields)

    for obj in obj_list:
        product_data = [getattr(obj.model, field) for field in product_fields]
        obj_data = [getattr(obj, field) for field in obj_fields if field not in same_fields]
        prof_ratio = profitability_ratio(obj)
        writer.writerow([prof_ratio] + product_data + obj_data)

    return response


def export_promos_to_csv(response, obj_list):
    writer = csv.writer(response)

    promo_fields = ['id', 'price']
    pc_fields = [field.name for field in PC._meta.fields]
    laptop_fields = [field.name for field in Laptop._meta.fields]
    printer_fields = [field.name for field in Printer._meta.fields]
    same_fields = list(set(pc_fields) & set(laptop_fields))

    same_fields_to_csv = ['computer:' + field for field in same_fields]
    printer_fields_to_csv = ['printer:' + field for field in printer_fields]

    writer.writerow(promo_fields + same_fields_to_csv + printer_fields_to_csv)

    for obj in obj_list:
        promo_data = [getattr(obj, field) for field in promo_fields]

        if type_check(obj.computer.model)[0] == "PC":
            computer = PC.objects.get(model=obj.computer.model)
        elif type_check(obj.computer.model)[0] == "Laptop":
            computer = Laptop.objects.get(model=obj.computer.model)
        printer = Printer.objects.get(model=obj.printer.model)

        computer_data = [getattr(computer, field) for field in same_fields]
        printer_data = [getattr(printer, field) for field in printer_fields]
        writer.writerow(promo_data + computer_data + printer_data)

    return response
