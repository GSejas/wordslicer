import re
from io import open
from SubTime import Time

class StrReader(object):

    SubsList  = []
    searchWord = ""

    def __init__(self, SearchedWord):
        self.searchWord = SearchedWord

    def SubList2File(self, FileName, List = []):

        if List.__len__()==0:
            List = self.SubsList

        gg = open(FileName, "w", encoding="latin-1")
        for i in range(len(List)):
             startH = List[i][0].hours
             startM = List[i][0].minutes
             startS = List[i][0].seconds
             endH = List[i][1].hours
             endM = List[i][1].minutes
             endS = List[i][1].seconds
             string1 ='%d\n' % (i+1)
             gg.write(string1.decode('latin-1'))
             stringFirstPart = "%02d:%02d:%06.3f" %(startH, startM, startS)
             stringSecondPart = "%02d:%02d:%06.3f" %(endH, endM, endS)
             thirdString = stringFirstPart[:-4]+","+stringFirstPart[9:]+" --> "+\
                   stringSecondPart[:-4] + "," + stringSecondPart[9:]+"\n"
             gg.write( thirdString.decode('latin-1') )

             for j in range(len(List[i][3])):
                 gg.write(List[i][3][j])
             gg.write(" \n\n".decode('latin-1'))
        gg.close()



    def ReOffset(self, List):
        ZeroStart = Time(0,0,0.0)
        for i in range(len(List)):
            if i == 0:
                #tmpList.append([ZeroStart, List[i][3], List[i][3], ])
                List[i][0] = ZeroStart
                List[i][1] = List[i][2]
            else:
                List[i][0] = List[i-1][1]
                List[i][1] = List[i-1][1] + List[i][2]
        return List

#SearchWord = "\ auf"
#TimeLabel = re.compile('((\d{2}):(\d{2}):(\d{2}(,(\d{3}))?)).*?((\d{2}):(\d{2}):(\d{2}(,(\d*))?))')
#StringPattern = "(<i>)?(.*\n)(<\/i>)?"
#Text = re.compile(StringPattern)
#BigPattern = re.compile('((\d{2}):(\d{2}):(\d{2}(,(\d{3}))?)).*?((\d{2}):(\d{2}):(\d{2}(,(\d*))?))\n(<i>)?(.*)(<\/i>)?\n(<i>)?(.*)(<\/i>)?')
#BigPattern = re.compile(r'(?:(\d{2}):(\d{2}):(\d{2}(?:,(?:\d{3}))?)).*?(?:(\d{2}):(\d{2}):(\d{2}(?:,(?:\d{3}))?))\n(?:<i>)?(.*)(?:<\/i>)?\n(?:<i>)?(.*)(?:<\/i>)?')

    def ParseFile(self, FileName):
        tmpSubsList = []
        with open(FileName, mode="r", encoding="latin-1") as subs:
            WholeText = subs.read()
          #  pattern = r'(?:(\d{2}):(\d{2}):(\d{2}(?:,(?:\d{3}))?)).*?(?:(\d{2}):(\d{2}):(\d{2}(?:,(?:\d{3}))?)).*?\n(?:(?:<i>)?(.*'+searchWord+'?.*)(?:<\/i>)?)(?:\n(?:<i>)?(?:\w|\d|\-)(.*'+searchWord+'?.*)(?:<\/i>)?\n)?'
            pattern = r'(?:(\d{2}):(\d{2}):(\d{2}(?:,(?:\d{3}))?)).*?(?:(\d{2}):(\d{2}):(\d{2}(?:,(?:\d{3}))?)).*?\n(?:(?:<i>)?(.*)(?:<\/i>)?)(?:\n(?:<i>)?((?:\w|\d|\-).*)(?:<\/i>)?\n)?'
            regex = re.compile(pattern, re.IGNORECASE)
            for mach in regex.finditer(WholeText):
                TextList = []
                match = 0
                Start = Time(int(mach.group(1)), int(mach.group(2)), float(mach.group(3).replace(',','.')))
                End = Time(int(mach.group(4)), int(mach.group(5)), float(mach.group(6).replace(',','.')))
                Dif = End - Start


                #print "%s %s %s %s" % (mach.start(), mach.group(1), mach.group(2), mach.group(3) )
                #print "%s %s %s %s" % (mach.start(), mach.group(4), mach.group(5), mach.group(6))
                if 0:
                    if  mach.group(7):
                        #print mach.group(7)
                        TextList.append(mach.group(7))
                        if self.searchWord in mach.group(7):
                            match = 1
                    if  mach.group(8):
                        TextList.append(mach.group(8))
                        #print mach.group(8)
                        if self.searchWord in mach.group(8):
                            match = 1
                    if match == 1:
                        self.SubsList.append([Start, End, Dif,TextList]) #The final list is drawn up
                        tmpSubsList.append([Start, End, Dif,TextList])
        return tmpSubsList
#
# srtFileName = "Keinohrhasen.srt"
# SearWord = "auf"
# SubtitlesFile = StrReader(SearWord)
# SubtitlesFile.ParseFile(srtFileName)
# SubtitlesFile.WriteResult(srtFileName[:-4]+"_tmp.srt")
# SubsList = SubtitlesFile.ReOffset(SubtitlesFile.SubsList)
# SubtitlesFile.WriteResult(srtFileName[:-4]+"_"+SearWord+".srt")
