file_list = []
with open('benchmark_images.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        file_list.append([row[0],row[2].split('_')[1],row[2],row[1]])

print file_list
