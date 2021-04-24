#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd #library data analisis dlm tabel
import numpy as np #agregasi & aljabar linier
import matplotlib.pyplot as plt #visualisasi
import seaborn as sns #visualisasi
df = pd.read_excel("survey_probstat.xlsx")


# In[7]:


df.shape


# In[8]:


from numpy import nan as NA


# In[9]:


trash = []
def cleaning1 (init, dat):
    global df
    global trash
    for i in dat:
        for j in range(1,2021):
            if type(df.iloc[j,i])==int:
                df.iloc[j,init] = df.iloc[j,i]
    for x in dat:
        trash.append(x)


# In[10]:


cleaning1([2],[3])
cleaning1([5],[6])
cleaning1([7],[8,9,10,11,12])
cleaning1([13],[14,15,16,17,18])
cleaning1([19],[20,21,22,23,24])
cleaning1([26],[27,28,29])
cleaning1([37],[38,39])
cleaning1([40],[41,42,43,44,45,46,47,48])
cleaning1([49],[50,51])
cleaning1([53],[54,55,56,57,58])
cleaning1([59],[60,61,62,63,64])
cleaning1([77],[78,79,80,81,82,83,84])
cleaning1([85],[86,87,88,89,90,91,92])
cleaning1([93],[*range(94,101)])
cleaning1([101],[*range(102,109)])
cleaning1([109],[*range(110,117)])
cleaning1([117],[*range(118,125)])
cleaning1([125],[*range(126,133)])
cleaning1([133],[*range(134,141)])
cleaning1([141],[*range(142,149)])
cleaning1([149],[*range(150,157)])
cleaning1([157],[*range(158,165)])
cleaning1([165],[166])
cleaning1([167],[168])
cleaning1([169],[170])
cleaning1([171],[172])
cleaning1([173],[174])
cleaning1([175],[176])
cleaning1([177],[178])
cleaning1([249],[*range(250,254)])
cleaning1([254],[*range(255,259)])
cleaning1([259],[*range(260,264)])
cleaning1([264],[*range(265,269)])
cleaning1([269],[*range(270,274)])
cleaning1([274],[*range(275,279)])
cleaning1([279],[*range(280,284)])
cleaning1([284],[*range(285,289)])
cleaning1([289],[*range(290,294)])
cleaning1([294],[*range(295,299)])
cleaning1([299],[*range(300,304)])
cleaning1([309],[310])
cleaning1([345],[346])
cleaning1([389],[390,391,392,393,394,395])
cleaning1([396],[397,398,399,400,401])
cleaning1([408],[409])
cleaning1([422],[423,424])
cleaning1([435],[436])
cleaning1([437],[438])
cleaning1([439],[440])
cleaning1([441],[442])
cleaning1([443],[444])
cleaning1([445],[446])
cleaning1([447],[448])
cleaning1([449],[450])
cleaning1([451],[452])
cleaning1([453],[454])
cleaning1([455],[456])
cleaning1([457],[458])
cleaning1([459],[460])
cleaning1([461],[462])
cleaning1([515],[516,517,518,519])
cleaning1([539],[540])
cleaning1([572],[573,574,575])
cleaning1([576],[*range(577,581)])
cleaning1([581],[*range(582,587)])
cleaning1([587],[588])
cleaning1([606],[607])
cleaning1([608],[609])


# In[11]:


#Jawaban lainnya: one-answer
cleaned1['Pekerjaan?'] = cleaned1['Pekerjaan?'].fillna(cleaned1['Unnamed: 25'])


# In[12]:


def cleaningmult (dat):
    global df
    for i in dat:
        for j in range(1,2021):
            if type(df.iloc[j,i]) == int:
                df.iloc[j,i] = 1


# In[13]:


multanswer = [30,31,32,33,34,35,36,*range(65,76),*range(179,248),*range(304,309),*range(311,345),*range(348,389),*range(402,408),*range(410,422),*range(425,435),*range(463,515),*range(520,539),*range(542,572),*range(589,606)]


# In[14]:


cleaningmult(multanswer) 


# In[15]:


df


# In[404]:


cleaned2 = df.drop_duplicates(['NIM Surveyor (Mahasiswa)','Nama Responden'], keep = 'last')


# In[405]:


cleaned2.shape


# In[406]:


cleaned2 = cleaned2.dropna(how='all',subset=['Apakah Anda pernah menggunakan layanan pembayaran melalui QR Code?','Unnamed: 409'])


# In[407]:


cleaned2.shape


# In[20]:


(cleaned2.iloc[0,5]) = np.NaN #hilangkan judul
cleaned2['Jenis kelamin ?'] = cleaned2['Jenis kelamin ?'].map({1: 'Laki-laki',2:'Perempuan'})
sns.countplot(data=cleaned2, y='Jenis kelamin ?')


# In[387]:


cleaned2.iloc[0,7] = np.NaN #hilangkan judul
cleaned2['Usia :'] = cleaned2['Usia :'].map({1: '<15 tahun',2:'15-20 tahun',3:'21-30 tahun',4:'31-40 tahun',5:'41-50 tahun',6:'>50 tahun'})
sns.countplot(data=cleaned2, y='Usia :')
cleaned2['Usia :'].value_counts()


# In[397]:


confidint(13)
confidint(1172)
confidint(181)
confidint(43)
confidint(84)
confidint(44)


# In[398]:


(cleaned2.iloc[0,13]) = np.NaN
cleaned2['Pendidikan Terakhir?'] = cleaned2['Pendidikan Terakhir?'].map({1: 'SD',2:'SMP',3:'SMA',4:'S1',5:'S2',6:'S3'})
sns.countplot(data=cleaned2, y='Pendidikan Terakhir?')
cleaned2['Pendidikan Terakhir?'].value_counts()


# In[399]:


confidint(3)
confidint(16)
confidint(1127)
confidint(351)
confidint(35)
confidint(2)


# In[400]:


global cleaned2
for i in [19]:
    for j in range(0,1545):
        if (cleaned2.iloc[j,i])== 1:
            cleaned2.iloc[j,i] = 'Pelajar/Mahasiswa'
        elif (cleaned2.iloc[j,i])== 2:
            cleaned2.iloc[j,i] = 'Karyawan Swasta'
        elif (cleaned2.iloc[j,i])== 3:
            cleaned2.iloc[j,i] = 'Ibu Rumah Tangga'
        elif (cleaned2.iloc[j,i])== 4:
            cleaned2.iloc[j,i] = 'Pegawai Negeri'
        elif (cleaned2.iloc[j,i])== 5:
            cleaned2.iloc[j,i] = 'Profesional'
        elif (cleaned2.iloc[j,i])== 6:
            cleaned2.iloc[j,i] = 'Pengusaha'

#Penambahan tabel "Lainnya"      
cleaned2['Pekerjaan?'] = cleaned2['Pekerjaan?'].fillna(cleaned2['Unnamed: 25'])

(cleaned2.iloc[0,19]) = np.NaN
fig_dims = (10, 8)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(data=cleaned2, y='Pekerjaan?',ax=ax)
cleaned2['Pekerjaan?'].value_counts()


# In[401]:


confidint(1245)
confidint(136)
confidint(51)
confidint(28)
confidint(22)
confidint(22)


# In[408]:


(cleaned2.iloc[0,26]) = np.NaN
cleaned2['Penghasilan per bulan?'] = cleaned2['Penghasilan per bulan?'].map({1: '<2 juta',2:'2-5 juta',3:'5-10 juta',4:'>10 juta'})
sns.countplot(data=cleaned2, y='Penghasilan per bulan?')
cleaned2['Penghasilan per bulan?'].value_counts()


# In[409]:


confidint(1134)
confidint(198)
confidint(102)
confidint(79)


# In[410]:


for i in range(30,37):
    cleaned2.iloc[0,i]=np.NaN
