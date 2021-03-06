
# -*- coding: utf-8 -*-
from .plugin import P
logger = P.logger

class EntityRatings(object):
    def __init__(self, value, max=10, votes=0, name='', image_url=''):
        self.name = name
        self.max = max
        self.default = True
        self.value = value
        self.votes = votes
        self.image_url = image_url

    def __repr__(self):
        tmp = 'name : %s\n' % self.name
        tmp += 'value : %s\n' % self.value
        tmp += 'max : %s\n' % self.max
        return tmp


    def as_dict(self):
        return {
            'name' : self.name,
            'max' : self.max,
            'default' : self.default,
            'value' : self.value,
            'votes' : self.votes,
            'image_url' : self.image_url,
        }

class EntityThumb(object):
    def __init__(self, aspect='', value='', thumb='', site='', score=0):
        # banner, clearart, clearlogo, discart, landscape, poster
        self.aspect = aspect 
        self.value = value  #원본 url
        self.thumb = thumb  #썸네일 url
        self.site = site
        self.score = score

    def as_dict(self):
        return {
            'aspect' : self.aspect,
            'value' : self.value,
            'thumb' : self.thumb,
            'site' : self.site,
            'score' : self.score,
        }

"""
class EntityArt(object):
    def __init__(self, aspect='', url='', thumb_url='', site='', score=0):
        # banner, clearart, clearlogo, discart, landscape, poster
        self.aspect = aspect 
        self.url = url  #원본 url
        self.thumb_url = thumb_url  #썸네일 url
        self.site = site
        self.score = score

    def as_dict(self):
        return {
            'aspect' : self.aspect,
            'url' : self.value,
            'thumb_url' : self.thumb,
            'site' : self.site,
            'score' : self.score,
        }
"""

class EntityActor(object):
    def __init__(self, name, site=''):
        self.name = ''
        self.name2 = ''
        self.role = ''
        self.order = ''
        self.thumb = ''
        self.originalname = name
        self.site = site
        self.type = ''

    def as_dict(self):
        return {
            'name' : self.name,
            'role' : self.role,
            'order' : self.order,
            'thumb' : self.thumb,
            'originalname' : self.originalname,
            'site' : self.site,
            'name2' : self.name2,
            'type' : self.type,
        }
    

class EntityExtra(object):
    def __init__(self, content_type, title, mode, content_url, premiered=None, thumb=None):
        self.content_type = content_type #PrimaryTrailer Trailer, DeletedScene, BehindTheScenes, Interview, SceneOrSample, Featurette, Short, Other
        self.content_url = content_url
        self.title = title
        self.mode = mode #mp4
        self.premiered = premiered
        self.thumb = thumb
        

    def as_dict(self):
        return {
            'content_type' : self.content_type,
            'content_url' : self.content_url,
            'title' : self.title,
            'mode' : self.mode,
            'premiered' : self.premiered,
            'thumb' : self.thumb,
        }


class EntityExtra2(object):
    def __init__(self):
        self.content_type = 'Trailer' #PrimaryTrailer Trailer, DeletedScene, BehindTheScenes, Interview, SceneOrSample, Featurette, Short, Other
        self.content_url = ''
        self.title = ''
        self.mode = ''
        self.premiered = '1900-01-01'
        self.thumb = ''
        

    def as_dict(self):
        return {
            'content_type' : self.content_type,
            'content_url' : self.content_url,
            'title' : self.title,
            'mode' : self.mode,
            'premiered' : self.premiered,
            'thumb' : self.thumb,
        }


class EntityMovie(object):
    # https://kodi.wiki/view/NFO_files/Movies
    def __init__(self, site, code):
        self.site = site
        self.code = code  # uniqueid

        self.title = None
        self.originaltitle = None
        self.sorttitle = None
        self.ratings = None
        self.userrating = None
        self.plot = None
        self.runtime = None
        self.thumb = None
        self.fanart = None
        self.genre = None
        self.country = None
        self.credits = None
        self.director = None
        self.premiered = None
        self.year = None
        self.studio = None
        self.trailer = None
        self.actor = None
        self.tag = None #colletion
        self.tagline = None
        self.extras = None
        self.mpaa = None
        """
        self.top250 = None
        self.outline = None
        
        """

    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title
        tmp += 'originaltitle : %s\n' % self.originaltitle
        return tmp


    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,
            'originaltitle' : self.originaltitle,
            'sorttitle' : self.sorttitle,
            'ratings' : [x.as_dict() for x in self.ratings] if self.ratings is not None else None,
            'userrating' : self.userrating,
            'plot' : self.plot,
            'runtime' : self.runtime,
            'thumb' : [x.as_dict() for x in self.thumb] if self.thumb is not None else None,
            'fanart' : self.fanart,
            'genre' : self.genre,
            'country' : self.country,
            'credits' : self.credits,
            'director' : self.director,
            'premiered' : self.premiered,
            'year' : self.year,
            'studio' : self.studio,
            'trailer' : self.trailer,
            'actor' : [x.as_dict() for x in self.actor] if self.actor is not None else None,
            'tag' : self.tag,
            'tagline' : self.tagline,
            'extras' :  [x.as_dict() for x in self.extras] if self.extras is not None else None,
            'mpaa' : self.mpaa
        }





class EntitySearchItemTvDaum(object):
    def __init__(self, site):
        self.site = site
        self.code = ''
        self.title = ''
        self.year = ''        
        self.image_url = ''        
        self.desc = ''
        self.score = 0
        

        self.status = 1 #1:방송중, 0:방송종료, 2:방송예정
        self.extra_info = ''
        self.studio = ''
        self.broadcast_info = ''
        self.broadcast_term = ''
        self.series = []
        self.equal_name = []

        self.genre = ''
        self.episode = -1

    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title        
        tmp += 'year : %s\n' % self.year        
        tmp += 'image_url : %s\n' % self.image_url
        tmp += 'desc : %s\n' % self.desc
        tmp += 'score : %s\n' % self.score

        tmp += 'status : %s\n' % self.status
        tmp += 'extra_info : %s\n' % self.extra_info
        tmp += 'studio : %s\n' % self.studio
        tmp += 'broadcast_info : %s\n' % self.broadcast_info
        tmp += 'broadcast_term : %s\n' % self.broadcast_term
        tmp += 'series : %s\n' % self.series

        return tmp


    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,            
            'year' : self.year,            
            'image_url' : self.image_url,
            'desc' : self.desc,            
            'score' : self.score,
            'status' : self.status,
            'extra_info' : self.extra_info,
            'studio' : self.studio,
            'broadcast_info' : self.broadcast_info,
            'broadcast_term' : self.broadcast_term,
            'series' : self.series,
            'equal_name' : self.equal_name,
            'genre' : self.genre,
            'episode' : self.episode,

        }


class EntitySearchItemTv(object):
    def __init__(self, site):
        self.site = site
        self.code = ''
        self.title = ''
        self.image_url = ''
        self.studio = ''
        self.genre = ''

        self.year = ''        
        self.desc = ''
        self.score = 0
        self.status = 1 #1:방송중, 0:방송종료, 2:방송예정
        self.extra_info = ''
        self.broadcast_info = ''
        self.broadcast_term = ''
        self.series = []
        self.equal_name = []
        self.episode = -1

    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title        
        return tmp


    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,            
            'image_url' : self.image_url,
            'studio' : self.studio,
            'genre' : self.genre,
            'score' : self.score,
        }
        """
            'year' : self.year,            
            'desc' : self.desc,            
            
            'status' : self.status,
            'extra_info' : self.extra_info,
            'broadcast_info' : self.broadcast_info,
            'broadcast_term' : self.broadcast_term,
            'series' : self.series,
            'equal_name' : self.equal_name,
            'episode' : self.episode,
        """



