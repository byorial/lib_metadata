
# -*- coding: utf-8 -*-
import time

import requests
import traceback

from lxml import html

from framework import SystemModelSetting, py_urllib
from framework.util import Util
from system import SystemLogicTrans

from .plugin import P
logger = P.logger

class SiteUtil(object):
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie' : 'over18=1;age_check_done=1;',
    } 

    @staticmethod 
    def get_tree(url, proxy_url=None, headers=None):
        return html.fromstring(SiteUtil.get_text(url, proxy_url=proxy_url, headers=headers))
    
    @staticmethod 
    def get_text(url, proxy_url=None, headers=None):
        proxies = None
        if proxy_url is not None and proxy_url != '':
            proxies = {"http"  : proxy_url, "https" : proxy_url}
        if headers is None:
            headers = SiteUtil.default_headers

        res = requests.get(url, headers=headers, proxies=proxies)
        if res.status_code != 200:
            return None
        #logger.debug(headers)
        #logger.debug(res.text)
        return res.text


    @staticmethod
    def process_image_mode(image_mode, image_url, proxy_url=None):
        ret = image_url
        if image_mode == '1':
            tmp = '{ddns}/metadata/api/image_proxy?url=' + py_urllib.quote_plus(image_url)
            if proxy_url is not None:
                tmp += '&proxy_url=' + py_urllib.quote_plus(proxy_url)
            ret = Util.make_apikey(tmp)
        elif image_mode == '2':
            tmp = '{ddns}/metadata/api/discord_proxy?url=' + py_urllib.quote_plus(image_url)
            ret = Util.make_apikey(tmp)
        elif image_mode == '3':
            from framework.common.notify import discord_proxy_image
            ret = discord_proxy_image(image_url)
        elif image_mode == '4': #landscape to poster
            ret = '{ddns}/metadata/normal/image_process.jpg?mode=landscape_to_poster&url=' + py_urllib.quote_plus(image_url)
            ret = ret.format(ddns=SystemModelSetting.get('ddns'))
            #ret = Util.make_apikey(tmp)

        return ret

    av_genre = {u'巨尻':u'큰엉덩이', u'ギャル':u'갸루', u'着エロ':u'착에로', u'競泳・スクール水着':u'학교수영복', u'日焼け':u'태닝', u'指マン':u'핑거링', u'潮吹き':u'시오후키', u'ごっくん':u'곳쿤', u'パイズリ':u'파이즈리', u'手コキ':u'수음', u'淫語':u'음란한말', u'姉・妹':u'남매', u'お姉さん':u'누님', u'インストラクター':u'트레이너', u'ぶっかけ':u'붓카케', u'シックスナイン':u'69', u'ボディコン':u'타이트원피스', u'電マ':u'전동마사지', u'イタズラ':u'짖궂음', u'足コキ':u'풋잡', u'原作コラボ':u'원작각색', u'看護婦・ナース':u'간호사', u'コンパニオン':u'접객업', u'家庭教師':u'과외', u'キス・接吻':u'딥키스', u'局部アップ':u'음부확대', u'ポルチオ':u'자궁성감자극', u'セーラー服':u'교복', u'イラマチオ':u'격한페라·딥스로트', u'投稿':u'투고', u'キャンギャル':u'도우미걸', u'女優ベスト・総集編':u'베스트총집편', u'クンニ':u'커닐링구스', u'アナル':u'항문노출', u'超乳':u'폭유', u'復刻':u'리마스터', u'投稿':u'투고', u'義母':u'새어머니', u'おもちゃ':u'노리개', u'くノ一':u'여자닌자', u'羞恥' : u'수치심', u'ドラッグ':u'최음제', u'パンチラ':u'판치라', u'巨乳フェチ':u'큰가슴', u'巨乳':u'큰가슴', u'レズキス':u'레즈비언', u'レズ':u'레즈비언', u'スパンキング':u'엉덩이때리기', u'放尿・お漏らし':u'방뇨·오모라시', u'アクメ・オーガズム':u'절정·오르가즘', u'ニューハーフ':u'쉬메일', u'鬼畜':u'색마·양아치', u'辱め':u'능욕', u'フェラ':u'펠라치오'}

    av_genre_ignore_ja = [u'DMM獨家']

    av_genre_ignore_ko = [u'고화질', u'독점전달', u'세트상품', u'단체작품', u'기간한정세일', u'기리모자', u'데지모', u'슬림', u'미소녀', u'미유', u'망상족', u'거유', u'에로스', u'작은', u'섹시']

    av_studio  = {u'乱丸':u'란마루', u'大洋図書':u'대양도서', u'ミル':u'미루', u'無垢':u'무쿠', u'サムシング':u'Something', u'本中':u'혼나카', u'ナンパJAPAN':u'난파 재팬', u'溜池ゴロー':u'다메이케고로', u'プラム':u'프라무', u'アップス':u'Apps', u'えむっ娘ラボ':u'엠코 라보', u'クンカ':u'킁카', u'映天':u'에이텐', u'ジャムズ':u'JAMS', u'牛感':u'규칸'}


    

    @staticmethod
    def trans(text, do_trans=True, source='ja', target='ko'):
        if do_trans:
            return SystemLogicTrans.trans(text, source=source, target=target)
        return text


    @staticmethod
    def discord_proxy_get_target(image_url):
        from framework.common.notify import discord_proxy_get_target 
        return discord_proxy_get_target(image_url)
    
    @staticmethod
    def discord_proxy_get_target_poster(image_url):
        from framework.common.notify import discord_proxy_get_target 
        return discord_proxy_get_target(image_url + 'av_poster')
    

    @staticmethod
    def discord_proxy_set_target(source, target):
        from framework.common.notify import discord_proxy_set_target 
        return discord_proxy_set_target(source, target)

    @staticmethod
    def discord_proxy_set_target_poster(source, target):
        from framework.common.notify import discord_proxy_set_target 
        return discord_proxy_set_target(source + 'av_poster', target)


    @staticmethod
    def get_image_url(image_url, image_mode, proxy_url=None, with_poster=False):
        try:
            ret = {}
            tmp = SiteUtil.discord_proxy_get_target(image_url)
            if tmp is None:
                ret['image_url'] = SiteUtil.process_image_mode(image_mode, image_url, proxy_url=proxy_url)
            else:
                ret['image_url'] = tmp

            if with_poster:
                ret['poster_image_url'] = SiteUtil.discord_proxy_get_target_poster(image_url)
                if ret['poster_image_url'] is None:
                    tmp = SiteUtil.process_image_mode('4', ret['image_url']) #포스터이미지 url 본인 sjva
                    #if image_mode == '3': # 디스코드 url 모드일때만 포스터도 디스코드로
                    ret['poster_image_url'] = SiteUtil.process_image_mode('3', tmp) #디스코드 url / 본인 sjva가 소스이므로 공용으로 등록
                    SiteUtil.discord_proxy_set_target_poster(image_url, ret['poster_image_url'])
            
        except Exception as exception: 
            logger.error('Exception:%s', exception)
            logger.error(traceback.format_exc())
        return ret