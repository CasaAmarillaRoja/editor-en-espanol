# -*- coding: utf-8 -*-
import io
M='mal'; B='bien'; A='ambas'
# (título, veredicto, [(marca, ejemplo)], nota)
S=[]

S.append(("acentuacion","Acentuación","La tilde diacrítica y los casos que más se fallan. Las reglas generales no se repiten aquí: se dan por sabidas.",[
("Tilde en <i>solo</i> y en los demostrativos","error",[(M,"Sólo vino éste"),(B,"Solo vino este")],
 "Nunca estuvo justificada: no se opone una forma tónica a una átona. Se admite la tilde solo si hay riesgo real de ambigüedad, pero el contexto casi siempre la resuelve. <i>Esto</i>, <i>eso</i> y <i>aquello</i> no se tildan jamás."),
("Monosílabos sin correlato átono","error",[(M,"dió, fué, fuí, vió, tí"),(B,"dio, fue, fui, vio, ti")],
 "La tilde diacrítica solo distingue pares con correlato átono: <i>té/te</i>, <i>mí/mi</i>, <i>sé/se</i>, <i>sí/si</i>, <i>tú/tu</i>, <i>él/el</i>, <i>dé/de</i>, <i>más/mas</i>. Excepción: <i>tés</i>, plural de <i>té</i>, conserva la tilde."),
("<i>Más</i> siempre con tilde","error",[(M,"Dos mas dos son cuatro"),(B,"Dos más dos son cuatro")],
 "Aunque se pronuncie átona. Solo va sin tilde <i>mas</i> cuando equivale a <i>pero</i>."),
("La conjunción <i>o</i> entre cifras","error",[(M,"4 ó 5"),(B,"4 o 5")],
 "La tilde diacrítica ya no se usa para evitar confusiones gráficas."),
("Mayúsculas","error",[(M,"OSCAR, PANADERIA"),(B,"Óscar, PANADERÍA")],
 "Las academias nunca han establecido que las mayúsculas no se tilden."),
("Siglas y símbolos","error",[(M,"CÍA, á (área), lím"),(B,"CIA, a, lim")],
 "Las siglas en mayúsculas no llevan tilde nunca; los símbolos tampoco, por ser de uso internacional. Sí se tildan los acrónimos pasados a minúscula o con solo la inicial mayúscula: <i>láser</i>, <i>Fundéu</i>."),
("Compuestos con y sin guion","error",[(M,"décimocuarto, lógico-matematico"),(B,"decimocuarto, lógico-matemático")],
 "Sin guion, el primer elemento pierde su tilde y la palabra se acentúa como si fuera simple. Con guion, cada elemento conserva la suya."),
("Verbo más pronombres","error",[(M,"dême, tráigamélo"),(B,"deme, tráigamelo")],
 "Se acentúan como palabras simples según las reglas generales: <i>deme</i> es llana terminada en vocal, <i>tráigamelo</i> es sobresdrújula."),
("Palabras con dos acentuaciones","ambas",[(A,"periodo · período"),(A,"cardiaco · cardíaco"),(A,"olimpiada · olimpíada"),(A,"alveolo · alvéolo")],
 "También <i>amoniaco/amoníaco</i>, <i>rubeola/rubéola</i>, <i>bronquiolo/bronquíolo</i>. Elige una y mantenla en todo el texto."),
("Variación entre España y América","depende",[(A,"chófer · chofer"),(A,"fútbol · futbol"),(A,"vídeo · video"),(A,"icono · ícono")],
 "Las terminadas en <i>-sfera</i> son llanas en España (<i>biosfera</i>, <i>estratosfera</i>), salvo <i>atmósfera</i>; en América tienden a esdrújulas."),
("Diéresis","error",[(M,"paragues, ambigüo"),(B,"paragüero, ambiguo")],
 "La diéresis solo marca la <i>u</i> que se pronuncia entre <i>g</i> y <i>e/i</i>: <i>pingüino</i>, <i>vergüenza</i>, <i>lingüista</i>. No se pone ante otra vocal: <i>paraguas</i>, <i>antiguo</i>, <i>averiguar</i>."),
]))

