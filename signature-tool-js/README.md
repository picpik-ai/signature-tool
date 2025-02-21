# 使用示例

``` javascript
const PicpikSigner = require('path_to_picpik-signer.js');

// 示例使用
const publicKey = "abcdefg";
const privateKey = "123456";
const apiKey = "ABCDEFG";

const signer = new PicpikSigner(publicKey, privateKey, apiKey);

// 服务端 API 需要的 payload
const servicePayload = {
  prompt: "这是生成图片所需的提示词。",
  width: 512,
  height: 512,
  refImage: "如果是图生图，此处填原图的base64字符串"
};

// 用于 picpik AI 业务的签名
let signature = signer.signService(servicePayload);
servicePayload.signature = signature;

console.log(`servicePayload=${JSON.stringify(servicePayload, null, 4)}\n`);

// 控制台 API 需要的 payload
const consolePayload = {
  Action: "StartPicpikApp",
  PublicKey: "abcdefg",
  AppId: "your_app_id"
};

// 用于操作管理 picpik 实例节点的签名
signature = signer.signPlatform(consolePayload);
consolePayload.signature = signature;

console.log(`consolePayload=${JSON.stringify(consolePayload, null, 4)}\n`);

```