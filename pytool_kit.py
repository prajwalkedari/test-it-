
def txt2array(text_var):
	txt_var=text_var.split()
	return txt_var

def array2txt(txt_var,join_by=" "):
	 output_a2t =join_by.join(txt_var)
	 return output_a2t

def array2dic(array_1,array_2):
	dic={}
	for i in array_1:
		for j in array_2 :
			dic[i]=j
			array_2.remove(j)
			break
	return dic

def dic2array(dictionary):
	get=list(dictionary.items())
	list_key=list(dictionary.keys())
	list_value=list(dictionary.values())
	return list_key,list_value , get

def wordcounter(txt_var,word=" "):
	if word == " ":
		output = len(txt_var.split())
	else:
		output=word.count(txt_var)
	return output
	
def get_txt_between(text_var,parse_1,parse_2):
	try:
		if parse_1 ==" ":
	    		text_var=text_var.split(parse_2)[0]
		elif parse_2 == " ":
				text_var=text_var.split(parse_1)[1]
		else:
			text_var=text_var.split(parse_1)[1]
			text_var=text_var.split(parse_2)[0]
		
		return text_var
	except IndexError:
		pass
def add_txt_between(text_var,string_var,parse_1,parse_2):
	try:
		if text_var =="none":
			pass
		elif parse_1 == " ":
				text1=text_var.split(parse_2)[0]
				text_var=string_var+string_var
		elif parse_2 == " ":
				text1=text_var.split(parse_1)[1]
				text_var=text1+string_var
		else:
			text1=text_var.split(parse_1)[0]
			text2=text_var.split(parse_2)[1]
			text_var=text1+string_var+text2
		
		return text_var
	except IndexError:
		pass


def average(lis):
	l=0
	a=len(lis)
	for i in lis:
            l=l+i
	rtn= l/a
	return rtn

def hrs2min(Hour):
	minute=Hour*60	
	return minute
def sec2hrs(seconds):
    	seconds = seconds % (24 * 3600)
    	hour = seconds // 3600
    	seconds %= 3600
    	minutes = seconds // 60
    	seconds %= 60
    	return "%d:%02d:%02d" % (hour, minutes, seconds)


def min2hrs(Minute,Fromat=False):
	minmm=int(Minute%60)
	hrs=int(Minute/60)
	return f"{hrs}:{minmm}"


