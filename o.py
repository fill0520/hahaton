import json
from random import randint

def comma(str):
	return (str if (len(str)==2) else '0'+str)

def date():
	return "{}.{}.{}".format(comma(str(randint(1, 31))),comma(str(randint(8, 9))),str(2018))


def timeNight():
	return "{}:{}:{}".format(comma(str(randint(0, 6))),comma(str(randint(0, 60))),comma(str(randint(0,60))))
def timeDay():
	return "{}:{}:{}".format(comma(str(randint(6, 23))),comma(str(randint(0, 60))),comma(str(randint(0,60))))


prefix = ['0500', '0501', '0502', '0505', '0507','0700', '0702', '0703', '0704', '0705', '0707', '0708', '0709']

def num():
	p = '0123456789'
	post = ''
	for _ in range(6):
		post += p[randint(0,9)]
	return str(prefix[randint(0,12)]+post)

def createNight():
	return {
	"Call":{
	"Date":date(),
	"Time":timeNight(),
	"Number to":num(),
	"Dialing time":"32"
	},

	"Internet":{
	"Megabytes":"122",
	"Date":date(),
	"Time":timeNight()
	},

	"SMS":{
	"Text size":"120",
	"Number to":num(),
	"Date":date(),
	"Time":timeNight()
	}

}
def createDay():
	return {
	"Call":{
	"Date":date(),
	"Time":timeDay(),
	"Number to":num(),
	"Dialing time":"32"
	},

	"Internet":{
	"Megabytes":"122",
	"Date":date(),
	"Time":timeDay()
	},

	"SMS":{
	"Text size":"120",
	"Number to":num(),
	"Date":date(),
	"Time":timeDay()
	}

}

 


jsNight = []
jsDay = []
for _ in range(2):
	jsNight.append(createNight())
	jsDay.append(createDay())


print(json.dumps(jsNight, indent=4))
print(json.dumps(jsDay, indent=4))

