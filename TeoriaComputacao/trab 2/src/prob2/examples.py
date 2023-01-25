# codigo origem: https://github.com/tonisidneimc/Regex-Engine
# https://online.visual-paradigm.com
import regeng

if __name__ == "__main__" :
	
	#grouping, union, closure and concatenation
	r = regeng.Regex('(a|b)*c')

	print(r.match('baabac')) #True
	print(r.match('cabbba')) #False
	print(r.match('c')) #True

	#match an acepptable identifier name
	r = regeng.Regex('([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9])*')

	print(r.match('')) #False
	print(r.match('identifer')) #True
	print(r.match('987c')) #False
	print(r.match('_usr501132')) #True

	#match numbers from 0 to 99
	r = regeng.Regex('[0-9]?[0-9]')

	print(r.match('00')) #True
	print(r.match('125')) #False
	print(r.match('12')) #True
	print(r.match('5')) #True