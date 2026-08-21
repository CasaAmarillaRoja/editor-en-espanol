# -*- coding: utf-8 -*-
import io, json
ES = json.load(io.open('es_full.json',encoding='utf-8'))
EN = json.load(io.open('en_full.json',encoding='utf-8'))

# (es_display, en_display, es_lookup, en_lookup, marca_EN, marca_ES|None, recambio, nivel, nota)
V=[
("asumir","assume","asumir","assume","to accept something to be true",None,"suponer, dar por sentado, presuponer",1,""),
("realizar","realize","realizar","realize","to understand a situation",None,"darse cuenta de, percatarse, caer en la cuenta",1,""),
("soportar","support","soportar","support","to agree with and give encouragement",None,"apoyar, respaldar; <i>(inform.)</i> admitir, ser compatible con",1,""),
("resumir","resume","resumir","resume","it starts again after a pause",None,"reanudar, retomar, continuar",1,""),
("salvar","save","salvar","save","to put information into a computer",None,"guardar; <b>ahorrar</b> <i>(tiempo)</i>",1,"Trece acepciones y ninguna es «guardar»."),
("atender","attend","atender","attend","to go to an event, place",None,"asistir a, acudir a, concurrir a",1,""),
("pretender","pretend","pretender","pretend","to behave as if something is true",None,"fingir, aparentar, simular",1,""),
("calificar","qualify","calificar","qualify","to have the legal right",None,"reunir los requisitos, clasificarse, tener derecho a",1,""),
("direccionar","address","direccionar","address","to give attention to or deal with a matter",None,"abordar, tratar, afrontar, atajar",1,""),
("deprivar","deprive","deprivar","deprive","to prevent someone from having",None,"privar de, despojar de",1,"No figura en el diccionario."),
("admitir","admit","admitir","admit","to agree that something is true","aceptar (‖ recibir voluntariamente)","reconocer, confesar",2,"<b>No es un error.</b> El DLE define <i>reconocer</i> usando <i>admitir</i> —acepciones 7 y 8: «Admitir o aceptar algo como legítimo»—, así que se definen mutuamente. Lo delator es la frecuencia: la traducción del inglés vuelca siempre <i>admit</i> en <i>admitir</i> y desplaza a <i>reconocer</i>, que es el verbo que el español prefiere para asumir una falta."),
("navegar","navigate","navegar","navigate","to deal effectively with a difficult situation",None,"sortear, lidiar con, afrontar, manejarse en",1,"Ojo al reparto: el <i>navigate</i> informático —«to move around a website»— <b>sí</b> lo tiene el español, en la acepción 6. El que falta es el figurado, y Cambridge solo lo recoge en su diccionario de inglés de negocios. Ninguna de las ocho acepciones españolas lo cubre."),
("introducir","introduce","introducir","introduce","to tell someone another person","granjearle el trato","presentar, dar a conocer",2,"La acepción 3 cubre meter a alguien en un círculo, no presentar a dos personas entre sí."),
("impactar","impact","impactar","impact","to have an influence on something","Impresionar, desconcertar","afectar a, repercutir en, incidir en",2,""),
("someter","submit","someter","submit","to give or offer something for a decision","Proponer a la consideración","enviar, remitir, entregar",2,"<b>«presentar» no vale de recambio:</b> el DLE lo lista como sinónimo de <i>someter</i>."),
("anticipar","anticipate","anticipar","anticipate","to imagine or expect that something will happen","Adivinar lo que ha de suceder","esperar, augurar, barruntar",3,"<b>«prever» no vale de recambio:</b> es sinónimo de <i>anticipar</i> en el DLE."),
("demandar","demand","demandar","demand","to ask for something forcefully","Pedir, rogar","—",3,"El DLE lista <i>exigir, reclamar, requerir, instar</i> como sinónimos."),
("remover","remove","remover","remove","to take something or someone away","Quitar, apartar u obviar","—",3,"<b>No es un calco.</b> La RAE lo documenta desde 1325 y dice que no hay razón para censurarlo: viene del étimo latino."),
("ignorar","ignore","ignorar","ignore","to intentionally not listen","No hacer caso de algo","—",3,"La RAE reconoce el calco y lo admite: asentado en el uso culto desde la primera mitad del siglo XX."),
("aplicar","apply","aplicar","apply","to request something, usually officially","Presentar una solicitud oficial","—",3,""),
("accesar","access","accesar","access","to be able to use or obtain something","Tener acceso a algo","—",3,""),
("asistir","assist","asistir","assist","to help","Socorrer, favorecer, ayudar","—",3,""),
("reportar","report","reportar","report","to give a description of something","Transmitir, comunicar, dar noticia","—",3,""),
("encriptar","encrypt","encriptar","encrypt","secret code","cifrar","—",3,""),
("editar","edit","editar","edit","to make changes to a text or film","Modificar un documento o archivo","—",3,""),
]
A=[
("severo","severe","severo","severe","causing very great pain",None,"grave, intenso, agudo",1,"<b>«serio» no vale de recambio:</b> el DLE lo lista como sinónimo de <i>severo</i>. La única acepción cercana, la 3, se limita a las estaciones del año."),
("eventual · eventualmente","eventual(ly)","eventualmente","eventually","in the end, especially after a long time",None,"finalmente, con el tiempo, a la larga",1,"La acepción española es la contraria de la inglesa."),
("relevante","relevant","relevante","relevant","connected with what is happening",None,"pertinente, atinente, que viene al caso",1,""),
("dramático","dramatic","dramático","dramatic","very sudden or noticeable",None,"drástico, brusco, acusado, pronunciado",1,"De los tres sentidos ingleses, el español cubre dos: «relating to plays and acting» es la acepción 1, y «full of action and excitement» la 5. Solo falta «very sudden or noticeable». <b>«espectacular» no vale de recambio:</b> el DLE lo lista como sinónimo."),
("doméstico","domestic","doméstico","domestic","relating to a person",None,"nacional, interno, interior",1,""),
("comprensivo","comprehensive","comprensivo","comprehensive","complete and including everything",None,"exhaustivo, completo, pormenorizado",1,""),
("extensivo","extensive","extensivo","extensive","covering a large area","Que se extiende o se puede extender","extenso, amplio, dilatado",2,"La divergencia es real —<i>extensivo</i> es «aplicable a más cosas», <i>extenso</i> es «grande»— pero el lector recupera el sentido sin tropezar. Vale en racimo, no como prueba."),
("desafiante","challenging","desafiante","challenging","difficult, in a way that tests",None,"exigente, arduo, difícil, trabajoso",1,""),
("casual","casual","casual","casual","Casual clothes are not formal",None,"informal, desenfadado, de sport",1,""),
("interesantemente","interestingly","interesantemente","interestingly","used to introduce a piece of information",None,"curiosamente, lo curioso es que",1,""),
("notorio","notorious","notorio","notorious","famous for something bad",None,"de mala fama, infame, desacreditado",1,"<b>Invierte la polaridad:</b> en inglés es siempre malo; en español, neutro o elogioso."),
("vibrante","vibrant","vibrante","vibrant","energetic, exciting, and full of enthusiasm",None,"animado, bullicioso, pujante, lleno de vida",1,""),
("abrupto","abrupt","abrupto","abrupt","sudden and unexpected","Áspero, violento, rudo, destemplado","súbito, repentino, inesperado",2,"El otro sentido inglés, «using too few words when talking», es la acepción 2. Y esa acepción roza la brusquedad temporal, así que la frontera es borrosa: señálalo en racimo, no aislado."),
("simpático","sympathetic","simpático","sympathetic","understand and care about someone",None,"compasivo, comprensivo, solidario",1,""),
("cínico","cynical","cínico","cynical","believing that people are only interested in themselves",None,"escéptico, descreído, desconfiado",1,"El español acusa de desvergüenza; el inglés solo describe desconfianza."),
("adepto","adept","adepto","adept","having a natural ability",None,"experto, diestro, ducho, versado",1,""),
("honesto","honest","honesto","honest","telling the truth",None,"veraz, sincero, franco",2,"El DLE no recoge «veraz»: honesto es rectitud moral, no veracidad. Pero el uso es tan general que señalarlo aislado no se sostiene."),
("adicionalmente","additionally","adicionalmente","additionally","also or in addition",None,"además, asimismo, por otra parte",2,"No figura en el DLE, aunque los adverbios en <i>-mente</i> se forman libremente."),
("definitivamente","definitely","definitivamente","definitely","without any doubt","De manera definitiva","sin duda, desde luego, por supuesto",2,""),
("notablemente","notably","notablemente","notably","especially or most importantly","De manera notable","en particular, sobre todo, señaladamente",2,"El español marca grado; el inglés marca foco."),
("integral","integral","integral","integral","necessary and important as a part of a whole","Que comprende todos los elementos","esencial, fundamental, consustancial",2,"Ojo a la acepción 5: la parte integral entra en el todo <b>sin serle esencial</b> — lo contrario del calco."),
("masivo","massive","masivo","massive","very large in size","Que se aplica en gran cantidad","enorme, ingente, colosal",2,""),
("regular","regular","regular","regular","happening or doing something often","Que se hace o se produce a intervalos regulares","habitual, asiduo, fiel",2,""),
("consistente","consistent","consistente","consistent","always behaving or happening in a similar",None,"constante, uniforme, sistemático",2,"La definición no recoge el calco, pero el DLE lista <i>coherente</i> y <i>congruente</i> entre los sinónimos de <i>consistente</i>, así que esos dos no valen de recambio."),
("elaborado","elaborate","elaborado","elaborate","containing a lot of careful detail","preparado o dispuesto con interés y cuidado","complejo, minucioso, detallado",2,""),
("excitante","exciting","excitante","exciting","making you feel excited","Que excita","—",3,"El DLE lista <i>estimulante, apasionante, intrigante</i> como sinónimos. La connotación sexual es de uso, no de norma."),
("ordinario","ordinary","ordinario","ordinary","not different or special","Común, regular y que sucede habitualmente","—",3,"La primera acepción es la inglesa. Lo peyorativo es la tercera."),
("patético","pathetic","patético","pathetic","unsuccessful or showing no ability","Penoso, lamentable o ridículo","—",3,""),
("agresivo","aggressive","agresivo","aggressive","determined to win or succeed","Que actúa con dinamismo, audacia y decisión","—",3,""),
("crítico","critical","crítico","critical","of the greatest importance","Idóneo o más oportuno","—",3,""),
("prominente","prominent","prominente","prominent","very well known and important","Ilustre, famoso, destacado","—",3,""),
("bizarro","bizarre","bizarro","bizarre","very strange and unusual","Raro, extravagante o fuera de lo común","—",3,"Incorporado al DLE tras décadas de censura."),
("sensible","sensitive","sensible","sensitive","A sensitive subject","Delicado, que por su naturaleza","—",3,""),
("sofisticado","sophisticated","sofisticado","sophisticated","intelligent or made in a complicated way","Técnicamente complejo o avanzado","—",3,""),
("nominado","nominated","nominado","nominate","to officially suggest someone for an election","presentada o propuesta como candidata","—",3,""),
("aparente","apparent","aparente","apparent","able to be seen or understood","Que aparece y se muestra a la vista","—",3,"Conviven dos sentidos opuestos —«que parece y no es» y «que se muestra a la vista»— y el contexto decide."),
("plausible","plausible","plausible","plausible","seeming likely to be true","Atendible, admisible, recomendable","—",3,""),
("asertivo","assertive","asertivo","assertive","behaves confidently","expresa su opinión de manera firme","—",3,""),
("errático","erratic","errático","erratic","not regular, certain, or expected","Impredecible o que cambia con frecuencia","—",3,""),
]
S=[
("condición","condition","condición","condition","any of different types of diseases",None,"enfermedad, afección, dolencia, trastorno",1,""),
("asunción","assumption","asunción","assumption","something that you accept as true",None,"suposición, supuesto, hipótesis, premisa",1,"Como <i>asumir</i> no significa suponer, <i>asunción</i> no significa suposición."),
("data","data","data","data","information, especially facts or numbers",None,"datos, información",1,"Significa «fecha» o «plazo»."),
("facilidades","facilities","facilidad","facility","a place, especially including buildings",None,"instalaciones, dependencias, equipamiento",1,"El plural existe, pero significa «facilidades de pago», no «edificios»."),
("premisas","premises","premisa","premises","the land and buildings owned by someone",None,"local, instalaciones, sede, recinto",1,"<b>Marcador débil:</b> aparece en traducción jurídica automática, pero es raro."),
("carácter","character","carácter","character","a person represented in a film",None,"personaje",1,""),
("argumento","argument","argumento","argument","a disagreement, or the process of disagreeing",None,"discusión, disputa, riña, altercado",1,""),
("agenda","agenda","agenda","agenda","a secret aim or reason",None,"intereses, propósitos, motivaciones ocultas",1,""),
("oficial","officer","oficial","officer","a member of the police force",None,"agente",2,"Las acepciones militares y administrativas no cubren al agente de policía."),
("evidencia","evidence","evidencia","evidence","facts, information, documents","Prueba determinante en un proceso","pruebas, indicios, datos",2,"<b>El caso puro del conflicto:</b> el DLE la recoge, el DPD la censura como calco."),
("tópico","topic","tópico","topic","a subject that is discussed","tema (‖ parte de un enunciado)","asunto, cuestión, materia",2,"La acepción que la ampara es de lingüística. <b>«tema» no vale de recambio:</b> el DLE lo lista como sinónimo. Y al revés: <code>tópico</code> <i>sí</i> es la traducción correcta de <i>trope</i> en su sentido de motivo repetido — misma palabra, mal recambio para <i>topic</i> y buen recambio para <i>trope</i>."),
("crimen","crime","crimen","crime","an illegal act","Delito grave","delincuencia",2,"<b>«delito» no vale de recambio:</b> el DLE lo lista como sinónimo de <i>crimen</i>."),
("consistencia","consistency","consistencia","consistency","the quality of always behaving","Trabazón, coherencia","constancia, uniformidad, regularidad",2,"<b>«coherencia» no vale de recambio:</b> el DLE la lista como sinónimo."),
("rango","range","rango","range","between an upper and a lower limit","Amplitud de la variación","gama, abanico, intervalo, horquilla",2,"Amparado en estadística. Fuera de ahí, no."),
("balance","balance","balance","balance","the amount of money you have in a bank account","Valoración en un momento concreto","saldo, equilibrio",2,""),
("patología","pathology","patología","pathology","a disease or medical condition","Conjunto de síntomas de una enfermedad","enfermedad, dolencia, afección",2,"La acepción designa el cuadro de síntomas, no la enfermedad misma."),
("políticas","policies","política","policy","a set of ideas or a plan of what to do","Orientaciones o directrices que rigen la actuación","—",3,"La acepción 12 es exactamente <i>policy</i>."),
("localización","location","localización","location","a place or position","Escenario de un rodaje","—",3,"Amparada además por sus sinónimos, que incluyen <i>ubicación</i> y <i>emplazamiento</i>."),
("audiencia","audience","audiencia","audience","the group of people together in one place","Público que atiende los programas","—",3,""),
("librería","library","librería","library","a collection or set of books","biblioteca (‖ lugar en que se tienen libros)","—",3,"Incluido el uso informático."),
("vegetales","vegetables","vegetal","vegetable","used as food","Hortalizas en general","verduras",3,"Amparado en siete variedades americanas. <b>«hortalizas» no vale de recambio:</b> el DLE lo lista como sinónimo."),
("aplicación","application","aplicación","application","an official request for something","Solicitud oficial que se presenta","—",3,""),
("corporación","corporation","corporación","corporation","a large company or group of companies","Empresa, normalmente de grandes dimensiones","—",3,""),
("estimado","estimate","estimado","estimate","a guess of what the size, value","Cálculo o valoración anticipados","—",3,""),
("escenario","scenario","escenario","scenario","a description of possible actions or events","Posibilidades o perspectivas","—",3,"«El peor escenario» está amparado por la acepción 5."),
("compromiso","compromise","compromiso","compromise","reduce their demands","Acuerdo pactado entre distintas partes","—",3,"El DLE trae el ejemplo literal."),
("tropo","trope","tropo","trope","often used in a particular artist",None,"tópico, lugar común, cliché, motivo recurrente",1,"<b>El otro sentido inglés sí es <i>tropo</i>:</b> la acepción 2 de Cambridge —la retórica, con la sinécdoque como ejemplo— coincide exactamente con la acepción 2 del DLE. El calco es solo el primero, el del motivo repetido en la ficción y los medios. Los sinónimos que da el DLE para <i>tropo</i> son <i>metáfora, imagen, alegoría, símil</i>: ninguno sirve para «cliché»."),
("ironía · irónicamente","irony · ironically","ironía","irony","a situation in which something which was intended",None,"lo curioso del caso; precisamente, justamente; contrasentido",1,"El sentido verbal <b>sí</b> lo tiene el español: la acepción 3 responde a «the use of words that are the opposite of what you mean». El que falta es el situacional, que Cambridge pone primero. Las tres acepciones del DLE exigen <i>burla</i>, y sus sinónimos son <i>sorna, sarcasmo, causticidad, mordacidad, guasa, retintín</i>: llamar ironía a un resultado inesperado atribuye una burla que nadie hizo. La forma más productiva es el adverbio, «Irónicamente, …», calcado de <i>Ironically, …</i>. <b>Y el recambio no es <i>paradoja</i>:</b> el DLE la define como «contrarios a la lógica», y aquí lo que se contradice es la intención, no la lógica. El DLE no sanciona ningún sustantivo de una palabra para esto, así que la reparación es sintáctica: <i>curioso</i> en su acepción 4 «que llama la atención por su rareza», <i>precisamente</i> en el uso enfático que el propio DLE recoge («acabó perjudicando precisamente a quienes pretendía ayudar»), o <i>contrasentido</i> en su acepción 3 para registro formal."),
("epítome","epitome","epítome","epitome","the typical or highest example",None,"paradigma, encarnación, personificación, arquetipo",1,"<b>Cero solapamiento.</b> Casi todas las filas de esta tabla comparten algún sentido entre los dos idiomas; esta no. Cambridge da una única acepción, y el DLE da dos que son ambas de resumir. Sus sinónimos lo confirman: <i>resumen, compendio, extracto, sumario, sinopsis, breviario</i>. «Es el epítome de la elegancia» se lee en español como «es el resumen de la elegancia». Los recambios están tomados del DLE: <i>paradigma</i> es «ejemplo o ejemplar» y sus sinónimos incluyen <i>arquetipo</i> y <i>modelo</i>; <i>personificación</i> trae <i>encarnación</i> entre los suyos. Y la trampa vale en los dos sentidos: traducir el <i>epítome</i> español por <i>epitome</i> es igual de falso — sería <i>summary</i> o <i>abridgement</i>."),
]
CHIP={1:('t1','no consta'),2:('t2','en pugna'),3:('t3','aceptado')}

