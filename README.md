# Picpik签名工具

## 基础说明

您在通过API调用的方式使用Picpik产品时，将会需要由 **API请求参数所生成的 `signautre`** 作为安全性认证。

## API 签名说明

Picpik API分为以下两类：
### Platform API
用于Picpik平台提供的**资源管理的API**。

* API文档：[platform_api_doc.md](platform_api_doc.md)
* 秘钥： **`PublicKey`,`PrivateKey`** ，可以从 **[PICPIK用户中心](https://studio.picpik.ai/user-center)** 获取。


### Service API

用于Picpik中所购买的服务节点提供的**业务API**。

* API文档：您所购买的Picpik服务节点中，可访问 **`http://your_service_ip:80`** 。
* 秘钥：**`ApiKey`** 可以从 **[PICPIK用户应用信息](https://studio.picpikai.com/v2/application-service)** 获取。


## 工具使用示例

### [python3](signautre-tool-python/demo.md)


> 签名工具适配的语言将会逐渐完善，若以下没有您所需要的目标语言，可以尝试以下方式：
> * 联系我们：  **[develop@picpik.ai](develop@picpik.ai)** 
> * 自行研发：[签名规则](signature_rule.md)