class EntityShow(object):
    # https://kodi.wiki/view/NFO_files/Movies
    def __init__(self, site, code):
        self.site = site
        self.code = code  # uniqueid

        self.title = ''
        self.originaltitle = ''
        self.sorttitle = ''
        self.ratings = []
        self.userrating = ''

        self.season = 1 # 시즌카운트
        self.episode = 0 # 에피소드 카운트
        self.plot = ''
        self.tagline = ''
        self.thumb = []
        self.fanart = []
        self.mpaa = ''
        
        self.genre = []
        self.tag = [] #colletion
        self.premiered = ''
        self.year = ''
        self.status = 1 #1:방송중, 2:방송종료, 0:방송예정
        self.studio = ''
        self.trailer = ''
        self.actor = []
        self.namedseason = []

        # kodi spec에 없음.
        self.country = [] #없음
        self.credits = [] #에피소드  #극본
        self.director = [] #에피소드 #감독
        self.extras = []

        self.extra_info = {'episodes':{}}


    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title
        tmp += 'originaltitle : %s\n' % self.originaltitle
        return tmp


    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,
            'originaltitle' : self.originaltitle,
            'sorttitle' : self.sorttitle,
            'ratings' : [x.as_dict() for x in self.ratings] if self.ratings is not None else None,
            'userrating' : self.userrating,
            'season' : self.season,
            'episode' : self.episode,
            'plot' : self.plot,
            'tagline' : self.tagline,
            'thumb' : [x.as_dict() for x in self.thumb] if self.thumb is not None else None,
            'fanart' : self.fanart,
            'mpaa' : self.mpaa,
            'genre' : self.genre,
            'tag' : self.tag,
            'premiered' : self.premiered,
            'year' : self.year,
            'status' : self.status,
            'studio' : self.studio,
            'trailer' : self.trailer,
            'actor' : [x.as_dict() for x in self.actor] if self.actor is not None else None,
            'country' : self.country,
            'credits' : [x.as_dict() for x in self.credits] if self.credits is not None else None,
            'director' :  [x.as_dict() for x in self.director] if self.director is not None else None,
            'extras' :  [x.as_dict() for x in self.extras] if self.extras is not None else None,
            'extra_info' : self.extra_info,
        }


class EntityEpisode(object):

    def __init__(self, site, code):
        self.site = site
        #self.parent_code = parent_code
        self.code = code  # uniqueid
        self.episodedetails = ''
        self.title = ''
        self.originaltitle = ''
        self.showtitle = ''
        self.ratings = []
        self.userrating = ''
        self.season = 1 # 시즌카운트
        self.episode = 0 # 에피소드 카운트
        self.plot = ''
        self.tagline = ''
        self.runtime = 0
        self.thumb = []
        self.premiered = ''
        self.year = ''
        self.extras = []
        self.extra_info = {}
        self.mpaa = ''

    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title
        tmp += 'originaltitle : %s\n' % self.originaltitle
        return tmp


    def as_dict(self):
        return {
            'site' : self.site,
            #'parent_code' : self.parent_code,
            'code' : self.code,
            'episodedetails' : self.episodedetails,
            'title' : self.title,
            'originaltitle' : self.originaltitle,
            'showtitle' : self.showtitle,
            'ratings' : [x.as_dict() for x in self.ratings] if self.ratings is not None else None,
            'userrating' : self.userrating,
            'season' : self.season,
            'episode' : self.episode,
            'plot' : self.plot,
            'tagline' : self.tagline,
            'runtime' : self.runtime,
            'thumb' : [x.as_dict() for x in self.thumb] if self.thumb is not None else None,
            'premiered' : self.premiered,
            'year' : self.year,
            'extras' :  [x.as_dict() for x in self.extras] if self.extras is not None else None,
            'extra_info' : self.extra_info,
            'mpaa' : self.mpaa,
        }



class EntitySearchItemMovie(object):
    def __init__(self, site):
        self.site = site
        self.code = ''
        self.title = ''
        self.title_en = ''
        
        self.image_url = ''
        self.year = 1900
        self.desc = ''
        self.extra_info = {}
        self.score = 0
        self.originaltitle = ''

    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title        
        return tmp

    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,   
            'title_en' : self.title_en,         
            'image_url' : self.image_url,
            'year' : self.year,
            'desc' : self.desc,
            'extra_info' : self.extra_info,
            'score' : self.score,
            'originaltitle': self.originaltitle,
        }
        """
            'year' : self.year,            
            'desc' : self.desc,            
            
            'status' : self.status,
            'extra_info' : self.extra_info,
            'broadcast_info' : self.broadcast_info,
            'broadcast_term' : self.broadcast_term,
            'series' : self.series,
            'equal_name' : self.equal_name,
            'episode' : self.episode,
        """

