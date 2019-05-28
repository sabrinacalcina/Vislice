import bottle
import model

vislice = model.Vislice('stanje.json')
#id = vislice.nova_igra()
#igra, stanje = vislice.igre[id]

@bottle.get('/')
def index():
    return bottle.template('index.tpl')


#dodajmo dekorator @bootle...
@bottle.get('/img/<ime>')
def slike(ime):
    return bottle.static_file(ime, root='img')

#@bottle.post('/igra/')
#def nova_igra():
#    id = vislice.nova_igra()
#    return bottle.redirect('/igra/{0}/'.format(id))
#
#
#@bottle.get('/igra/<id_igre:int>/')
#def pokazi_igro(id_igre):
#    igra, stanje = vislice.igre[id_igre]
#    return bottle.template('igra.html', id_igre=id_igre, igra=igra, poskus=stanje)
#
#@bottle.post('/igra/<id_igre:int>/')
#def ugibaj(id_igre):
#    crka = bottle.request.forms.getunicode('crka')
#    vislice.ugibaj(id_igre, crka)
#    bottle.redirect('/igra/{0}/'.format(id_igre))




@bottle.post('/nova_igra/')
def nova_igra_2():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', str(id_igre), path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro_2():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.html', id_igre=id_igre, igra=igra, poskus=stanje)
    
@bottle.post('/igra/')
def ugibaj_2():
    id_igre = int(bottle.request.get_cookie('id_igre'))
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')



bottle.run(reloader=True, debug=True)