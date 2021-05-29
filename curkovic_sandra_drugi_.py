import random
pokusaj=3


def igra(korisnik, racunalo,pokusaj):
    i=0
    
    if(korisnik==racunalo): #ako je unos i racunala i korisnika isti
        print("Nitko nije pobjednik") #ispisi nitko nije dobio
        
    
    for x in lista: #provjera liste
        if(i==korisnik-1): #pocetni i=0 i ukoliko je i=0 i broj koji je korisnik unio(npr.1(-1))
            unosrijecimakorisnik=x #rijec se pridodljelje sto je racunalo unijelo 
            print("Korisnik je zapravo unio: " +unosrijecimakorisnik) #na koju rijec se odnosi broj koji je korisnik unio
        i=i+1

    i=0
    for x in lista:
        if(i==racunalo-1): #ako se podudara index  u listi i broj koji je izabralo racunalo, tu rijec koju predstavlja index je racunalo izabralo 
            unosrijecimaracunalo=x
            print("Racunalo je zapravo odabralo: " +unosrijecimaracunalo) 
        i=i+1
    
    for x in pravila:
        if (unosrijecimakorisnik in x and unosrijecimaracunalo in x): #ako su obe izabrane rijeci u podlisti liste
            listanova=x #izvdoji tu listu i spremi je u drugu
    
    j=0
    if((listanova[j]==unosrijecimakorisnik) and (korisnik!=racunalo)): #ako je prva rijec u novoj listi ==unos korisnika
            print("Korisnik je izgubio, a računalo pobjedilo") #korisnik je izgubio jer je lista  napravljena tako da rijec koja ima manji index je rijec koja gubi u igri protiv druge rijeci
            
    elif(korisnik!=racunalo):
         print("Korisnik je pobjedio, a računalo izgubilo")
        

    if(pokusaj==0):
        print("Gotova igra")       



pravila=[ ["škare", "kamen"], ["papir", "škare"], ["kamen", "papir"]] #pravila igre (skare=0, kamen=1, kamen je jaci)
lista=["kamen", "papir", "škare"] #prva da se zna na sto se odnosi uneseni broj
listanova=[]


while(pokusaj<=3 and pokusaj>0):
    korisnik=int(input("Unesi 1 za kamen,2 papir, 3 škare: ")) #unos korisnika
    #print("Unijeli ste: " +str(korisnik)) #sto je korisnik unio
    racunalo=random.randint(1,3) #random broj 1-3
    pokusaj=pokusaj-1
    print("Racunalo je unijelo: " +str(racunalo)) #sto je racunalo unijelo
    igra(korisnik,racunalo,pokusaj)




   
    
                
           
         
        
            

        
        
        
    
            
            
           
               




    

    

    
        





    
    
        






