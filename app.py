from flask import Flask, jsonify, make_response, render_template,request, session, url_for, redirect
import time
import requests
import re
import random

app = Flask(__name__)

# 一言
def Hitokoto():
    try:
        types = ["a", "b", "c", "d", "i", "j", "k"]
        url = "https://v1.hitokoto.cn/?encode=json&charset=utf-8&c="+types[random.randint(0,len(types)-1)]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        response = requests.get(url, headers=headers)
        res = response.json()
        return (res['from'], res['hitokoto'])
    except:
        return ("StarMan", "加油！")

def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    res = requests.get(url, headers=headers)
    return res

@app.route('/getText', methods=['GET', 'POST'])
def getTexts():
    if request.get_json():
        if request.get_json()["method"] == "index":
            texts = getCharacter(request.get_json()["xingzuo"])
        if request.get_json()["method"] == "male":
            texts = males(request.get_json()["xingzuo"])
        if request.get_json()["method"] == "female":
            texts = females(request.get_json()["xingzuo"])
        if request.get_json()["method"] == "match":
            texts = getMatch(request.get_json()["xingzuo"])
    return jsonify({"texts": texts})

# 如何追xx座男生
def males(xingzuo):
    xingzDic = {"baiyang": "https://www.zuixingzuo.net/baiyang/show5974.html",
                "jinniu": "https://www.zuixingzuo.net/jinniu/show5978.html",
                "shuangzi": "https://www.zuixingzuo.net/shuangzi/show5979.html",
                "juxie": "https://www.zuixingzuo.net/juxie/show5981.html",
                "shizi": "https://www.zuixingzuo.net/shizi/show5982.html",
                "chunv": "https://www.zuixingzuo.net/chunv/show5985.html",
                "tiancheng": "https://www.zuixingzuo.net/tiancheng/show5987.html",
                "tianxie": "https://www.zuixingzuo.net/tianxie/show5989.html",
                "sheshou": "https://www.zuixingzuo.net/sheshou/show5991.html",
                "mojie": "https://www.zuixingzuo.net/mojie/show5993.html",
                "shuiping": "https://www.zuixingzuo.net/shuiping/show5995.html",
                "shuangyu": "https://www.zuixingzuo.net/shuangyu/show5998.html"}

    res = getHtml(xingzDic[xingzuo]).text
    # print(res)
    texts = re.findall(r'<div class="show_cnt">([\s\S]*?)<p class="ARTICLE_INDEX"', res)
    # print(texts)
    return texts

# 如何追 xx座女生
def females(xingzuo):
    xingzDic = {"baiyang": "https://www.zuixingzuo.net/baiyang/show5973.html",
                "jinniu": "https://www.zuixingzuo.net/jinniu/show5975.html",
                "shuangzi": "https://www.zuixingzuo.net/shuangzi/show5976.html",
                "juxie": "https://www.zuixingzuo.net/juxie/show5980.html",
                "shizi": "https://www.zuixingzuo.net/shizi/show5983.html",
                "chunv": "https://www.zuixingzuo.net/chunv/show5984.html",
                "tiancheng": "https://www.zuixingzuo.net/tiancheng/show5986.html",
                "tianxie": "https://www.zuixingzuo.net/tianxie/show5988.html",
                "sheshou": "https://www.zuixingzuo.net/sheshou/show5990.html",
                "mojie": "https://www.zuixingzuo.net/mojie/show5992.html",
                "shuiping": "https://www.zuixingzuo.net/shuiping/show5994.html",
                "shuangyu": "https://www.zuixingzuo.net/shuangyu/show5996.html"}

    res = getHtml(xingzDic[xingzuo]).text
    # print(res)
    texts = re.findall(r'<div class="show_cnt">([\s\S]*?)<p class="ARTICLE_INDEX"', res)
    # print(texts)
    return texts

# 星座最佳匹配
def getMatch(xingzuo):
    url = "https://www.zuixingzuo.net/match/zuipei/"+xingzuo+".html"
    res = getHtml(url).text
    texts = re.findall(r'<div class="show_cnt">([\s\S]*?)</div>', res)
    imgs = re.findall(r'(<img.*"/>)', texts[0])
    text = re.sub(imgs[0], '', texts[0])
    return text

# 获取星座性格
def getCharacter(xingzuo):
    url = "https://www.zuixingzuo.net/xingge/"+xingzuo+"/"
    res = getHtml(url).text
    texts = re.findall(r'<div class="show_cnt">([\s\S]*)<p class="ARTICLE_INDEX"', res)
    imgs = re.findall(r'(<img.*"/>)', texts[0])
    texts = re.sub(imgs[0], '', texts[0])
    return texts


@app.route('/male')
def male():
    hitokoto = {}
    hitokoto['from'], hitokoto['hitokoto'] = Hitokoto()
    return render_template('index.html', hitokoto=hitokoto, flags="male")

@app.route('/female')
def female():
    hitokoto = {}
    hitokoto['from'], hitokoto['hitokoto'] = Hitokoto()
    return render_template('index.html', hitokoto=hitokoto, flags="female")

@app.route('/match')
def match():
    hitokoto = {}
    hitokoto['from'], hitokoto['hitokoto'] = Hitokoto()
    return render_template('index.html', hitokoto=hitokoto, flags="match")

@app.route('/about')
def about():
    hitokoto = {}
    hitokoto['from'], hitokoto['hitokoto'] = Hitokoto()
    return render_template('index.html', hitokoto=hitokoto, flags="about")

@app.route('/')
def index():
    hitokoto = {}
    hitokoto['from'], hitokoto['hitokoto'] = Hitokoto()
    # chars = getCharacter()
    return render_template('index.html', hitokoto=hitokoto, flags="index")

app.secret_key = '123sdf'
if __name__ == '__main__':
    app.run(debug=True)