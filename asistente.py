import speech_recognition as sr
import subprocess as sub
import pyautogui as auto
import pyttsx3 as voz
from time import sleep
from datetime import datetime

def speack(audio):
    edit = voz.init()
    edit.setProperty('rate', 150)
    edit.setProperty('voice', 'TTS_MS_ES-MX_SABINA_11.0') # voz con acento mexicano
    edit.say(audio)
    edit.runAndWait()

def interpretar(comando_de_audio):
    recuerdaTexto =  comando_de_audio
    comando_de_audio = comando_de_audio.split(' ')
    #print(type(dato))
    ver_video = ('vídeo' or 'video') in comando_de_audio
    escribir = ('escribir' or 'texto') in comando_de_audio
    finaliza = ('finaliza' or 'finalizar') in comando_de_audio
    hora = ('hora') in comando_de_audio
    recuerda = ('recuerda') in comando_de_audio
    nota = ('notas' or 'nota') in comando_de_audio
    abrir = ('react' or 'curso') in comando_de_audio

    #print(type(vd))
    if ver_video is True:
        abrir_youtube()
    elif escribir is True:
        abrir_blocNotas()
    elif finaliza is True:
        finalizar()
    elif hora is True:
        time()
    elif recuerda is True:
        recuerda_esto(recuerdaTexto)
    elif nota is True:
        notas()
    elif abrir is True:
        abir_curso()
    else:
        speack('No me programaste para hacer esa tarea')



def abrir_blocNotas():
    speack('Espera un momento')
    sub.call('start notepad.exe', shell=True)
    sleep(1.5)
    auto.write('¡Listo! empieza a escribir tu texto Oscar')
    speack('¡Listo! empieza a escribir tu texto Oscar')


def abrir_youtube():
    speack('Espera un momento')
    sub.call([r'E:/edit/navegar.bat'])
    return None

def recuerda_esto(texto):
    f = open ('record.txt','w')
    f.write(texto)
    f.close()
    sleep(1.5)
    speack('El recordatorio se guardo correctamente')


def notas():
    speack('Espera un momento')
    f = open ('record.txt', 'r')
    speack(f.read())

def finalizar():
    print('finalizar')
    quit()
    

def time():
    speack('Espera un momento')
    formatoHora = "%H:%M:%S"
    hoy = datetime.today()
    Time = hoy.strftime(formatoHora) 
    speack('La hora actual es')
    print(Time)
    speack(Time)

def abir_curso():
    speack('Espera un momento')
    sub.call([r'E:/edit/curso.bat'])
    sleep(1.5)
    speack('Listo puedes continuar. y no lo olvides ¡Nunca dejes de aprender!')
    return None

speack("¡Hola Oscar! soy Edit en que te puedo ayudar el día de hoy")
while True:
  
    # escuchar el audio con el micrófono de mi computadora
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("¡Ordena!")
        audio = r.listen(source)


    try:
        # Si se entendió el audio
        comando = r.recognize_google(audio, language='es-EC')
        print("Creo que dijiste: " + comando)
        speack("Creo que dijiste: " + comando)
        interpretar(comando)  # lo que se debe hacer con el comando de audio

    except sr.UnknownValueError:
        # si no se entendió
        print("No te pude entender")

    except sr.RequestError as e:
        # si no se tiene conexión a internet o al servicio de google
        print("No pude obtener respuesta del servicio de Google Speech Recognition; {0}".format(e))

sys.exit()