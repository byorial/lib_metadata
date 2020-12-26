
# -*- coding: utf-8 -*-
import requests
import traceback

from lxml import html

from framework import SystemModelSetting
from framework.util import Util
from system import SystemLogicTrans

from .plugin import P
from .entity_av import EntityAVSearch
from .entity_base import EntityMovie, EntityThumb, EntityActor, EntityRatings
from .site_util import SiteUtil

logger = P.logger

site_name = 'javbus'
site_base_url = 'https://www.javbus.com'
module_char = 'C'
site_char = 'B'

class SiteJavbus(object):
    @staticmethod 
    def search(keyword, do_trans=True, proxy_url=None, image_mode='0'):
        try:
            ret = {'data':[]}
            keyword = keyword.strip().lower()
            # 2020-06-24
            
            if keyword[-3:-1] == 'cd':
                keyword = keyword[:-3]
            keyword = keyword.replace(' ', '-')
            url = '{site_base_url}/search/{keyword}'.format(site_base_url=site_base_url, keyword=keyword)
            tree = SiteUtil.get_tree(url, proxy_url=proxy_url)
            #lists = tree.xpath('//*[@id="waterfall"]/div')
            lists = tree.xpath('//a[@class="movie-box"]')
            
            for node in lists:
                try:
                    item = EntityAVSearch(site_name)
                    tag = node.xpath('.//img')[0]
                    item.image_url = tag.attrib['src'].lower()
                    tmp = SiteUtil.discord_proxy_get_target(item.image_url)
                    if tmp is None:
                        item.image_url = SiteUtil.process_image_mode(image_mode, item.image_url, proxy_url=proxy_url)
                    else:
                        item.image_url = tmp
                    tag = node.xpath('.//date')
                    item.ui_code = tag[0].text_content().strip()
                    item.code = module_char + site_char + node.attrib['href'].split('/')[-1]
                    item.desc = u'발매일 : ' + tag[1].text_content().strip()
                    item.year = int(tag[1].text_content().strip()[:4])
                    item.title = item.title_ko = node.xpath('.//span/text()')[0].strip()
                    if do_trans:
                        item.title_ko = SystemLogicTrans.trans(item.title, source='ja', target='ko')
                    item.score = 100 if keyword.lower() == item.ui_code.lower() else 60 - (len(ret['data'])*10)
                    if item.score < 0:
                        item.socre = 0
                    #logger.debug(item)
                    ret['data'].append(item.as_dict())
                except Exception as exception: 
                    logger.error('Exception:%s', exception)
                    logger.error(traceback.format_exc()) 
            ret['data'] = sorted(ret['data'], key=lambda k: k['score'], reverse=True) 
            ret['ret'] = 'success'
            return ret
        except Exception as exception: 
            logger.error('Exception:%s', exception)
            logger.error(traceback.format_exc())
            ret['ret'] = 'exception'
            ret['data'] = str(exception)
        return ret


    @staticmethod 
    def info(code, do_trans=True, proxy_url=None, image_mode='0'):
        try:
            ret = {}
            url = '{site_base_url}/{code}'.format(site_base_url=site_base_url, code=code[2:])
            tree = SiteUtil.get_tree(url, proxy_url=proxy_url)

            entity = EntityMovie(site_name, code)
            entity.country = [u'일본']
            entity.mpaa = u'청소년관람불가'
            entity.thumb = []
            tag = tree.xpath('/html/body/div[5]/div[1]/div[1]/a/img')[0]
            
            data = SiteUtil.get_image_url(tag.attrib['src'], image_mode, proxy_url=proxy_url, with_poster=True)
            entity.thumb.append(EntityThumb(aspect='landscape', value=data['image_url']))
            entity.thumb.append(EntityThumb(aspect='poster', value=data['poster_image_url']))
            
            tags = tree.xpath('/html/body/div[5]/div[1]/div[2]/p')
            for tag in tags:
                tmps = tag.text_content().strip().split(':')
                if len(tmps) == 2:
                    key = tmps[0].strip()
                    value = tmps[1].strip()
                elif len(tmps) == 1:
                    value = tmps[0].strip().replace(' ', '').replace('\t', '').replace('\r\n', ' ')
                
                if value == '':
                    continue
                
                logger.debug('key:%s value:%s', key, value)
                #if key == u'識別碼:'
                if key == u'識別碼':
                    entity.title = entity.originaltitle = entity.sorttitle = value
                elif key == u'發行日期':
                    entity.premiered = value
                    entity.year = int(value[:4])
                elif key == u'長度':
                    entity.runtime = int(value.replace(u'分鐘', '')) 
                elif key == u'導演':
                    entity.director = value
                elif key == u'製作商':
                    entity.studio = value
                    if do_trans:
                        if value in SiteUtil.av_studio:
                            entity.studio = SiteUtil.av_studio[value]
                        else:
                            entity.studio = SiteUtil.trans(value, do_trans=do_trans)
                #elif key == u'發行商':
                #    entity.studio = value
                elif key == u'系列':
                    entity.tag = [SiteUtil.trans(value, do_trans=do_trans), entity.title.split('-')[0]]
                elif key ==  u'類別':
                    entity.genre = []
                    for tmp in value.split(' '):
                        if tmp in SiteUtil.av_genre:
                            entity.genre.append(SiteUtil.av_genre[tmp])
                        elif tmp in SiteUtil.av_genre_ignore_ja:
                            continue
                        else:
                            genre_tmp = SiteUtil.trans(tmp, do_trans=do_trans).replace(' ', '')
                            if genre_tmp not in SiteUtil.av_genre_ignore_ko:
                                entity.genre.append(genre_tmp)
                elif key == u'演員':
                    if value.find(u'暫無出演者資訊') != -1:
                        continue
                    entity.actor = []
                    for tmp in value.split(' '):
                        entity.actor.append(EntityActor(tmp))
            entity.tagline = SiteUtil.trans(tree.xpath('/html/body/div[5]/h3/text()')[0].strip(), do_trans=do_trans).replace(entity.title, '').strip()
            entity.plot = entity.tagline

            tags = tree.xpath('//*[@id="sample-waterfall"]/a')
            entity.fanart = []
            for tag in tags:
                entity.fanart.append(SiteUtil.process_image_mode(image_mode, tag.attrib['href'], proxy_url=proxy_url))


            ret['data'] = entity.as_dict()
            ret['ret'] = 'success'
            return ret
        except Exception as exception: 
            logger.error('Exception:%s', exception)
            logger.error(traceback.format_exc())
            ret['ret'] = 'exception'
            ret['data'] = str(exception)
        return ret