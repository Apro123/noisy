#!/usr/bin/env python3

#this python scrip creates a clean config json file that has 'clean' websites
#in case if you are running the noisy.py in a controlled envionment such as
#college or school
#In addition this script contains an ssl certificate check using the top 1
#million webites from ALexa
#This file makes the cleanConfig.json file
from random import randint
import csv
import http.client

# websites = []
# conn = http.client.HTTPSConnection("www.python.org")
# conn.request("GET", "/")
# r1 = conn.getresponse()
# print(r1.status, r1.reason)

#using template config.json to make a new json file
with open("templateConfig.txt", 'r') as file:
    #reading all data
    templateData = file.readlines()


with open('top-1m.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        website = "www." + str(row[0])

        #'clear' out the adult websites
        if("porn" in website or "sex" in website or "chick" in website or "xxx" in website):
            continue

        # using http.client to test whether the websites contain an ssl certificate
        try:
            # conn = http.client.HTTPSConnection(website)
            # conn.request("GET", "/")
            # r1 = conn.getresponse()
            website = "https://" + website
        except:
            website = "http://" + website
        # websites.append("\t\t" + website)
        line_count += 1
        if(line_count == 1):
            templateData[6] = "\t\t\t\"" + website + "\"\n"
        else:
            templateData.insert((randint(0, line_count - 1) + 6), "\t\t\t\"" + website + "\"\n")
        print("Processed " + str(line_count) + " lines. Number: " + str(line_count) + " = " + website)



#making new file for the new config.json
with open("cleanConfig.json", "w+") as file:
    file.writelines(templateData)
