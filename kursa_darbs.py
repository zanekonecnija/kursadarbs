print()
import random
import time 
MAPE = 'Faili/' # mape kurā saglabās rezultātus
f = open("rezultats.txt", "a", encoding="UTF-8") # datne... kur 'append' elementi 
z = open("noteikumi.txt", "r", encoding="UTF-8")
noteikumi = []
arr = []
arr_2 = []
punkti =0
uzdevumi = ["Kā saīsināti apzīmē molmasas mērvienību?(g/mol ; g/kmolu ;)", "Nosaki grafīta molmasas skaitlisko vērtību!", "Cik protonu ir ķīmiskajam elementam sēram?", "Kurš ķīmiskais elements dabā ir sastopams vienkāršas vielas veidā?(cl, ca, c, mg)", "Vai dotajā vienādojumā ir nepieciešami koeficienti? (Na + S → Na2S) (jā/Nē)", "Kāds ir nosaukums dotajai skābei(H2SO3)?", "Kādu indikatoru visbiežāk izmanto neitralizācijas reakcijās?", "Anjons ir pozitīvi vai negatīvi lādēts jons?", "Kāda ķīmiskā formula ir tvana gāzei?", "Kādā laboratorijas traukā pagatavo sērskābes šķīdumu no ūdens un koncentrētas sērskābes?"]
par_atbildes = ["g/kmol", "12", "16", "c", "jā", "sērpaskābe", "fenolftaleīns", "negatīvi", "co", "vārglāze"]

for rinda in z:
    noteikumi.append(rinda) # no datnes nolasa spēles noteikumus un pievieno list

for i in range (len(noteikumi)):
    print(noteikumi[i], end="") # izvada spēles noteikumus
print()

print("Ja vēlaties beigt spēli tad ierakstiet (beigt) ")

while True:
    try:
       reizes = int(input("Cik uzdevumus vēlieties saņemt: ")) #asks for an integer input from user
    except ValueError: 
       print("Nepareizi dati!") #print statement
       continue
    else:
        break

start = time.time() # uzņem laiku 

for k in range (reizes):
    x = random.randrange(0,(len(uzdevumi))) # nosaka random intervālu kādā izvēlēsies vārdu
    jautajums = uzdevumi[x]
    atbilde = str(input(jautajums))

    for i in range (1): # jāizpildās vienu rezi
        z  = [] # izveido sarakstu 
        for j in range(1): # jāizpildās vienu reizi
            s = (jautajums, " - jūsu atbilde - ", atbilde)
            z.append(s) # tai rindai pievieno vārdu 
        arr.append(z) # basically 2D list darbības 
    
    for i in range (1): # jāizpildās vienu rezi
        z  = [] # izveido sarakstu 
        for j in range(1): # jāizpildās vienu reizi
            s = (jautajums, " - pareizā atbilde - ", par_atbildes[x])
            z.append(s) # tai rindai pievieno vārdu 
        arr_2.append(z) # basically 2D list darbības 
        
    if atbilde == par_atbildes[x]:
        punkti = punkti+1

stop = time.time() # tiek apturēts laiks    
print()
print("Jūsu atbildes:")
for i in range (reizes):
    for j in range(1):
        print(f"{i+1}.jautājums: {arr[i][j]}") # izvada reultātus 2D list veidā

print()
print("Pareizās atbildes:")
for i in range (reizes):
    for j in range(1):
        print(f"{i+1}.jautājums: {arr_2[i][j]}") # izvada reultātus 2D list veidā


print(f"Jūs ieguvāt {punkti} no {reizes} punktiem")
print("Paldies!")
f.write("Spēle ir beigusies\n")
f.write(f"Jūs ieguvāt {punkti} no {reizes} punktiem\n") # izvada rezultātus datnē, kur ir f.write
print(f"Spēli paveicāt {round(stop-start, 2)} sekundēs") # izvada cik sekundes ir pagājušas
f.write(f"Spēli paveicāt {round(stop-start, 2)} sekundēs\n")
f.write("Paldies!\n")