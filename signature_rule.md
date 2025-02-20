# 签名规则

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

### 1、拼接参数，构造被签名参数串

按照请求参数的名称进行升序排列，并以排序后的keyvalue，拼接所有参数。并在最后加上 `PrivateKey` 或者 `ApiKey` 。

#### Platform API最后拼接 `PrivateKey` 
```json
{
    "Action": "StartPicpikApp",
    "PublicKey": "abcdefg",
    "AppId": "your_app_id"
}
```
> 拼接后的content = "**ActionStartPicpikAppAppIdyour_app_idPublicKeyabcdefg123456**"

#### Service API最后拼接 `ApiKey` 
```json
{
    "height": 512,
    "prompt": "这是生成图片所需的提示词。",
    "refImage": "如果是图生图，此处填原图的base64字符串",
    "width": 512
}
```
> 拼接后的content = "**height512prompt这是生成图片所需的提示词。refImage如果是图生图，此处填原图的base64字符串width512ABCDEFG**"

<br>

**注意：**
- **仅在Service API签名算法中**，对于 string 类型，若长度超过128个字符，只取前128个字符参与签名算法即可。**注意是前128个字符，不是bytes**
- 对于 boolean 类型，应编码为 `true` / `false`，首字母需小写。
- 对于浮点数类型，如果小数部分为 0，应仅保留整数部分，如 `42.0` 应保留 `42`
- 对于浮点数类型，不能使用科学计数法
- 对于数组类型，将数组的每个元素直接转为字符串拼接
- 对于map类型，将每个字段按照名称进行升序排列，然后将每个字段的名称和值拼接

### 2. 计算签名

#### Platform API

使用 **SHA1** 编码签名串，生成最终签名，即是请求参数 `signature` 的值。
按照上述算法，本例中，计算出的 `Signature` 为 **c5e65ad1936ff695436917bf807d2281db33e7a3** 。

#### Service API

使用 **md5** 编码签名串，生成最终签名，即是请求参数 `signature` 的值。
按照上述算法，本例中，计算出的 `signature` 为 **f082f8b52582dda6c0e976a39d2196b2** 。

### 3. 将签名结果放入请求参数中
#### Platform API

```json
{
    "Action": "StartPicpikApp",
    "PublicKey": "abcdefg",
    "AppId": "your_app_id",
    "Signature": "c5e65ad1936ff695436917bf807d2281db33e7a3"
}
```

#### Service API

```json
{
    "prompt": "这是生成图片所需的提示词。",
    "width": 512,
    "height": 512,
    "refImage": "如果是图生图，此处填原图的base64字符串",
    "signature": "f082f8b52582dda6c0e976a39d2196b2"
}
```
