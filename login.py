#encoding:utf8
import urllib
import urllib2
import re
def Getaccount():
	port=['4300','4301','4302','4303','4304','4305','4306','4307','4308']
	i=0
	
	headers={
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'Cookie':'RK=0I2uxizPSc; LW_sid=q1f4I9v7k5D7R6O5e4S9p7P8V1; LW_uid=q1Z419f7X5k7n6o5A449A708K2; pgv_pvi=5160215552; tvfe_boss_uuid=d2e9e2992c2f6b14; eas_sid=61Z57067j5p3m9G2x7s9S3d2J6; pac_uid=1_123456789; ptcz=18cfc32c59a21faa22f4c97613a01e184bd5ed3838c42b8d0ac4c41b76873fe9; o_cookie=123456789; pgv_pvid=9730655232; pt2gguin=o0123456789; _qpsvr_localtk=1527494364831; pgv_si=s3689689088; pgv_info=ssid=s250026112; confirmuin=0; ptdrvs=gzHJNsKwyLge2eJpGUpPEsyTJs02UlEErMI1rTCOTl8_; ptvfsession=99a88037b2b433ab61922b20b970bb64c5ea90bc19cb04c8cbe0ef5fbbbb91efef5eefbb321ef3775d04b1301e840b1fce347b7eea0d121a; ptisp=ctc;ETK=; skey=@k8jlvoMlF; ptnick_123456789=e5ad99e98791e58589; _qz_referrer=i.qq.com; pt_login_sig=rJ2-e-RdO-U1BKb64PgKp1WbCqOtwdxctdpenMQXMnGLxG2ZrAUisGboQlV5rlOf; pt_clientip=ca667d47e5b1f515; pt_serverip=86930abf06592ed7; pt_local_token=-1909176059; uikey=b01f2c4333cd59b37cfcca5f8dd2e20f50d17ba13cac145b6ae7d324d3db476a; pt_guid_sig=cf3d82b3651d1715cf4d1fab6d4a32d404e1aea65c3081f6d8ef2fe8e4e4b820; pt_recent_uins=c4ef4c627886a903aec329578da7cdfad8b1ed0642acf27a117548094cbee3f74d00864bf00874333301d1afb3e56d1221590d2a92c5b064; qrsig=qLA88IWo1bVkCs9O-mKn1Dr7sMUXkbnIUxXPOY70n8i5VmsZ0tZsHl9NqXkrj5zF',
	'Host':'localhost.ptlogin2.qq.com:4301',
	'Referer':'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=0',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	while(i<len(port)):
		try:
			req=urllib2.Request(url='https://localhost.ptlogin2.qq.com:'+port[i]+'/pt_get_uins?callback=ptui_getuins_CB&r=0.39923783252274414&pt_local_tk=-1909176059',headers=headers)
			result=urllib2.urlopen(req).read()
			result=[re.compile(r'account":"(\d+)"').findall(result),re.compile(r'nickname":"([^"]+)"').findall(result)]
			return result
		except Exception as e:
			i+=1
	return []
	


if __name__ == '__main__':
	result=Getaccount()
	print result
	
	if(result==[]):
		print "当前没有登录qq"
	else:
		num=len(result[0])
		print "当前登录了"+repr(num)+"个QQ"
		for i in range(num):
			print "qq:"+result[0][i]
			print "昵称:"+result[1][i]

