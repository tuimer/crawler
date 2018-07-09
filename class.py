import re
from urllib import request



class Spider(object):
	"""爬取主播名字和人气"""
	url='https://www.panda.tv/cate/kingglory'
	root_pattern='<div class="video-info">([\s\S]*?)</div>'#匹配的根节点  \s换成.
	name_pattern='</li>([\s\S]*?)<span>'
	number_pattern='<span class="video-number">([\s\S]*?)</span>'

	
	def __fetch_content(self):
		r=request.urlopen(spider.url)
		htmls=r.read()
		htmls=str(htmls,encoding='utf-8')#将字节码bytes转换为字符串
		return htmls


	def __analysis(self,htmls):
		root_html=re.findall(spider.root_pattern,htmls)
		anchors=[]
		for html in root_html:
			name=re.findall(spider.name_pattern,html)
			number=re.findall(spider.number_pattern,html)
			anchor={'name':name,'number':number}
			anchors.append(anchor)
		return anchors

	def __refine(self,anchors):#精炼数据
		l=lambda anchor:{
			'name':anchor['name'][0].strip(),
			'number':anchor['number'][0]
			}
		return list(map(l,anchors))

	#业务处理 排序
	def __sort(self,anchors):
		anchors=sorted(anchors,key=sel.__sort_seed,reverse=Ture)#key传入函数，决定按何种方式排序数据
		return anchors

	def __sort_seed(self,anchor):
		r=re.findall('\d',ancho['number'])
		number=float(r[0])
		if '万' in anchor['number']:
			number*=10000
		return number


	def __show(self,anchors):
		for rank in range(0,len(anchors)):
			print('rank '+str(rank+1)+':'+anchors[rank]['name']+'----'+anchors[rank]['number'])


	def go(self):#spider类的入口方法,总控方法的调用
		htmls=self.__fetch_content()#取内容
		anchors=self.__analysis(htmls)
		anchors=list(self.refine(anchors))
		anchors=self.__sort(anchors)#业务处理
		self.__show(anchors )
		

spider=Spider()
spider.go()
