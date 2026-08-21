# -*- coding: utf-8 -*-
import io
C='cursiva'; Q='comillas'; R='redonda'; S='simples'; X='nunca'
# (cosa, destino, ejemplo, nota, derivado)
G=[]
G.append(("Libros y textos",[
("Libro, obra completa",C,"<i>Cien años de soledad</i>","",0),
("Capítulo de un libro",Q,"«El rayo de luna», de las <i>Leyendas</i>","Obligatorias si se cita junto a la obra que lo contiene.",0),
("Artículo en obra colectiva",Q,"«El léxico de hoy», en <i>El lenguaje en los medios de comunicación</i>","",0),
("Poema dentro de un libro",Q,"«Oda al rey de Harlem», de <i>Poeta en Nueva York</i>","Citado solo, sin la obra madre, puedes elegir comillas o cursiva.",0),
("Mención abreviada de un título",C,"el <i>Buscón</i> · el <i>Estebanillo</i>","La cursiva no alcanza al artículo. Se mantiene al referirse a ediciones concretas: <i>el Buscón de 1626</i>.",0),
("Título dentro de otro título",Q,"<i>Nueva interpretación de «Yerma»</i>","Comillas dentro de la cursiva.",0),
("Colección editorial",R,"un manual de Alianza Universidad","La mayúscula ya delimita la extensión: la cursiva sobra.",0),
("Libro sagrado y sus partes",R,"la Biblia · el Corán · el Génesis · la Torá","Tampoco se marca una edición concreta: <i>la Biblia de Ferrara</i> va en redonda.",0),
("Texto legal o normativo",R,"el Código Civil · el Tratado de Maastricht","Solo si el título es larguísimo se limita la mayúscula al primer elemento y entonces sí va cursiva.",0),
("Tesis, informe, monografía",C,"<i>Gramática descriptiva de la lengua española</i>","",0),
]))
G.append(("Prensa",[
("Periódico o revista",C,"<i>El País</i> · <i>Diario Médico</i> · <i>Nuevo Estilo</i>","Con mayúscula en todas las palabras significativas, y con independencia de cómo aparezca en la portada.",0),
("Artículo de prensa",Q,"«La cara oculta del turismo»","",0),
("Sigla de una publicación",C,"<i>BRAE</i> · <i>DEA</i> · <i>JOOP</i>","Las siglas que responden a títulos heredan su cursiva. Las demás siglas van en redonda.",0),
("Extranjerismo en titular",S,"Neymar consigue su cuarto ‘hat-trick’","Uso propio de la prensa: las comillas simples sustituyen a la cursiva en titulares.",0),
]))
G.append(("Música",[
("Disco o álbum",C,"<i>Un canto a Galicia</i>","",1),
("Canción",Q,"«Volver» · «Mediterráneo»","Es pieza dependiente dentro de un disco. Citada sola, puedes elegir comillas o cursiva.",1),
("Ópera, sinfonía, obra completa",C,"<i>La traviata</i>","",1),
("Movimiento o aria dentro de la obra",Q,"«Nessun dorma», de <i>Turandot</i>","",1),
]))
G.append(("Cine, televisión y teatro",[
("Película",C,"<i>La lengua de las mariposas</i>","",0),
("Serie o programa",C,"<i>El hormiguero</i> · <i>Caiga quien caiga</i>","",0),
("Episodio de una serie",Q,"«La boda roja», de <i>Juego de tronos</i>","",1),
("Obra de teatro",C,"<i>Hamlet</i> · <i>Doña Rosita</i>","",0),
("Acotación escénica",C,"<i>(Llora)</i> · <i>(Gritando)</i>","La cursiva alcanza también a los paréntesis.",0),
("Videojuego",C,"<i>El túnel</i>","Los títulos de obras de creación incluyen los (video)juegos.",0),
]))
G.append(("Arte y exposiciones",[
("Cuadro o escultura",C,"<i>Las meninas</i> · <i>La danza del fuego</i>","",0),
("Fotografía con título",C,"<i>Muerte de un miliciano</i>","",0),
("Exposición",Q,"la exposición «Atapuerca: nuestros antecesores»","En redonda y entre comillas, no en cursiva.",0),
("Ponencia, discurso, conferencia",Q,"«Goya y su tiempo»","Igual los planes y proyectos de carácter cultural.",0),
("Lema, consigna, eslogan",Q,"bajo el lema «Un equipo, un país»","",0),
]))
G.append(("Nombres propios",[
("Entidad, organismo, marca",R,"Lamborghini · Rijksmuseum · Microsoft Excel","Aunque la denominación sea de otra lengua.",0),
("Sigla y acrónimo",R,"ONG · FBI · TIC","Aunque su desarrollo sea inglés: <i>FBI</i> (Federal Bureau of Investigation) va en redonda.",0),
("Seudónimo, alias, apodo",R,"Alfonso X el Sabio · la Faraona","",0),
("Apodo entre nombre y apellido",Q,"Ernesto «Che» Guevara · María <i>Navajitas</i> Mendoza","Solo aquí se resalta: entre el nombre de pila y el apellido, o si ocupa el lugar del nombre. Cursiva o comillas.",0),
("Barco, avión, objeto único",R,"el Titanic · el Big Ben","",0),
("Especie y subespecie",C,"<i>Panthera leo</i> · <i>Homo sapiens</i>","Cursiva, con mayúscula inicial solo en el primer elemento.",0),
("Taxón superior en español",R,"orden coleópteros · familia cactáceas","",0),
("Escritura sin cursiva",R,"Se tatuó la palabra 勇气","Un sistema que carece de cursiva no se fuerza.",0),
]))
G.append(("Palabras y expresiones",[
("Extranjerismo crudo",C,"otra de sus <i>boutades</i> · <i>okonomiyaki</i>","En textos impresos, la cursiva es preferible a las comillas para esto.",0),
("Extranjerismo adaptado",R,"bádminton · boicot · escúter","Ya se ajusta a nuestra ortografía: no se resalta.",0),
("Derivado español de voz extranjera",R,"beethoveniano · hollywoodiense · pizzería","Aunque conserve la grafía extraña.",0),
("Locución latina no adaptada",C,"<i>in dubio pro reo</i> · <i>Carthago delenda est</i>","Y sus abreviaturas: <i>et al.</i>, <i>ibidem</i>.",0),
("Latinismo adaptado",R,"currículum · déficit · ultimátum","",0),
("Fórmula de tratamiento extranjera",R,"sir Arthur Conan Doyle · madame de Maintenon","Con independencia de su grado de adaptación.",0),
("La palabra de la que se habla",C,"La palabra <i>gulag</i> es un préstamo del ruso","Función metalingüística. En manuscrito o soporte sin cursiva, comillas.",0),
("El significado de una palabra",S,"<i>apis</i> ‘abeja’ y <i>cultura</i> ‘cultivo, crianza’","Uso técnico propio de las comillas simples.",0),
("Palabra impropia, vulgar o irónica",C,"dijo que la comida llevaba muchas <i>especies</i>","Alternan cursiva y comillas. En impreso se prefiere la cursiva.",0),
("Creación ocasional o neologismo",C,"no soporto a los <i>contradigolotodo</i>","Si el neologismo ya está asentado, redonda: <i>los simpapeles</i>.",0),
("<i>sic</i>",C,"«Migüel» (<i>sic</i>)","",0),
("Variable matemática o magnitud",C,"si <i>a</i> = <i>b</i> y <i>b</i> = <i>c</i>","",0),
("Cifra, símbolo y función",R,"sen · lim · 3 kg · +","En textos técnicos van en redonda, igual que corchetes y llaves.",0),
]))
G.append(("Citas y fragmentos",[
("Cita breve integrada",Q,"El presidente respondió: «No hay motivos de alarma»","",0),
("Cita exenta en bloque",R,"sangrada, cuerpo menor, sin comillas","Si se delimita con comillas, no se usa cursiva — ni siquiera si la cita está en otra lengua.",0),
("Pensamiento de un personaje",Q,"«Esto empieza mal», pensó Bastidas","",0),
("Palabras textuales en estilo indirecto",Q,"reconocieron sentir «impotencia y congoja»","Solo si se respeta la correlación de tiempos y personas. Si hay que retocarlas, se quitan las comillas.",0),
("Prólogo, dedicatoria, epígrafe",C,"—","Sean o no del propio autor de la obra.",0),
("Cita indirecta",X,"Dijo que él no soportaba aquella situación","<b>No lleva ningún resalte.</b> Al estar integrada en el discurso, no se marca de ninguna manera.",0),
]))

