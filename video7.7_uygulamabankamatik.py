#BANKAMATIK


user={
    '12345601': {
    'ad':'Elif Barlik',
    'bakiye':3000,
    'ekHesap':2000
},
    '12345602': {
    'ad':'Zumra Barlik',
    'bakiye':4000,
    'ekHesap':2000
}}

def paraCek(hesapNo):
    miktar=float(input('Cekmek istediginiz miktar: '))
    if miktar<=user[hesapNo]['bakiye']:
        print(f"Parayi Cekebilirsiniz.Kalan Bakiye: {user[hesapNo]['bakiye']-miktar}")
        user[hesapNo]['bakiye']-=miktar
    elif miktar<=(user[hesapNo]['bakiye']+user[hesapNo]['ekHesap']):
        bool=input('Ana hesapta bakiyeniz yetersiz.Ek hesabi kullanmak ister misiniz(e/h): ')
        if bool=='e':
            print(f"Parayi Cekebilirsiniz. Kalan ek bakiye: {(user[hesapNo]['ekHesap'])-(miktar-user[hesapNo]['bakiye'])}")
            user[hesapNo]['bakiye']=0
            user[hesapNo]['ekHesap']-=miktar-user[hesapNo]['bakiye']
        elif bool=='h':
            print('Maalesef bakiyeniz yetersiz')
        else:
            print('Lutfen gecerli harfi girin!')
    else:
        print('Maalesef bakiyeniz yetersiz.')


def banka(hesapNo):

    print(f"Merhaba {user[hesapNo]['ad']}")
    paraCek(hesapNo)


no=input('Hesap No Girin: ')
banka(no)
while True:
    tekrar=input('Baska islem yapmak ister misiniz(e/h): ')
    if tekrar=='e':
        farkli=input('Farkli hesap numarasi ile giris yapmak ister misiniz(e/h): ')
        if farkli=='e':
            no2=input('Hesap No Girin: ')
            banka(no2)
        elif farkli=='h':
            banka(no)
        else:
            print('Lutfen gecerli harfi girin!')
    elif tekrar=='h':
        print('Cikis Yapidi Tesekkurler...')
        break
    else:
        print('Lutfen gecerli harfi girin!')

