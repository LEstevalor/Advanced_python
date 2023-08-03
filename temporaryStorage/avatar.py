"""
def avatar(self, request, *args, **kwargs):
    username = kwargs.get("username")  # 没有带username，url的w+就不会匹配到
    user_info = IegUsersImages.objects.filter(username=username).first()

    if not user_info:
        timestamp = str(int(time.time()))  # 生成时间戳，注意服务器的时间与标准时间差不能大于180秒
        nonce = str(random.randint(1000, 9999))  # 随机字符串，十分钟内不重复即可
        signature = hashlib.sha256()
        string = timestamp + PAASTOKEN + nonce + timestamp
        signature.update(string.encode())
        signature = signature.hexdigest().upper()  # 输出大写的结果
        headers = {'content-type': 'application/json'}
        headers['x-rio-paasid'] = PAASID
        headers['x-rio-nonce'] = nonce
        headers['x-rio-timestamp'] = timestamp
        headers['x-rio-signature'] = signature

        try:
            url = GET_HEAD_IMG_BASE_URL + "/" + str(IMG_SIZE) + "/" + username + ".png"
            logger.info(f"请求的URL为：{url}，paasid为{PAASID}，nonce为{nonce},timestamp为{timestamp},signature为{signature}")
            response = requests.get(url=url, headers=headers)
            logger.info(f"URL请求成功，图片数据{response.content}")
            user_info = IegUsersImages.objects.create(username=username, image=response.content)
        except Exception as err:
            logger.error("error:get_head_img:{}，请求参数：{}和{}".format(err, IMG_SIZE, username))

    return HttpResponse(user_info.image, content_type='image/jpg')
"""
