"""
Uzun Collatz Zincirleri:
Collatz sanısı ilk hafta uygulamasında anlatılmıştır. Bu ödevdeki 
amaç 1 ile kullanıcıdan alınan sayı arasında collatz zincir uzunluğu
yüzün(100) üzerinde olan kaç adet sayı olduğunu hesaplamaktır.

Örneğin kullanıcı 50 girdiğinde program 4 çıktısını vermelidir:
50 girdisi için zincir uzunluğu 100 üzerinde olan sayılar:
27(112):27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
31(107):31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
41(110):41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
47(105): 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1
Örnekteki sayıların her birinin zinciri 47'nin zincirini tamamen içermektedir

Dikkat edilmesi gereken hususlar:
- Kodunuzun çalışmasına süre olarak sınır getirilmiştir(en fazla 32 saniye)
- Collatz zinciri hesaplanırken aynı sayıları tekrar tekrar hesaplamaktan kaçınılmalıdır
- Örneğin 5 sayısının zinciri(5,16,8,4,2,1) ile 16 sayısının zinciri(16,8,4,2,1) ortak
  öğeler içermektedir
- Zincir uzunluklarını bir sözlük yapısında tutarsanız tekrar tekrar hesaplamanın önüne geçebilirsiniz
- Örneğin zincir[16] = 5, zincir[5] = zincir[16] + 1 = 6
- Özyinelemeli yaklaşımla çözüm daha kolay olacaktır
"""
sayi = int(input(''))
zincir={}
sayac=0
def zincir_uzunlugu(sayi):
    if sayi in zincir:
        return zincir[sayi]
    if sayi==1:
        return 1
    if sayi%2 ==0:
        yeni=sayi//2
    else:
        yeni=sayi*3+1

    zinciruz=zincir_uzunlugu(yeni)+1

    zincir[sayi]=zinciruz


    return zinciruz

zincir_uzunlugu(sayi)

for i in range(1,sayi+1):
    uzunluk=zincir_uzunlugu(i)
    if(uzunluk > 100):
        sayac=sayac+1
        

print(sayac)     
