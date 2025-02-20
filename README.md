# Picpik签名工具

## 基础说明

您在通过API调用的方式使用Picpik产品时，将会需要由 **API请求参数所生成的 `signautre`** 作为安全性认证。

## API 签名说明

Picpik API分为以下两类：
### Platform API
**[API文档](#https://github.com/JoshuaYin/signature-tool/blob/main/platform_api_doc.md)**

用于Picpik平台提供的**资源管理的API**，签名字段为 **`Signature`**。签名所需秘钥是 **`PublicKey`,`PrivateKey`** ，可以从 **[PICPIK用户中心](https://studio.picpik.ai/user-center)** 获取。


### Service API

API文档在您所购买的Picpik服务节点中，可访问 **`http://your_service_ip:80`** 。

用于Picpik中所购买的服务节点提供的**业务API**。签名字段为 **`signature`**。签名所需秘钥是 **`ApiKey`** 可以从 **[PICPIK用户应用信息](https://studio.picpikai.com/v2/application-service)** 获取。


<br><br>
**本文档中的代码示例语言均为Python3**

## 数据模拟

```python
public_key = 'abcdefg'
private_key = '123456'
api_key  = 'ABCDEFG'
```

您可以使用上述的 `PublicKey` , `PrivateKey` , `ApiKey` 调试代码， 如得到与后文一致的签名结果，即表示代码是正确的，可再换为您自己对应的Key，以及业务所需的其它API请求参数。


```json
# Platform API参数案例
{
    "Action": "StartPicpikApp",
    "PublicKey": "abcdefg",
    "AppId": "your_app_id"
}

# Service API参数案例
{
    "prompt": "这是生成图片所需的提示词。",
    "width": 512,
    "height": 512,
    "refImage": "如果是图生图，此处填原图的base64字符串"
}
```

## 构造签名

### 拼接参数，构造被签名参数串

按照请求参数的名称进行升序排列，并以排序后的keyvalue，拼接所有参数。并在最后加上 `PrivateKey` 或者 `ApiKey` 。

* Platform API最后拼接 `PrivateKey` 
```json
{
    "Action": "StartPicpikApp",
    "PublicKey": "abcdefg",
    "AppId": "your_app_id"
}
```
> 拼接后的content = "**ActionStartPicpikAppAppIdyour_app_idPublicKeyabcdefg123456**"

* Service API最后拼接 `ApiKey` 
```python
{
    "height": 512,
    "prompt": "这是生成图片所需的提示词。",
    "refImage": "如果是图生图，此处填原图的base64字符串",
    "width": 512
}
```
> 拼接后的content = "**height512prompt这是生成图片所需的提示词。refImage如果是图生图，此处填原图的base64字符串width512ABCDEFG**"

> **注意：**
> - 对于 string 类型，若长度超过128个字符，只取前128个字符参与签名算法即可。**注意是前128个字符，不是bytes**
> - 对于 boolean 类型，应编码为 `true` / `false`，首字母需小写。
> - 对于浮点数类型，如果小数部分为 0，应仅保留整数部分，如 `42.0` 应保留 `42`
> - 对于浮点数类型，不能使用科学计数法
> - 对于数组类型，将数组的每个元素直接转为字符串拼接
> - 对于map类型，将每个字段按照名称进行升序排列，然后将每个字段的名称和值拼接

### 3. 计算签名

使用 **md5** 编码签名串，生成最终签名，即是请求参数 `signature` 的值。

按照上述算法，本例中，计算出的 `signature` 为 **31ed96a9ac923cad93f30f1a74cb8db0** 。

## 编码示例

> 目前仅提供python编码示例

```python
import hashlib

# 生成签名算法入口
def gen_signature(body, api_key):
    content = map_2_string(body)
    content += api_key
    md5_hash = hashlib.md5()
    md5_hash.update(content.encode('utf-8'))
    md5 = md5_hash.hexdigest()
    return md5


def map_2_string(params):
    content = []
    for key in extract_sorted_keys(params):
        content.append(f"{key}{any_2_string(params[key])}")
    return "".join(content)


def any_2_string(v):
    if isinstance(v, bool):
        return simple_2_string(v).lower()
    elif isinstance(v, float) and int(v) == v:
        return simple_2_string(int(v))
    elif isinstance(v, dict):
        return map_2_string(v)
    elif isinstance(v, list):
        return slice_2_string(v)
    elif isinstance(v, str):
        return format_string(v)
    else:
        return simple_2_string(v)


def slice_2_string(arr):
    s = ""
    for v in arr:
        s += any_2_string(v)
    return s


def simple_2_string(v):
    if v is None or v == "":
        return ""

    return str(v)


def format_string(v, limit=128):
    if len(v) > limit:
        return v[:limit]

    return v


def extract_sorted_keys(obj):
    return sorted(obj.keys())


payload = {
    "prompt": "这是生成图片所需的提示词。",
    "width": 512,
    "height": 512,
    "refImage": "如果是图生图，此处填原图的base64字符串"
}
api_key = "abcdefg"

signature = gen_signature(payload, api_key)

payload['signature'] = signature
```