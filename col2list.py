#!/usr/bin/python
import argparse
import csv

parser = argparse.ArgumentParser(description='Convert a column of data to a comma separated list.')
parser.add_argument('input', type=str, help='File to get data from')
parser.add_argument('col', type=int, help='Column number to convert')
parser.add_argument('--output', type=str, help='File to dump list to')
parser.add_argument('--sep', type=str, default='\t', help='Separater to split columns on')
args = parser.parse_args()

with open(args.input, 'rb') as f:
	reader = csv.reader( f, delimiter=args.sep )

	data = []

	for row in reader:
		data.append( row[args.col].strip() )


	print( ','.join(data) )

	if args.output:
		with open(args.output, 'w') as fout:
			fout.write( data )
