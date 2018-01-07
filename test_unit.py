

########### Test sur le Joueur et les Get ##########


def test_get_pioche(joueur):
	pioche = [4,5,6,7, 'bonjour']
	joueur['pioche']= pioche
	return pioche == get_pioche(joueur)

def test_get_cdb(joueur):
	cdb = [4,5,6,7, 'bonjour', ]
	joueur['cdb']= cdb
	return cdb == get_cdb(joueur)

def test_get_reserve(joueur):
	reserve = [4,5,6,7, 'bonjour', ]
	joueur['reserve']= reserve
	return reserve == get_reserve(joueur)

def test_get_royaume(joueur):
	royaume = [4,5,6,7, 'bonjour', ]
	joueur['royaume']= royaume
	return royaume == get_royaume(joueur)

def test_get_royaume(joueur):
	cimetiere = [4,5,6,7, 'bonjour', ]
	joueur['cimetiere']= cimetiere
	return cimetiere == get_cimetiere(joueur)

def test_get_main(joueur):
	main = [4,5,6,7, 'bonjour', ]
	joueur['main']= main
	return main == get_main(joueur)

def test_get_idet(joueur):
	joueur['ident']= 1
	return  get_indent(joueur) == 1

###########Tes cdb ###############

def test_placer_dans_cdb():
	cdb = creer_cdb()
	carte = creer_carte(1, "Garde", "def")
	pos = 2
	placer_dans_cdb(carte, cdb, pos)
	if !( !position_vide(pos,cdb) and est_dans_cdb(carte,cdb)):
		print("erreur placer_dans_cdb : carte non reconnu comme placée")
		return False
	return True
def test_est_dans_cdb():
	cdb = creer_cdb()
	indent = [1,2,3,4,5, 6]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
		if !est_dans_cdb(carte, cdb):
			print("erreur est_dans_cdb : les cartes ajoutées dans cdb ne sont pas détectées par est_dans_cdb")
			return False
	return True


def test_position_vide():
	cdb = creer_cdb()
	positions = [1,2,3,4,5, 6]
	for pos in positions :
		carte= pos
		if !position_vide(pos, cdb):
			print("erreur test_position_vide : position non vide alors que normalement si")
			return False
		placer_dans_cdb(carte, cdb, pos)
		if position_vide(pos, cdb):
			print("erreur test_position_vide : position vide alors qu'on a rajouter un élément'")
			return False
	return True
def test_retirer_du_cdb():
	cdb = creer_cdb()
	indent = [1,2,3,4,5, 6]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
	positions = indent
	for pos in positions :
		carte = pos
		retirer_du_cdb(pos,cdb)
		if est_dans_cdb(carte, cdb):
				print("erreur retirer_du_cdb : les cartes retirees du cdb  sont toujours détectées par est_dans_cdb")
				return False
	return True
def test_is_front():
	cdb = creer_cdb()
	indent = [1,2,3,4,6]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
	return (is_front(1) and !is_front(2))

def test_get_position_utilisables():
	cdb = creer_cdb()
	carte = creer_carte(1, "Garde", "def")
	pos = 2
	placer_dans_cdb(carte, cdb, pos)
	positions = [1,3,4,5, 6]
	if get_positions_utilisables(cdb) == positions:
		return True
	return False

def test_est_position_utilisables():
	cdb = creer_cdb()
	carte = creer_carte(1, "Garde", "def")
	pos = 2
	placer_dans_cdb(carte, cdb, pos)
	
	if !est_position_utilisables(cdb,2) and est_position_utilisables(cdb,3):
		return True
	return False

def test_mettre_en_position_def():
	cdb = creer_cdb()
	carte = creer_carte(1, "Garde", "def")
	pos = 2
	placer_dans_cdb(carte, cdb, pos)
	mettre_en_position_def(cdb)
	return est_en_posture_defensive(carte)


def test_get_nombre_carte_cdb(cdb):
	cdb = creer_cdb()
	indent = [1,2,3,4,5,6]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
		if get_nombre_carte_cdb(cdb) != i :
			return False
	return True

def test_reste_carte_en_position_defensive()
	cdb = creer_cdb()
	indent = [1,2,3,4,5,6]
	for i in indent :
		carte = creer_carte(i, "Garde", "def")
		pos = i
		placer_dans_cdb(carte, cdb, pos)
		mettre_en_offensif(carte)
		if reste_carte_en_position_defensive():
			return False
	mettre_en_defensive(carte)
	return reste_carte_en_position_defensive()


################## Pioche ######################

def test_creerPioche():
	DeckGen= creerDeck()
    p=creer_pioche(1,DeckGen)
    return pioche_vide(p) == False


def test_melangerPioche():
    P= creer_pioche()
    T=P
    melanger_pioche(P)
    return T!=P


def test_piochercarte():
    DeckGen= creerDeck()
    pioche=creer_pioche(1,DeckGen)
    PiocheDebut = pioche
    carte=piocher_carte(pioche)

    return (PiocheDebut != pioche) and (get_type(carte) != null )


##################### Reserve ############

def test_PlacerdansReserve():
    res= creer_reserve()
    carte = creer_carte(1, "Garde", "def")
    placer_dans_reserve(carte,res)
    return est_dans_reserve( carte,res)

def test_EstDansreserve():
    res=creer_reserve()
    carte = creer_carte(1, "Garde", "def")
    placer_dans_reserve(carte)
    if not est_dans_reserve(carte,res):
        return False
    retirer_de_reserve(carte,res)
    return not est_dans_reserve(carte,res)

def test_get_nombre_carte_reserve():
    res=creer_reserve()
    i=1
    carte = creer_carte(1, "Garde", "def")
    while i<10 :
        placer_dans_reserve(carte,res)
        if i!= get_nombre_carte_reserve(res):
            return False
        i+=1
        return True


############### Cimetière ################

def test_PlacerdansCimetiere():
    cim = creer_cimetiere()
    carte = creer_carte(1, "Garde", "def")
    placer_dans_cimetiere(carte, cim)
    return est_dans_cimetiere(carte, cim)



