# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import sanitized_Request


class MasterClassIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?masterclass\.com/classes/[a-z\-]+/chapters/(?P<id>[a-z\-]+)/watch'
    _TEST = {
        'url': 'https://www.masterclass.com/classes/judy-blume-teaches-writing/chapters/jbl-introduction/watch',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': 'jbl-introduction',
            'ext': 'mp4',
            'title': '',
            'thumbnail': r're:^https?://.*\.jpg$',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_initialize(self):
        self._login()

    def _download_webpage(self, url_or_request, *args, **kwargs):
        request = (url_or_request if isinstance(url_or_request, compat_urllib_request.Request)
                   else sanitized_Request(url_or_request))
        request.add_header('Accept-Language', '*')
        return super(MasterClassIE, self)._download_webpage(request, *args, **kwargs)

    def _login(self):
        username, password = self._get_login_info()
        if username is None:
            return

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')

        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }
