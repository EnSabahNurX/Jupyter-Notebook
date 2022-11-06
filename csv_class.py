import csv
# with open('02_CSV_data.csv', 'r') as my_csv_file:
#     reader = csv.reader(my_csv_file)
#     for row in reader:
#         print(row)
# del reader
# my_csv_file.close()
dados = [('aaa', 111), ('bbb', 222), ('ccc', 333)]
csv_out = open("03_CSV_data.csv", "w")
writer = csv.writer(csv_out)
writer.writerow((['campo1', 'campo2']))
writer.writerows(dados)

del writer
csv_out.close()
