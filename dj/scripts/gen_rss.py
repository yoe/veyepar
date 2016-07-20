#!/usr/bin/python

# push encoded files to data center box
# uses rsync. 

import os, subprocess
import process

import datetime
import PyRSS2Gen

import django
from main.models import Show, Location, Episode

def make_video_rss(fh, eps):
    items = []                 
    for ep in eps:
        info = PyRSS2Gen.RSSItem(
            title = ep.name,
            description = ep.description,
            guid = PyRSS2Gen.Guid(ep.conf_url),
            pubDate = ep.end,
            link = ep.conf_url,
            enclosure = PyRSS2Gen.Enclosure(
                url = 'http://meetings-archive.debian.net/pub/debian-meetings/%s/%s/%s.webm' % (ep.end.year, ep.show.slug, ep.slug),
                length = os.stat('/home/veyepar/Videos/veyepar/%s/%s/webm/%s.webm' % (ep.show.client.slug, ep.show.slug, ep.slug)).st_size,
                type = 'video/webm',
                )
        )
        items.append(info)
                          
    rss = PyRSS2Gen.RSS2( 
        title = "Debconf 16 video RSS feed",
        link = "https://debconf16.debconf.org",
        description = "The published videos from Debconf 16",
        lastBuildDate = datetime.datetime.now(),
        items = items)

    rss.write_xml(fh, encoding = 'UTF-8')

if __name__ == '__main__':
    django.setup()
    fh = open('rss2.xml', 'w')
    eps = Episode.objects.filter(state='12').filter(show__in='4')
    make_video_rss(fh, eps)
    close(fh)
