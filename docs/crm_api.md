# JUSI CRM 服务接口文档

## 基本信息

| 项目 | 说明 |
|------|------|
| 基础地址 | `https://service.jusiai.com` |
| API 前缀 | `/api/v1.0` |
| 数据格式 | JSON |
| 字符编码 | UTF-8 |

---

## 保存客户留资信息

客户在 JUSI 官网提交联系方式和需求信息时调用此接口。

### 请求

```
POST https://service.jusiai.com/api/v1.0/customer_info
Content-Type: application/json
```

### 请求参数

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | 是 | 姓名 / 称呼 |
| phone | string | 是 | 手机号，需为中国大陆11位手机号（1开头，第二位3-9） |
| company | string | 否 | 公司 / 机构名称，默认空字符串 |
| email | string | 否 | 电子邮箱，如提供则需符合标准邮箱格式，默认空字符串 |
| requirements | string | 否 | 客户需求描述，默认空字符串 |

### 校验规则

- **手机号**（必填）：必须匹配正则 `^1[3-9]\d{9}$`，即中国大陆11位手机号
- **邮箱**（选填）：如提供，必须匹配正则 `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

### 响应参数

| 参数 | 类型 | 说明 |
|------|------|------|
| code | int | 状态码：200 成功，400 参数错误，500 服务器错误 |
| message | string | 结果描述 |

### 响应示例

**成功：**

```json
{
  "code": 200,
  "message": "ok"
}
```

**手机号格式错误：**

```json
{
  "code": 400,
  "message": "手机号格式不正确"
}
```

**邮箱格式错误：**

```json
{
  "code": 400,
  "message": "邮箱格式不正确"
}
```

**服务器错误：**

```json
{
  "code": 500,
  "message": "保存客户信息失败"
}
```

---

## 调用示例

### cURL

```bash
curl -X POST https://service.jusiai.com/api/v1.0/customer_info \
  -H "Content-Type: application/json" \
  -d '{
    "name": "张三",
    "phone": "13800138000",
    "company": "某某科技有限公司",
    "email": "zhangsan@example.com",
    "requirements": "希望了解AI客服解决方案"
  }'
```

### Python (requests)

```python
import requests

url = "https://service.jusiai.com/api/v1.0/customer_info"
data = {
    "name": "张三",
    "phone": "13800138000",
    "company": "某某科技有限公司",
    "email": "zhangsan@example.com",
    "requirements": "希望了解AI客服解决方案"
}

response = requests.post(url, json=data)
print(response.json())
```

### JavaScript (fetch)

```javascript
const response = await fetch('https://service.jusiai.com/api/v1.0/customer_info', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: '张三',
    phone: '13800138000',
    company: '某某科技有限公司',
    email: 'zhangsan@example.com',
    requirements: '希望了解AI客服解决方案'
  })
});

const result = await response.json();
console.log(result);
```

### 仅填写必填字段

```bash
curl -X POST https://service.jusiai.com/api/v1.0/customer_info \
  -H "Content-Type: application/json" \
  -d '{
    "name": "李四",
    "phone": "13912345678"
  }'
```
