# coding:utf-8

from handlers import weibo, index, fanfou_digest, hot_twitter, toutiao

urls = [
    (r"/", index.MainHandler),
    (r"/weibo", weibo.WeiboHandler),
    (r"/fanfou", fanfou_digest.FanfouDigest),
    (r"/hottwitter", hot_twitter.HotTwitter),
    (r"/toutiao", toutiao.Toutiao),
]