S.append(("coma","La coma","El signo que más se falla, y casi siempre por la misma razón: se pone donde se oye una pausa.",[
("Coma ≠ pausa","error",[(M,"Los alumnos que aprobaron, salieron antes")],
 "<b>La regla madre de la puntuación española.</b> La coma marca fronteras sintácticas, no pausas de la pronunciación. Ni toda pausa pide coma ni toda coma pide pausa."),
("Entre sujeto y verbo","error",[(M,"Mi hermano y su mujer, vinieron ayer"),(B,"Mi hermano y su mujer vinieron ayer")],
 "Nunca, ni con sujetos largos ni con enumeraciones ni con relativas dentro. Solo tres excepciones: si hay un inciso intercalado, si el sujeto termina en <i>etcétera</i>, y ante estructuras del tipo <i>o bien…, o bien…</i>"),
("Ante <i>y</i>, <i>o</i>, <i>ni</i>","error",[(M,"Compró pan, leche, y huevos"),(B,"Compró pan, leche y huevos")],
 "<b>Pero hay cuatro excepciones en las que sí va, y una es obligatoria:</b> cuando cierra una enumeración cuyos miembros van con punto y coma; cuando enlaza con todo lo anterior y no solo con el último miembro (<i>Compró pan, leche y huevos, y salió</i>); cuando lo que introduce es un inciso (<i>Lo hizo todo solo, y me parece fenomenal</i>); y opcionalmente cuando la conjunción se repite ante tres o más elementos."),
("Ante <i>pero</i>","error",[(M,"Te lo iba a decir pero no estaba seguro"),(B,"Te lo iba a decir, pero no estaba seguro")],
 "Obligatoria. Solo se prescinde de ella cuando <i>pero</i> une elementos inferiores a la oración: <i>Trabajo lento pero seguro</i>. Detrás de <i>pero</i> no se pone coma, salvo que siga un elemento que la exija."),
("Ante <i>sino</i>","error",[(M,"No lo hizo María sino Teresa"),(B,"No lo hizo María, sino Teresa")],
 "Obligatoria, incluso cuando introduce grupos que no son oraciones."),
("Con <i>tanto… como…</i>","error",[(M,"Tanto los veteranos, como los novatos deben presentarse"),(B,"Tanto los veteranos como los novatos deben presentarse")],
 "No se separan los dos miembros."),
("En comparativas","error",[(M,"Estoy más feliz, que nadie"),(B,"Estoy más feliz que nadie")],
 "El segundo término de <i>más… que…</i>, <i>tan(to)… como…</i>, <i>tan(to)… que…</i> suele llevar pausa al hablar, pero nunca coma al escribir."),
("Especificativas y explicativas","error",[(B,"Los papeles que estaban encima de la mesa se volaron"),(B,"Los papeles, que estaban encima de la mesa, se volaron")],
 "<b>Las dos son correctas y significan cosas distintas.</b> Sin comas, solo se volaron los que estaban encima de la mesa. Con comas, se volaron todos, y de paso se informa de dónde estaban. La coma cambia el sentido, no la elegancia."),
("Vocativos","error",[(M,"Dime Juan"),(B,"Dime, Juan"),(B,"Gracias, amigas, por esta velada")],
 "Siempre delimitados por coma, en cualquier posición."),
("Circunstanciales antepuestos","bien",[(B,"En el siglo XX, se vivía bien sin Internet"),(B,"Si no sabes cómo hacerlo, pregúntame"),(A,"Si vienes tráeme la maleta")],
 "Se recomienda la coma tras el elemento antepuesto, y también rodearlo si va en medio. Si es muy breve y no hay riesgo de mala lectura, puede omitirse. Pospuesto no se separa: <i>Te traeré la maleta si vienes esta tarde</i>."),
("Conectores discursivos","bien",[(B,"Ahora bien, habría que estar seguros"),(B,"No sabía hacerlo y, sin embargo, le salió muy bien")],
 "<i>Sin embargo</i>, <i>no obstante</i>, <i>es decir</i>, <i>o sea</i>, <i>por (lo) tanto</i>, <i>ahora bien</i> van seguidos de coma, y precedidos de coma, punto y coma o punto."),
("Repetición enfática","error",[(M,"Me gusta el café, café"),(B,"Me gusta el café café"),(B,"Es muy muy bonito")],
 "Cuando una expresión se repite para enfatizar o precisar, no se separa con coma."),
]))

S.append(("otros-signos","Punto, punto y coma, dos puntos","",[
("El punto siempre fuera del signo doble","error",[(M,"Me dijo: «No te vayas.»"),(B,"Me dijo: «No te vayas».")],
 "El punto va detrás de comillas, rayas, paréntesis y corchetes de cierre. No se omite si delante hay signo de interrogación o exclamación."),
("Nunca punto tras interrogación o exclamación","error",[(M,"¿Vienes?."),(B,"¿Vienes?")],
 "Pero sí se escribe punto <i>antes</i> del signo de apertura si cierra el enunciado anterior: <i>Me llamo Lucía. ¿Tú?</i>"),
("Elementos que no se cierran con punto","bien",[(B,"Títulos y titulares aislados en su línea"),(B,"Fechas en línea aparte"),(B,"Lemas y eslóganes"),(B,"Pies de foto"),(B,"Celdas de tablas")],
 "Tampoco el nombre del autor de una cita exenta. Salvo en los títulos, el punto será tanto más aceptable cuanto más complejo sea el elemento."),
("Punto abreviativo y punto final","error",[(M,"Trajo libros, cuadernos, etc.."),(B,"Trajo libros, cuadernos, etc.")],
 "Cuando coinciden, solo se escribe uno."),
("Punto y coma en enumeraciones con comas","bien",[(B,"Vinieron Martín, mi primo; Antonio, mi hermano; mis tíos, Javier y Elena, y mi madre")],
 "Se pone punto y coma entre todos los elementos aunque alguno no lleve comas. Ante la conjunción final, lo más recomendable es la coma."),
("Dos puntos en saludos de carta","error",[(M,"Estimados vecinos,"),(B,"Estimados vecinos:")],
 "Si el saludo va en línea aparte, dos puntos, nunca coma. En correo o mensajería, si se sigue en la misma línea, vale el punto: <i>Hola, Sonia. ¿Cómo va todo?</i>"),
("Mayúscula tras dos puntos","depende",[(B,"Siempre hace lo mismo: empieza mal, pero acaba bien"),(B,"El senador afirmó: «No defraudaremos a los electores»")],
 "Normalmente minúscula. Mayúscula tras saludo de carta si se cambia de línea, tras elementos anunciadores (<i>Modo de empleo:</i>), tras epígrafe, al comienzo de cita y en enumeraciones cuyos elementos cierran con punto."),
]))

