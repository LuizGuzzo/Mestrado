# import re
import argparse
import regeng

# codigo Origem: https://github.com/tonisidneimc/Regex-Engine

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r','--regex', type=str)
parser.add_argument('-f', '--file', type=str)
args = parser.parse_args()

if ".txt" in args.file[-4:]:
	with open(args.file) as f:
		txt = f.readline()
	print("txt: ",txt)
else:
	txt = args.file

if ".txt" in args.regex[-4:]:
	with open(args.regex) as f:
		reg = f.readline()
	print("regex: ",reg)
else:
	reg = args.regex


# x = re.search(reg, txt)

r = regeng.Regex(reg)
x = r.match(txt)


if x:
	print("YES! We have a match!")
else:
	print("No match")

