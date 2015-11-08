#coding:utf-8
import urllib2
import post_encode
from weibo_login import WeiboLogin
import get_weibo
if __name__ == '__main__':
	Login = WeiboLogin('ruansongsong@gmail.com', '644179052')
	if Login.login() == True:
		print "登录成功"
	html = urllib2.urlopen("http://s.weibo.com/weibo/%25E9%2583%2591%25E7%2588%25BD&page=2").read()
	# print len(html)
	# print html
	# get_weibo.decode_html(html)
	get_weibo.write_all_info(html)