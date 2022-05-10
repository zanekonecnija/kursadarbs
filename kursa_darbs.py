import random
import time 
import math
f = open("rezultats.txt", "a", encoding="UTF-8") # datne... kur 'append' elementi 
z = open("noteikumi.txt", "r", encoding="UTF-8")
noteikumi = []#tukšs lists, kurā var saglabāt noteikumus
arr = []#vienkārši tukšs lists
punkti =0#sākuma panktu skaits (0)
uzdevumi = ["Kā saīsināti apzīmē molmasas mērvienību?(g/mol ; g/kmolu ;)", "Nosaki grafīta molmasas skaitlisko vērtību!", "Cik protonu ir ķīmiskajam elementam sēram?", "Kurš ķīmiskais elements dabā ir sastopams vienkāršas vielas veidā?(cl, ca, c, mg)", "Vai dotajā vienādojumā ir nepieciešami koeficienti? (Na + S → Na2S) (jā/Nē)", "Kāds ir nosaukums dotajai skābei(H2SO3)?", "Kādu indikatoru visbiežāk izmanto neitralizācijas reakcijās?", "Anjons ir pozitīvi vai negatīvi lādēts jons?", "Kāda ķīmiskā formula ir tvana gāzei?", "Kādā laboratorijas traukā pagatavo sērskābes šķīdumu no ūdens un koncentrētas sērskābes?", "Kādā krāsā nokrāsosies universālindikators, ja to iemērks šķīdumā ar bāzisku vidi?", "Kāda ir glikozes ķīmiskā formula", "Kāda ir karbonskābju funkcionālā grupa?", "Fosfors veido vairākas vienkāršas vielas: balto, sarkano un violeto fosforu. Kā sauc šo parādību?", "Kā sauc esteru veidošanās reakcija no spirtiem un skābēm?"]
par_atbildes = ["g/kmol", "12", "16", "c", "jā", "sērpaskābe", "fenolftaleīns", "negatīvi", "co", "vārglāze", "zils", "C6H12O6", "COOH", "alotropija", "esterificēšanās"]
atbilzu_lapas_jaut = uzdevumi.copy() # nokopē list elementus vēl vienā lista (pārkopē)

def noteikumu_nolasisana():#tiek definēta noteikumu nolasīšanas funkcija
    global noteikumi#noteikumi tiek definēts kā "globālais mainīgais"
    for rinda in z:#tiek izpildīts cikls
        noteikumi.append(rinda) # no datnes nolasa spēles noteikumus un pievieno list

def noteikumu_izvade(noteikumi):#tiek definēta noteikumu izvades funkcija
    for i in range (len(noteikumi)):#cikls tiek izpildīts tik reizes, cik listā ir elementu
        print(noteikumi[i], end="") # izvada spēles noteikumus
    print()#tiek izvadīta atstarpe

def reizess():#tiek definēta "reizes" funkcija
    global reizes#reizes tiek definēts kā ""globālais mainīgais
    while True:
        try:
            reizes = int(input("Cik uzdevumus vēlieties saņemt: ")) #asks for an integer input from user (paņēmu no interneta)
        except ValueError: 
            print("Nepareizi dati!") #print statement
            continue
        if 1 > reizes or 10 < reizes:
            print("Ievadījāt pārāk lielu/mazu skaitli!")
            continue#cikls tiek turpināts, kad tiek ievadīti nepareizi dati
        else:
            break#cikls tiek pārtraukts, kad tiek ievadīti pareizi dati

noteikumu_nolasisana() # izsauc noteikumu_nolasisana funkciju
noteikumu_izvade(noteikumi) # izsauc noteikumu izvades funkciju
reizess() # izsauc reizess funkciju
start = time.time() # uzņem laiku 

for k in range (reizes):#viss cikls izpildās tik reizes, cik izvēlējāties jautājumus
    x = random.randrange(0,(len(uzdevumi))) # nosaka random intervālu kādā izvēlēsies vārdu
    jautajums = uzdevumi[x] # str tipa mainīgais 
    uzdevumi.pop(x) # izņem jautājumu, lai tas vairāk neatkārtotos
    atbilde = str(input(jautajums))#tiek pajautāts jautājums lietotājam

    for i in range (1): # jāizpildās vienu rezi
        z  = [] # izveido sarakstu 
        for j in range(1): # jāizpildās vienu reizi
            s = (jautajums, " - jūsu atbilde - ", atbilde) # mainīgajā saglabā
            z.append(s) # tai rindai pievieno vārdu 
        arr.append(z) # basically 2D list darbības 
        
    if atbilde == par_atbildes[x]:#ja ievadīta atbilde = pareizo atbildi
        punkti = punkti+1 # pieskaita punktiem +1 

stop = time.time() # tiek apturēts laiks    
print()#izvada tukšu rindu
print("Jūsu atbildes:")
for i in range (reizes):#tiek izpildīts tik reizes, cik izvēlējāties uzdevumus
    for j in range(1):#izpilda 1 reizi
        print(f"{i+1}.jautājums: {arr[i][j]}") # izvada reultātus 2D list veidā

print()
print("Atbilžu lapa:")
for i in range (len(atbilzu_lapas_jaut)):#cikls tiek izpildīts tik reizes, cik ir atbilžu lapas elementu
    print(f"{atbilzu_lapas_jaut[i]} pareizā atbilde - {par_atbildes[i]}")#tiek izvadīts atbildžu lapas jautājums un atbilde

print()
print(f"Jūs ieguvāt {punkti} no {reizes} punktiem")
f.write("Spēle ir beigusies\n")#šo tekstu izvada failā rezultats.txt
f.write(f"Jūs ieguvāt {punkti} no {reizes} punktiem\n") # izvada rezultātus datnē, kur ir f.write
print(f"Spēli paveicāt {round(stop-start, 2)} sekundēs") # izvada cik sekundes ir pagājušas
f.write(f"Spēli paveicāt {round(stop-start, 2)} sekundēs\n")#izvada tik sekundes, cik pildīji testu, arī failā rezultati.txt
print(f"Jūsu iegūto punktu skaita {punkti} faktoriāls ir {math.factorial(punkti)} ") # lai būtu izmantota math funkcijas
f.write("Paldies!\n")#izvada failā rezultats.txt
print("Paldies!")#vienkārši izvadās uz ekrāna