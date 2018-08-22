# -*- coding: utf-8 -*-
from SubParsev2 import StrReader
import subprocess
import os

FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS
MKVMERGE_BIN = "mkvmerge" # on Linux ans Mac OS




class ParserExtended(StrReader):

    SubsDir = ""
    VidsDir = ""
    ResultDir = ""

    def __init__(self, SearchedWord, SubsDir, VidsDir, ResultDir):

        self.searchWord = SearchedWord
        self.SubsDir = SubsDir
        self.VidsDir = VidsDir
        self.ResultDir = ResultDir

    def ParseListSRTs(self):
        SubsNameList = self.FindFile(self.SubsDir)
        VidsNameList = self.FindFile(self.VidsDir)
        tmpVideoNames = []
        j = 0

        aaa = open("run_this.sh", "a")
        for srtFileName in SubsNameList:
            if len(srtFileName):
                tmpList = self.ParseFile(srtFileName)
                self.SubList2File('TMP/'+srtFileName[(len(srtFileName)-7):-4]+ "_tmp.srt", tmpList) # le ponemos un nombre cualquier
                for i in range(len(tmpList)): # en este bloque hacemos el video slice de la lista temporal
                    startH = tmpList[i][0].hours
                    startM = tmpList[i][0].minutes
                    startS = tmpList[i][0].seconds
                    endH = tmpList[i][2].hours
                    endM = tmpList[i][2].minutes
                    endS = tmpList[i][2].seconds
                    StartTime = "%02d:%02d:%06.3f" % (startH, startM, startS)
                    Duration = "%02d:%02d:%06.3f" % (endH, endM, endS)
                    print "Start time " + StartTime
                    print "Duration " + Duration
                    InputName = "Vids/"+VidsNameList[j]
                    OutputName = 'TMP/'+VidsNameList[j][:-4]+'%s' % i+'_TMP.mkv'
                    tmpVideoNames.append(OutputName)
                    print "*****************************************************"
                    print "** "
                    print "**    Beginning to slice Clip from Original VIDEO"
                    print "**"
                    print "*Input    " + InputName
                    print "**"
                    print "*Output:*    " + OutputName
                    print "**"
                    print "**    " + tmpList[i][3][0]
                    print "*****************************************************"
                    self.VideoSlicer(aaa,StartTime, Duration, InputName, OutputName)
                j = j + 1
        gg = open("tmp_Video_list.txt", "w")
        for Name in tmpVideoNames:
            gg.write("file '"+Name+"'\n")
        gg.close()



        self.SubsList = self.ReOffset(self.SubsList)
        self.SubList2File('Video_'+ self.searchWord + ".srt", self.SubsList)

        # Here we concatenate the temporal videos
        aaa.close()
      #  subprocess.call(['bash', 'run_this.sh'])
        self.VideoConcat()


    def FindFile(self, Dir):
        cmd = 'ls ' + Dir
        Proc = subprocess.Popen(cmd,
                                shell=True,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)

        output, _ = Proc.communicate()
        FileNames = output.split("\n")  # list of names
        return FileNames

    def VideoSlicer(self, aaa, StartTime, Duration, InputName, OutputName):
        aaa.write("ffmpeg -y -i '"+InputName+"' -ss "+StartTime+" -t "+Duration+" -vcodec libx264 -crf 35 '"+OutputName+"'\n")
#
#        cmdFFPEG = [FFMPEG_BIN,
#                    '-y',
#                    '-i',                    InputName,
#                    '-ss',                    StartTime,
##                    '-t',                       Duration,
 #                   '-vcodec', 'libx264',
 #                   '-crf',                    '35',
 #                   OutputName]
 #       ffmpeg_p = subprocess.Popen(cmdFFPEG, stderr=subprocess.PIPE)

#        output, _ = ffmpeg_p.communicate()
#        print(output)
#        print(_)

    def VideoConcat(self):
        OutputStringFile = 'Video_'+self.searchWord+'.mkv'
        OutputStringFile3 = 'VideoWsrt_'+self.searchWord+'.mkv'


        cmdFFPEG = [FFMPEG_BIN,
                   # '-f',
          #          '-r', "20",
          #          '-s', "960x540",
                    '-f',                    'concat',
                    '-safe',                    '0',
                    '-i',                       "tmp_Video_list.txt",
                    '-acodec', 'copy',
                    OutputStringFile]
        ffmpeg_p = subprocess.Popen(cmdFFPEG, stderr=subprocess.PIPE)

        output, _ = ffmpeg_p.communicate()

        print(_)

        OutputSubsFile = 'Video_'+self.searchWord+'.srt'

        cmdFFPEG2 = [MKVMERGE_BIN,
                    '-o',                    OutputStringFile3,
                    OutputStringFile,
                    OutputSubsFile]

        ffmpeg_p2 = subprocess.Popen(cmdFFPEG2, stderr=subprocess.PIPE)

        output, _ = ffmpeg_p2.communicate()

        print(_)



VidsDir = "Vids"
SubsDir = "$PWD/Subs/**"
OutDir = ""
ListWords = ["hatt","verrat","wird","wurd","befehl","begin","entl","erzieh"]
# os.remove("run_this.txt")
aaa = open("run_this.sh", "w")
aaa.write("")
aaa.close()
for i in ListWords:
    ClassObject = ParserExtended(i, SubsDir, VidsDir, OutDir)
    ClassObject.ParseListSRTs()