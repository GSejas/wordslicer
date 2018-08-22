import re
from io import open
from SubTime import Time
import pysubs2
import random
import csv

#
# with open(FileName, mode="r", encoding="latin-1") as subs:
#     WholeText = subs.read()
name = "/home/jorge/Documents/Python Projects/WordSlicer/Subs/Barbara.2012.720p.BluRay.x264.anoXmous_swe.srt"
subs = pysubs2.load(name , encoding="utf-8")
with open("movie_database.csv","a") as mv_db:
#with open("movie_database.csv","wb", encoding="utf-8") as mv_db:
    wr = csv.writer(mv_db, dialect='excel')
    for line in subs:
        hash = random.getrandbits(128)
        # print(line)
        print(line.text)
        print(line.duration)
        print(pysubs2.time.ms_to_str(line.start, True))
        print(pysubs2.time.ms_to_str(line.end, True))
        #wr.writerows([line.text, line.duration, pysubs2.time.ms_to_str(line.start, True), pysubs2.time.ms_to_str(line.end, True)])
        text =  line.text
        dur = line.duration
        startt = pysubs2.time.ms_to_str(line.start, True)
        endt = pysubs2.time.ms_to_str(line.end, True)
        lang =  "sw"

        wr.writerow([line.text, startt, endt])
        #mv_db.write("\""+line.text+"\","+"\""+str(dur)+"\",\""+startt+"\",\""+endt+"\"\n")
    #sa = SSAEvent(start=make_time(s=0), end=make_time(s=line.duration/1000), text="Hello World!")
    # with open("Output/"+str(hash)+".str", "w") as fs:
    #     fs.write("")
    # subs = pysubs2.load("Output/"+str(hash)+".str")
    # subs.insert(0, pysubs2.ssaevent(start=0, end=line.duration, text="New first subtitle"))
    # subs.save()
    #line.save(str(hash)+".str")