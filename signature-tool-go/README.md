# 使用示例

``` go
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
    // 示例使用
    publicKey := "abcdefg"
    privateKey := "123456"
    apiKey := "ABCDEFG" 
    
    signer := NewPicpikSigner(publicKey, privateKey, apiKey)
    
    // 用于 picpik AI业务的API
    servicePayload := map[string]interface{}{
    	"prompt":   "这是生成图片所需的提示词。",
    	"width":    512,
    	"height":   512,
    	"refImage": "如果是图生图，此处填原图的base64字符串",
    }   
    signature := signer.SignService(servicePayload)
    servicePayload["signature"] = signature 
    servicePayloadJSON, _ := json.MarshalIndent(servicePayload, "", "    ")
    fmt.Printf("service_payload=%s\n", servicePayloadJSON)
    
    // 用于操作管理 picpik 实例节点的API
    consolePayload := map[string]interface{}{
    	"Action":    "StartPicpikApp",
    	"PublicKey": "abcdefg",
    	"AppId":     "your_app_id",
    }
    
    signature = signer.SignPlatform(consolePayload)
    consolePayload["signature"] = signature 
    consolePayloadJSON, _ := json.MarshalIndent(consolePayload, "", "    ")
    fmt.Printf("console_payload=%s\n", consolePayloadJSON)
}

```