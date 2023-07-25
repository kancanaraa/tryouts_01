import inspect

def object_to_dict(obj, depth=1):
    if depth < 1:
        return str(obj)

    dictionary = {}
    for attr in dir(obj):
        if not attr.startswith("_"):  # Özel metod ve özellikleri atla
            value = getattr(obj, attr)
            if inspect.isroutine(value):  # Eğer metot ise değerini almayı atla
                continue
            elif inspect.isclass(value) or inspect.ismodule(value):  # Eğer class veya modül ise string olarak kaydet
                dictionary[attr] = str(value)
            elif inspect.isbuiltin(value):  # Eğer built-in fonksiyon ise değerini almayı atla
                continue
            else:  # Eğer değer bir nesne ise, bu nesnenin özelliklerini ve değerlerini al
                if attr not in dictionary:
                    dictionary[attr] = object_to_dict(value, depth-1)
                else:
                    dictionary[attr + "_depth" + str(depth)] = object_to_dict(value, depth-1)
    return dictionary

from parser import parse_opendrive

file_path = "straight_500m.xodr"  # OpenDRIVE XML dosyasının yolu
opendrive_object = parse_opendrive(file_path)

dictionary = object_to_dict(opendrive_object, depth=2)

print(dictionary)
