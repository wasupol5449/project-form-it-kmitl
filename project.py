# ม.5 วสุพล คล้ายขำ / Email: wasupolklaykam@gmail.com / ชื่อDiscord: ม.5 โชค วสุพล ปทุมธานี 
# สูตรหาแรงไฟฟ้า = F = (k*Q1*Q2)/R^2
# สูตรหาพลังงานไฟฟ้า = E (k*Q1*Q2)/R
# F = แรงไฟฟ้า หน่วยN / E = พลังงานไฟฟ้า หน่วยJ / k = ค่าคงที่ 9×(10^9) / Q1 = ประจุไฟฟ้าจุดที่1 หน่วยC / Q2 = ประจุไฟฟ้าจุดที่2 หน่วยC / R = ระยะห่างระหว่างจุดประจุ หน่วยm
import math

print("เรามาหาค่าของแรงไฟฟ้าและค่าของพลังงานไฟฟ้ากันเถอะ")
Q1 = int(input('ประจุไฟฟ้าจุดที่1 = '))
Q2 = int(input('ประจุไฟฟ้าจุดที่2 = '))
R = int(input('ระยะห่างระหว่างจุดประจุ = '))
F =  ((9000000000*Q1*Q1)/(R**2))
E =  ((9000000000*Q1*Q1)/R)

print("แรงไฟฟ้าเท่ากับ %s นิวตัน" %F)
print("พลังงานไฟฟ้าเท่ากับ %s จูล" %E)