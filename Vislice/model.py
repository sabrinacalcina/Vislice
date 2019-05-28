import random, json

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        self.crke = crke if crke is not None else []

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        izpis = ''
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                izpis += crka
            else:
                izpis += '_'
        return izpis


    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        velika_crka = crka.upper()
        if velika_crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(velika_crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                PORAZ
            else:
                if velika_crka in self.pravilne_crke():
                    return PRAVILNA_CRKA
                elif velika_crka in self.napacne_crke():
                    return NAPACNA_CRKA
            

bazen_besed = []
with open('besede.txt', 'r', encoding='utf-8') as f:
    for vrstica in f:
        bazen_besed.append(vrstica.strip())


def nova_igra():
    import random   
    izbrana_beseda = random.choice(bazen_besed)
    return Igra(izbrana_beseda)



class Vislice:
    def __init__(self, datoteka_s_stanjem):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.nalozi_igre_iz_datoteke()

    def prost_id_igre(self):
        return len(self.igre)

    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra, stanje = self.igre[id_igre]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)
        self.zapisi_igre_v_datoteko()

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as f:
            igre = json.load(f)
            self.igre = {}
            for id_igre, vrednosti in igre.items():
                self.igre[id_igre] = (Igra(vrednosti['geslo'], crke=vrednosti['crke']) , vrednosti['poskus'])

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w') as f:
            igre = {}
            for id_igre, (igra, poskus) in self.igre.items():
                igre[id_igre] = {'geso': igra.geslo, 'crke': igra.crke, 'poskus': poskus}
            json.dump(igre, f)
            









    




        


