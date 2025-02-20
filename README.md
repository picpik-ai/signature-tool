# Picpik签名工具

## 基础说明

您在通过API调用的方式使用Picpik产品时，将会需要由 **API请求参数所生成的 `signautre`** 作为安全性认证。

## API 签名说明

#### Platform API
用于Picpik平台上的资源管理API

签名字段为 `Signature`



#### Picpik中所创建的节点的业务服务API

## 秘钥说明

> **`PublicKey`,`PrivateKey`** 用于Picpik平台上的资源管理API计算签名使用。可以从 **[PICPIK用户中心](https://studio.picpik.ai/user-center)** 获取。
> <br>
> **`ApiKey`** 用于您在Picpik中所创建的节点的业务服务API计算签名使用。可以从 **[PICPIK用户应用中心](https://studio.picpikai.com/v2/application-service)** 获取。


## 数据模拟
> 本例中以Python3为例

```python
public_key = 'abcdefg'
private_key = '123456'
api_key  = 'abcdefg'
```

您可以使用上述的 `PublicKey` , `PrivateKey` , `ApiKey` 调试代码， 如得到与后文一致的签名结果，即表示代码是正确的，可再换为您自己对应的Key，以及业务所需的其它API请求参数。

本例中假设用户请求参数串如下:

**实际使用过程中，应包含：除`signature`外所有已填写的参数。**

> Picpik平台API参数

```json
{
    "Action": "StartPicpikApp",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "AppId": "xxx",
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

```json
{
    "prompt": "这是生成图片所需的提示词。",
    "width": 512,
    "height": 512,
    "refImage": "如果是图生图，此处填原图的base64字符串"
}
```

## 构造签名

> 如果[示例代码](#编码示例)中包含您使用的语言，建议直接使用其中的`gen_signature`函数构造签名。

如果示例代码中没有您使用的语言，可以联系我们补充或者按照以下规则生成签名：

### 1. 按照请求参数的名称进行升序排列
```json
{
    "height": 512,
    "prompt": "这是生成图片所需的提示词。",
    "refImage": "如果是图生图，此处填原图的base64字符串",
    "width": 512
}
```

### 2. 构造被签名参数串

被签名串的构造规则为: 被签名串 = 所有请求参数拼接(无需 HTTP 转义)。**并在本签名串的结尾拼接 API 密钥（`ApiKey`）**。

```
height512prompt这是生成图片所需的提示词。refImage如果是图生图，此处填原图的base64字符串width512abcdefg
```

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