# รับค่าน้ำหนักจากผู้ใช้ (กิโลกรัม)
weight = float(input("Enter your weight (kg): "))
# รับค่าส่วนสูงจากผู้ใช้ (เซนติเมตร)
height_cm = float(input("Enter your height (cm): "))
# แปลงส่วนสูงจากเซนติเมตรเป็นเมตร
height_m = height_cm / 100
# คำนวณค่า BMI
bmi = weight / (height_m ** 2)
# แสดงผลลัพธ์ BMI
print(f"BMI = {bmi:.2f}")
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")