S.append(("comillas","Comillas, raya y paréntesis","",[
("Jerarquía de comillas","bien",[(B,"«Antonio me dijo: “Vaya ‘cacharro’ se ha comprado Julián”»")],
 "En español se recomienda abrir con angulares « », y dentro de ellas inglesas “ ” y luego simples ‘ ’. Empezar por las inglesas no es incorrecto, sobre todo si hay limitaciones técnicas, pero el orden inverso sí lo es."),
("La raya de inciso va pegada","error",[(M,"La subasta — la mayor del año — cerró en junio"),(B,"La subasta —la mayor del año— cerró en junio")],
 "Pegada a la primera y última palabra que enmarca, separada por espacio de lo que queda fuera. Y la raya de cierre es obligatoria incluso a final de enunciado: <i>Se llama José Luis —al menos que yo sepa—</i>."),
("Raya, guion y semirraya","error",[(M,"1998–2012 (semirraya)"),(B,"1998-2012 (guion)"),(B,"—inciso— (raya)")],
 "Tres signos distintos con tres funciones. Para intervalos, guion simple sin espacios. La semirraya (–) es de la tipografía inglesa y el español no la usa para rangos."),
("Inciso dentro de paréntesis","bien",[(B,"…(la bibliografía existente —incluso en español— es extensa)…")],
 "Dentro de paréntesis, el inciso va con rayas. Y al revés: dentro de un inciso con rayas, el dato se mete en paréntesis."),
("Nunca punto antes del paréntesis de cierre","error",[(M,"(Supongo que estaba pensando en otras cosas.)"),(B,"(Supongo que estaba pensando en otras cosas).")],
 "Tampoco coma, punto y coma ni dos puntos. Sí puede ir un punto abreviativo, o el cierre de otro signo doble."),
("Comillas simples para significados","bien",[(B,"<i>apis</i> ‘abeja’ y <i>cultura</i> ‘cultivo, crianza’")],
 "Uso técnico propio de las simples. También marcan extranjerismos en titulares de prensa, donde sustituyen a la cursiva."),
("Citas dentro del discurso indirecto","error",[(M,"El presidente dijo que «me preocupa la corrupción»"),(B,"Para el presidente, «la corrupción es lo más preocupante»"),(B,"El presidente dijo que le preocupaba la corrupción")],
 "La cita literal tiene que respetar la correlación de personas y tiempos. Si hay que cambiar las palabras para encajarlas, se quitan las comillas."),
]))

S.append(("interrogacion","Interrogación y exclamación","",[
("Los signos son dobles","error",[(M,"Cuánto costó?"),(B,"¿Cuánto costó?")],
 "Suprimir el de apertura por imitación de otras lenguas es incorrecto."),
("Qué queda fuera de los signos","bien",[(B,"Entonces, ¿venís mañana?"),(B,"Antonio, ¡calla!"),(B,"¡Calla, Antonio!")],
 "Fuera: conectores y vocativos antepuestos, tópicos, construcciones con <i>si</i> o <i>aunque</i> antepuestas, adverbios extraoracionales. Dentro si van en posición media o final. <i>Y</i> y <i>o</i> se recomienda meterlos dentro; con <i>pero</i> valen las dos."),
("Cadenas de preguntas","ambas",[(A,"¿Quién eres? ¿Cómo te llamas?"),(A,"¿Quién eres?, ¿cómo te llamas?")],
 "O cada pregunta es un enunciado y empieza en mayúscula, o todas son un enunciado, separadas por coma o punto y coma y con minúscula."),
("Combinación para mayor énfasis","bien",[(B,"¿¡Qué me estás contando!?"),(B,"¡¿Qué me estás contando?!")],
 "Repetir el signo de exclamación es válido (<i>¡¡¡Bravoooo!!!</i>); repetir el de interrogación es preferible evitarlo. Para sorpresa, se combinan los dos signos, y lo mejor es abrir y cerrar con ambos."),
("Cuándo se pueden omitir","bien",[(B,"Qué es la ciencia (título)"),(B,"Y quién lo sabe (retórica)"),(B,"Ay, qué contento estoy")],
 "En títulos con forma de pregunta, en preguntas retóricas que no esperan respuesta y en exclamativas inequívocas."),
]))

