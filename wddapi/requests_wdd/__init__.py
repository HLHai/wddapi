import requests

# requests_burp_analysis
# 为了更好的获取文件，这里选择传入文件流的方式。
# 传入文件流，以及method方法可以返回url以及header头部信息
def r_b_a(f,method):
	return_dir={}
	j=0
	url=""
	s=0
	date=""
	for i in f.readlines():
		if j==0:
			p=i.strip().split()
			url=p[1]
			if p[0]=="POST":
				s=1
			j=1
			continue
		else:
			p=i.strip().split(":")
		if j==1:
			url=method+"://"+p[1]+url
			url=url.replace(" ","")
			j=2
			continue
		if p[0]=="":
			continue
		if s==1:
			date=p[0]
			continue
		r=p[0].replace(" ","")
		l=p[1].replace(" ","")
		return_dir.update({r:l})
	return url,return_dir,date,s

# 利用
def r_b_end(f,method):
	url,header,date,s=r_b_a(f,method)
	if s==1:
		html=requests.post(url,headers=header,data=date)
	else:
		html=requests.get(url,headers=header)
	return html
	

