
# 🔐 MD5 Collision Attack Demo

> Demo thực tế tấn công va chạm trên hàm băm MD5: tạo hai tệp thực thi có cùng mã băm nhưng hành vi hoàn toàn khác nhau.

---

## 🧠 Tổng Quan

Tấn công va chạm (collision attack) cho phép tạo **hai thông điệp khác nhau** nhưng có cùng **hash MD5**.

Cấu trúc:

```text
prefix + collisionA + suffix
prefix + collisionB + suffix
```

Do tính chất *length extension* của MD5, việc thêm `suffix` giống nhau sau phần `collision` không làm thay đổi giá trị băm. Điều này cho phép:

- Hai file khác nhau.
- Cùng một mã băm.
- Hành vi khác biệt khi thực thi.

---

## 🎯 Mục Tiêu

Tạo 2 file:

| Tên file     | Hành vi khi thực thi                |
|--------------|--------------------------------------|
| `md5_data1`  | In ra dòng thông báo đơn giản.       |
| `md5_data2`  | Mở shell `/bin/sh`.                  |

---

## ⚙️ Các Bước Thực Hiện

### 📌 1. Tạo prefix

<details>
<summary>📁 Nội dung file <code>prefix</code></summary>

```php title="prefix"
#!/usr/bin/php
<?php
```

![prefix](image/image-0.png)
</details>

---

### ⚡ 2. Tạo phần collision với fastcoll

Clone công cụ:

```bash
#!/bin/bash -ex

[ -e fastcoll ] || git clone https://github.com/upbit/clone-fastcoll fastcoll
cd fastcoll
make

cd ..
mkdir bin
cp fastcoll/fastcoll bin
```

Tạo collision:

```bash
fastcoll -p prefix -o md5_data1 md5_data2
```

![fastcoll](image/image-1.png)  
![fastcoll-output](image/image-2.png)

---

### ✍️ 3. Thêm mã độc lập vào phần `suffix`

```python title="add_suffix.py"
with open("md5_data1", "ab") as f:
    f.write(b'echo "Hello from benign file!";\n')

with open("md5_data2", "ab") as f:
    f.write(b'system("/bin/sh");\n')
```

![python-suffix](image/image-3.png)  
![python-suffix2](image/image-4.png)

---

### 🧩 4. Gắn suffix vào cuối file

```bash
python3 add_suffix.py
```

![insert-suffix](image/image-5.png)

---

### ✅ 5. Kiểm tra mã băm

```bash
md5sum md5_data1
md5sum md5_data2
```

> 🎉 Kết quả: **2 file có cùng mã băm MD5**

![md5-check](image/image-6.png)

---

### 🚀 6. Thực thi và kiểm chứng

- **File 1: `md5_data1`**

  Kết quả: in ra dòng chữ.

  ![run1](image/image-7.png)

- **File 2: `md5_data2`**

  Kết quả: mở shell `/bin/sh`.

  ![run2](image/image-8.png)