S.append(("mayusculas","Mayúsculas y minúsculas","El inglés capitaliza por costumbre en sitios donde el español no lo hace nunca. Aquí están todos.",[
("Días, meses y estaciones","error",[(M,"el Lunes 3 de Enero, en Primavera"),(B,"el lunes 3 de enero, en primavera")],""),
("Cargos, dignidades y tratamientos","error",[(M,"el Rey Felipe, el Papa Francisco, Don Pedro"),(B,"el rey Felipe, el papa Francisco, don Pedro")],
 "También cuando van solos y se refieren a una persona concreta: <i>el rey</i>, <i>el papa</i>. Y en personajes conocidos: <i>don Quijote</i>, <i>san Agustín</i>, <i>sor Juana</i>."),
("Lenguas, monedas, religiones y formas de gobierno","error",[(M,"el Español, el Euro, el Islam, la República"),(B,"el español, el euro, el islam, la república")],
 "Solo con mayúscula en denominaciones oficiales o periodos históricos concretos: <i>República Argentina</i>, <i>la Monarquía</i> (de Roma)."),
("Puntos cardinales","error",[(M,"el Norte, el Suroeste"),(B,"el norte, el suroeste"),(B,"América del Sur")],
 "Minúscula, salvo que formen parte de un nombre propio."),
("Disciplinas y ramas del saber","error",[(M,"estudia Física y Derecho Penal"),(B,"estudia física y derecho penal"),(B,"la asignatura de Física y Química")],
 "Minúscula como disciplina; mayúscula solo como nombre de asignatura, curso o carrera."),
("Títulos de obra: solo la primera palabra","error",[(M,"Cien Años De Soledad"),(B,"Cien años de soledad"),(B,"El túnel")],
 "<b>Este es el calco más visible del inglés.</b> En español solo van en mayúscula la primera palabra y los nombres propios. En cambio, los libros sagrados y los textos legales llevan mayúscula en todas las significativas: <i>la Biblia</i>, <i>el Código Civil</i>."),
("Guerras y revoluciones","bien",[(B,"la guerra civil española"),(B,"la guerra de los Seis Días"),(B,"la Primera Guerra Mundial"),(B,"la Revolución francesa")],
 "En guerras y batallas, mayúscula solo en el nombre específico. En revoluciones, todos los elementos salvo el gentilicio."),
("Mayúscula institucional","bien",[(B,"el Gobierno, el Estado, la Iglesia, la Policía"),(B,"los Gobiernos de los dos países"),(B,"la Iglesia cristiana")],
 "Se mantiene en plural, pero no se extiende a los modificadores."),
("Nombre propio que pasa a común","error",[(M,"un Donjuán, el Párkinson, un Rioja"),(B,"un donjuán, el párkinson, un rioja")],
 "Incluidas las marcas convertidas en nombre común: <i>rímel</i>, <i>clínex</i>. Pero se mantiene la mayúscula si se refiere al producto de la marca: <i>un Toyota</i>, <i>un Gauguin</i>."),
("Todo en mayúsculas","depende",[(B,"Carteles, portadas, inscripciones, lemas"),(M,"ESTO EN UN CORREO O CHAT")],
 "Válido en carteles, portadas, cabeceras y fórmulas jurídicas (<i>CERTIFICA</i>). En internet se lee como grito y es preferible evitarlo."),
]))

S.append(("cursiva","Cursiva, redonda y negrita","",[
("Extranjerismos crudos en cursiva","bien",[(B,"otra de sus <i>boutades</i> insoportables"),(B,"<i>in dubio pro reo</i>")],
 "Las palabras de otra lengua que no se ajustan a nuestra ortografía van en cursiva, igual que las locuciones latinas no adaptadas."),
("Pero las adaptadas, en redonda","error",[(M,"<i>bádminton</i>, <i>boicot</i>, <i>pizzería</i>"),(B,"bádminton, boicot, pizzería")],
 "También en redonda los derivados españoles de voces extranjeras: <i>beethoveniano</i>, <i>hollywoodiense</i>, <i>darwinismo</i>."),
("Nombres propios, marcas y siglas en redonda","error",[(M,"<i>Lamborghini</i>, <i>FBI</i>, <i>Rijksmuseum</i>"),(B,"Lamborghini, FBI, Rijksmuseum")],
 "Aunque sean de otra lengua y aunque su desarrollo lo sea: <i>FBI</i> (Federal Bureau of Investigation) va en redonda."),
("Títulos de obra en cursiva","bien",[(B,"<i>Los miserables</i>, <i>Las meninas</i>, <i>El País</i>")],
 "También publicaciones periódicas, con mayúscula en todas las palabras significativas. Las piezas dentro de una obra van entre comillas si se citan junto a la obra: «El rayo de luna», de las <i>Leyendas</i>."),
("Leyes y libros sagrados en redonda","error",[(M,"<i>el Código Penal</i>, <i>la Biblia</i>"),(B,"el Código Penal, la Biblia")],
 "La mayúscula ya delimita su extensión, así que la cursiva es innecesaria. Solo se recurre a ella si el título legal es tan largo que se limita la mayúscula al primer elemento."),
("Función metalingüística","bien",[(B,"La palabra <i>gulag</i> es un préstamo del ruso"),(B,"El prefijo <i>pos-</i> tiene la variante <i>post-</i>")],
 "Cuando se habla de la palabra en cuanto palabra. En soportes sin cursiva, comillas."),
("Nomenclatura científica","bien",[(B,"<i>Panthera leo</i>, <i>Homo sapiens</i>"),(B,"orden coleópteros, familia cactáceas")],
 "Género, especie y subespecie en cursiva y con inicial mayúscula en el primer elemento. Los taxones superiores en nombre español van en redonda y minúscula."),
("Redonda dentro de cursiva","bien",[(B,"<i>La palabra</i> escúter <i>viene del inglés</i> scooter")],
 "En un texto en cursiva, el resalte se hace con redonda: funciona como un negativo."),
]))