DEST={'cursiva':('d-cur','cursiva'),'comillas':('d-com','«comillas»'),
      'redonda':('d-red','redonda'),'simples':('d-sim','‘simples’'),'nunca':('d-nun','sin resalte')}
def render():
    nav=[]; body=[]
    for gi,(titulo,filas) in enumerate(G):
        gid='g%d'%gi
        nav.append('<a href="#%s"><span class="tn">%s</span>%s</a>'%(gid,len(filas),titulo))
        r=[]
        for cosa,dest,ej,nota,der in filas:
            dc,dl=DEST[dest]
            d='<span class="dchip %s">%s</span>'%(dc,dl)
            marca='<span class="der" title="Deducido del principio general">deducido</span>' if der else ''
            n='<span class="nota">%s</span>'%nota if nota else ''
            r.append('<tr><td class="cosa">%s%s</td><td class="dest">%s</td>'
                     '<td class="ej">%s%s</td></tr>'%(cosa,marca,d,ej,n))
        body.append('<section id="%s"><h2>%s</h2><div class="scroller"><table>'
          '<thead><tr><th>Qué es</th><th>Va en</th><th>Ejemplo</th></tr></thead>'
          '<tbody>%s</tbody></table></div></section>'%(gid,titulo,''.join(r)))
    t=io.open('tpl-cursiva.html',encoding='utf-8').read()
    t=t.replace('{{NAV}}',''.join(nav)).replace('{{BODY}}',''.join(body))
    t=t.replace('{{N}}',str(sum(len(x[1]) for x in G)))
    io.open('cursiva-o-comillas.html','w',encoding='utf-8').write(t)
    print('filas:',sum(len(x[1]) for x in G))
render()
