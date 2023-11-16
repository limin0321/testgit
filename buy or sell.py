myMoney = int(input("มีเงินเท่าไหร่ : "))
uCan = myMoney * 0.5
price = int(input("ราคาสินค้า : "))
D_one = myMoney - price
if D_one > uCan:
    print("ซื้อได้นะงับ")
else:
    print("เก็บเงินดีกว่าเนอะ")
