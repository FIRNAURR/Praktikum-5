print("Hello world")
print("yaudah")

x = 5
y = 5
z = x**y
print("selamat datang di GitHub")

class Balok :

    def __init__(self, P,L,T):
        self.Panjang = P
        self.Lebar = L
        self.Tinggi = T

    def Panjangbalok(self, P):
        self.Panjang = P
    
    def Lebarbalok(self, L):
        self.Lebar = L

    def Tinggibalok(self):
        self.Tinggi = T
    
    def HitungLuasbalok(self):
        return (self.Panjang * self.Lebar * self.Tinggi)

    def HitungKelilingbalok(self):
        return 4 * (self.Panjang + self.Lebar + self.Tinggi)
    
    def cetakluas(self):
        print('Luas Balok= %.2f' % self.HitungLuasbalok())

    def cetakkeliling(self):
        print('Keliling Balok= %.2f' % self.HitungKelilingbalok())

hasil1 = Balok(2,4,6)
hasil1.cetakluas()
print(hasil1)
hasil1.cetakkeliling()
print(hasil1)

stk = [1,2,3,4,5]
print(stk)
#memasukkan data baru
stk.append(11)
print("data masuk", 11)
print("data sekarang", stk)
print(len(stk))

