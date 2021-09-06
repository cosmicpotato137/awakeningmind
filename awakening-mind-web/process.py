import json
import urllib2

template = "<div class='ytb-back'>\n        <div>\n            <h5 style='top:0px;wdith:95%;'><a href='http://youtu.be/{yid}'>{title}</a>\n            </h5>\n            <p id='less{id}' class='text-left'>\n                {less_content}\n            </p>\n            <div id='less{id}-btn' class='less-btn' onclick=\"more('less{id}','more{id}')\">READ MORE</div>\n            <p id='more{id}' class='more-content'>\n                {more_content}\n            </p>\n             <div id='more{id}-btn' class='more-btn' onclick=\"more('more{id}','less{id}')\">READ LESS</div>\n        </div>\n    </div>"
abstract = "<div class='resource-abstract'>{resources}</div>"
res = "<a href='{res_url}' class='clear-a-style'><div class='res-back' style=\"{res_back}\"><div style='height:93px;wdith:197px;margin-right:4px;font-size:50px;'>{res_icon}</div><div class='res-mask'></div><div class='res-title'>{res_title}</div></div></a>"

pin = """ 			<div class="pin">
                <img src="http://img.youtube.com/vi/{ID}/0.jpg" />
                <p>
                    {DESC} <a href="http://youtu.be/{ID}"> more </a>
                </p>
            </div>"""


with open('youtube.json') as data_file:    
    videos = json.load(data_file)

for v in videos["youtube"]:
	ID = v["id"]
	data = json.load(urllib2.urlopen('https://www.googleapis.com/youtube/v3/videos?part=snippet&id=' + ID + '&key=AIzaSyAclZnZkHqBVAEgM9dUQf1oMWaHu_tQ_aE'))
	content = data["items"][0]["snippet"]["description"]
	print pin.replace("{ID}", ID).replace("{DESC}", content)

# print data["items"][0]["snippet"]["title"]
# print data["items"][0]["snippet"]["description"]