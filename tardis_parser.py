## Created by Amol Agrawal 7:29 PM, 4th March, 2015
## Outputs to output.txt

from pyparsing import *


####First Line Parsing####
num=Word(nums+".")
word=Word(alphas)
saved=Group(num+OneOrMore(word))
saves=Group(num+OneOrMore(Word(printables)))
tot=num+saved+saved+saved+saved+saves
#########################

#####First Dataset Parsing######
word1 = Word(printables, max=1)
word2 = Word(alphanums, max=2)
word3 = Word(alphanums, max=3)
part = Group(word1+Optional(word2)+Optional(word3))
sent = OneOrMore(part)
###############################

#####Second Dataset Parsing(Currently under work)####
element=Word(alphanums+'.')
index = Word(nums)
energy= Word(nums+'.-')
j= Word(nums+".")
space=Literal(' ')
label=Group(Word(printables)+Word(printables)+Word(printables)) | Word(printables)+Word(printables) | Word(printables)
gland=energy
suma=Word(nums+".+E")
c4=Word(nums+".-E")
c6=Word(nums+".-E",max=8)
sumf=energy
eigen1=Group(energy+Word(printables, max=7)+index)
total=element+index+energy+j+label+gland+suma+c4+c6+sumf+eigen1+Optional(eigen1)+Optional(eigen1) 
######################################

fd=open("gf1401.gam")
print_f=open("output.txt",'w')
for i,lines in enumerate(fd):
	if i < 33 :
		if i==0:
			print_f.write(str(tot.parseString(lines))+'\n')
			continue
		print_f.write(str(sent.parseString(lines))+'\n')
	else:
		if i>32 and i<38:
			continue
		if i < 49:
			print_f.write(str(total.parseString(lines))+'\n') ##Currently under work
		else:
			break

