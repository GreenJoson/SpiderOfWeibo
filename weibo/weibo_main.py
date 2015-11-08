#coding:utf-8
import urllib2
import post_encode
from weibo_login import WeiboLogin
import get_weibo
if __name__ == '__main__':
	Login = WeiboLogin('用户名', '密码')
	if Login.login() == True:
		print "登录成功"
	#可以根据page来循环以便达到爬取多页的目的
	html = urllib2.urlopen("http://s.weibo.com/weibo/%25E9%2583%2591%25E7%2588%25BD&page=2").read()
	#调用解析html内容的函数		
	get_weibo.write_all_info(html)