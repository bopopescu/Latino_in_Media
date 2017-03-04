import urllib
import http.client
import json
import csv
import codecs
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')
def getmoviesbyyear():
	dcode=dict()
	dcode["comedy"]=35
	dcode["action"]=28
	dcode["animation"]=16
	dcode["adventure"]=12
	dcode["crime"]=80
	dcode["documentary"]=99
	dcode["drama"]=18
	placeofbirthLatino=["Columbia"]
	year=raw_input("Enter year: ")
	g=raw_input("Entre the genre: ")
	genre=dcode.get(g)
	url="https://api.themoviedb.org/3/discover/movie?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US&region=US&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year="+str(year)+"&with_genres=35&year="+str(year)+"&without_genres=28,12,16,18,80,99,18,10751,14,36,27,10402,9648,10749,878,10770,53,37,10752&with_original_language=en"
	with open('year2017.json') as data_file:
		data = json.load(data_file)
		print data["total_pages"]
		for i in range(1,data["total_pages"]+1):
			print "Page",i
			print "-------------------------------------------"
			time.sleep(3)
			url="https://api.themoviedb.org/3/discover/movie?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US&region=US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(i)+"&primary_release_year="+str(year)+"&with_genres=35&year="+str(year)+"&without_genres=28,12,16,18,80,99,18,10751,14,36,27,10402,9648,10749,878,10770,53,37,10752&with_original_language=en"
			urllib.urlretrieve (url,"year2017.json");
			
			with open('year2017.json') as data_file2:
				data2 = json.load(data_file2)
				print "data2"
				print data2
				if "results" in data2.keys():
					print "in results"
					for i in data2["results"]:
						if i.get("original_language")=="en":

							print i.get("original_title")
							f=open('Comedy2017Cast.csv', 'a')
							g=open('Comedy2017Crew.csv','a')
							s=(i.get("original_title").encode('utf-8','ignore').decode('utf-8'))
							#s=unicode(s.strip(codecs.BOM_UTF8), 'utf-8')
							f.write(s)
							g.write(s)
							rescast=i.get("id")
							print str(rescast)
							#time.sleep(2)
							url2="https://api.themoviedb.org/3/movie/"+str(rescast)+"/casts?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c"
							urllib.urlretrieve (url2,"./cast2017.json");
							with open('cast2017.json') as data_file2:
								datac = json.load(data_file2)
								strtemp="" 
								strtemp2=""
								pob=""
								if "cast" in datac.keys():
									for j in datac["cast"]:
										print j.get("name")
								
										#time.sleep(1)
										url3="https://api.themoviedb.org/3/person/"+str(j.get("id"))+"?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US"
										urllib.urlretrieve(url3,"./placeofbirth.json")
										pob=""
										pp=""
										attach=""
										with open('placeofbirth.json') as data_file3:
											dataperson = json.load(data_file3)
											if "place_of_birth" in dataperson.keys():
												pob=dataperson["place_of_birth"]
												if pob!=None:
													if "Colombia" in pob:
														attach="Latinx"
											print "pob",pob

											if "profile_path" in dataperson.keys():
												if dataperson["profile_path"]!=None:
													pp="http://image.tmdb.org/t/p/w185//"+dataperson["profile_path"]
											#if not pob:
										strtemp=strtemp+j.get("name").encode('utf-8','ignore').decode('utf-8')+","+j.get("character").encode('utf-8','ignore').decode('utf-8')+","+str(pob)+","+str(pp)+","+str(attach)+"\n"
										#strtemp=strtemp+j.get("name").encode('utf-8')+"\t\t"+j.get("character").encode('utf-8')+"\n"

									for j in datac["crew"]:
										print j.get("name")
										#strtemp2=strtemp2+j.get("name").encode('utf-8')+"\t\t"+j.get("job").encode('utf-8')+"\n"
										#time.sleep(1)
										url3="https://api.themoviedb.org/3/person/"+str(j.get("id"))+"?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US"
										urllib.urlretrieve(url3,"./placeofbirth.json")
										pob=""
										pp=""
										attach=""
										with open('placeofbirth.json') as data_file3:
											dataperson = json.load(data_file3)
											if "place_of_birth" in dataperson.keys():
												pob=dataperson["place_of_birth"]
												if pob!=None:
													if "Colombia" in pob:
														attach="Latinx"
											print "pob",pob
											#if not pob:

											if "profile_path" in dataperson.keys():
												if dataperson["profile_path"]!=None:
													pp="http://image.tmdb.org/t/p/w185//"+dataperson["profile_path"]
										strtemp2=strtemp2+j.get("name").encode('utf-8','ignore').decode('utf-8')+","+j.get("job").encode('utf-8','ignore').decode('utf-8')+","+str(pob)+","+str(pp)+","+str(attach)+"\n"
										#strtemp2=strtemp2+j.get("name").encode('utf-8')+"\t\t"+j.get("character").encode('utf-8')+"\n"

							f.write("\n")
							g.write("\n")			
							f.write("Cast")
							g.write("Crew")
							f.write("\n")
							g.write("\n")
							f.write(strtemp)
							g.write(strtemp2)
							f.write("\n")
							g.write("\n")

						'''with f as myfile:
							writer = csv.writer(myfile, dialect = 'excel')
							writer.writerow(str(i.get("original_title")).encode('utf-8'))'''


	
def getmoviesdirect():
	conn = http.client.HTTPSConnection("api.themoviedb.org")
	payload = "{}"
	conn.request("GET", "/3/discover/movie?with_genres=35&primary_release_year=2017&page=1&include_video=false&include_adult=false&sort_by=vote_count.desc&language=en-US&api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c", payload)
	res = conn.getresponse()
	data = res.read()
	print (type(data))
	print(data.decode("utf-8"))
	print ("----------------------------------------")
	print(type(data))


def main():
	getmoviesbyyear()

if __name__ == '__main__':
	try:
		main()
	except Exception,e:
		print(e)