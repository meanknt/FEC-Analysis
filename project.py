import csv
import pygal
def percap(lis, ris, count):
    with open('percap.csv') as pc:
        pc = csv.reader(pc)
        for i in pc:
            lis.append(i)
        print(*lis, sep="\n")
        print(len(lis))
        print(len(lis[1]))

        num = 0
        for row in range(len(lis[0])):
            for col in range(len(lis)):
                if row != 1:
                    ris.append(lis[col][row])
                    ris = list(map(float, ris))
                else:
                    num += float(lis[col][1])
                    ris.append(lis[col][row])
                    ris = list(map(float, ris))
            count.append(ris)
            ris = []
        print('%.2f'%num)
        print('%.2f'%(num/len(lis)))
    return count

def main(lis, ris, count):
    with open('fec.csv') as rio:
        data = csv.reader(rio)
        for i in data:
            lis.append(i) #keep data

        print(*lis, sep="\n") #print(data)
        print(len(lis)) #count year
        print(len(lis[1])) #count row

        for row in range(1, len(lis[1])-1): #row
            for col in range(1, len(lis)): #colum
                ris.append(lis[col][row].replace(',', '')) #keep and cut ','
                ris = list(map(int, ris)) #change string to integers
            ris.insert(0, lis[0][row])
            count.append(ris) #keep num in ris to count
            ris = [] #recycle
        print(*count, sep='\n\n')

        line_chart = pygal.Line()
        line_chart.title = 'Final Energy Consumption (Unit: ktoe)'
        line_chart.x_labels = range(1992, 2017)
        line_chart.add(count[0][0], count[0][1:])
        line_chart.add(count[1][0], count[1][1:])
        line_chart.add(count[2][0], count[2][1:])
        line_chart.add(count[3][0], count[3][1:])
        line_chart.add(count[4][0], count[4][1:])
        line_chart.render_to_file('FEC_csv_pygal.svg')

        per = percap([], [], [])
        line_chart = pygal.Bar()
        line_chart.title = 'Final Energy Consumption Per Capita (toe/person)'
        line_chart.x_labels = range(1993, 2017)
        line_chart.add('Percapita', per[1])
        line_chart.render_to_file('Percap_csv_pygal.svg')
main([], [], [])
