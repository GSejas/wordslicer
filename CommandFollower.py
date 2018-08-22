FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS

import subprocess
# command = [FFMPEG_BIN,
#            '-y',
#            '-i',           'IBM Rational DOORS - Linking and traceability-2tN_cVQP214.mp4',
#           # '-vcodec',      'copy',
#           # '-acodec',      'copy',
#            '-ss',          '00:00:01.000',
#            '-t',           '00:00:10.000',
#          #  '-c',      'copy',
#            '-c:v',      'libx264',
#            '-c:a',      'aac',
#            '-strict',      'experimental',
#            #'-map', '0'
#            'foo1.mp4'
#            ]
command = [FFMPEG_BIN,
           '-y',
           '-i',           'Vids/roor-bayonetta-sd.mkv',
          # '-vcodec',      'copy',
          # '-acodec',      'copy',
           '-ss',          '00:00:10.000',
           '-t',           '00:00:40.000',
           '-c',      'copy',
           #'-c:v',      'libx264',
           #'-c:a',      'aac',
           #'-strict',      'experimental',
           #'-map', '0'
           'TMP/foo1.mp4'
           ]
ffmpeg_p = subprocess.Popen(command,
                            stderr=subprocess.PIPE)

output, _ = ffmpeg_p.communicate()
print(_)
