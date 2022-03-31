import random

def random_some_number():
  return int(random.random() * 10)

foods = ['ข้าวผัด','ผัดกระเพาะ','ข้าวมันไก่','มาม่าผัด','ส้มตำ','ลาบก้อย','หมูทอด','หมูปิ้ง','ลาบเหนือ','บะหมี่']


print(foods[random_some_number()])