import requests
import datetime
import json
import time

def getNowtime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class logger:
    def info(msg):
        print(getNowtime() + " [Info] " + msg)

    def error(msg):
        print(getNowtime() + " [Error] " + msg)

    def warning(msg):
        print(getNowtime() + " [Warning] " + msg)

def main():
    logger.info("开始获取图片列表")

    r = requests.get("https://rezero.fandom.com/zh/api.php?action=query&format=json&meta=siteinfo&siprop=statistics")
    data = r.json()
    count_images = data["query"]["statistics"]["images"]
    del r, data

    logger.info(f'总计 {count_images} 张图片')

    aicontinue = ""
    images = []

    while 1:
        if aicontinue == None:
            logger.info("获取完成")
            break

        params = {
            "action": "query",
            "list": "allimages",
            "ailimit": 500,
            "aiprop": "timestamp|user|url|size|sha1",
            "format": "json"
        }
        if aicontinue != "":
            params["aicontinue"] = aicontinue

        retry = 0
        while 1:
            r = requests.get("https://rezero.fandom.com/zh/api.php", params=params)
            if r.status_code != 200:
                if retry <= 2:
                    retry += 1
                    logger.warning(f'请求失败, 进行第 {retry} 次重试')
                    time.sleep(1)
                    continue
                
                logger.error("请求失败, 退出程序")
                exit(1)
            
            data = r.json()
            for image in data["query"]["allimages"]:
                images.append({
                    "name": image["name"],
                    "timestamp": image["timestamp"],
                    "uploader": image["user"],
                    "size": image["size"],
                    "width": image["width"],
                    "height": image["height"],
                    "sha1": image["sha1"],
                    "url": image["url"]
                })

            aicontinue = None
            if "continue" in data:
                aicontinue = data["continue"]["aicontinue"]
            
            logger.info(f'成功获取 {len(data["query"]["allimages"])} 张图片')
            break
        
    
    f = open("wiki_images.json", "w", encoding="utf-8")
    f.write(json.dumps(images, ensure_ascii=False))
    f.close()


if __name__ == "__main__":
    main()