S.append(("cifras","Cifras, fechas, horas y símbolos","Aquí es donde el calco del inglés produce errores de dato, no de estilo.",[
("Separador de millares","error",[(M,"1,250,000 · 1.250.000"),(B,"1 250 000")],
 "<b>No se admite ni el punto ni la coma:</b> solo el espacio, preferiblemente fino. Y solo en cifras de más de cuatro dígitos que expresen cantidad. <b>No se separan</b> los años (<i>el 40000 a. C.</i>), la numeración legal (<i>artículo 1584</i>), los códigos postales (<i>28004</i>) ni ningún otro identificador."),
("Separador decimal","ambas",[(A,"6,5 €"),(A,"6.5 €"),(M,"6’5 €")],
 "Coma y punto son ambos válidos, según la preferencia de cada zona. Lo que no vale es el apóstrofo. Elige uno y no los alternes dentro de un texto."),
("Porcentajes","error",[(M,"el dos %"),(B,"el 2 %"),(B,"el dos por ciento"),(B,"el 2 por ciento")],
 "El símbolo va separado de la cifra por un espacio. Cifra con símbolo o palabra con palabra; lo que no se puede es mezclar palabra y símbolo."),
("Fecha desarrollada","error",[(M,"Octubre 30, 2020"),(B,"30 de octubre de 2020"),(B,"Madrid, 6 de octubre de 2017")],
 "Día, mes y año unidos por preposición, mes en minúscula. El orden <i>mes día, año</i> es estadounidense."),
("Fecha abreviada","ambas",[(A,"6-10-2017"),(A,"6/10/2017"),(A,"6.10.2017")],
 "Guion, barra o punto. No se añade cero a la izquierda salvo por exigencia técnica."),
("La hora","ambas",[(A,"las 15:06 h"),(A,"las 15.06"),(M,"las 15’34 h")],
 "Dos puntos en contexto técnico, punto admitido fuera de él. Fuera de contextos técnicos se pueden omitir los ceros irrelevantes (<i>las 3:18</i>, <i>las 15 h</i>); al suprimirlos hace falta el símbolo <i>h</i>. Nunca apóstrofo."),
("Años y décadas","error",[(M,"del ’98, los 30’s, las ONG’s"),(B,"del 98, los 30, las ONG")],
 "El apóstrofo no marca omisión de cifras ni plural. Para intervalos, deja al menos dos cifras del segundo año: <i>2017-18</i>, no <i>2017-8</i>."),
("Símbolos","error",[(M,"3 kgs., 15h"),(B,"3 kg, 15 h")],
 "Sin punto, invariables en plural, pospuestos y separados por un espacio. Excepción pegada: los grados, <i>10°</i>. El tiempo se abrevia <i>h</i>, <i>min</i>, <i>s</i>: <i>35 h 14 min 5 s</i>, nunca con los signos de los ángulos."),
("Símbolo monetario","depende",[(B,"3 $ · 4,5 € (España: pospuesto y separado)"),(B,"$3 (América: antepuesto y pegado)")],
 "Las dos convenciones son correctas en su zona. Lo que conviene es desambiguar la moneda cuando el símbolo se comparte: <i>50 USD</i>."),
("Cifras o palabras","depende",[(B,"cinco personas (texto literario)"),(B,"5 personas (texto técnico, titular, cartel)")],
 "En texto no técnico se prefieren las palabras, salvo números complejos. En técnico, publicitario o periodístico, cifras."),
]))

