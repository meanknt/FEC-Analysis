import csv
import pygal
def main(lis, ris, count):
	with open('percap.csv') as pc:
		pc = csv.reader(pc)
		for i in pc:
			lis.append(i)
		print(*lis, sep="\n")
		print(len(lis))
		print(len(lis[1]))

		for row in range(len(lis[0])):
			for col in range(len(lis)):
				ris.append(lis[col][row])
				ris = list(map(float, ris)) 
			count.append(ris)
			ris = []
		print(*count, sep='\n\n')

		line_chart = pygal.Bar()
		line_chart.title = 'Final Energy Consumption Per Capita (toe/person)'
		line_chart.x_labels = range(1993, 2017)
		line_chart.add('Percapita', count[1])
		line_chart.render_to_file('Percap_csv_pygal.svg')

main([], [], [])