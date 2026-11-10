# API lab results 
  
## Part 0 
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: A Mean Quattro Formaggi
- Step 0.12, results of the three runs without a session (optional): 
- Step 0.16, blocks of "how many of the three tools are excluded": 0 tools, 1 tool, 2 tools, 3 tools
  
## Defect report
- Title: POST /api/pizza ตอบสถานะ 500 เมื่อระบุไม่ใช้ Tool ทั้ง 3 ชนิด
- Request: POST https://quickpizza.grafana.com/api/pizza โดยแนบ token ใน header Authorization และส่ง body เป็น {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
- Expected result: ระบบตอบสถานะ 400 พร้อมข้อความ error ในรูปแบบ JSON เนื่องจากไม่มีพิซซ่าที่ตรงตามเงื่อนไข
- Actual result: ระบบตอบสถานะ 500 และ body ว่าง (Content-Length: 0)
- Severity: Medium เพราะระบบยังใช้งานส่วนอื่นได้และข้อมูลไม่เสียหาย แต่ผู้ใช้ไม่ทราบสาเหตุของข้อผิดพลาดเนื่องจากไม่มีข้อความ error ตอบกลับ
  


## Part A 
- Step A4, status codes when the other user reads, changes and deletes: read 404, change 400, delete 400
  
## Part B 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8.