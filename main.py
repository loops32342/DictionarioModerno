word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "WTH":"Que diablos?",
            "TYSM":"Muchas gracias",
            "BRAINROT":"Contenido generado por IA que afecta a tu cerebro.Un ejemplo:Italian brainrot",
            "Aura":"Mucho carisma,mucha habilidad",
            "Skill issue":"Falta de habilidad"
            }
if word in meme_dict.keys():
    print("Palabra encontrada:",meme_dict[word])
    
else:
    print("Lo sentimos su palabra",word,"no ha sido encontrada")