class EntityMovie2(object):
    def __init__(self, site, code):
        self.site = site
        self.code = code  # uniqueid

        self.title = ''
        self.originaltitle = ''
        self.sorttitle = ''

        self.ratings = []
        self.genre = []
        self.country = []
        self.runtime = 0
        self.premiered = ''
        self.year = 1900
        self.mpaa = ''
        self.tagline = ''
        self.plot = ''
        self.extra_info = {}

        self.actor = []
        self.credits = []
        self.director = []
        self.producers = []
        self.studio = ''

        self.userrating = ''
        self.art = []
        #self.fanart = []
        #self.trailer = []
        self.tag = [] #colletion
        self.extras = []
        self.review = []
        self.code_list = []
        
        

    def __repr__(self):
        tmp = 'site : %s\n' % self.site
        tmp += 'code : %s\n' % self.code
        tmp += 'title : %s\n' % self.title
        tmp += 'originaltitle : %s\n' % self.originaltitle
        return tmp


    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,
            'originaltitle' : self.originaltitle,
            'sorttitle' : self.sorttitle,

            'ratings' : [x.as_dict() for x in self.ratings] if self.ratings is not None else None,
            'genre' : self.genre,
            'country' : self.country,
            'runtime' : self.runtime,
            'premiered' : self.premiered,
            'year' : self.year,
            'mpaa' : self.mpaa,
            'tagline' : self.tagline,
            'plot' : self.plot,
            'extra_info' : self.extra_info,
            'actor' : [x.as_dict() for x in self.actor] if self.actor is not None else None,
            'credits' : self.credits,
            'director' : self.director,
            'producers' : self.producers,
            'studio' : self.studio,
            'art' : [x.as_dict() for x in self.art] if self.art is not None else None,
            
            #'fanart' : self.fanart,
            #'trailer' : self.trailer,
            
            'tag' : self.tag,
            'userrating' : self.userrating,
            'extras' :  [x.as_dict() for x in self.extras] if self.extras is not None else None,
            'review' : [x.as_dict() for x in self.review] if self.review is not None else None,
            'code_list' : self.code_list,
        }

class EntityReview(object):
    def __init__(self, site, author='', source='', link='', text='', rating=0):
        self.site = site
        self.author = author
        self.source = source
        self.link = link
        self.text = text
        self.rating = rating

    def as_dict(self):
        return {
            'site' : self.site,
            'author' : self.author,
            'source' : self.source,
            'link' : self.link,
            'text' : self.text,
            'rating' : self.rating,
        }






class EntitySearchItemFtv(object):
    # FU => tvdb
    # W => 왓챠
    # D => 
    # FU
    def __init__(self, site):
        self.site = site
        self.code = ''
        self.title = ''
        self.image_url = ''
        self.studio = ''
        self.premiered = '1900-01-01'
        self.score = 0
        self.status = '' # Continuing, Ended
        self.extra_info = {}
        self.desc = ''
        self.title_original = ''


        #self.title_ko = ''
        self.seasons = []
        self.title_en = ''
        self.country = []
        self.genre = []
        self.year = ''        
        

    def as_dict(self):
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,
            #'title_ko' : self.title_ko,  
            'title_en' : self.title_en,  
            'title_original' : self.title_original,  
            'country' : self.country,  
            'image_url' : self.image_url,
            'studio' : self.studio,
            'genre' : self.genre,
            'extra_info' : self.extra_info,
            'premiered' : self.premiered,  
            'seasons' : self.seasons,  
            'year' : self.year,   
            'desc' : self.desc,                   
            'score' : self.score,
            'status' : self.status,
        }

from collections import OrderedDict