S.append(("concordancia","Concordancia","La mayoría de estos casos admite las dos opciones. Corregirlos como si solo hubiera una es el error más frecuente.",[
("<i>La mayoría de los asistentes</i>","ambas",[(A,"La mayoría de los asistentes aprobó la propuesta"),(A,"La mayoría de los asistentes aprobaron la propuesta")],
 "Igual con <i>el resto de</i>, <i>la mitad de</i>, <i>un grupo de</i>, <i>el X por ciento de</i>, <i>un montón de</i>… Con verbo copulativo se prefiere el plural: <i>La mayoría de las personas son sinceras</i>. Sin determinante (<i>infinidad de</i>, <i>multitud de</i>) es más normal el plural."),
("Colectivos como <i>gente</i>, <i>pareja</i>, <i>ejército</i>","error",[(M,"La gente vinieron pronto"),(B,"La gente vino pronto")],
 "Concuerdan en singular aunque designen varias entidades. En oración contigua con sujeto implícito sí cabe el plural: <i>La gente vino pronto. Estaban deseando ver el concierto</i>."),
("<i>Este tipo de eventos</i>","ambas",[(A,"Este tipo de eventos suele tener éxito"),(A,"Este tipo de eventos suelen tener éxito")],
 "El singular es más formal. Con <i>ser</i>, el plural es la opción general: <i>Este tipo de personas son muy divertidas</i>."),
("<i>Había</i> / <i>hubo</i> impersonal","error",[(M,"Habían diez personas · Hubieron problemas"),(B,"Había diez personas · Hubo problemas")],
 "<i>Haber</i> impersonal carece de sujeto y va siempre en singular. <i>Hubieron</i> solo es correcto en el pretérito anterior (<i>Cuando hubieron terminado, se marcharon</i>) y en la perífrasis <i>haber de</i> + infinitivo (<i>Hubieron de recorrer muchos lugares</i>)."),
("<i>Se venden casas</i>","error",[(M,"Se vende casas"),(B,"Se venden casas"),(B,"Se tienen que revisar los expedientes")],
 "El nombre es sujeto de la pasiva refleja y el verbo concuerda. También en perífrasis. Pero no se extiende a lo que no es perífrasis: <i>Se intentó establecer alianzas</i>."),
("<i>Se busca a los culpables</i>","error",[(M,"Se buscan a los culpables"),(B,"Se busca a los culpables")],
 "Si el nombre va precedido de <i>a</i>, no hay concordancia."),
("<i>El culpable soy yo</i>","bien",[(B,"El culpable soy yo"),(B,"El verdadero problema son las nuevas leyes")],
 "Con <i>ser</i>, el pronombre personal atrae siempre la concordancia. Uniendo singular y plural se prefiere el plural, en cualquier orden."),
("<i>Uno de los que</i>","error",[(M,"Yo soy uno de los que quiero hacerlo"),(B,"Yo soy uno de los que quieren hacerlo"),(A,"Yo soy uno de los que quiere hacerlo")],
 "El verbo que sigue va en plural; el singular también se admite. Lo que no vale es ponerlo en la persona del sujeto."),
("<i>Ustedes</i>","error",[(M,"Ustedes sabéis que esto es así"),(B,"Ustedes saben que esto es así")],
 "<i>Usted</i> y <i>ustedes</i> concuerdan en tercera persona."),
("Nombres unidos por <i>y</i>","ambas",[(B,"El perro y el gato se alejaron"),(A,"La educación y la cultura constituye/constituyen la base"),(B,"El presidente y principal accionista confirmó la decisión")],
 "Plural si son entidades distintas; singular si se entienden como conjunto, si son la misma entidad o si lo unido son oraciones."),
]))

S.append(("pronombres","Pronombres","",[
("Leísmo de cosa","error",[(M,"Cierra el libro y ponle ahí"),(B,"Cierra el libro y ponlo ahí")],
 "<i>Le(s)</i> nunca para complemento directo de cosa."),
("Leísmo de persona","depende",[(B,"A Juan lo vi ayer"),(A,"A Juan le vi ayer"),(M,"A Juan y a Antonio les vi ayer"),(M,"A María le vi ayer")],
 "Se admite <i>le</i> para el directo de persona solo en masculino singular. Se rechaza en plural y en femenino, singular o plural."),
("Laísmo","error",[(M,"La dije que viniera · ¿Qué la pasa?"),(B,"Le dije que viniera · ¿Qué le pasa?")],
 "<i>La</i> solo vale si es realmente el complemento directo: <i>Dije una palabra > La dije</i>."),
("Loísmo","error",[(M,"Los dije que no se movieran"),(B,"Les dije que no se movieran")],""),
("<i>Le saluda atentamente</i>","bien",[(B,"Le saludo atentamente"),(B,"Les informamos de que no abrimos hasta las 8:30 h")],
 "<i>Le(s)</i> como directo es correcto para el interlocutor al que se trata de usted, sobre todo en masculino y en fórmulas fijadas."),
("Verbos que piden indirecto","error",[(M,"La permitieron ir sola a la fiesta"),(B,"Le permitieron ir sola a la fiesta"),(B,"La obligaron a ir acompañada")],
 "Indirecto con <i>permitir</i>, <i>prohibir</i>, <i>proponer</i>, <i>impedir</i>, <i>mandar</i>, <i>ordenar</i>. Directo con <i>obligar a</i>, <i>invitar a</i>, <i>convencer de</i>, <i>animar a</i>, <i>autorizar a</i>."),
("Posesivo tras adverbio","error",[(M,"detrás mío, delante suyo, encima nuestro"),(B,"detrás de mí, delante de él, encima de nosotros"),(A,"al lado mío · a mi lado · al lado de mí")],
 "Con adverbios de lugar, la variante con <i>de</i>. Las femeninas (<i>detrás suya</i>) están aún más desprestigiadas. En cambio, cuando cabe el posesivo antepuesto, el pospuesto también vale: <i>por tu culpa · por culpa tuya</i>."),
]))

