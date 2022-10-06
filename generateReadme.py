# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'http://dingxiaowei.cn/'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'} 

def addIntro(f):
	txt = '''  
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dingxiaowei&show_icons=true&theme=graywhite"/>
</p>

<p align="center"> 8+年技术博主，CSDN认证博客专家，游戏开发爱好者 </p>  
<p align="center"> 曾待过几家上市游戏公司，现为菊厂高级研发工程师，拥有丰富的 挖坑 踩坑 填坑 背锅经验 🐶   </p>  
<p align="center"> 擅长Unity游戏开发，热爱新技术，喜欢钻研</p>  


''' 
	f.write(txt)

def addProjectInfo(f):
	txt ='''
### 开源项目  
- [Unity性能监测工具](https://github.com/dingxiaowei/MonitorTool)Unity性能监测工具	
- [UnityExcelTool](https://github.com/dingxiaowei/ExcelTool)Unity通用打表工具	
- [GFFrameWork](https://github.com/dingxiaowei/GFFrameWork) Unity通用框架 
- [UGUIScrollRect](https://github.com/dingxiaowei/ScrollRect) UGUIScrollview各种花式高性能效果
- [AladdinShader](https://github.com/dingxiaowei/AladdinShader) 我的shader入门
- [UIAnimationSystem](https://github.com/dingxiaowei/UIAnimationSystem) UI动画工具
- [Aladdin_XLua](https://github.com/dingxiaowei/Aladdin_XLua) 我的XLua入门
   
[查看更多](https://github.com/dingxiaowei/)	 

	''' 
	f.write(txt) 

def addZhuanlanInfo(f):
	txt ='''
### 我的专栏  
- [Unity设计模式](http://dingxiaowei.cn/tags/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F/)
- [Wwise音频引擎入门实战](https://edu.uwa4d.com/course-intro/0/131)  
- [Shader入门](http://dingxiaowei.cn/tags/Shader/)  
- [Visual Effect Graph入门实战](https://edu.uwa4d.com/course-intro/0/171)  
- [Jenkins自动化打包](https://edu.uwa4d.com/course-intro/0/149)    
- ……

	''' 
	f.write(txt) 


def addBlogInfo(f):  
	http = urllib3.PoolManager(num_pools=5, headers = headers)
	resp = http.request('GET', blogUrl)
	resp_tree = etree.HTML(resp.data.decode("utf-8"))
	# html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4") 
	html_data = resp_tree.xpath(".//article[@class='blog-list-box']")
	f.write("\n### 我的博客\n")
	cnt = 0
	for i in html_data: 
		if cnt >= 5:
			break
		# title = i.xpath('./a/text()')[1].strip()
		title = i.xpath("./a/div/h4/text()")[0].strip()
		url = i.xpath('./a/@href')[0] 
		item = '- [%s](%s)\n' % (title, url)
		f.write(item)
		cnt = cnt + 1
	f.write('\n[查看更多](https://dingxiaowei2013.blog.csdn.net/)\n')


if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	f.write('<table align="center"><tr>\n')
	f.write('<td valign="top" width="33%">\n')
	addProjectInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="33%">\n')
	addBlogInfo(f)
	f.write('\n</td>\n')
	f.write('<td valign="top" width="33%">\n')
	addZhuanlanInfo(f)
	f.write('\n</td>\n')
	f.write('</tr></table>\n')
	f.close 

