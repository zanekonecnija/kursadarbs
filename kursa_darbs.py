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
uzdevumi = ["Kā saīsināti apzīmē molmasas mērvienību?", "Nosaki grafīta molmasas skaitlisko vērtību!", "Cik protonu ir ķīmiskajam elementam sēram?", "Kurš ķīmiskais elements dabā ir sastopams vienkāršas vielas veidā?(cl, ca, c, mg)", "Vai dotajā vienādojumā ir nepieciešami koeficienti? (Na + S → Na2S) (jā/Nē)", "Kāds ir nosaukums dotajai skābei(H2SO3)?", "Kādu indikatoru visbiežāk izmanto neitralizācijas reakcijās?", "Anjons ir pozitīvi vai negatīvi lādēts jons?", "Kāda ķīmiskā formula ir tvana gāzei?", "Kādā laboratorijas traukā pagatavo sērskābes šķīdumu no ūdens un koncentrētas sērskābes?"]
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