S.append(("verbo","El verbo","",[
("Gerundio de posterioridad","error",[(M,"Estudió en Santiago, yendo después a Bogotá"),(B,"Estudió en Santiago y fue después a Bogotá")],
 "<b>El calco más delator del inglés.</b> El gerundio no puede expresar una simple sucesión temporal. Se tolera cuando la posterioridad es tan inmediata que se percibe como simultaneidad, o cuando cabe una inferencia causal o consecutiva: <i>Se tira contra él, tumbándolo</i>."),
("Gerundio ilativo","depende",[(A,"Murió dejándole como herencia la casa"),(A,"…acentuándose su actividad sexual en esa época")],
 "El gerundio usado para sumar u oponer ideas, en lugar de <i>y le dejó</i> o <i>y se acentúa</i>. La RAE lo documenta, pero deja la conexión lógica a cargo del lector. <b>En caso de duda entre simultaneidad y posterioridad, la recomendación de la RAE es evitar el gerundio.</b>"),
("Queísmo","error",[(M,"No me acordé que era tu cumpleaños"),(B,"No me acordé de que era tu cumpleaños")],
 "<b>La prueba:</b> sustituye la subordinada por <i>eso</i>. Si se conserva la preposición (<i>No me acordé de eso</i>), hace falta <i>de que</i>."),
("Dequeísmo","error",[(M,"Pienso de que Juan va a venir tarde"),(B,"Pienso que Juan va a venir tarde")],
 "Misma prueba al revés: <i>Pienso eso</i>, no <i>Pienso de eso</i>. Solo <i>que</i> ante sujetos (<i>Me alegra que vengas</i>) y ante complementos directos (<i>He oído que te casas</i>)."),
("Deísmo","error",[(M,"Quiere de casarse · Se le veía de venir"),(B,"Quiere casarse · Se le veía venir")],
 "Considerado incluso vulgar."),
("Condicional de futuro del pasado","bien",[(B,"Más tarde recordaría aquella primera noche como un deslumbramiento"),(B,"Sabía que un día se escaparía de ese modo")],
 "Uso correcto y muy útil en narrativa: el condicional expresa un hecho futuro visto desde una perspectiva pasada. No hace falta sustituirlo por <i>iba a</i> + infinitivo."),
("<i>Temas a tratar</i>","depende",[(B,"los temas a tratar, las cantidades a ingresar"),(M,"Tenemos asuntos a tratar"),(B,"Tenemos asuntos que tratar")],
 "Aceptable en el lenguaje económico y administrativo, en construcciones asentadas. Fuera de ahí se recomienda <i>que</i> + infinitivo."),
]))

S.append(("relativos","Relativos, conjunciones y negación","",[
("<i>Cuyo</i>, no <i>que su</i>","error",[(M,"Tengo un amigo que su hermano es arquitecto"),(B,"Tengo un amigo cuyo hermano es arquitecto")],
 "Cuando el nombre anterior al relativo es el poseedor. <i>Que su</i> no siempre es incorrecto: <i>Me gusta el coche que su madre le regaló</i>."),
("<i>Quien</i> con antecedente en especificativas","error",[(M,"El niño quien vino ayer lo sabía todo"),(B,"El niño que vino ayer lo sabía todo"),(B,"Juan, quien vino ayer, lo sabía todo")],
 "<i>Quien</i> no admite antecedente en relativa especificativa si no lleva preposición. En explicativas sí."),
("Duplicar el relativo","error",[(M,"Era un sitio que recordaba haberlo visto"),(B,"Era un sitio que recordaba haber visto")],
 "No deben repetirse dentro de la relativa elementos que ya aporta el relativo. Sí vale con verbos distintos: <i>algo que, si lo pruebas, te encantará</i>."),
("<i>El cual</i> frente a <i>que</i>","bien",[(B,"Tiene cuatro hijos, dos de los cuales son chicas"),(M,"Tiene cuatro hijos, dos de los que son chicas"),(B,"Vi una casa que no tenía ventanas")],
 "Con preposición son intercambiables. Pero <i>cual</i> es obligado tras cuantificador y en <i>gracias a lo cual</i>, <i>según el cual</i>; y en especificativa sin preposición hay que usar <i>que</i>."),
("<i>y</i> → <i>e</i>, <i>o</i> → <i>u</i>","error",[(M,"simpática y inteligente · uno o otro"),(B,"simpática e inteligente · uno u otro")],
 "El cambio es fónico, no gráfico: también ante <i>h</i> muda (<i>aguja e hilo</i>) y ante voces extranjeras que se leen con /i/ u /o/ (<i>carta e e-mail</i>). No cambia ante diptongo (<i>madera y hierro</i>) ni ante <i>h</i> aspirada (<i>Franco y Hitler</i>) ni ante <i>iPad</i>."),
("Doble negación","bien",[(B,"No vino nadie"),(M,"Vino nadie"),(M,"Nadie no vino")],
 "En español la doble negación no cancela el sentido negativo: es obligatoria si la palabra negativa va tras el verbo. Si va delante, no se combina con <i>no</i>."),
("Coordinar artículos","error",[(M,"los y las representantes"),(B,"los representantes y las representantes")],
 "Si hay que desdoblar, se repite el nombre. Y no se admite la arroba, la <i>e</i> ni la <i>x</i>: <i>l@s niñ@s</i>, <i>les niñes</i>, <i>lxs niñxs</i> contravienen las reglas del español."),
]))

