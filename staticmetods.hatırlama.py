"""
Python'da staticmethod  sınıfın bir üyesi olarak tanımlanan,
ancak bu metodun çalıştırılması için sınıf örneğine (instance) ihtiyaç duyulmayan bir fonksiyondur. 
Yani statik metotlar, ne sınıfın özelliklerine (attributes) ne de diğer metodlarına erişebilir. 
Statik metotlar, daha çok sınıfın genel işlevselliğiyle ilgili işlemleri yürütmek için kullanılır, 
ancak bu işlemler sınıfın örneklerine bağlı değildir.
"""

"""
Neden Statik Metot Kullandık?
   Sınıfın Örneğine İhtiyaç Yok: bir Student nesnesine ait belirli verilere (örneğin self.studentNumber, self.name gibi) 
   ihtiyaç duymuyor. Bunun yerine, doğrudan bir öğrenci listesi (student listesi) ile çalışıyor. 
   Dolayısıyla, bu fonksiyonu çağırmak için sınıf örneği oluşturmaya gerek yok.
   Sadece öğrenci listesi gönderilerek çalıştırılabiliyor.
"""

class Matematik:
    
    @staticmethod
    def topla(a, b):
        return a + b

    @staticmethod
    def carp(a, b):
        return a * b

# Statik metodlar sınıf adıyla çağrılabilir, örnek oluşturulmasına gerek yoktur.
print(Matematik.topla(5, 7))  # Çıktı: 12
print(Matematik.carp(4, 6))   # Çıktı: 24

# İsteğe bağlı olarak örnek üzerinden de çağrılabilir, ancak bu yaygın değildir.
m = Matematik()
print(m.topla(5, 7))          # Çıktı: 12
