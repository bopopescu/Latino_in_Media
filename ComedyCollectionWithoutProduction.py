import urllib
import json
import re
import csv
import codecs
import sys
import time
import requests
from imp import reload
import urllib.request
import os


#LA_COUNTRIES = ["Cuba", "Dominican Republic","Puerto Rico", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Mexico", "Nicaragua", "Panama", "Argentina", "Bolivia", "Chile", "Colombia", "Ecuador",  "Guyana", "Paraguay", "Peru", "Uruguay", "Venezuela"]
reload(sys)
#sys.setdefaultencoding('utf8')
def getmoviesbyyear():
	totalmovies=0
	dcode=dict()
	totalactors=0
	latinoactors=0
	latinolead=0
	genlead=0
	gensupport=0
	latinosupport=0	
	dcode["comedy"]=35
	dcode["action"]=28
	dcode["animation"]=16
	dcode["adventure"]=12
	dcode["crime"]=80
	dcode["documentary"]=99
	dcode["drama"]=18
	wikipedialist=[[],[]]
	wikipedialistcrew=[[],[]]
	overviewlist=list()
	foverview=open('movieoverview.txt','a')
	LA_COUNTRIES=re.compile(".*Cuba.*|.*Dominican Republic.*|.*Puerto Rico.*|.*Costa Rica.*|.*El Salvador.*|.*Guatemala.*|.*Mexico.*|.*Nicaragua.*|.*Panama.*|.*Argentina.*|.*Nicaragua.*|.*Bolivia.*|.*Chile.*|.*Colombia.*|.*Ecuador.*|.*Guyana.*|.*Paraguay.*|.*Peru.*|.*Uruguay.*|.*Venezuela.*")
	LA_NAMES=re.compile(".*ez$|.*do$|.*ro$")
	year=input("Enter year: ")
	g=input("Entre the genre: ")
	genre=dcode.get(g)
	pc=[1,2,3,4,5,6,7,8,9,11,12,13,14,16,17,25,8411]
	f=open('Comedy'+str(year)+'Cast.csv', 'a')
	g=open('Comedy'+str(year)+'Crew.csv','a')
	
	url="https://api.themoviedb.org/3/discover/movie?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US&region=US&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year="+str(year)+"&with_genres=35&year="+str(year)+"&without_genres=28,12,16,18,80,99,18,10751,14,36,27,10402,9648,10749,878,10770,53,37,10752&with_original_language=en&certification_country=US"
	urllib.request.urlretrieve (url,"year2017.json");
	with open('year2017.json') as data_file:
		data = json.load(data_file)
		print("Total Pages",data["total_pages"])
			
		for i in range(1,data["total_pages"]+1):
			print ("Page",i)
			print ("-------------------------------------------")
			time.sleep(3)
			url="https://api.themoviedb.org/3/discover/movie?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US&region=US&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(i)+"&primary_release_year="+str(year)+"&with_genres=35&year="+str(year)+"&without_genres=28,12,16,18,80,99,18,10751,14,36,27,10402,9648,10749,878,10770,53,37,10752&with_original_language=en&certification_country=US"
			urllib.request.urlretrieve (url,"year2017.json");
			

			with open('year2017.json') as data_file2:
					
				data2 = json.load(data_file2)
				print ("data2")
				print (data2)
				if "results" in data2.keys():
					print ("in results")
					for i in data2["results"]:
						movieproduction=""
						movieid=i.get("id")
						urlmovie="https://api.themoviedb.org/3/movie/"+str(movieid)+"?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US"
						urllib.request.urlretrieve (urlmovie,"./moviedetails.json");
						with open('moviedetails.json') as movie_file:
							movied = json.load(movie_file)
							if "production_companies" in movied.keys():
								print("PRODCUTION")
								print(movied["production_companies"])
								for d in movied["production_companies"]:
									movieproduction=movieproduction+d["name"]+" "




						if i.get("original_language")=="en":

							print (i.get("original_title"))
							
							s=(i.get("original_title").encode('utf-8','ignore').decode('utf-8'))
							#s=unicode(s.strip(codecs.BOM_UTF8), 'utf-8')
							totalmovies=totalmovies+1
							f.write("//Movie title//\n")
							f.write(s+"\n")
							f.write("//Production Company//\n")
							f.write(movieproduction+"\n")
							g.write("//Movie title//\n")
							g.write(s)
							g.write("//Production Company//\n")
							g.write(movieproduction+"\n")
							rescast=i.get("id")
							print (str(rescast))
							overviewmovie=i.get("overview")
							print("overview",str(overviewmovie))
							overviewlist.append(str(overviewmovie))
							foverview.write(overviewmovie)
							foverview.write("\n")
							foverview.write("\n")
							if LA_COUNTRIES.findall(overviewmovie) or LA_NAMES.findall(overviewmovie):
								for startwithcap in LA_COUNTRIES.findall(overviewmovie):
									if startwithcap.istitle():
										print (startwithcap)
										f.write("\n")
										f.write("possible Latino movie")
										f.write("\n")
										g.write("\n")
										g.write("possible Latino movie")
										g.write("\n")
								for startwithcap in LA_NAMES.findall(overviewmovie):
									if startwithcap.istitle():
										print (startwithcap)
										f.write("\n")
										f.write("possible Latino movie")
										f.write("\n")
										g.write("\n")
										g.write("possible Latino movie")
										g.write("\n")



							#time.sleep(2)
							url2="https://api.themoviedb.org/3/movie/"+str(rescast)+"/casts?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c"
							urllib.request.urlretrieve (url2,"./cast2017.json");
							with open('cast2017.json') as data_file2:
								datac = json.load(data_file2)
								strtemp="" 
								strtemp2=""
								pob=""

								if "cast" in datac.keys():

									for j in datac["cast"]:
										flag=0
										attachleadornot=""
										attachnamebased=""
										imdbid=""
										printlead=0
											
										print (j.get("name"))
										tmdbid=j.get("id")
										time.sleep(1)
										urlimdb="https://api.themoviedb.org/3/person/"+str(tmdbid)+"/external_ids?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US"
										urllib.request.urlretrieve(urlimdb,"./actorimdb.json")
										with open('actorimdb.json') as data_fileimdb:
											try:
												temp=json.load(data_fileimdb)
												if "imdb_id" in temp.keys():
													imdbid=temp["imdb_id"]
												if "facebook_id" in temp.keys():
													facebook_id=temp["facebook_id"]
													print("Facebook id",facebook_id)

											except ValueError:
												print('Decoding error')
										if j.get("order")<=2:
											printlead=1

											genlead=genlead+1
											print("overview changed")
											overviewlist[-1]=overviewmovie+str(j.get("name"))
										else:
											gensupport=gensupport+1
												
										if LA_NAMES.findall(j.get("name")):
											attachnamebased="Latinx"
											print ("order",j.get("order"))
											latinoactors=latinoactors+1
											flag=1
											if j.get("order")>2:
													attachleadornot="Not lead"
													latinosupport=latinosupport+1
														
											else:
												latinolead=latinolead+1
													
								
										time.sleep(1)
										url3="https://api.themoviedb.org/3/person/"+str(j.get("id"))+"?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US"
										urllib.request.urlretrieve(url3,"./placeofbirth.json")
										pob=""
										pp=""
										attach=""
										gen=""
										with open('placeofbirth.json') as data_file3:
											dataperson = json.load(data_file3)
											if not os.path.exists("./trainingset/"+dataperson["name"]):
												os.makedirs("./trainingset/"+dataperson["name"])
												factordetails=open("./trainingset/"+dataperson["name"]+'/'+dataperson["name"], 'w')
												factordetails.write(str(dataperson["biography"]))

											
											if "gender" in dataperson.keys():
												gen=dataperson["gender"]
											if "place_of_birth" in dataperson.keys():
												pob=dataperson["place_of_birth"]
												if pob!=None:
													if LA_COUNTRIES.findall(pob):
														
														attach="Latinx"
														if flag==0:
															latinoactors=latinoactors+1
															if j.get("order")>2:
																latinosupport=latinosupport+1
																	
															else:
																latinolead=latinolead+1
																	
												if imdbid == None:
													pob_2 = ""
													if pob == None:
														pob_2 = str(pob)
													imdbid_2 = ""
													wikipedialist[0].append([str(j.get("name")),imdbid_2,pob_2])
												else:
													pob_2 = ""
													if pob == None:
														pob_2 = str(pob)
													imdbid_2 = str(imdbid)[2:]
													wikipedialist[1].append([str(j.get("name")),imdbid_2,pob_2])


											print ("pob",pob)

											if "profile_path" in dataperson.keys():
												if dataperson["profile_path"]!=None:
													pp="http://image.tmdb.org/t/p/w185//"+dataperson["profile_path"]
											#if not pob:

										strtemp=strtemp+j.get("name").encode('utf-8','ignore').decode('utf-8')+";"+j.get("character").encode('utf-8','ignore').decode('utf-8')+";"+str(pob)+";"+str(pp)+";"+str(gen)+";"+str(attachnamebased)+";"+str(attach)+";"+str(printlead)+"\n"
										totalactors=totalactors+1
										#strtemp=strtemp+j.get("name").encode('utf-8')+"\t\t"+j.get("character").encode('utf-8')+"\n"


								if "cast" in datac.keys():
									for j in datac["crew"]:
										attachnamebased=""
											
										print (j.get("name"))
										time.sleep(1)
										tmdbid=j.get("id")
										urlimdb="https://api.themoviedb.org/3/person/"+str(tmdbid)+"/external_ids?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US"
										urllib.request.urlretrieve(urlimdb,"./actorimdb.json")
										imdbidcrew=""
										with open('actorimdb.json') as data_fileimdb:
											try:
												temp=json.load(data_fileimdb)
												if "imdb_id" in temp.keys():
													imdbidcrew=temp["imdb_id"]
												if "facebook_id" in temp.keys():
													facebook_id=temp["facebook_id"]
													print("Facebook id",facebook_id)
											except ValueError:
												print("Decoding issue")

										if LA_NAMES.findall(j.get("name")):
											attachnamebased="Latinx"
										#strtemp2=strtemp2+j.get("name").encode('utf-8')+"\t\t"+j.get("job").encode('utf-8')+"\n"
										time.sleep(1)
										url3="https://api.themoviedb.org/3/person/"+str(j.get("id"))+"?api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c&language=en-US"
										urllib.request.urlretrieve(url3,"./placeofbirth.json")
										pob=""
										pp=""
										attach=""
										gen=""
										with open('placeofbirth.json') as data_file3:
											dataperson = json.load(data_file3)
											if "gender" in dataperson.keys():
												gen=dataperson["gender"]
											if "place_of_birth" in dataperson.keys():
												pob=dataperson["place_of_birth"]
												if pob!=None:
													if LA_COUNTRIES.findall(pob):
														
														attach="Latinx"
												if imdbidcrew == None:
													pob_2 = ""
													if pob == None:
														pob_2 = str(pob)
													imdbid_2 = ""
													wikipedialistcrew[0].append([str(j.get("name")),imdbid_2,pob_2])
												else:
													pob_2 = ""
													if pob == None:
														pob_2 = str(pob)
													imdbid_2 = str(imdbidcrew)[2:]
													wikipedialistcrew[1].append([str(j.get("name")),imdbid_2,pob_2])

											print ("pob",pob)
											#if not pob:

											if "profile_path" in dataperson.keys():
												if dataperson["profile_path"]!=None:
													pp="http://image.tmdb.org/t/p/w185//"+dataperson["profile_path"]
										strtemp2=strtemp2+j.get("name").encode('utf-8','ignore').decode('utf-8')+";"+j.get("job").encode('utf-8','ignore').decode('utf-8')+";"+str(pob)+";"+str(pp)+";"+str(gen)+";"+str(attachnamebased)+";"+	str(attach)+"\n"
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
							
		#print(totalactors)
		#print(latinoactors)
	f.write("Total_Movies;"+str(totalmovies))
	f.write("\n")
	f.write("Total_Actors;"+str(totalactors))
	f.write("\n")
	f.write("Latino_Actors;"+str(latinoactors))
	f.write("\n")
	f.write("Latino_Lead;"+str(latinolead))
	f.write("\n")
	f.write("General_Lead;"+str(genlead))
	f.write("\n")
	f.write("General_Support;"+str(gensupport))
	f.write("\n")
	f.write("Latino_Support;"+str(latinosupport))
		
	print ('\n')
	print(wikipedialist)
	print ("YEAR: " + str(year))
	print(wikipedialistcrew)
	return (str(year), wikipedialist)

		



	
def getmoviesdirect():
	url = 'http://api.themoviedb.org'
	params = '/3/discover/movie?with_genres=35&primary_release_year=2017&page=1&include_video=false&include_adult=false&sort_by=vote_count.desc&language=en    -US&api_key=17ce03ebb1e89f2dcf4eec0e9c2b8e6c'
	result = requests.get(str(url + params), headers = {}).json()
	print (result)
	print (type(data))
	print(data.decode("utf-8"))
	print ("----------------------------------------")


def main():
	getmoviesbyyear()

#if __name__ == '__main__':
#	try:
#		main()
#	except Exception,e:
#		print(e)