S.append(("grafias","Grafías que se confunden","",[
("<i>porque</i> / <i>por que</i> / <i>por qué</i> / <i>porqué</i>","bien",[(B,"Lo hice porque quería (causa)"),(B,"La razón por que no puedo es esa (= por la que)"),(B,"¿Por qué haces eso? · No tienes por qué"),(B,"No entiendo el porqué (= el motivo)")],
 "Y con <i>apostar</i>, <i>brindar</i>, <i>rogar</i>, <i>esforzarse</i> valen las dos: <i>Brindaron por que / porque le fuera bien</i>."),
("<i>sino</i> / <i>si no</i>","bien",[(B,"No lo hizo Juan, sino Pedro"),(B,"No solo se lo sabe, sino que lo explica bien"),(B,"¿Quién sino Juan podía hacerlo?"),(B,"Si no lo haces tú, lo hará él")],
 "<i>Sino</i> es conjunción átona tras negación, o vale por <i>excepto</i>; también el nombre <i>sino</i> ‘destino’. <i>Si no</i> es condicional más adverbio tónico: <i>Lo hicieron cientos, si no miles, de veces</i>."),
("<i>conque</i> / <i>con que</i>","bien",[(B,"Es peligroso, conque mucho cuidado"),(B,"No me vengas con que no lo sabías"),(B,"No es ese el sentido con que se usa (= con el que)")],""),
("<i>a ver</i> / <i>haber</i>","bien",[(B,"A ver si vienes más a menudo"),(B,"A ver, ¿qué te pasa?"),(B,"Parece haber alguien"),(B,"Haberlo dicho en su momento")],""),
("<i>adonde</i> / <i>a donde</i>","ambas",[(A,"Síguele adonde vaya"),(A,"Síguele a donde vaya"),(A,"¿Adónde vas? · ¿A dónde vas?")],
 "Las dos grafías están admitidas en ambos pares."),
("<i>dondequiera</i> y compañía","bien",[(B,"Te seguiré adondequiera que vayas"),(B,"Llévale adonde quiera su madre")],
 "En una palabra cuando indican indistinción; en varias cuando los elementos conservan su significado pleno."),
]))

S.append(("espacios","Espacios que no deben partirse","Lista práctica: aquí va espacio de no separación, para que los dos elementos no queden en líneas distintas.",[
("Abreviaturas complejas","bien",[(B,"p. ej. · EE. UU. · J. L. González")],
 "Espacio fino y de no separación entre los bloques. Y punto abreviativo tras cada bloque."),
("Abreviatura y su término","bien",[(B,"D.ª Ana Ruiz · pág. 45")],""),
("Número y su término","bien",[(B,"Carlos III · 45 volúmenes")],""),
("Cifra y símbolo pospuesto","bien",[(B,"73 km · 58 € · 15 h")],"Salvo superíndices: <i>35’</i>."),
("Porcentaje en palabras","bien",[(B,"veinte por ciento")],""),
("Grupos numéricos","bien",[(B,"5 657 891")],""),
("<i>Etc.</i> al final","bien",[(B,"…comercio, etc.")],"Para que la abreviatura no quede sola en su línea."),
]))

S.append(("dialogos","Diálogos","",[
("Toda intervención cierra con punto","bien",[(B,"—Hola.")],"Aunque sea brevísima."),
("Comentario del narrador","bien",[(B,"—Hola —saludó Juan."),(B,"—Bien —contestó Juan—. ¿Tú?"),(B,"—Hola, Silvia —dijo Juan—, ¿qué tal?")],
 "La raya va pegada al comentario. Si la intervención sigue, el comentario se cierra con raya y el signo que corresponda. Coma, punto y coma y dos puntos van tras la segunda raya."),
("Narrador con verbo de lengua","bien",[(B,"—¿Estás contenta? —quiso saber Juan."),(B,"—Hola, Silvia. —Juan se ruborizó—. ¿Qué tal?")],
 "Si el comentario lleva verbo de habla o describe cómo lo dice, el punto va después. Si es un enunciado independiente, el punto va delante."),
("Diálogo dentro de párrafo","bien",[(B,"«Hola», dijo Juan"),(B,"«Hola, Silvia —dijo Juan—. ¿Qué tal?»")],
 "Entre comillas, con el comentario separado por coma. Si la intervención sigue, el comentario va entre rayas sin cerrar las comillas."),
]))

VER={'error':('v-err','error'),'ambas':('v-amb','ambas válidas'),'depende':('v-dep','depende'),'bien':('v-ok','así es')}
MK={'mal':('e-mal','mal'),'bien':('e-bien','bien'),'ambas':('e-amb','vale')}

def render():
    toc=[]; body=[]
    for sid,titulo,intro,reglas in S:
        toc.append('<a href="#%s"><span class="tn">%s</span>%s</a>'%(sid,len(reglas),titulo))
        r=[]
        for t,ver,ejs,nota in reglas:
            vc,vl=VER[ver]
            lineas=''.join('<div class="ej %s"><span class="mk">%s</span><span class="tx">%s</span></div>'
                           %(MK[m][0],MK[m][1],e) for m,e in ejs)
            n='<p class="nota">%s</p>'%nota if nota else ''
            r.append('<article class="regla"><header class="rh"><h3>%s</h3><span class="chip %s">%s</span></header>'
                     '<div class="ejs">%s</div>%s</article>'%(t,vc,vl,lineas,n))
        ib='<p class="sec-intro">%s</p>'%intro if intro else ''
        body.append('<section id="%s"><h2>%s</h2>%s<div class="reglas">%s</div></section>'
                    %(sid,titulo,ib,''.join(r)))
    t=io.open('tpl-manual.html',encoding='utf-8').read()
    t=t.replace('{{TOC}}',''.join(toc)).replace('{{BODY}}',''.join(body))
    t=t.replace('{{NREGLAS}}',str(sum(len(x[3]) for x in S))).replace('{{NSEC}}',str(len(S)))
    io.open('manual-de-dudas.html','w',encoding='utf-8').write(t)
    print('reglas:',sum(len(x[3]) for x in S),'| secciones:',len(S))
render()