class EntityFtv(object):
    def __init__(self, site, code):
        self.site = site
        self.code = code  # uniqueid

        self.title = ''
        self.originaltitle = ''
        self.mpaa = ''
        self.plot = ''
        self.premiered = ''
        self.year = ''
        self.studio = ''
        self.art = []
        self.genre = []
        self.status = '' #Ended Continuing
        self.season_count = 0
        self.seasons = OrderedDict()
        self.extra_info = {}
        self.actor = []
        self.writer = [] 
        self.director = [] 
        self.extras = []
        self.ratings = []
        


        
        self.sorttitle = ''
        
        self.userrating = ''
        self.season = 1 # 시즌카운트
        self.episode = 0 # 에피소드 카운트
        self.tagline = ''
        self.tag = [] #colletion
        self.trailer = ''
        self.namedseason = []
        # kodi spec에 없음.
        self.country = [] #없음
        

        

    def as_dict(self):
        tmp = dict(self.seasons)
        for key in tmp.keys():
            tmp[key] = tmp[key].as_dict()
        return {
            'site' : self.site,
            'code' : self.code,
            'title' : self.title,
            'originaltitle' : self.originaltitle,
            'mpaa' : self.mpaa,
            'plot' : self.plot,
            'premiered' : self.premiered,
            'year' : self.year,
            'studio' : self.studio,
            'art' : [x.as_dict() for x in self.art] if self.art is not None else None,
            'genre' : self.genre,
            'status' : self.status,
            'seasons' : self.seasons,
            'season_count' : self.season_count,
            'seasons' : tmp,
            'extra_info' : self.extra_info,
            'actor' : [x.as_dict() for x in self.actor] if self.actor is not None else None,
            'writer' : self.writer,
            'director' : self.director,
            'extras' :  [x.as_dict() for x in self.extras] if self.extras is not None else None,
            'ratings' : [x.as_dict() for x in self.ratings] if self.ratings is not None else None,
        }
        """
            
            'sorttitle' : self.sorttitle,
            
            'userrating' : self.userrating,
            'season' : self.season,
            'episode' : self.episode,
            'tagline' : self.tagline,
            'tag' : self.tag,
            
            'trailer' : self.trailer,
            
            'country' : self.country,
            'credits' : [x.as_dict() for x in self.credits] if self.credits is not None else None,
            'director' :  [x.as_dict() for x in self.director] if self.director is not None else None,
            
            
        }
        """


class EntityActor2(object):
    def __init__(self, site='', name='', name_en='', name_ko='', role='', image=''):
        self.site = site
        self.name = name
        self.name_en = name_en
        self.name_ko = name_ko
        self.role = role
        self.image = image

    def as_dict(self):
        return {
            'site' : self.site,
            'name' : self.name,
            'name_en' : self.name_en,
            'name_ko' : self.name_ko,
            'role' : self.role,
            'image' : self.image,
        }

class EntitySeason(object):
    def __init__(self, parent_code, season_no):
        self.parent_code = parent_code
        self.season_no = season_no
        self.art = []
        self.episodes = OrderedDict()
        self.title = ''

    def as_dict(self):
        tmp = dict(self.episodes)
        for key in tmp.keys():
            tmp[key] = tmp[key].as_dict()
        return {
            'parent_code' : self.parent_code,
            'season_no' : self.season_no,
            'art' : [x.as_dict() for x in self.art] if self.art is not None else None,
            'episodes' : tmp,
            'title' : self.title
        }

class EntityEpisode2(object):
    def __init__(self, season_no, episode_no):
        self.season_no = season_no
        self.episode_no = episode_no
        self.art = []
        self.title = ''
        self.plot = ''
        self.guests = []
        self.premiered = ''
        self.rating = ''
        self.is_title_kor = False
        self.is_plot_kor = False



    def as_dict(self):
        return {
            'season_no' : self.season_no,
            'episode_no' : self.episode_no,
            'art' : self.art,
            'title' : self.title,
            'plot' : self.plot,
            'guests' : self.guests,
            'premiered' : self.premiered,
            'rating' : self.rating,
            'directors' : self.directors,
            'writers' : self.writers,
            'is_title_kor' : self.is_title_kor,
            'is_plot_kor' : self.is_plot_kor,
        }