def lista(senses, marca, faltante=False):
    out=[]
    for s in senses:
        hit = marca and marca.lower() in s.lower()
        cls = ' class="hit"' if hit else ''
        out.append('<li%s>%s</li>'%(cls,s))
    tag = '<div class="nohit">Ninguna acepción recoge el sentido inglés</div>' if faltante else ''
    return tag + '<ol class="senses">' + ''.join(out) + '</ol>'

def rows(data):
    o=[]
    for esd,end,esk,enk,men,mes,fix,lvl,note in data:
        cls,lab = CHIP[lvl]
        en_html = lista(EN.get(enk,['(no recuperado)']), men)
        es_html = lista(ES.get(esk,['(no recuperado)']), mes, faltante=(mes is None))
        fcell = '<span class="dash">no hace falta</span>' if fix=="—" else fix
        n = '<span class="note">%s</span>'%note if note else ''
        o.append('<tr><td class="term"><code>%s</code><span class="src">&larr; %s</span>'
                 '<span class="chip %s">%s</span></td>'
                 '<td class="dic en">%s</td><td class="dic es">%s</td>'
                 '<td class="fix">%s%s</td></tr>'%(esd,end,cls,lab,en_html,es_html,fcell,n))
    return '\n'.join(o)

t=io.open('tpl2.html',encoding='utf-8').read()
t=t.replace('{{VERBOS}}',rows(V)).replace('{{ADJ}}',rows(A)).replace('{{SUST}}',rows(S))
io.open('anglicismos-delatores.html','w',encoding='utf-8').write(t)
print('filas:',len(V)+len(A)+len(S))
