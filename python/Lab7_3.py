import re

input_file = input("Введите имя входного файла: ")

output_file = input("Введите имя выходного файла: ")

with open(input_file, "r") as f_inp, open(output_file, "w+") as f_out:
    data_inp = f_inp.read()
    newfile = re.sub(r'[^\w\s]', '', data_inp)
    newfile = newfile.lower()
    f_out.write(newfile)
f_inp.close()
f_out.close()
with open(output_file) as func:
    data = func.read()
print(data)
func.close()