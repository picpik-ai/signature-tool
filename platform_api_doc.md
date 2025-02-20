# Picpik V2 API

### ListPicpikBundles
> 获取所有Picpik应用

请求：

| 参数名       | 类型   | 描述信息            | 必填 |
|--------------|--------|---------------------|:-----|
| Action       | String | 对应的 API 指令名称 | 是   |
| PublicKey | String | 用户公钥，可从 PICPIK用户中心 获取 | 是   |
| Signature | String | 根据公钥及 API 指令生成的用户签名 | 是   |
| Page      | Int | 页数，不传默认查询全部      |  否    |
| PageSize      | Int | 每页大小，默认20      |  否    |
| request_uuid | String | API请求uuid         | 是   |

请求示例：
```json
{
    "Action": "ListPicpikBundles",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "Page": 1,
    "PageSize": 20,
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

响应：

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| RetCode      | Int    | 返回状态码，为 0 则为成功返回，非 0 为失败          | 是   |
| Action       | String | 操作指令名称                                      | 是   |
| Message      | String | 返回错误消息，当 RetCode 非 0 时提供详细的描述信息 |      |
| request_uuid | String | 返回请求时填写的uuid                              |      
| Bundles | Map[String]PicpikBundleInfo | Bundle列表                             |   是   |
| TotalCount | Int | 总数量                         |   是   |

**PicpikBundleInfo数据结构**

| 字段名 | 类型   | 描述信息   | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| Name | String | 应用名称                             |   是   |
| BundleId | String | Bundle Id                             |   是   |
| Description | String | 描述                           |   是   |
| MDText | String | markdown描述                           |   是   |
| ActualHourPrice | String | 当前每小时的价格吗，单位：分                          |   是   |
| OriginalHourPrice | String | 原始每小时的价格，单位：分                        |   是   |
| LogoUrl | String | 封面图url     |   是   |
| Region | String | 地域     |   是   |
| Version | String | 版本     |   是   |
| CreateTime | Int | 创建时间 |   是   |


响应示例：
```json
{
	"Action": "ListPicpikBundlesResponse",
	"RetCode": 0,
	"Message": "",
	"request_uuid": "432c57d3-102b-4817-9e98-28054b33db8e",
	"Bundles": [
	    {
	       "Name": "应用名称",
	       "BundleId": "xxx",
	       "Description": "描述",
	       "MDText": "xxx",
	       "ActualHourPrice": "9.99",
	       "OriginalHourPrice": "11.99",
	       "LogoUrl": "xxx",
	       "Region": "xxx",
	       "Version": "xxx",
	       "CreateTime": 1735285262,
	    }
	]
	"TotalCount": 1
}
```

### CreatePicpikApp
> 创建Picpik服务实例

请求：

| 参数名       | 类型   | 描述信息            | 必填 |
|--------------|--------|---------------------|:-----|
| Action       | String | 对应的 API 指令名称 | 是   |
| PublicKey | String | 用户公钥，可从 PICPIK用户中心 获取 | 是   |
| Signature | String | 根据公钥及 API 指令生成的用户签名 | 是   |
| Region      | String | 地域      |  是    |
| BundleId      | String | Bundle Id      |  是    |
| Remark      | String | 备注     |  否    |
| Count      | Int | 创建数量     |  否    |
| request_uuid | String | API请求uuid         | 是   |

请求示例：
```json
{
    "Action": "CreatePicpikApp",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "Region": "cn-wlcb",
    "BundleId": "xxx",
    "Remark": "xxx",
    "Count": 2,
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

响应：

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| RetCode      | Int    | 返回状态码，为 0 则为成功返回，非 0 为失败          | 是   |
| Action       | String | 操作指令名称                                      | 是   |
| Message      | String | 返回错误消息，当 RetCode 非 0 时提供详细的描述信息 |      |
| Results      | Map[String]CreatePicpikAppResult | 创建结果 |      |

**CreatePicpikAppResult数据结构**

| 字段名 | 类型   | 描述信息   | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| AppId | String | 实例ID                             |   是   |
| RetCode | Int | 状态码                             |   是   |
| ErrMsg | String | 错误信息描述                           |   是   |

响应示例：

```json
{
    "Action": "CreatePicpikAppResponse",
    "RetCode": 0,
    "Message": "",
    "Results": [
        {
            "AppId": "xxx",
            "RetCode": 0,
            "ErrMsg": "",
        },
        {
            "AppId": "xxx",
            "RetCode": 0,
            "ErrMsg": "",
        },
    ],
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

### ListPicpikApps
> 查看已创建Aigc服务实例

请求：

| 参数名       | 类型   | 描述信息            | 必填 |
|--------------|--------|---------------------|:-----|
| Action       | String | 对应的 API 指令名称 | 是   |
| PublicKey | String | 用户公钥，可从 PICPIK用户中心 获取 | 是   |
| Signature | String | 根据公钥及 API 指令生成的用户签名 | 是   |
| Page      | Int | 页数，不传默认查询全部      |  否    |
| PageSize      | Int | 每页大小，默认20      |  否    |
| AppId | String | 实例ID，查询具体实例详情时，传此参数 | 否 |
| request_uuid | String | API请求uuid         | 是   |

请求示例：

```json
{
    "Action": "ListPicpikApps",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "Page": 1,
    "PageSize": 20,
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

响应：

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| RetCode      | Int    | 返回状态码，为 0 则为成功返回，非 0 为失败          | 是   |
| Action       | String | 操作指令名称                                      | 是   |
| Message      | String | 返回错误消息，当 RetCode 非 0 时提供详细的描述信息 |      |
| Apps | Map[String]PicpikAppInfo | 应用列表                             |   是   |
| TotalCount | Int | 总数量                         |   是   |

**PicpikAppInfo数据结构**

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| AppId | String | 实例ID                             |   是   |
| BundleId | String | 应用ID                             |   是   |
| BundleName | String | bundle名称                            |   是   |
| BundleVersion | String | bundle版本                            |   是   |
| Remark | String | 备注                            |   是   |
| IP | String | 访问地址                             |   是   |
| State | Int | 实例状态, 请查看实例状态说明 |   是   |
| ApiKey | String | API Key |   是   |
| CreateTime | Int | 实例创建时间 |   是   |

**实例状态**
| State | 说明   |
|-------|--------|
| 1 | 运行中 |
| 2 | 初始化中 |
| 3 | 初始化ComfySrv服务中 |
| 4 | Comfy启动中 |
| 5 | 关机中 |
| 6 | 已关机 |
| 7 | 删除中 |
| 8 | 已删除 |
| 9 | 重启中 |
| 10 | 启动中 |
| -2 | 初始化失败 |
| -3 | 初始化ComfySrv服务失败 |
| -4 | 启动失败 |
| -5 | 关机失败 |
| -6 | 删除失败 |
| -7 | 重启失败 |
| -8 | 创建失败 |
| -9 | ComfySrv服务中断 |

响应示例：

```json
{
	"Action": "ListPicpikAppsResponse",
	"RetCode": 0,
	"Message": "",
	"request_uuid": "432c57d3-102b-4817-9e98-28054b33db8e",
	"Apps": [
	   {
	       "BundleName": "xxx",
	       "BundleVersion": "xxx",
	       "BundleId": "xxx",
	       "Remark": "xxx",
	       "AppId": "xxx",
	       "IP": "10.10.1.12",
	       "State": 1,
	       "ApiKey": "432c57d328054b33db8e",
	       "CreateTime": 1735285262
	   }
	]
	"TotalCount": 1
}
```

### ModifyPicpikAppRemark
> 修改实例备注

请求：

| 参数名       | 类型   | 描述信息            | 必填 |
|--------------|--------|---------------------|:-----|
| Action       | String | 对应的 API 指令名称 | 是   |
| PublicKey | String | 用户公钥，可从 PICPIK用户中心 获取 | 是   |
| Signature | String | 根据公钥及 API 指令生成的用户签名 | 是   |
| AppId      | String | 实例ID      |  是    |
| NewRemark      | String | 备注      |  是    |
| request_uuid | String | API请求uuid         | 是   |

请求示例：

```json
{
    "Action": "StartPicpikApp",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "AppId": "xxx",
    "NewRemark": "xxx",
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

响应：

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| RetCode      | Int    | 返回状态码，为 0 则为成功返回，非 0 为失败          | 是   |
| Action       | String | 操作指令名称                                      | 是   |
| Message      | String | 返回错误消息，当 RetCode 非 0 时提供详细的描述信息 |      |

响应示例：

```json
{
	"Action": "StartPicpikAppResponse",
	"RetCode": 0,
	"Message": "",
	"request_uuid": "432c57d3-102b-4817-9e98-28054b33db8e"
}
```


### StartPicpikApp
> 启动Aigc服务实例

请求：

| 参数名       | 类型   | 描述信息            | 必填 |
|--------------|--------|---------------------|:-----|
| Action       | String | 对应的 API 指令名称 | 是   |
| PublicKey | String | 用户公钥，可从 PICPIK用户中心 获取 | 是   |
| Signature | String | 根据公钥及 API 指令生成的用户签名 | 是   |
| AppId      | String | 实例ID      |  是    |
| request_uuid | String | API请求uuid         | 是   |

请求示例：

```json
{
    "Action": "StartPicpikApp",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "AppId": "xxx",
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

响应：

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| RetCode      | Int    | 返回状态码，为 0 则为成功返回，非 0 为失败          | 是   |
| Action       | String | 操作指令名称                                      | 是   |
| Message      | String | 返回错误消息，当 RetCode 非 0 时提供详细的描述信息 |      |

响应示例：

```json
{
	"Action": "StartPicpikAppResponse",
	"RetCode": 0,
	"Message": "",
	"request_uuid": "432c57d3-102b-4817-9e98-28054b33db8e"
}
```

### StopPicpikApp
> 关闭Aigc服务实例

请求：

| 参数名       | 类型   | 描述信息            | 必填 |
|--------------|--------|---------------------|:-----|
| Action       | String | 对应的 API 指令名称 | 是   |
| PublicKey | String | 用户公钥，可从 PICPIK用户中心 获取 | 是   |
| Signature | String | 根据公钥及 API 指令生成的用户签名 | 是   |
| AppId      | String | 实例ID      |  是    |
| request_uuid | String | API请求uuid         | 是   |

请求示例：

```json
{
    "Action": "StopPicpikApp",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "AppId": "xxx",
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

响应：

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| RetCode      | Int    | 返回状态码，为 0 则为成功返回，非 0 为失败          | 是   |
| Action       | String | 操作指令名称                                      | 是   |
| Message      | String | 返回错误消息，当 RetCode 非 0 时提供详细的描述信息 |      |

响应示例：

```json
{
	"Action": "StopPicpikAppResponse",
	"RetCode": 0,
	"Message": "",
	"request_uuid": "432c57d3-102b-4817-9e98-28054b33db8e"
}
```

### RestartPicpikApp
> 重启Aigc服务实例

请求：

| 参数名       | 类型   | 描述信息            | 必填 |
|--------------|--------|---------------------|:-----|
| Action       | String | 对应的 API 指令名称 | 是   |
| PublicKey | String | 用户公钥，可从 PICPIK用户中心 获取 | 是   |
| Signature | String | 根据公钥及 API 指令生成的用户签名 | 是   |
| AppId      | String | 实例ID      |  是    |
| request_uuid | String | API请求uuid         | 是   |

请求示例：

```json
{
    "Action": "RestartPicpikApp",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "AppId": "xxx",
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

响应：

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| RetCode      | Int    | 返回状态码，为 0 则为成功返回，非 0 为失败          | 是   |
| Action       | String | 操作指令名称                                      | 是   |
| Message      | String | 返回错误消息，当 RetCode 非 0 时提供详细的描述信息 |      |

响应示例：

```json
{
	"Action": "RestartPicpikAppResponse",
	"RetCode": 0,
	"Message": "",
	"request_uuid": "432c57d3-102b-4817-9e98-28054b33db8e"
}
```

### DeletePicpikApp
> 删除Aigc服务实例（调用前，请确保实例处于关机状态）

请求：

| 参数名       | 类型   | 描述信息            | 必填 |
|--------------|--------|---------------------|:-----|
| Action       | String | 对应的 API 指令名称 | 是   |
| PublicKey | String | 用户公钥，可从 PICPIK用户中心 获取 | 是   |
| Signature | String | 根据公钥及 API 指令生成的用户签名 | 是   |
| AppId      | String | 实例ID      |  是    |
| request_uuid | String | API请求uuid         | 是   |

请求示例：

```json
{
    "Action": "DeletePicpikApp",
    "PublicKey": "ALLak9M4cNdHXKOJAJJ4k8Hh1hZS2EgJF1D0FlPwfl",
    "Signature": "0131f4e4296f3ca8e1220b47247e83a4315ea8e1",
    "AppId": "xxx",
    "request_uuid":"b91fcfbe-bb35-47ce-a168-bd6252c75270"
}
```

响应：

| 字段名       | 类型   | 描述信息                                          | 必填 |
|--------------|--------|---------------------------------------------------|:-----|
| RetCode      | Int    | 返回状态码，为 0 则为成功返回，非 0 为失败          | 是   |
| Action       | String | 操作指令名称                                      | 是   |
| Message      | String | 返回错误消息，当 RetCode 非 0 时提供详细的描述信息 |      |

响应示例：

```json
{
	"Action": "DeletePicpikAppResponse",
	"RetCode": 0,
	"Message": "",
	"request_uuid": "432c57d3-102b-4817-9e98-28054b33db8e"
}
```