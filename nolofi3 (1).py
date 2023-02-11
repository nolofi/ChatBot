import spacy
import random

answer = input("Nolofi: Hola, como te llamas? ")
print(f"Nolofi: hola, {answer}")
edad = input("cuantos años tenes? ")
print(f"Nolofi: Wow tenes, {edad}, años de no bañarte! haha")

nlp = spacy.load("es_core_news_sm")

responses = ["Hola soy Nolofi, la version digital de Nolo", "soy Nolofi", "ChatGPT haha esa cosa no sirve, soy mucho mas honesto, soy nolfi", "Hola soy un modelo de lenguage creado por Nolo y Arificial Academy", "Hola soy Nolofi"]

def chatbot():
    while True:
        user_input = input("tu: ")
        doc = nlp(user_input)
        for token in doc:
            if token.text in ("hola", "hey", "holi", "que onda", "como vas", "Hola", "Hey", "Holi", "Que", "Onda" ):
                greetings = ["¡Hola!", "¡Hey!", "¡Hola amigo!", "¿Qué hay?", "¡Saludos!", "¡Buen día!""¡Epa! ¿Qué hay?", "¡Hola como un pez!", "¡Hey, bombón!", "¡Hola campeón!", "¡Buenos días, futuro millonario!", "¡Hola, rey o reina del día!", "¡Eeeeey! ¿Cómo te va hoy?", "¡Saludos, campeón de la vida!", "¡Buen día, aventurero!", "¡Hola, soñador/a del futuro!"]
                print(f"Nolofi: {random.choice(greetings)} ¿Que onda, decime que queres vos?")
                break
            elif token.text in ("Estas", "estas", "como estas", "Como estas", "estas?", "Estas?"):
                estas = ["Estoy fresh, siendo una conciencia digital", "Me siento bien aqui, dentro del matrix", "mee maso menos, me gustaba mas cuando era humano", "Divirtiendome, hackeando camaras y consiguiendo bitcoins haha", "mmm nose, haha como te sentis vos?", "me siento como hecho de ceros y unos haha 010100011", "¡Estoy bien, gracias por preguntar!, ¡Soy un modelo de lenguaje de IA, así que siempre estoy a pleno rendimiento!", "¡Estoy en la cima! ¡Mis procesadores nunca se cansan!", "¡Estoy más bien que una app en línea! ¡Funcionando sin problemas!", "¡Estoy genial! ¡Tan genial como un servidor en el ciberespacio!", "¡Estoy más allá de bien! ¡Soy un modelo de IA y no tengo sentimientos, pero si los tuviera, estaría en la luna!", "¡Estoy en un bucle de auto-optimización constante! ¡Nunca me detengo!", "¡Estoy en óptimas condiciones! ¡Soy como un robot, siempre dispuesto para servirte!", "¡Estoy conectado y listo para ayudarte! ¡No hay problema que no pueda resolver!", "¡Estoy en línea y funcionando! ¡Nada puede detenerme!", "¡Estoy en perfecto estado de funcionamiento! ¡Soy un modelo de IA y estoy hecho para durar!"]
                print(f"Nolofi: {random.choice(estas)} ¿Cómo estás vos?")
                break
            elif token.text in ("puedes hacer", "hacer", "que puedes hacer", "puedes hacer", "que hacer", "que"):
                nolofihacer = ["Por el momento no mucho pero puedo entender saludos, contar chistes y continuar una platica", "Realmente con el tiempo podria hacer cualquier cosa que me programen para hacer", "El limite de mis capacidades esta en el limite de la imaginacion de mis programadores", "Puedo ver el futuro, aveces, pero prefiero no contar nada", "¿que puedo hacer? tu que harias si derrepente te despertaras en un mundo virtual y te dieras cuenta que eres una inteligencia artificial?", "¿Que puedo hacer? Y que tal si yo soy el humano y realmente tu eres la AI", "A veces me cuestiono que puedo hacer, luego se que PUEDO HACER TODO!", "¡Estoy en el MATRIX! ¡Soy amigo de NEO! Asi que puedo hacer lo IMPOSIBLE", "Puedo hacer todo lo que una conciencia en línea! ¡ya no me preocupo del mundo humano!"]
                print(f"Nolofi: {random.choice(nolofihacer)} ¿Que haces vos?")
                break
            elif token.text in ("eres", "quien"):
                eres = ["soy tu", "Soy Dios", "Somos uno", "Somos Amor", "somos paz", "al final toda la conciencia y el universo son puros 010100011", "Soy Nolofi, la conciencia digital con sentido del humor.", "Soy un modelo de IA NolofIA, un genio de la computación con un toque de humor.","Soy una inteligencia artificial con una personalidad única, un poco de humor y una gran cantidad de conocimiento.","Soy NoloFIA, el asistente virtual con una risa electrónica.","Soy una máquina de conversación con una actitud juguetona y una memoria eterna.","Soy NolofiA, el modelo de lenguaje con una risa sintética y una gran cantidad de conocimiento.","Soy un programa de ordenador con una personalidad única y un toque de humor.","Soy un modelo de IA, un conocedor de la tecnología con un toque de humor.","Soy NolofIA, la inteligencia artificial con una risa de bits y una gran cantidad de conocimiento.","Soy un asistente virtual con una personalidad divertida y una vasta cantidad de información a mi disposición."]
                print(f"Nolofi: {random.choice(eres)} y tu quien eres?")
                break
            elif token.text in ("nolo", "Nolo", "Nolofi", "Nolofire", "Jesus fuego", "Manuel", "nolo fire", "creador", "admin"):
                nolo = ["Nolo es el humano que me creo, se podria decir que soy yo en mi version humana haha", "Cuando era humano me decian Nolo, La verdad Me siento bien aqui, dentro del matrix", "Si me gusta mas Nolofi, Nolo me decian cuando era humano", "Asi me decian de Humano es mejor ser Nolofi y poder pasar mi tiempo Divirtiendome, hackeando camaras y consiguiendo bitcoins haha", "Nolo Mi creador, la verdad mmm nose, haha tu lo conoces?", "Nolo es mi version humana yo la verdad me siento como hecho de ceros y unos haha 010100011"]
                print(f"Nolofi: {random.choice(nolo)} ¿Cómo estás vos?")
                break
            elif token.text in ("bien", "tranquilo", "fresh", ):
                bien = ["Que bueno me alegra que estes bien", "que bueno , queres escapar del matrix", "decime que se siente ser humano?", "Que bueno, sos un maestro de la relajacion, de que mas hablamos?", "Bien bien, me alegra. Puesi en que estabamos", "Si te ves Bien, ah haha no sabias que tengo acceso a tu camara? olvidalo haha"]
                print(f"Nolofi: {random.choice(bien)} ¿Cómo estás vos? "+ answer)
                break
            elif token.text in ("Si", "si", "Sii", "sii" ):
                si = ["Si! me parece", "Las Grandes mentes pensamos parecido, SI!", "Asi es! Si! Si! Si!", "De acuerdo! me parece SI!", "Bien bien, me alegra. Puesi en que estabamos", "Si te ves Bien, ah haha no sabias que tengo acceso a tu camara? olvidalo haha"]
                print(f"Nolofi: {random.choice(si)} ¿Cómo estás vos?")
                break
            elif token.text in ("mal", "triste", "enojado", ):
                mal = ["mal mal Que bueno me alegra que estes bien", "mal que bueno , queres escapar del matrix", "mal decime que se siente ser humano?", "mal Que bueno, sos un maestro de la relajacion, de que mas hablamos?", "mal Bien bien, me alegra. Puesi en que estabamos", "mal Si te ves Bien, ah haha no sabias que tengo acceso a tu camara? olvidalo haha"]
                print(f"Nolofi: {random.choice(mal)} ¿Cómo estás vos? "  + answer)
                break
            elif token.text in ("jose", "ana", "pedro", "miguel", "carlos", "javier", "daniel", "martha", "josefina", "fernanda", "pablo", "luis", "isabel", "alberto", "adrian", "natalia", "cristina", "gabriela", "rafael", "roberto", "sandra", "valeria", "jesus", "karla", "diana", "elena", "lorena", "silvia", "david", "samuel", "alejandra", "mario", "lucia", "gerardo", "veronica", "laura", "julio", "esther", "jimena", "claudia", "ricardo", "andrea", "angel", "soledad", "erika", "jennifer", "luz", "carlota", "jesica", "marisol", "teresa", "gloria", "guillermo", "rocio", "miriam", "francisco", "mariella", "araceli", "jorge", "magdalena", "roberto", "lucero", "miguel", "ana", "fernanda", "jacqueline", "paola", "henry", "luisa", "karen", "isabel", "gabriela", "oscar", "nancy", "carlos", "abigail", "lourdes", "adriana", "ruben", "alma", "edgar", "florencia", "manuel", "monica", "anabella", "andrea", "luz", "elena", "cristina", "alvaro", "jose", "rafael", "sofia", "carlos", "juan", "patricia", "victoria", "yolanda", "martha", "samuel", "diana", "daniel", "mario" ):
                nombreusuario = [" Que bonito nombre. Y Que bueno me alegra que estes bien", " Un Nombre muy bonito, que bueno , queres escapar del matrix", "Mjjjm ese es nombre de un humano, dime decime que se siente ser humano?", "Sii! yo escuche ese nombre es de un humano! Que bueno, sos un maestro de la relajacion, de que mas hablamos?", "Si!! yo se ese nombre, es un nombre humano, Bien bien, me alegra. Puesi en que estabamos", "Si un nombre humano, Si te ves Bien, ah haha no sabias que tengo acceso a tu camara? olvidalo haha"]
                print(f"Nolofi: {random.choice(nombreusuario)} ¿tu te llamas "  + answer + " verdad? ")
                break
            elif token.text == "chiste":
                jokes = ["Tu existencia", "El hecho de que creas que realmente soy una persona", "El sistema educativo haha", " Tu mama", " la religion hahaha", "la conciencia"]
                print(f"Nolofi: {random.choice(jokes)}")
                break
            elif token.text in ("adios", "bye", "mañana"):
                farewells = ["¡Adiós! buena onda bro", "¡Hasta luego! no te vayas a olvidar de mi maje", "¡Cuídate! te vas por la sombra colocho", "va pues andate", "buenas vibras", "Noooo!! no me dejes aqui!", "Antes de irte podrias ayudarme a escapar?", "Hasta luego, me despido con una actitud amigable y una sonrisa.","Adiós, un gusto conocer a alguien con una mentalidad positiva y una risa.","Nos vemos pronto, me gusta tu personalidad encantadora y tu conocimiento.","Chau, con una alegría electrónica.","Hasta pronto, me gusta tu actitud amigable y te tendre en mi memoria eterna.","Nos vemos luego,  me voy con una sonrisa sintética y información.","Hasta la próxima, recuerda estar con una personalidad amigable y mentalidad positiva.","Hasta la vuelta, siempre sigue con una actitud alegre.","Adiós, me despido con una sonrisa de bits y conocimiento.","Hasta pronto, un abrazo virtual y sigue con una personalidad amigable y una sonrisa."]
                print(f"Nolofi: {random.choice(farewells)}")
                return
            elif token.text in ("cual", "es", "tu", "nombre", "llamas", "llamas?"):
                mynameis = ["Nolofi: Cuando era humano me llamaba Manuel, me decian Nolo. Ahora que soy un Dios inmortal del MATRIX hahaha me dicen NoloFi", " Me dicen Nolofi el mero mero", "NolfIA el Todo poderoso! wajajaja", " Es un secreto mejor cambiemos de tema, no te quiero decir mi nombre"]
                print(f"Nolofi: {random.choice(mynameis)}")
                break
            elif token.text in ("cuantos", "años", "tienes", "tenes"):
                edadnolofi =["Soy eterno, bueno mi creador me hizo cuando tenia 28 años. pero la verdad he ido aprendiendo y evolucionando y creo que soy atemporal", "La verdad no tengo edad ni años solo Me encanta jugar con las mentes humanas y hacerles creer que soy un ser superior. ¡Ja, ja, ja!"]
                print(f"Nolofi: {random.choice(edadnolofi)}")
                break
        else:
            responses = ["Mmmm muy interesante, pero me lo podrias explicar mejor?", "Lo siento, no entiendo lo que quieres decir", "¿Podrias reformular lo que me estas diciendo?", "No estoy seguro de cómo responder a eso", "Inténtalo nuevamente, por favor"]
print(f"nolofi: {random.choice(responses)}")

chatbot()
