
from lxml import etree
SPIFF_NS = "http://xspf.org/ns/0/"
VLC_NS = "http://www.videolan.org/vlc/playlist/ns/0/"
playlist = etree.Element('playlist', nsmap={None:SPIFF_NS, "vlc":VLC_NS})
title = etree.SubElement(playlist, 'title')
title.text = "MYplaylist"
tracklist = etree.SubElement(playlist, 'trackList')
for i in range(5):
    track = etree.SubElement(tracklist, 'Track')
    location = etree.SubElement(track, 'location')
    location.text = "file://"
    extension = etree.SubElement(track, 'extension', application="http://www.videolan.org/vlc/playlist/0")
    id  = etree.SubElement( extension, etree.QName(VLC_NS, 'id') )
    id.text = str(i)
    option = etree.SubElement( extension, etree.QName(VLC_NS, 'option') )
    option.text = "sub-file="
    option = etree.SubElement( extension, etree.QName(VLC_NS, 'option') )
    option.text = "file-caching=300"

with open('homemade.xml', 'w') as f:
    f.write(etree.tostring(playlist, pretty_print=True).decode("utf-8"))
