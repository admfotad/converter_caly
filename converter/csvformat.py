import csv
from converter.format import Format

class Csv(Format):
	def read(self):
		reader = csv.DictReader(self.file)
		return list(reader)
		
	
	def write(self, data):
		writer=csv.DictWriter(self.file, fieldnames=data[0].keys())
		writer.writeheader()
		writer.writerows(data)
