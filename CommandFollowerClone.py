import subprocess

FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS
SubsDir = "$PWD/Subs/**"
VidsDir = "Vids/"

#Vidscmd = 'ls ' + Dir + ' *.mp4'


def FindFile(Dir):
    cmd = 'ls ' + Dir
    Proc = subprocess.Popen(cmd,
                                shell=True,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
    output, _ = Proc.communicate()
    FileNames = output.split("\n") # list of names
    return FileNames

VideosNames = FindFile(VidsDir)
SubsNames = FindFile(SubsDir)

print VideosNames
print SubsNames

cmdFFPEG = [FFMPEG_BIN,
           '-y',
           '-i',           'batman.and.harley.quinn.2017.german.bdrip.x264-contribution.mkv',
           '-ss',          '00:00:30.000',
           '-t',           '00:00:40.000',
           '-c',           'copy',
           'foo1.mp4']
