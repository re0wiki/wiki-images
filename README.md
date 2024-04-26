# wiki-images
一键获取wiki上所有图片的详细信息

获取完成后会在当前目录下生成 `wiki_images.json` 文件

获取失败后会重试3次（虽然目前不会失败），随后会退出程序（迷惑操作，~~后期如果真出现问题了再改~~）

# 使用方法
直接 `python3 list_images.py` 即可（需安装 `requests` 库）

# 文件示例内容

```
[
  {
    "name": "00277.jpeg",
    "timestamp": "2021-02-24T14:54:08Z",
    "uploader": "IchiSanNi",
    "size": 537936,
    "width": 1114,
    "height": 1600,
    "sha1": "dfda9afc47a7acafa01184198a655802b46458c5",
    "url": "https://static.wikia.nocookie.net/rezero/images/e/e5/00277.jpeg/revision/latest?cb=20210224145408&path-prefix=zh"
  }
]
```