dom = cleaned2[['Domisili saat ini', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34','Unnamed: 35', 'Unnamed: 36']].copy()
dom = dom.rename(columns={'Domisili saat ini': 'Jakarta', 'Unnamed: 31':'Bandung','Unnamed: 32': 'Yogyakarta','Unnamed: 33': 'Tangerang','Unnamed: 34':'Surabaya','Unnamed: 35':'Bali','Unnamed: 36':'Lainnya'})
dom.sum().plot(kind='barh')


# In[413]:


print(dom['Jakarta'].value_counts())
print(dom['Bandung'].value_counts())
print(dom['Yogyakarta'].value_counts())
print(dom['Tangerang'].value_counts())
print(dom['Surabaya'].value_counts())
print(dom['Bali'].value_counts())


# In[414]:


confidint(337)
confidint(334)
confidint(34)
confidint(95)
confidint(49)
confidint(19)


# In[29]:


#Visualisasi data "Lainnya"
x = dom['Lainnya'].sort_values(ascending=True)
a=pd.DataFrame(x)
sns.countplot(data=a.head(50), y='Lainnya')


# In[37]:


(cleaned2.iloc[0,37]) = np.NaN #hapus judul
cleaned2['Apakah aktivitas online anda meningkat dalam 3 bulan terakhir?'] = cleaned2['Apakah aktivitas online anda meningkat dalam 3 bulan terakhir?'].map({1: 'Ya',2:'Tidak',3:'Sama saja'})
sns.countplot(data=cleaned2, y='Apakah aktivitas online anda meningkat dalam 3 bulan terakhir?')


# In[44]:


(cleaned2.iloc[0,40]) = np.NaN #hapus judul
cleaned2['Rata-rata durasi menggunakan internet Aktif tiap hari ?'] = cleaned2['Rata-rata durasi menggunakan internet Aktif tiap hari ?'].map({1: '1 jam',2:'2 jam',3:'3 jam', 4:'4 jam',5:'5 jam',6:'6 jam',7:'7 jam',8:'8 jam',9: '>8 jam'})
sns.countplot(data=cleaned2, y='Rata-rata durasi menggunakan internet Aktif tiap hari ?')


# In[51]:


(cleaned2.iloc[0,49]) = np.NaN #hapus judul
cleaned2['Akses atau provider internet yang digunakan selama ini?'] = cleaned2['Akses atau provider internet yang digunakan selama ini?'].map({1: 'Mobile data',2:'Broadband',3:'Broadband & mobile data'})
sns.countplot(data=cleaned2, y='Akses atau provider internet yang digunakan selama ini?')


# In[53]:


cleaned2.iloc[0,52] = np.nan
lowercased = cleaned2['Unnamed: 52'].str.lower()
lc = pd.DataFrame(lowercased)

sns.countplot(data=lc.head(50), y='Unnamed: 52')


# In[58]:


cleaned3 = cleaned2.rename(columns={'Berapa pengeluaran Anda untukÂ belanja kebutuhan internet (baik mobile data maupun paket broadband/ wifi) per bulan ?': 'Biaya Mobile Data'})
cleaned3.iloc[0,53]=np.NaN
cleaned3['Biaya Mobile Data'] = cleaned3['Biaya Mobile Data'].map({1: '< 100ribu',2:'100-200 ribu',3:'201-300 ribu', 4:'301-400ribu', 5:'401-500ribu',6:'>500ribu'})
sns.countplot(data=cleaned3, y='Biaya Mobile Data')


# In[60]:


cleaned4 = cleaned2.rename(columns={'Unnamed: 59': 'Biaya Broadband'})
cleaned4.iloc[0,59]=np.NaN
cleaned4['Biaya Broadband'] = cleaned4['Biaya Broadband'].map({1: '< 100ribu',2:'100-200 ribu',3:'201-300 ribu', 4:'301-400ribu', 5:'401-500ribu',6:'>500ribu'})
sns.countplot(data=cleaned4, y='Biaya Broadband')


# In[128]:


cleact = cleaned2
for i in range(65,77):
    cleact.iloc[0,i]=np.NaN
for s in [76]:
    for j in range(0,1545):
        if type(cleact.iloc[j,s]) == str:
                    cleact.iloc[j,i] = 1
act = cleact[['Manakah dari aktivitas berikut yang mengalami peningkatan selama 3 bulan terakhir?', 'Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68', 'Unnamed: 69','Unnamed: 70', 'Unnamed: 71', 'Unnamed: 72', 'Unnamed: 73', 'Unnamed: 74', 'Unnamed: 75', 'Unnamed: 76']].copy()
actx = act.rename(columns={'Manakah dari aktivitas berikut yang mengalami peningkatan selama 3 bulan terakhir?': 'Belanja online', 'Unnamed: 66':'Streaming video','Unnamed: 67': 'Video Conference','Unnamed: 68': 'Delivery','Unnamed: 69':'Kelas olahraga online','Unnamed: 70':'Kelas online','Unnamed: 71':'Akses media sosial','Unnamed: 72':'Game Online','Unnamed: 73':'Akses E-sport','Unnamed: 74':'Membeli obat secara online','Unnamed: 75':'Konsultasi kesehatan secara online','Unnamed: 76':'Lainnya'})
actx.sum().plot(kind='barh',title='Peningkatan aktivitas selama 3 bulan terakhir')


# In[127]:


cleaned2.iloc[0,76] = np.nan
cleaned2.iloc[48,76] = np.nan
lowercased1 = cleaned2['Unnamed: 76'].str.lower()
lc1 = pd.DataFrame(lowercased1)

sns.countplot(data=lc1.tail(400), y='Unnamed: 76')


# In[92]:


#2.6


# In[ ]:


#2.7


# In[129]:


clecomm = cleaned2
for i in range(179,185):
    clecomm.iloc[0,i]=np.NaN
for s in [184]:
    for j in range(0,1545):
        if type(clecomm.iloc[j,s]) == str:
                    clecomm.iloc[j,i] = 1
comm = clecomm[['Media komunikasi yang paling sering digunakan untuk Work From Home/Â School From Home ?', 'Unnamed: 180', 'Unnamed: 181', 'Unnamed: 182', 'Unnamed: 183','Unnamed: 184']].copy()
commx = comm.rename(columns={'Media komunikasi yang paling sering digunakan untuk Work From Home/Â School From Home ?': 'Email', 'Unnamed: 180':'Chatting','Unnamed: 181': 'Conference call','Unnamed: 182': 'Video streaming','Unnamed: 183':'web download','Unnamed: 184':'Lainnya'})
commx.sum().plot(kind='barh', title='Media komunikasi dalam WFH')


# In[137]:


#representasi jawaban lainnya
cleaned2.iloc[0,184] = np.nan
lowercased2 = cleaned2['Unnamed: 184'].str.lower()
lc2 = pd.DataFrame(lowercased2)

sns.countplot(data=lc2.head(500), y='Unnamed: 184')


# In[158]:


cleapp = cleaned2
for i in range(185,193):
    cleapp.iloc[0,i]=np.NaN
for s in [192]:
    for j in range(0,1545):
        if type(cleapp.iloc[j,s]) == str:
                    cleapp.iloc[j,s] = 1
app = cleaned2[['Aplikasi apa yang biasa digunakan untuk Work From Home/ School from Home ?', 'Unnamed: 186', 'Unnamed: 187', 'Unnamed: 188', 'Unnamed: 189','Unnamed: 190','Unnamed: 191','Unnamed: 192']].copy()
appx = app.rename(columns={'Aplikasi apa yang biasa digunakan untuk Work From Home/ School from Home ?': 'Whatsapp', 'Unnamed: 186':'Zoom','Unnamed: 187': 'Google meet','Unnamed: 188': 'Ms. Teams','Unnamed: 189':'Cisco webex','Unnamed: 190':'Skype for business','Unnamed: 191':'goToMeeting','Unnamed: 192':'Lainnya'})
appx=appx.astype(float)
appx.sum().plot(kind='barh', title='Aplikasi komunikasi dalam WFH')


# In[165]:


cleaned2.iloc[0,184] = np.nan
lowercased3 = cleaned2['Unnamed: 192'].str.lower()
lc3 = pd.DataFrame(lowercased3)

sns.countplot(data=lc3.head(250), y='Unnamed: 192')


# In[171]:


clewhy = cleaned2
for i in range(193,200):
    clewhy.iloc[0,i]=np.NaN
for s in [199]:
    for j in range(0,1545):
        if type(clewhy.iloc[j,s]) == str:
                    clewhy.iloc[j,s] = 1
why = clewhy[['Alasan menggunakan aplikasi tersebut (Mohon sebutkan 3 alasan utama)', 'Unnamed: 194', 'Unnamed: 195', 'Unnamed: 196', 'Unnamed: 197','Unnamed: 198','Unnamed: 199']].copy()
whyx = why.rename(columns={'Alasan menggunakan aplikasi tersebut (Mohon sebutkan 3 alasan utama)': 'Mudah digunakan', 'Unnamed: 194':'Digunakan banyak orang','Unnamed: 195': 'hemat kuota','Unnamed: 196': 'Lebih aman','Unnamed: 197':'durasi unlimited','Unnamed: 198':'telah ditetapkan korporasi','Unnamed: 199':'Lainnya'})
whyx.sum().plot(kind='barh', title='Alasan menggunakan aplikasi komunikasi dalam WFH')


# In[169]:


cleaned2.iloc[0,199] = np.nan
lowercased4 = cleaned2['Unnamed: 199'].str.lower()
lc4 = pd.DataFrame(lowercased4)

sns.countplot(data=lc4.head(1000), y='Unnamed: 199')


# In[173]:


clebank = cleaned2
for i in range(200,206):
    clebank.iloc[0,i]=np.NaN
for s in [205]:
    for j in range(0,1545):
        if type(clebank.iloc[j,s]) == str:
                    clebank.iloc[j,s] = 1
bank = clebank[['Apakah Anda menggunakan layanan-layanan bank berikut?', 'Unnamed: 201', 'Unnamed: 202', 'Unnamed: 203', 'Unnamed: 204', 'Unnamed: 205']].copy()
bankx = bank.rename(columns={'Apakah Anda menggunakan layanan-layanan bank berikut?': 'ATM', 'Unnamed: 201':'Internet','Unnamed: 202': 'M-banking','Unnamed: 203': 'SMS Banking','Unnamed: 204':'credit card','Unnamed: 205':'Datang ke kantor cabang'})
bankx.sum().plot(kind='barh', title='Layanan bank yang pernah digunakan')


# In[174]:


#3.2


# In[175]:


#3.3


# In[176]:


#3.4


# In[178]:


clekel = cleaned2
for i in range(304,309):
    clebank.iloc[0,i]=np.NaN
for s in [308]:
    for j in range(0,1545):
        if type(clebank.iloc[j,s]) == str:
                    clebank.iloc[j,s] = 1
kel = clekel[['Keluhan / Kerugian apa yang pernah Anda alami saat menggunakan layanan eChannel bank (ATM, internet banking, mobile banking, sms banking, CC)?', 'Unnamed: 305', 'Unnamed: 306', 'Unnamed: 307', 'Unnamed: 308']].copy()
kelx = kel.rename(columns={'Keluhan / Kerugian apa yang pernah Anda alami saat menggunakan layanan eChannel bank (ATM, internet banking, mobile banking, sms banking, CC)?': 'Layanan/Sistem Down', 'Unnamed: 305':'Proses gagal saldo terpotong','Unnamed: 306': 'Saldo terpotong tanpa transaksi','Unnamed: 307': 'Transaksi pembayaran yang sama terjadi 2 x','Unnamed: 308':'lainnya'})
kelx.sum().plot(kind='barh', title='Keluhan penggunaan eChannel')


# In[189]:


cleaned2.iloc[0,308] = np.nan
lowercased5 = cleaned2['Unnamed: 308'].str.lower()
lc5 = pd.DataFrame(lowercased5)

sns.countplot(data=lc5.head(100), y='Unnamed: 308')


# In[196]:


cleaned4 = cleaned2.rename(columns={'Apakah Anda pernah melakukan pendaftaran rekening melalui full online (sama sekali tidak datang ke kantor cabang bank) ?': 'Mendaftar rekening full-online'})
(cleaned4.iloc[0,309]) = np.NaN #hilangkan judul

cleaned4['Mendaftar rekening full-online'] = cleaned4['Mendaftar rekening full-online'].map({1: 'Pernah',2:'Tidak Pernah'})
sns.countplot(data=cleaned4, y='Mendaftar rekening full-online')


# In[201]:


cleon = cleaned2
for i in range(311,319):
    cleon.iloc[0,i]=np.NaN
for s in [318]:
    for j in range(0,1545):
        if type(cleon.iloc[j,s]) == str:
                    cleon.iloc[j,s] = 1                                                                                                #Digibank by Bank DBS	Permata Mobile X by Bank Permata	D-Bank by Bank Danamon	BRIMo by BRI	BCA	Lainnya, mohon sebutk
on = cleon[['Jika Pernah membuka layanan rekening bank secara online, bank apakah yang Anda daftar secara online?', 'Unnamed: 312', 'Unnamed: 313', 'Unnamed: 314', 'Unnamed: 315', 'Unnamed: 316', 'Unnamed: 317', 'Unnamed: 318']].copy()
onx = on.rename(columns={'Jika Pernah membuka layanan rekening bank secara online, bank apakah yang Anda daftar secara online?': 'Tidak Pernah', 'Unnamed: 312':'Jenius by Bank BTPN','Unnamed: 313': 'Digibank by Bank DBS','Unnamed: 314': 'Permata Mobile X by Bank Permata','Unnamed: 315':'D-Bank by Bank Danamon','Unnamed: 316':'BRIMo by BRI','Unnamed: 317':'BCA','Unnamed: 318':'Lainnya'})
onx.sum().plot(kind='barh', title='Bank yang pernah didaftarkan secara online')


# In[200]:


cleaned2.iloc[0,318] = np.nan
lowercased6 = cleaned2['Unnamed: 318'].str.lower()
lc6 = pd.DataFrame(lowercased6)

sns.countplot(data=lc6.head(600), y='Unnamed: 318')


# In[213]:


alasan = cleaned2[['Apakah yang menjadi alasan Anda menggunakan bank full online / digital bank tersebut?', 'Unnamed: 320', 'Unnamed: 321', 'Unnamed: 322', 'Unnamed: 323', 'Unnamed: 324']].copy()
for i in range(0,6):
    alasan.iloc[0,i]=np.NaN
for s in [5]:
    for j in range(0,1545):
        if type(alasan.iloc[j,s]) == str:
                    alasan.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
alasanx = alasan.rename(columns={'Apakah yang menjadi alasan Anda menggunakan bank full online / digital bank tersebut?': 'Tidak memiliki rekening di bank online', 'Unnamed: 320':'kemudahan transaksi','Unnamed: 321': 'kemudahan pembukaan rekening','Unnamed: 322': 'promo','Unnamed: 323':'karena sedang tren','Unnamed: 324':'Lainnya'})
alasanx.sum().plot(kind='barh', title='Alasan penggunaan bank online')


# In[223]:


cleaned2.iloc[0,324] = np.nan
lowercased7 = cleaned2['Unnamed: 324'].str.lower()
lc7 = pd.DataFrame(lowercased7)

sns.countplot(data=lc7.head(500), y='Unnamed: 324')


# In[227]:


fitur = cleaned2[['Fitur yang paling sering digunakan saat menggunakan bank full online/ digital bank tersebut?', 'Unnamed: 326', 'Unnamed: 327', 'Unnamed: 328', 'Unnamed: 329', 'Unnamed: 330', 'Unnamed: 331', 'Unnamed: 332']].copy()
for i in range(0,8):
    fitur.iloc[0,i]=np.NaN
for s in [7]:
    for j in range(0,1545):
        if type(fitur.iloc[j,s]) == str:
                    fitur.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
fiturx = fitur.rename(columns={'Fitur yang paling sering digunakan saat menggunakan bank full online/ digital bank tersebut?': 'Tidak memiliki rekening di bank online', 'Unnamed: 326':'Cek Saldo','Unnamed: 327': 'Transfer','Unnamed: 328': 'Pembelian Pulsa, eMoney, & voucher','Unnamed: 329':'Pembayaran Tagihan','Unnamed: 330':'Mutasi rekening/ History Transaksi/ Spending','Unnamed: 331':'Deposito','Unnamed: 332':'Lainnya'})
fiturx.sum().plot(kind='barh', title='Fitur bank online yang digunakan')


# In[224]:


cleaned2.iloc[0,332] = np.nan
lowercased8 = cleaned2['Unnamed: 332'].str.lower()
lc8 = pd.DataFrame(lowercased8)

sns.countplot(data=lc8.head(500), y='Unnamed: 332')


# In[229]:


keluhan = cleaned2[['Kerugian/ Keluhan apa yang pernah Anda yang dialami selama menggunakan bank full online/ digital banking tersebut?', 'Unnamed: 334', 'Unnamed: 335', 'Unnamed: 336', 'Unnamed: 337', 'Unnamed: 338', 'Unnamed: 339']].copy()
for i in range(0,7):
    keluhan.iloc[0,i]=np.NaN
for s in [6]:
    for j in range(0,1545):
        if type(keluhan.iloc[j,s]) == str:
                    keluhan.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
keluhanx = keluhan.rename(columns={'Kerugian/ Keluhan apa yang pernah Anda yang dialami selama menggunakan bank full online/ digital banking tersebut?': 'Tidak pernah mengalami keluhan', 'Unnamed: 334':'Sistem error/tak dapat diakses','Unnamed: 335': 'Transaksi tidak berhasil namun saldo berkurang','Unnamed: 336': 'Tidak melakukan transaksi tapi saldo berkurang','Unnamed: 337':'Kesulitan menghubungi customer service','Unnamed: 338':'Rekening dihack','Unnamed: 339':'Lainnya'})
keluhanx.sum().plot(kind='barh', title='Keluhan bank online yang digunakan')


# In[228]:


cleaned2.iloc[0,339] = np.nan
lowercased9 = cleaned2['Unnamed: 339'].str.lower()
lc9 = pd.DataFrame(lowercased9)

sns.countplot(data=lc9.head(500), y='Unnamed: 339')


# In[232]:


tp = cleaned2[['Jika Tidak Pernah melakukan pembukaan rekening secara online, apa yang menjadi alasan Anda?', 'Unnamed: 341', 'Unnamed: 342', 'Unnamed: 343', 'Unnamed: 344']].copy()
for i in range(0,5):
    tp.iloc[0,i]=np.NaN
for s in [4]:
    for j in range(0,1545):
        if type(tp.iloc[j,s]) == str:
                    tp.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
tpx = tp.rename(columns={'Jika Tidak Pernah melakukan pembukaan rekening secara online, apa yang menjadi alasan Anda?': 'Tidak tahu keberadaanya', 'Unnamed: 341':'Tidak tertarik','Unnamed: 342': 'Tidak perlu','Unnamed: 343': 'Tidak merasa aman','Unnamed: 344':'lainnya'})
tpx.sum().plot(kind='barh', title='Alasan tidak membuka rekening bank online')


# In[231]:


cleaned2.iloc[0,344] = np.nan
lowercased10 = cleaned2['Unnamed: 344'].str.lower()
lc10 = pd.DataFrame(lowercased10)

sns.countplot(data=lc10.head(250), y='Unnamed: 344')


# In[233]:


(cleaned2.iloc[0,345]) = np.NaN #hilangkan judul
cleaned2['Pernahkah Mendaftar kartu kredit online?'] = cleaned2['Apakah Anda pernah mendaftar Kartu Kredit melalui online?'].map({1: 'Pernah',2:'Tidak pernah'})
sns.countplot(data=cleaned2, y='Pernahkah Mendaftar kartu kredit online?')


# In[234]:


cleaned2.iloc[0,347] = np.nan
lowercased11 = cleaned2['Unnamed: 347'].str.lower()
lc11 = pd.DataFrame(lowercased11)

sns.countplot(data=lc11, y='Unnamed: 347')


# In[242]:


emoney = cleaned2[['Apakah Anda menggunakan eMoney berikut? (jawaban boleh lebih dari 1)', 'Unnamed: 349', 'Unnamed: 350', 'Unnamed: 351', 'Unnamed: 352', 'Unnamed: 353', 'Unnamed: 354', 'Unnamed: 355', 'Unnamed: 356', 'Unnamed: 357', 'Unnamed: 358', 'Unnamed: 359', 'Unnamed: 360']].copy()
for i in range(0,13):
    emoney.iloc[0,i]=np.NaN
for s in [12]:
    for j in range(0,1545):
        if type(emoney.iloc[j,s]) == str:
                    emoney.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
emoneyx = emoney.rename(columns={'Apakah Anda menggunakan eMoney berikut? (jawaban boleh lebih dari 1)': 'Tidak Menggunakan eMoney', 'Unnamed: 349':'Gopay','Unnamed: 350': 'OVO','Unnamed: 351': 'LinkAja','Unnamed: 352':'Dana', 'Unnamed: 353':'Paytren','Unnamed: 354': 'ShopeePay','Unnamed: 355': 'Flazz BCA','Unnamed: 356':'Brizzi', 'Unnamed: 357':'eMoney Mandiri','Unnamed: 358': 'JakCard','Unnamed: 359': 'iSaku','Unnamed: 360':'Lainnya'})
emoneyx.sum().plot(kind='barh', title='Rekening eMoney yang digunakan target survey')


# In[416]:


print(emoneyx['Tidak Menggunakan eMoney'].value_counts())
print(emoneyx['Gopay'].value_counts())
print(emoneyx['OVO'].value_counts())
print(emoneyx['LinkAja'].value_counts())
print(emoneyx['Paytren'].value_counts())
print(emoneyx['Dana'].value_counts())
print(emoneyx['ShopeePay'].value_counts())
print(emoneyx['Flazz BCA'].value_counts())
print(emoneyx['Brizzi'].value_counts())
print(emoneyx['eMoney Mandiri'].value_counts())
print(emoneyx['JakCard'].value_counts())
print(emoneyx['iSaku'].value_counts())
print(emoneyx['Lainnya'].value_counts())


# In[417]:


confidint(143)
confidint(1217)
confidint(1074)
confidint(259)
confidint(9)
confidint(627)
confidint(662)
confidint(271)
confidint(74)
confidint(313)
confidint(19)
confidint(25)
confidint(33)


# In[241]:


cleaned2.iloc[0,360] = np.nan
lowercased12 = cleaned2['Unnamed: 360'].str.lower()
lc12 = pd.DataFrame(lowercased12)

sns.countplot(data=lc12, y='Unnamed: 360')


# In[246]:


rsn = cleaned2[['Mengapa Anda menggunakan layanan tersebut?', 'Unnamed: 362', 'Unnamed: 363', 'Unnamed: 364', 'Unnamed: 365', 'Unnamed: 366', 'Unnamed: 367']].copy()
for i in range(0,7):
    rsn.iloc[0,i]=np.NaN
for s in [6]:
    for j in range(0,1545):
        if type(rsn.iloc[j,s]) == str:
                    rsn.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
rsnx = rsn.rename(columns={'Mengapa Anda menggunakan layanan tersebut?': 'Tidak Menggunakan eMoney', 'Unnamed: 362':'Simple','Unnamed: 363': 'Efisien secara waktu','Unnamed: 364': 'Tidak perlu ke bank','Unnamed: 365':'Promo', 'Unnamed: 366':'Aman','Unnamed: 367': 'Lainnya'})
rsnx.sum().plot(kind='barh', title='Alasan pengguna menggunakan eMoney')


# In[245]:


cleaned2.iloc[0,367] = np.nan
lowercased13 = cleaned2['Unnamed: 367'].str.lower()
lc13 = pd.DataFrame(lowercased13)

sns.countplot(data=lc13.head(500), y='Unnamed: 367')


# In[248]:


need = cleaned2[['Untuk keperluan apa Anda biasanya menggunakan layanan tersebut?', 'Unnamed: 369', 'Unnamed: 370', 'Unnamed: 371', 'Unnamed: 372', 'Unnamed: 373', 'Unnamed: 374', 'Unnamed: 375', 'Unnamed: 376', 'Unnamed: 377', 'Unnamed: 378', 'Unnamed: 379']].copy()
for i in range(0,12):
    need.iloc[0,i]=np.NaN
for s in [11]:
    for j in range(0,1545):
        if type(need.iloc[j,s]) == str:
                    need.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
needx = need.rename(columns={'Untuk keperluan apa Anda biasanya menggunakan layanan tersebut?': 'Tidak Menggunakan eMoney', 'Unnamed: 369':'Pembayaran transportasi online','Unnamed: 370': 'Pembayaran Tol','Unnamed: 371': 'Pembayaran Transportasi umum','Unnamed: 372':'Pembayaran tiket parkir', 'Unnamed: 373':'Pembelian delivery makanan','Unnamed: 374': 'Pembayaran Restoran/cafe','Unnamed: 375': 'Pembayaran di minimarket','Unnamed: 376':'Pembayaran e-commerce', 'Unnamed: 377':'Pembelian pulsa','Unnamed: 378': 'Pembayaran utilitas(PLN,PDAM,dll)','Unnamed: 379': 'Lainnya'})
needx.sum().plot(kind='barh', title='Rekening eMoney yang digunakan target survey')


# In[247]:


cleaned2.iloc[0,379] = np.nan
lowercased14 = cleaned2['Unnamed: 379'].str.lower()
lc14 = pd.DataFrame(lowercased14)

sns.countplot(data=lc14.head(500), y='Unnamed: 379')


# In[256]:


tpo = cleaned2[['Bagaimana cara top up yang biasa Anda lakukan?', 'Unnamed: 381', 'Unnamed: 382', 'Unnamed: 383', 'Unnamed: 384', 'Unnamed: 385', 'Unnamed: 386', 'Unnamed: 387', 'Unnamed: 388']].copy()
for i in range(0,9):
    tpo.iloc[0,i]=np.NaN
for s in [8]:
    for j in range(0,1545):
        if type(tpo.iloc[j,s]) == str:
                    tpo.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
tpox = tpo.rename(columns={'Bagaimana cara top up yang biasa Anda lakukan?': 'Tidak Menggunakan eMoney', 'Unnamed: 381':'ATM','Unnamed: 382': 'Mobile Banking','Unnamed: 383': 'Internet Banking','Unnamed: 384':'SMS Banking', 'Unnamed: 385':'Melalui driver','Unnamed: 386': 'Top up di Minimarket','Unnamed: 387': 'Melalui loket PPOB','Unnamed: 388':'Lainnya'})
tpox.sum().plot(kind='barh', title='Cara Top-up rekening eMoney')


# In[255]:


cleaned2.iloc[0,388] = np.nan
lowercased15 = cleaned2['Unnamed: 388'].str.lower()
lc15 = pd.DataFrame(lowercased15)

sns.countplot(data=lc15.head(1300), y='Unnamed: 388')


# In[258]:


cleaned2.iloc[0,389] = np.NaN #hilangkan judul
cleaned2['Nominal Top-up'] = cleaned2['Berapa biasanya nominal Anda melakukan top up/ isi ulang?'].map({1: 'Tidak Menggunakan eMoney',2:'<Rp25.000',3:'Rp25.000-Rp50.000',4:'Rp50,001-Rp100.000',5:'Rp100.001-Rp150.000',6:'Rp150.001-Rp300.000',7:'>Rp300.000'})
sns.countplot(data=cleaned2, y='Nominal Top-up')


# In[259]:


cleaned2.iloc[0,396] = np.NaN #hilangkan judul
cleaned2['Frekuensi Top-up'] = cleaned2['Berapa frekuensi top up/ Isi ulang ?'].map({1: 'Tidak Menggunakan eMoney',2:'Beberapa kali seminggu',3:'Sekali seminggu',4:'Sekali Sebulan',5:'Sangat jarang',6:'Hanya saat ingin menggunakan'})
sns.countplot(data=cleaned2, y='Frekuensi Top-up')


# In[262]:


kem = cleaned2[['Kendala apa yang pernah Anda alami saat menggunakan layanan tersebut?', 'Unnamed: 403', 'Unnamed: 404', 'Unnamed: 405', 'Unnamed: 406', 'Unnamed: 407']].copy()
for i in range(0,6):
    kem.iloc[0,i]=np.NaN
for s in [5]:
    for j in range(0,1545):
        if type(kem.iloc[j,s]) == str:
                    kem.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
kemx = kem.rename(columns={'Kendala apa yang pernah Anda alami saat menggunakan layanan tersebut?': 'Tidak Menggunakan eMoney', 'Unnamed: 403':'Aplikasi tak bisa diakses','Unnamed: 404': 'Nominal saldo berkurang saat tidak digunakan','Unnamed: 405': 'Saldo tak bertambah setelah Top-up','Unnamed: 406':'Kartu eMoney tak terdeteksi', 'Unnamed: 407':'Lainnya'})
kemx.sum().plot(kind='barh', title='Kendala Top-up rekening eMoney')


# In[261]:


cleaned2.iloc[0,407] = np.nan
lowercased16 = cleaned2['Unnamed: 407'].str.lower()
lc16 = pd.DataFrame(lowercased16)

sns.countplot(data=lc16.head(300), y='Unnamed: 407')


# In[263]:


cleaned2.iloc[0,408] = np.NaN #hilangkan judul
cleaned2['Pernahkah Melakukan transaksi QR-Code'] = cleaned2['Apakah Anda pernah menggunakan layanan pembayaran melalui QR Code?'].map({1: 'Pernah',2:'Tidak Pernah'})
sns.countplot(data=cleaned2, y='Pernahkah Melakukan transaksi QR-Code')


# In[268]:


qr = cleaned2[['Jika Pernah, layanan QR CodeÂ apa yang Anda gunakan ?', 'Unnamed: 411', 'Unnamed: 412', 'Unnamed: 413', 'Unnamed: 414']].copy()
for i in range(0,5):
    qr.iloc[0,i]=np.NaN
for s in [4]:
    for j in range(0,1545):
        if type(qr.iloc[j,s]) == str:
                    qr.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
qrx = qr.rename(columns={'Jika Pernah, layanan QR CodeÂ apa yang Anda gunakan ?': 'Gopay', 'Unnamed: 411':'OVO','Unnamed: 412': 'LinkAja','Unnamed: 413': 'Paytren','Unnamed: 414':'Lainnya'})
qrx.sum().plot(kind='barh', title='Layanan QR Code yang digunakan')


# In[264]:


cleaned2.iloc[0,414] = np.nan
lowercased17 = cleaned2['Unnamed: 414'].str.lower()
lc17 = pd.DataFrame(lowercased17)

sns.countplot(data=lc17.head(300), y='Unnamed: 414')


# In[271]:


usg = cleaned2[['Jika Pernah, dimana Anda menggunakan pembayaran melalui QR Code tersebut?', 'Unnamed: 416', 'Unnamed: 417', 'Unnamed: 418', 'Unnamed: 419', 'Unnamed: 420', 'Unnamed: 421']].copy()
for i in range(0,7):
    usg.iloc[0,i]=np.NaN
for s in [6]:
    for j in range(0,1545):
        if type(usg.iloc[j,s]) == str:
                    usg.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
usgx = usg.rename(columns={'Jika Pernah, dimana Anda menggunakan pembayaran melalui QR Code tersebut?': 'Mini Market', 'Unnamed: 416':'Cafe/Restoran','Unnamed: 417': 'Pedangang kaki lima','Unnamed: 418': 'Tempat hiburan','Unnamed: 419':'Pasar tradisional','Unnamed: 420': 'Supermarket/Mall','Unnamed: 421':'Lainnya'})
usgx.sum().plot(kind='barh', title='Penggunaan Layanan QR Code')


# In[269]:


cleaned2.iloc[0,421] = np.nan
lowercased18 = cleaned2['Unnamed: 421'].str.lower()
lc18 = pd.DataFrame(lowercased18)

sns.countplot(data=lc18.head(300), y='Unnamed: 421')


# In[272]:


cleaned2.iloc[0,422] = np.NaN #hilangkan judul
cleaned2['Frekuensi belanja online 6 bulan terakhir'] = cleaned2['Bagaimana frekuensi Anda melakukan belanja online dalam 6 bulan terakhir?'].map({1: 'Meningkat',2:'Menurun',3:'Tetap'})
sns.countplot(data=cleaned2, y='Frekuensi belanja online 6 bulan terakhir')


# In[423]:


onl = cleaned2[['Dalam 6 bulan terakhir, manakah dari kegiatan belanja online berikut yang mengalami peningkatan?', 'Unnamed: 426', 'Unnamed: 427', 'Unnamed: 428', 'Unnamed: 429', 'Unnamed: 430', 'Unnamed: 431', 'Unnamed: 432', 'Unnamed: 433', 'Unnamed: 434']].copy()
for i in range(0,10):
    onl.iloc[0,i]=np.NaN
for s in [9]:
    for j in range(0,1545):
        if type(onl.iloc[j,s]) == str:
                    onl.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
onlx = onl.rename(columns={'Dalam 6 bulan terakhir, manakah dari kegiatan belanja online berikut yang mengalami peningkatan?': 'Fashion/Mode', 'Unnamed: 426':'Groceries','Unnamed: 427': 'Makanan, minuman','Unnamed: 428': 'Buku, hobi, koleksi','Unnamed: 429':'Alat kecantikan, perawatan','Unnamed: 430': 'HP/Laptop/Komputer','Unnamed: 431':'Transportasi jarak jauh','Unnamed: 432':'Booking hotel','Unnamed: 433': 'Pulsa','Unnamed: 434':'Lainnya'})
onlx.sum().plot(kind='barh', title='Kegiatan yang meningkat secara online')


# In[424]:


print(onlx['Lainnya'].value_counts())
print(onlx['Pulsa'].value_counts())
print(onlx['Booking hotel'].value_counts())
print(onlx['Transportasi jarak jauh'].value_counts())
print(onlx['HP/Laptop/Komputer'].value_counts())
print(onlx['Alat kecantikan, perawatan'].value_counts())
print(onlx['Buku, hobi, koleksi'].value_counts())
print(onlx['Makanan, minuman'].value_counts())
print(onlx['Groceries'].value_counts())
print(onlx['Fashion/Mode'].value_counts())


# In[428]:


print ('n   |', 'min                | max')
print('Fashion/mode')
confidint(552)
print('Groceries')
confidint(364)
print('Makanan, minuman')
confidint(727)
print('buku, hobi, koleksi')
confidint(576)
print('alat kecantikan')
confidint(423)
print('HP/Laptop/Komputer')
confidint(199)
print('Transportasi jarak jauh')
confidint(173)
print('Booking hotel')
confidint(108)
print('Pulsa')
confidint(683)
print('Lainnya')
confidint(114)


# In[274]:


cleaned2.iloc[0,434] = np.nan
lowercased19 = cleaned2['Unnamed: 434'].str.lower()
lc19 = pd.DataFrame(lowercased19)

sns.countplot(data=lc19.head(250), y='Unnamed: 434')


# In[356]:


#5.3
#renaming 
kecenderungan = cleaned2.rename(columns={'Bagaimana kecenderungan Anda jika akan berbelanja hal-hal berikut?': 'Fashion / mode', 'Unnamed: 437':'Groceries','Unnamed: 439': 'Handphone','Unnamed: 441': 'Laptop/komputer','Unnamed: 443':'Elektronik rumah tangga','Unnamed: 445': 'Kosmetik','Unnamed: 447':'Buku, hobi, koleksi','Unnamed: 449':'Pulsa dan data', 'Unnamed: 451':'Makanan dan Minuman','Unnamed: 453': 'Tiket Pesawat','Unnamed: 455': 'Tiket kereta api','Unnamed: 457':'Hotel','Unnamed: 459': 'Tiket bioskop','Unnamed: 461':'Tiket wisata'})
#mapping

kecenderungan['Fashion / mode'] = kecenderungan['Fashion / mode'].map({1: 'Online',2:'Offline'})
kecenderungan['Groceries'] = kecenderungan['Groceries'].map({1: 'Online',2:'Offline'})
kecenderungan['Handphone'] = kecenderungan['Handphone'].map({1: 'Online',2:'Offline'})
kecenderungan['Laptop/komputer'] = kecenderungan['Laptop/komputer'].map({1: 'Online',2:'Offline'})
kecenderungan['Elektronik rumah tangga'] = kecenderungan['Elektronik rumah tangga'].map({1: 'Online',2:'Offline'})
kecenderungan['Kosmetik'] = kecenderungan['Kosmetik'].map({1: 'Online',2:'Offline'})
kecenderungan['Buku, hobi, koleksi'] = kecenderungan['Buku, hobi, koleksi'].map({1: 'Online',2:'Offline'})
kecenderungan['Pulsa dan data'] = kecenderungan['Pulsa dan data'].map({1: 'Online',2:'Offline'})
kecenderungan['Makanan dan Minuman'] = kecenderungan['Makanan dan Minuman'].map({1: 'Online',2:'Offline'})
kecenderungan['Tiket Pesawat'] = kecenderungan['Tiket Pesawat'].map({1: 'Online',2:'Offline'})
kecenderungan['Tiket kereta api'] = kecenderungan['Tiket kereta api'].map({1: 'Online',2:'Offline'})
kecenderungan['Hotel'] = kecenderungan['Hotel'].map({1: 'Online',2:'Offline'})
kecenderungan['Tiket bioskop'] = kecenderungan['Tiket bioskop'].map({1: 'Online',2:'Offline'})
kecenderungan['Tiket wisata'] = kecenderungan['Tiket wisata'].map({1: 'Online',2:'Offline'})

#konkatenasi
P = {}
Pref = pd.DataFrame(P)
Pref['Fashion/mode']=kecenderungan['Fashion / mode'].value_counts()
Pref['Groceries']=kecenderungan['Groceries'].value_counts()
Pref['Handphone']=kecenderungan['Handphone'].value_counts()
Pref['Laptop/komputer']=kecenderungan['Laptop/komputer'].value_counts()
Pref['Elektronik rumah tangga']=kecenderungan['Elektronik rumah tangga'].value_counts()
Pref['Kosmetik']=kecenderungan['Kosmetik'].value_counts()
Pref['Buku, hobi, koleksi']=kecenderungan['Buku, hobi, koleksi'].value_counts()
Pref['Pulsa dan data']=kecenderungan['Pulsa dan data'].value_counts()
Pref['Makanan dan Minuman']=kecenderungan['Makanan dan Minuman'].value_counts()
Pref['Tiket Pesawat']=kecenderungan['Tiket Pesawat'].value_counts()
Pref['Tiket kereta api']=kecenderungan['Tiket kereta api'].value_counts()
Pref['Hotel']=kecenderungan['Hotel'].value_counts()
Pref['Tiket bioskop']=kecenderungan['Tiket bioskop'].value_counts()
Pref['Tiket wisata']=kecenderungan['Tiket wisata'].value_counts()
figpref = Pref.plot(kind='bar', figsize=(10,8), alpha = 0.8, fontsize=10).get_figure()


# In[282]:


dmn = cleaned2[['Dimana Anda biasa berbelanja online? (jawaban boleh lebih dari 1)', 'Unnamed: 464', 'Unnamed: 465', 'Unnamed: 466', 'Unnamed: 467', 'Unnamed: 468', 'Unnamed: 469', 'Unnamed: 470']].copy()
for i in range(0,8):
    dmn.iloc[0,i]=np.NaN
for s in [7]:
    for j in range(0,1545):
        if type(dmn.iloc[j,s]) == str:
                    dmn.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
dmnx = dmn.rename(columns={'Dimana Anda biasa berbelanja online? (jawaban boleh lebih dari 1)': 'Marketplace (Lazada, Tokopedia, dll)', 'Unnamed: 464':'Jasa Layanan Delivery Online','Unnamed: 465': 'Website Toko Online','Unnamed: 466': 'Instagram','Unnamed: 467':'Line','Unnamed: 468': 'WhatsApp','Unnamed: 469':'Facebook','Unnamed: 470':'Lainnya'})
dmnx.sum().plot(kind='barh', title='Tempat berbelanja online')


# In[281]:


cleaned2.iloc[0,470] = np.nan
lowercased20 = cleaned2['Unnamed: 470'].str.lower()
lc20 = pd.DataFrame(lowercased20)

sns.countplot(data=lc20, y='Unnamed: 470')


# In[288]:


fav = cleaned2[['Mohon sebutkan 3 toko online favorit, dimana dalam 3 bulan terakhir anda melakukan belanja online?', 'Unnamed: 472', 'Unnamed: 473', 'Unnamed: 474', 'Unnamed: 475', 'Unnamed: 476', 'Unnamed: 477', 'Unnamed: 478', 'Unnamed: 479', 'Unnamed: 480', 'Unnamed: 481']].copy()
for i in range(0,11):
    fav.iloc[0,i]=np.NaN
for s in [10]:
    for j in range(0,1545):
        if type(fav.iloc[j,s]) == str:
                    fav.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
favx = fav.rename(columns={'Mohon sebutkan 3 toko online favorit, dimana dalam 3 bulan terakhir anda melakukan belanja online?': 'Tokopedia', 'Unnamed: 472':'Shopee','Unnamed: 473': 'Bukalapak','Unnamed: 474': 'Lazada','Unnamed: 475':'JD.id','Unnamed: 476': 'Blibli','Unnamed: 477':'Gojek','Unnamed: 478':'Grab','Unnamed: 479': 'Traveloka','Unnamed: 480':'Tiket.com','Unnamed: 481':'Lainnya'})
favx.sum().plot(kind='barh', title='Toko online favorit pengguna')


# In[421]:


print(favx['Tokopedia'].value_counts())
print(favx['Shopee'].value_counts())
print(favx['Bukalapak'].value_counts())
print(favx['Lazada'].value_counts())
print(favx['JD.id'].value_counts())
print(favx['Blibli'].value_counts())
print(favx['Gojek'].value_counts())
print(favx['Grab'].value_counts())
print(favx['Traveloka'].value_counts())
print(favx['Tiket.com'].value_counts())
print(favx['Lainnya'].value_counts())


# In[422]:


confidint(891)
confidint(1170)
confidint(178)
confidint(165)
confidint(51)
confidint(53)
confidint(1006)
confidint(731)
confidint(239)
confidint(83)
confidint(74)


# In[285]:


cleaned2.iloc[0,481] = np.nan
lowercased21 = cleaned2['Unnamed: 481'].str.lower()
lc21 = pd.DataFrame(lowercased21)

sns.countplot(data=lc21.head(600), y='Unnamed: 481')


# In[292]:


prf = cleaned2[['Apa saja yang menjadi alasan utama Anda lebih menyukai belanja secara online?', 'Unnamed: 483', 'Unnamed: 484', 'Unnamed: 485', 'Unnamed: 486', 'Unnamed: 487', 'Unnamed: 488']].copy()
for i in range(0,7):
    prf.iloc[0,i]=np.NaN
for s in [6]:
    for j in range(0,1545):
        if type(prf.iloc[j,s]) == str:
                    prf.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
prfx = prf.rename(columns={'Apa saja yang menjadi alasan utama Anda lebih menyukai belanja secara online?': 'Lebih Murah', 'Unnamed: 483':'Banyak promo','Unnamed: 484': 'Lebih banyak pilihan','Unnamed: 485': 'Belanja darimana dan kapan saja','Unnamed: 486':'Mudah dan Praktis','Unnamed: 487': 'Menghindari keramaian','Unnamed: 488':'Lainnya'})
prfx.sum().plot(kind='barh', title='Alasan preferensi belanja online')


# In[432]:


print(prfx['Lebih Murah'].value_counts())
print(prfx['Banyak promo'].value_counts())
print(prfx['Lebih banyak pilihan'].value_counts())
print(prfx['Belanja darimana dan kapan saja'].value_counts())
print(prfx['Mudah dan Praktis'].value_counts())
print(prfx['Menghindari keramaian'].value_counts())
print(prfx['Lainnya'].value_counts())


# In[433]:


print ('n   |', 'min                | max')
print('Lebih Murah')
confidint(811)
print('Banyak promo')
confidint(1133)
print('Lebih banyak pilihan')
confidint(815)
print('Belanja darimana dan kapan saja')
confidint(1039)
print('Mudah dan Praktis')
confidint(1165)
print('Menghindari keramaian')
confidint(913)
print('Lainnya')
confidint(24)


# In[290]:


cleaned2.iloc[0,488] = np.nan
lowercased22 = cleaned2['Unnamed: 488'].str.lower()
lc22 = pd.DataFrame(lowercased22)

sns.countplot(data=lc22.head(1000), y='Unnamed: 488')


# In[431]:


off = cleaned2[['Apa saja yang menjadi alasan Anda lebih menyukai belanja secara offline / langsung datang ke toko?', 'Unnamed: 490', 'Unnamed: 491', 'Unnamed: 492', 'Unnamed: 493', 'Unnamed: 494', 'Unnamed: 495', 'Unnamed: 496', 'Unnamed: 497']].copy()
for i in range(0,9):
    off.iloc[0,i]=np.NaN
for s in [8]:
    for j in range(0,1545):
        if type(off.iloc[j,s]) == str:
                    off.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
offx = off.rename(columns={'Apa saja yang menjadi alasan Anda lebih menyukai belanja secara offline / langsung datang ke toko?': 'Lebih Murah', 'Unnamed: 490':'Dapat memilih barang langsung','Unnamed: 491': 'Barang dapat langsung dibawa pulang','Unnamed: 492': 'Tidak ada biaya pengiriman','Unnamed: 493':'Dapat memastikan keaslian dan kualitas','Unnamed: 494': 'Lebih aman','Unnamed: 495':'Kurang familiar dengan app online','Unnamed: 496':'Sambil jalan-jaln','Unnamed: 497': 'Lainnya'})
offx.sum().plot(kind='barh', title='Alasan belanja offline')


# In[294]:


cleaned2.iloc[0,497] = np.nan
lowercased23 = cleaned2['Unnamed: 497'].str.lower()
lc23 = pd.DataFrame(lowercased23)

sns.countplot(data=lc23, y='Unnamed: 497')


# In[297]:


pay = cleaned2[['Bagaimana Anda biasanya melakukan pembayaran saat belanja online (jawaban boleh lebih dari satu)', 'Unnamed: 499', 'Unnamed: 500', 'Unnamed: 501', 'Unnamed: 502', 'Unnamed: 503', 'Unnamed: 504', 'Unnamed: 505', 'Unnamed: 506', 'Unnamed: 507']].copy()
for i in range(0,10):
    pay.iloc[0,i]=np.NaN
for s in [9]:
    for j in range(0,1545):
        if type(pay.iloc[j,s]) == str:
                    pay.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
payx = pay.rename(columns={'Bagaimana Anda biasanya melakukan pembayaran saat belanja online (jawaban boleh lebih dari satu)': 'Cash on Delivery', 'Unnamed: 499':'Transfer virtual account','Unnamed: 500': 'Transfer via iBanking/mBanking','Unnamed: 501': 'Transfer via ATM','Unnamed: 502':'eMoney/eWallet Marketplace','Unnamed: 503': 'Paylater','Unnamed: 504':'Debit/Kredit online','Unnamed: 505':'Minimarket','Unnamed: 506': 'Fintech credit loan','Unnamed: 507':'Lainnya'})
payx.sum().plot(kind='barh', title='Preferensi pembayaran belanja online')


# In[296]:


cleaned2.iloc[0,507] = np.nan
lowercased24 = cleaned2['Unnamed: 507'].str.lower()
lc24 = pd.DataFrame(lowercased24)

sns.countplot(data=lc24, y='Unnamed: 507')


# In[302]:


kol = cleaned2[['Sebutkan kendala/ keluhan yang pernah dialami saat belanja online!', 'Unnamed: 509', 'Unnamed: 510', 'Unnamed: 511', 'Unnamed: 512', 'Unnamed: 513', 'Unnamed: 514']].copy()
for i in range(0,7):
    kol.iloc[0,i]=np.NaN
for s in [6]:
    for j in range(0,1545):
        if type(kol.iloc[j,s]) == str:
                    kol.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
kolx = kol.rename(columns={'Sebutkan kendala/ keluhan yang pernah dialami saat belanja online!': 'Pembayaran berjalan saat barang tak tersedia', 'Unnamed: 509':'saldo eWallet berkurang tanpa transaksi','Unnamed: 510': 'Pembayaran dilakukan tapi tak terdeteksi','Unnamed: 511': 'Barang yang sampai tak sesuai pesanan','Unnamed: 512':'Jumlah barang diterima kurang','Unnamed: 513': 'Barang rusak/salah tapi tak dapat direturn','Unnamed: 514':'Lainnya'})
kolx.sum().plot(kind='barh', title='Kendala belanja online')


# In[301]:


cleaned2.iloc[0,514] = np.nan
lowercased25 = cleaned2['Unnamed: 514'].str.lower()
lc25 = pd.DataFrame(lowercased25)

sns.countplot(data=lc25.head(300), y='Unnamed: 514')


# In[303]:


cleaned2.iloc[0,396] = np.NaN #hilangkan judul
cleaned2['Frekuensi Belanja online di sosial media'] = cleaned2['Seberapa sering Anda berbelanja online melalui social media (baik melalui facebook, instagram, line, whatsapp, dll)?'].map({1: '>5 kali sebulan',2:'2-5 kali sebulan',3:'sekali sebulan',4:'Sekali Sebulan',5:'Sangat jarang',6:'Tidak pernah'})
sns.countplot(data=cleaned2, y='Frekuensi Belanja online di sosial media')


# In[360]:


cleaned2.iloc[0,396] = np.NaN #hilangkan judul
cleaned2.iloc[0,5] = np.NaN
cleaned2['Jenis kelamin ?'] = cleaned2['Jenis kelamin ?'].map({1: 'Laki-laki',2:'Perempuan'})
cleaned2['Frekuensi Belanja online di sosial media'] = cleaned2['Seberapa sering Anda berbelanja online melalui social media (baik melalui facebook, instagram, line, whatsapp, dll)?'].map({1: '>5 kali sebulan',2:'2-5 kali sebulan',3:'sekali sebulan',4:'Sekali Sebulan',5:'Sangat jarang',6:'Tidak pernah'})
sns.countplot(data=cleaned2, y='Frekuensi Belanja online di sosial media', hue='Jenis kelamin ?')


# In[310]:


smd = cleaned2[['Jika Anda pernah berbelanja melalui social media seperti instagram, facebook, line , maupun melalui web langsung, apa saja yang menjadi alasannya?', 'Unnamed: 521', 'Unnamed: 522', 'Unnamed: 523', 'Unnamed: 524', 'Unnamed: 525', 'Unnamed: 526', 'Unnamed: 527', 'Unnamed: 528', 'Unnamed: 529']].copy()
for i in range(0,10):
    smd.iloc[0,i]=np.NaN
for s in [9]:
    for j in range(0,1545):
        if type(smd.iloc[j,s]) == str:
                    smd.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
smdx = smd.rename(columns={'Jika Anda pernah berbelanja melalui social media seperti instagram, facebook, line , maupun melalui web langsung, apa saja yang menjadi alasannya?': 'Tidak pernah', 'Unnamed: 521':'barang lebih beragam','Unnamed: 522': 'Lebih murah','Unnamed: 523': 'Lebih mudah','Unnamed: 524':'Lebih banyak promo','Unnamed: 525': 'Bisa customize','Unnamed: 526':'Bisa COD','Unnamed: 527':'Kualitas barang terjamin','Unnamed: 528': 'Barang hanya dijual di social media','Unnamed: 529':'Lainnya'})
smdx.sum().plot(kind='barh', title='Alasan belanja di social media')


# In[429]:


print(smdx['Tidak pernah'].value_counts())
print(smdx['barang lebih beragam'].value_counts())
print(smdx['Lebih murah'].value_counts())
print(smdx['Lebih mudah'].value_counts())
print(smdx['Lebih banyak promo'].value_counts())
print(smdx['Bisa customize'].value_counts())
print(smdx['Bisa COD'].value_counts())
print(smdx['Kualitas barang terjamin'].value_counts())
print(smdx['Barang hanya dijual di social media'].value_counts())
print(smdx['Lainnya'].value_counts())


# In[430]:


print ('n   |', 'min                | max')
print('Tidak perna')
confidint(537)
print('barang lebih beragam')
confidint(289)
print('Lebih murah')
confidint(206)
print('Lebih mudah')
confidint(230)
print('Lebih banyak promo')
confidint(206)
print('Bisa customize')
confidint(191)
print('Bisa COD')
confidint(104)
print('Kualitas barang terjamin')
confidint(79)
print('Barang hanya dijual di social media')
confidint(429)
print('Lainnya')
confidint(55)


# In[305]:


cleaned2.iloc[0,529] = np.nan
lowercased26 = cleaned2['Unnamed: 529'].str.lower()
lc26 = pd.DataFrame(lowercased26)

sns.countplot(data=lc26.head(500), y='Unnamed: 529')


# In[314]:


cry = cleaned2[['Jika Anda pernah berbelanja melalui social media, apakah anda pernah mendapat pengalaman tidak menyenangkan? Jika Ya, mohon sebutkan. (Hanya dijawab bagi orang yang pernah berbelanja melalui social media)', 'Unnamed: 531', 'Unnamed: 532', 'Unnamed: 533', 'Unnamed: 534', 'Unnamed: 535', 'Unnamed: 536', 'Unnamed: 537', 'Unnamed: 538']].copy()
for i in range(0,9):
    cry.iloc[0,i]=np.NaN
for s in [8]:
    for j in range(0,1545):
        if type(cry.iloc[j,s]) == str:
                    cry.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
cryx = cry.rename(columns={'Jika Anda pernah berbelanja melalui social media, apakah anda pernah mendapat pengalaman tidak menyenangkan? Jika Ya, mohon sebutkan. (Hanya dijawab bagi orang yang pernah berbelanja melalui social media)': 'Tidak pernah', 'Unnamed: 531':'Penjual ternyata penipu','Unnamed: 532': 'Barang tak sesuai gambar','Unnamed: 533': 'Barang tak dikirim setelah transfer','Unnamed: 534':'Barang sold out','Unnamed: 535': 'Penjual susah dihubungi','Unnamed: 536':'Barang palsu','Unnamed: 537':'Pengiriman lama','Unnamed: 538':'Lainnya'})
cryx.sum().plot(kind='barh', title='Pengalaman tak menyenangkan social media')


# In[312]:


cleaned2.iloc[0,538] = np.nan
lowercased27 = cleaned2['Unnamed: 538'].str.lower()
lc27 = pd.DataFrame(lowercased27)

sns.countplot(data=lc27.head(700), y='Unnamed: 538')


# In[315]:


cleaned2.iloc[0,422] = np.NaN #hilangkan judul
cleaned2['Pengetahuan FinTech'] = cleaned2['Apakah Anda mengenal dan mengetahui istilah Fintech?'].map({1: 'Tahu',2:'Tidak Tahu'})
sns.countplot(data=cleaned2, y='Pengetahuan FinTech')


# In[317]:


fin = cleaned2[['Apakah Anda pernah menggunakan layanan fintech lending / yang biasa disebut pinjaman online berikut?Â (jawaban boleh lebih dari 1)', 'Unnamed: 543', 'Unnamed: 544', 'Unnamed: 545', 'Unnamed: 546', 'Unnamed: 547', 'Unnamed: 548', 'Unnamed: 549', 'Unnamed: 550', 'Unnamed: 551', 'Unnamed: 552','Unnamed: 553', 'Unnamed: 554', 'Unnamed: 555', 'Unnamed: 556', 'Unnamed: 557']].copy()
for i in range(0,16):
    fin.iloc[0,i]=np.NaN
for s in [15]:
    for j in range(0,1545):
        if type(fin.iloc[j,s]) == str:
                    fin.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
finx = fin.rename(columns={'Apakah Anda pernah menggunakan layanan fintech lending / yang biasa disebut pinjaman online berikut?Â (jawaban boleh lebih dari 1)': 'Tidak pernah', 'Unnamed: 543':'Danamas','Unnamed: 544': 'Koinworks','Unnamed: 545': 'Amartha','Unnamed: 546':'Investree','Unnamed: 547': 'Modalku','Unnamed: 548':'Danacepat','Unnamed: 549':'Akseleran','Unnamed: 550': 'Akulaku','Unnamed: 551':'cicil','Unnamed: 552':'Uangteman','Unnamed: 553':'Taralite','Unnamed: 554':'Kredivo','Unnamed: 555': 'AwanTunai','Unnamed: 556':'Crowdo','Unnamed: 557':'Lainnya'})
finx.sum().plot(kind='barh', title='FinTech yang pernah digunakan')


# In[320]:


cleaned2.iloc[0,557] = np.nan
lowercased28 = cleaned2['Unnamed: 557'].str.lower()
lc28 = pd.DataFrame(lowercased28)

sns.countplot(data=lc28.head(700), y='Unnamed: 557')


# In[326]:


knp = cleaned2[['Mengapa Anda lebih memilih mengajukan pinjaman melaluiÂ fintech lending?', 'Unnamed: 559', 'Unnamed: 560', 'Unnamed: 561', 'Unnamed: 562', 'Unnamed: 563']].copy()
for i in range(0,6):
    knp.iloc[0,i]=np.NaN
for s in [5]:
    for j in range(0,1545):
        if type(knp.iloc[j,s]) == str:
                    knp.iloc[j,s] = 1                                                                      
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
knpx = knp.rename(columns={'Mengapa Anda lebih memilih mengajukan pinjaman melaluiÂ fintech lending?': 'Persyaratan mudah', 'Unnamed: 559':'Proses pengajuan cepat','Unnamed: 560': 'Proses pencairan cepat','Unnamed: 561': 'Tidak memerlukan jaminan','Unnamed: 562':'Hanya perlu uang sedikit','Unnamed: 563': 'Lainnya'})
knpx.sum().plot(kind='barh', title='Alasan meminjam dari FinTech')


# In[324]:


cleaned2.iloc[0,563] = np.nan
lowercased29 = cleaned2['Unnamed: 563'].str.lower()
lc29 = pd.DataFrame(lowercased29)

sns.countplot(data=lc29.head(200), y='Unnamed: 563')


# In[330]:


wf = cleaned2[['Untuk tujuan apa Anda mengajukan pinjaman?', 'Unnamed: 565', 'Unnamed: 566', 'Unnamed: 567', 'Unnamed: 568', 'Unnamed: 569', 'Unnamed: 570', 'Unnamed: 571']].copy()
for i in range(0,8):
    wf.iloc[0,i]=np.NaN
for s in [7]:
    for j in range(0,1545):
        if type(wf.iloc[j,s]) == str:
                    wf.iloc[j,s] = 1                                                                      
                                                                                                                              
wfx = wf.rename(columns={'Untuk tujuan apa Anda mengajukan pinjaman?': 'Tidak pernah meminjam, hanya meminjamkan', 'Unnamed: 565':'Modal usaha','Unnamed: 566': 'Keperluan sehari-haru','Unnamed: 567': 'Belanja di marketplace','Unnamed: 568':'Pembiayaan pendidikan','Unnamed: 569': 'Pembelian kendaraan','Unnamed: 570':'Berlibur','Unnamed: 571':'Lainnya'})
wfx.sum().plot(kind='barh', title='Alokasi uang pinjaman dari FinTech')


# In[328]:


cleaned2.iloc[0,571] = np.nan
lowercased30 = cleaned2['Unnamed: 571'].str.lower()
lc30 = pd.DataFrame(lowercased30)

sns.countplot(data=lc30.head(150), y='Unnamed: 571')


# In[331]:


cleaned2.iloc[0,572] = np.NaN #hilangkan judul
cleaned2['Nominal Pinjaman di FinTech'] = cleaned2['Berapa biasanya nominal Anda meminjam di digital lending?'].map({1: '<Rp1.000.000',2:'Rp1.000.000-Rp5.000.000',3:'Rp5.000.001-Rp10.000.000',4:'Rp10.000.000'})
sns.countplot(data=cleaned2, y='Nominal Pinjaman di FinTech')


# In[332]:


cleaned2.iloc[0,576] = np.NaN #hilangkan judul
cleaned2['Lama Proses Pengajuan hingga Cair'] = cleaned2['Berapa lama proses pengajuan pinjaman berlangsung hingga dana cair?'].map({1: '<1 jam',2:'1-3 jam',3:'3 jam - 1 hari',4:'1-3 hari',5: '>3 hari'})
sns.countplot(data=cleaned2, y='Lama Proses Pengajuan hingga Cair')


# In[333]:


cleaned2.iloc[0,581] = np.NaN #hilangkan judul
cleaned2['Lama waktu pinjaman'] = cleaned2['Berapa jangka waktu/tenor pinjaman yang Anda ajukan?'].map({1: '<15 hari',2:'16 hari - 1 bulan',3:'1 - 3 bulan',4:'3 - 6 bulan',5: '6 bulan - 1 tahun', 6: '>1 tahun'})
sns.countplot(data=cleaned2, y='Lama waktu pinjaman')


# In[336]:


vrf = cleaned2[['Apakah terdapat proses verifikasi/ peninjauan untuk pinjaman yang Anda ajukan?', 'Unnamed: 588']].copy()
for i in range(0,2):
    vrf.iloc[0,i]=np.NaN
for s in [1]:
    for j in range(0,1545):
        if type(vrf.iloc[j,s]) == str:
                    vrf.iloc[j,s] = 1
for x in [0]:
    for y in range(0,1545):
        if type(vrf.iloc[y,x]) != int:
                    vrf.iloc[y,x] = np.NaN
                                                                                                                              #Tidak memiliki rekening di bank online	kemudahan transaksi	kemudahan pembukaan rekening	promo	karena sedang tren	Lainnya, sebutkan
vrfx = vrf.rename(columns={'Apakah terdapat proses verifikasi/ peninjauan untuk pinjaman yang Anda ajukan?': 'Tidak, hanya foto KTP dan KK', 'Unnamed: 588':'Ya, ada proses verifikasi'})
vrfx.sum().plot(kind='barh', title='Adakah proses verifikasi saat melakukan pinjaman')


# In[335]:


cleaned2.iloc[0,588] = np.nan
lowercased31 = cleaned2['Unnamed: 588'].str.lower()
lc31 = pd.DataFrame(lowercased31)

sns.countplot(data=lc31.head(300), y='Unnamed: 588')


# In[342]:


msl = cleaned2[['Apakah Anda pernah mengalami masalah selama mengajukan pinjaman melalui jasaÂ fintechÂ lending? Jika pernah, mohon sebutkan!', 'Unnamed: 590', 'Unnamed: 591', 'Unnamed: 592', 'Unnamed: 593', 'Unnamed: 594']].copy()
for i in range(0,6):
    msl.iloc[0,i]=np.NaN
for s in [5]:
    for j in range(0,1545):
        if type(msl.iloc[j,s]) == str:
                    msl.iloc[j,s] = 1                                                                      
                                                                                                                              
mslx = msl.rename(columns={'Apakah Anda pernah mengalami masalah selama mengajukan pinjaman melalui jasaÂ fintechÂ lending? Jika pernah, mohon sebutkan!': 'Tidak pernah mengalami masalah', 'Unnamed: 590':'Aplikasi/web sulit diakses','Unnamed: 591': 'Bunga tinggi','Unnamed: 592': 'Penagihan dilakukan sepihak','Unnamed: 593':'Teror oleh debt collector','Unnamed: 594': 'Lainnya'})
mslx.sum().plot(kind='barh', title='Masalah pinjaman dari FinTech')


# In[341]:


cleaned2.iloc[0,594] = np.nan
lowercased32 = cleaned2['Unnamed: 594'].str.lower()
lc32 = pd.DataFrame(lowercased32)

sns.countplot(data=lc32.tail(250), y='Unnamed: 594')


# In[344]:


lyn = cleaned2[['Apakah Anda menggunakan fintech market provisioning berikut untuk membandingkan beberapa layanan?', 'Unnamed: 596', 'Unnamed: 597', 'Unnamed: 598', 'Unnamed: 599', 'Unnamed: 600']].copy()
for i in range(0,6):
    lyn.iloc[0,i]=np.NaN
for s in [5]:
    for j in range(0,1545):
        if type(lyn.iloc[j,s]) == str:
                    lyn.iloc[j,s] = 1                                                                      
                                                                                                                              
lynx = lyn.rename(columns={'Apakah Anda menggunakan fintech market provisioning berikut untuk membandingkan beberapa layanan?': 'Tidak pernah menggunakan', 'Unnamed: 596':'Cekaja','Unnamed: 597': 'Cermati','Unnamed: 598': 'HaloMoney','Unnamed: 599':'KreditGogo','Unnamed: 600': 'Lainnya'})
lynx.sum().plot(kind='barh', title='Penggunaan FinTech Market provisioning')


# In[346]:


cleaned2.iloc[0,600] = np.nan
lowercased33 = cleaned2['Unnamed: 600'].str.lower()
lc33 = pd.DataFrame(lowercased33)

sns.countplot(data=lc33, y='Unnamed: 600')


# In[347]:


inv = cleaned2[['Apakah Anda pernah mengï»¿gunakan fintech untuk investasi berikut?', 'Unnamed: 602', 'Unnamed: 603', 'Unnamed: 604', 'Unnamed: 605']].copy()
for i in range(0,5):
    inv.iloc[0,i]=np.NaN
for s in [4]:
    for j in range(0,1545):
        if type(inv.iloc[j,s]) == str:
                    inv.iloc[j,s] = 1                                                                      
                                                                                                                              
invx = inv.rename(columns={'Apakah Anda pernah mengï»¿gunakan fintech untuk investasi berikut?': 'Tidak pernah menggunakan', 'Unnamed: 602':'Bareksa','Unnamed: 603': 'Bibitnomic','Unnamed: 604': 'LiveOlive','Unnamed: 605':'Lainnya'})
invx.sum().plot(kind='barh', title='Penggunaan FinTech untuk Investasi')


# In[349]:


cleaned2.iloc[0,605] = np.nan
lowercased34 = cleaned2['Unnamed: 605'].str.lower()
lc34 = pd.DataFrame(lowercased34)

sns.countplot(data=lc34.head(700), y='Unnamed: 605')


# In[351]:


cleaned2.iloc[0,606] = np.NaN #hilangkan judul
cleaned2['Pengetahuan tentang regulasi OJK / BI mengenai fintech'] = cleaned2['Apakah Anda mengetahui terdapat regulasi OJK/ BI yang mengatur mengenai keberadaan fintech?'].map({1: 'Ya, Tahu',2:'Tidak tahu'})
sns.countplot(data=cleaned2, y='Pengetahuan tentang regulasi OJK / BI mengenai fintech')


# In[352]:


cleaned2.iloc[0,608] = np.NaN #hilangkan judul
cleaned2['Pentingkah status fintech terdaftar OJK / BI'] = cleaned2['Apakah status fintech yang terdaftar dan diawasi oleh OJK/BI menjadi salah satu pertimbangan penting bagi Anda untuk menggunakan layanan Fintech tersebut?'].map({1: 'Ya',2:'Tidak'})
sns.countplot(data=cleaned2, y='Pentingkah status fintech terdaftar OJK / BI')


# In[394]:


import math
def confidint(X):
    z = 1.96
    al = 1545
    p = X/al
    q = 1-p
    ci1 = z*(math.sqrt(p*q/30))
    print('30:',(p-ci1),'   ',(p+ci1))
    ci2 = z*(math.sqrt(p*q/100))
    print('100:',(p-ci2),'   ',(p+ci2))
    ci3 = z*(math.sqrt(p*q/al))
    print('1545:',(p-ci3),'   ',(p+ci3))
    


# In[395]:


#CI Jenis kelamin
cleaned2['Jenis kelamin ?'].value_counts()


# In[396]:


confidint(799)

confidint(739)


# In[ ]:




