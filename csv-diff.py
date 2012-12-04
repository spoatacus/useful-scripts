from __future__ import print_function
import argparse
import csv

parser = argparse.ArgumentParser(description="Removes items in 'other' from 'set' based on a 'key' column.")
parser.add_argument('set', type=str, help='File that contains primary set')
parser.add_argument('other', type=str, help='File that contains set to be removed')
parser.add_argument('set_key', type=int, help='Column to use as key in primary set')
parser.add_argument('other_key', type=int, help='Column to use as key in other set')
parser.add_argument('output', type=str, help='File to put results in')
args = parser.parse_args()

with open( args.set, 'r' ) as f1, open( args.other, 'r' ) as f2:
	csv1 = csv.reader( f1 )
	csv2 = csv.reader( f2 )

	# skip header row
	header = csv1.next()
	csv2.next()

	dict1 = {}
	dict2 = {}

	for row in csv1:
		try:
			key = row[args.set_key]
			dict1[key] = row
		except IndexError:
			print( row )

	for row in csv2:
		dict2[row[args.other_key]] = row


	print( 'len set: ', len(dict1) )
	print( 'len other: ', len(dict2) )


	key1 = dict1.viewkeys()
	key2 = dict2.viewkeys()
	diff = key1 - key2

	print( 'len diff: ', len(diff) )

	
	with open( args.output, 'w' ) as fout:
		csvWriter = csv.writer( fout, quoting=csv.QUOTE_ALL )

		csvWriter.writerow( header )

		for key in diff:
			csvWriter.writerow( dict1[key] )
