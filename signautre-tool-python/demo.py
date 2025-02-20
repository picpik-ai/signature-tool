import json

import picpik_signer

# 示例使用
public_key = "abcdefg"
private_key = "123456"
api_key = "ABCDEFG"

signer = picpik_signer.PicpikSigner(public_key, private_key, api_key)
service_payload = {
    "prompt": "这是生成图片所需的提示词。",
    "width": 512,
    "height": 512,
    "refImage": "如果是图生图，此处填原图的base64字符串"
}

# 用于 picpik AI业务的API
signature = signer.sign_service(service_payload)
service_payload['signature'] = signature

print(f"service_payload={json.dumps(service_payload, indent=4, ensure_ascii=False)}\n")

console_payload = {
    "Action": "StartPicpikApp",
    "PublicKey": "abcdefg",
    "AppId": "your_app_id"
}

# 用于操作管理 picpik 实例节点的API
signature = signer.sign_platform(console_payload)
console_payload['signature'] = signature

print(f"console_payload={json.dumps(console_payload, indent=4, ensure_ascii=False)}\n")
