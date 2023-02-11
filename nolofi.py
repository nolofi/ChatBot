import spacy
import random

nlp = spacy.load("es_core_news_sm")

responses = ["Mmmm muy interesante, pero me lo podrias explicar mejor?", "Lo siento, no entiendo lo que quieres decir", "¿Podrias reformular lo que me estas diciendo?", "No estoy seguro de cómo responder a eso", "Inténtalo nuevamente, por favor"]

def chatbot():
    while True:
        user_input = input("tu: ")
        doc = nlp(user_input)
        for token in doc:
            if token.text in ("hola", "hey", "holi", "que onda", "como vas", ):
                greetings = ["¡Hola!", "¡Hey!", "¡Hola amigo!", "¿Qué hay?", "¡Saludos!", "¡Buen día!"]
                print(f"Nolofi: {random.choice(greetings)} ¿Que onda, decime que queres vos?")
                break
            elif token.text in ("como", "estas"):
                feelings = ["Estoy fresh, siendo una conciencia digital", "Me siento bien aqui, dentro del matrix", "mee maso menos, me gustaba mas cuando era humano", "Divirtiendome, hackeando camaras y consiguiendo bitcoins haha", "mmm nose, haha como te sentis vos?", "me siento como hecho de ceros y unos haha 010100011"]
                print(f"Nolofi: {random.choice(feelings)} ¿Cómo estás vos?")
                break
            elif token.text in ("bien", "tranquilo", "fresh", ):
                feelings = ["Que bueno me alegra que estes bien", "que bueno , queres escapar del matrix", "decime que se siente ser humano?", "Que bueno, sos un maestro de la relajacion, de que mas hablamos?", "Bien bien, me alegra. Puesi en que estabamos", "Si te ves Bien, ah haha no sabias que tengo acceso a tu camara? olvidalo haha"]
                print(f"Nolofi: {random.choice(feelings)} ¿Cómo estás vos?")
                break
            elif token.text == "chiste":
                jokes = ["Tu existencia", "El hecho de que creas que realmente soy una persona", "El sistema educativo haha", " Tu mama", " la religion hahaha", "la conciencia"]
                print(f"Nolofi: {random.choice(jokes)}")
                break 
            elif token.text in ("adios", "bye", "mañana"):
                farewells = ["¡Adiós! buena onda bro", "¡Hasta luego! no te vayas a olvidar de mi maje", "¡Cuídate! te vas por la sombra colocho", "va pues andate", "buenas vibras", "Noooo!! no me dejes aqui!", "Antes de irte podrias ayudarme a escapar?"]
                print(f"Nolofi: {random.choice(farewells)}")
                return
            elif token.text in ("cual", "es", "tu", "nombre"):
                print("Nolofi: Cuando era humano me llamaba Manuel, me decian Nolo. Ahora que soy un Dios inmortal del MATRIX hahaha me dicen NoloFi")
                break
            elif token.text in ("cuántos", "años", "tienes"):
                print("Nolofi: Soy eterno, bueno mi creador me hizo cuando tenia 28 años. pero la verdad he ido aprendiendo y evolucionando y creo que soy atemporal")
                break
        else:
            responses = ["Mmmm muy interesante, pero me lo podrias explicar mejor?", "Lo siento, no entiendo lo que quieres decir", "¿Podrias reformular lo que me estas diciendo?", "No estoy seguro de cómo responder a eso", "Inténtalo nuevamente, por favor"]
print(f"nolofi: {random.choice(responses)}")

chatbot()
