"""
            /////// Semana 1 ///////

Día 1 (¿Qué es la CiberSeguridad y qué es un SOC?)

¿Qué es Ciberseguridad?
R= La ciberseguridad es la práctica de proteger equipos, redes, aplicaciones de software, sistemas críticos
y datos frente a amenazas digitales.

¿Qué es un SOC?
R= Un SOC, Security Operations Center o un Centro De Operaciones De Seguridad (COS)
es una unidad centralizada que se encarga de supervisar, analizar y responder a amenazas de ciberseguridad
en tiempo real.

¿Qué hace un SOC Analyst?
R= Un Analista SOC, es un profesional de la ciberseguridad que monitorea, detecta, investiga y responde a
incidentes de seguridad en la infraestructura de TI de una organización, actuando como la primera línea de
defensa contra amenazas cibernéticas.

Palabras en Inglés: Security, Attack, Network, System, Analyst

Día 2 (Redes Básicas 1)

¿Qué es Internet?
R= Internet es una Red Global Descentralizada De Computadoras Y Dispositivos Interconectados que permite
el intercambio de información, servicios y recursos en tiempo real a través de protocolos estandarizados,
principalmente TCP/IP.

¿Qué es una IP?
R= Una IP Internet Protocol o Protocolo De Internet, es un identificador único asignado a cada dispositivo
conectado a una red, ya sea a internet o a una red local. Funciona como una etiqueta numérica que permite la
comunicación entre dispositivos, facilitando el envío y recepción de datos a través de internet.

¿Qué es un puerto?
R= Un puerto de red es una interfaz virtual en un dispositivo, como un ordenador o servidor, que permite
la comunicación y el intercambio de datos a través de una red. Es un número único, que actúa como un punto
de entrada y salida para el tráfico de red.
Los puertos se numeran desde 0 hasta 65535 y se dividen en categorías como puertos bien conocidos (0-1023),
registrados (1024-49151) y dinámicos o privados (49152-65535), cada uno con funciones específicas en la gestión
de servicios como Web, Correo Electrónico o transferencia de archivos.
Cabe aclarar que los ataques entran por los puertos.

Palabras en Inglés: Internet, IP Address, Port

Día 3 (Redes Básicas 2)

¿Qué es HTTP?
R= HTTP que significa Protocolo De Transferencia De Hipertexto o HyperText Transfer Protocol es un protocolo
de transferencia de comunicación, que permite las transferencias de información a través de archivos (XML, HTML)
en la World Wide Web (WWW), como también servidores web. Utiliza el puerto 80 para comunicarse con el servidor
o web, a lo que no es seguro.

¿Qué es HTTPS?
R= HTTPS que significa Protocolo De Transferencia De Hipertexto Seguro o HyperText Transfer Protocol Secure
es una versión segura del protocolo HTTP que utiliza cifrado SSL/TLS para proteger la comunicación entre un
navegador web y un sitio web. HTTPS cifra la información enviada, utilizando el puerto predeterminado 443
lo que la hace más segura.

¿Cuál es la diferencía entre HTTP y HTTPS?
R= La diferencia entre http y https, radica en la seguridad de la transferencia de datos, como son contraseñas,
números de tarjetas de crédito, o datos personales. Ya que HTTP actúa en texto plano, sin cifrar, por el
contrarío a HTTPS que añade una capa de seguridad, utilizando el cifrado SSL/TLS.

Palabras en Inglés: Web, Secure, Data, Encrypted

Día 4 (Linux Básico)

¿Qué es Linux?
R= GNU/Linux es una familia de Sistemas Operativos tipo Unix de Código Abierto y Multiplataforma, desarrollado
originalmente por Linus Torvalds en 1991 como un núcleo (kernel) para sistemas operativos tipo Unix.
GNU/Linux es gratuito, libre y puede ser utilizado, modificado y redistribuido por cualquier persona bajó la
licencia de GPL de GNU.

¿Para qué se utiliza Linux?
R= Se utiliza para una gran variedad de propósitos, como: Servidores Web, Base de Datos, Desarrollo de Software,
Ciberseguridad, Sistemas Embebidos(Routers Inalámbricos, Camaras de Seguridad, Altavoces Inteligentes,
Televisores Inteligentes, Relojes Inteligentes y Dispositivos Médicos, como Electrocardiograma) debido a su
versatilidad, estabilidad y seguridad. Linux es el Sistema Operativo Subyacente de Android.

Palabras en Inglés: Linux, Command, File

Día 5 (Logs)

¿Qué son los Logs?
R= Los Logs, también conocidos como archivos de registro o bitácoras, son registros secuenciales y cronológicos
de eventos, acciones o procesos que ocurren en un sistema informático, aplicación, servidor o dispositivo.
Estos registros contienen información detallada sobre lo que sucede durante la operación de un sistema,
incluyendo fechas, horas, tipos de eventos y mensajes descriptivos.

¿Para qué sirven los Logs?
R= Su principal función es proporcionar una evidencia detallada del comportamiento del sistema, lo que permite
a los profesionales de TI comprender cómo se está ejecutando el software y detectar cualquier anomalía. Sus
usos más importantes son el diagnóstico de problemas, ya que permiten identificar errores, fallos o transacciones
fallidas, facilitando la resolución rápida de incidentes.

Ejemplos de Logs:
R= Un Log es un archivo que registra eventos, actividades o mensajes generados por un sistema, aplicación o
servicio, permitiendo su análisis para diagnóstico, seguridad o auditoria.

Log de Sistema En Linux: Un archivo común es /var/log/auth.log

Log de Servidor Web(Apache): Un Log de acceso Apache es 84.245.59.290 – – [01/Oct/2018:08:39:04 +0200]
"GET /module/CLNEWMSG/css/bubble.css?1251290622 HTTP/1.1" 304 136 "https://www.axarnet.es/alojamiento-web-linux/"
"Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0"

Log de Aplicación(Spring Boot): Un Log común es 2022-02-17 21:28:55.018 INFO 22308 --- [ restartedMain]
org.apache.catalina.core.StandardEngine : Starting Servlet engine: [Apache Tomcat/9.0.30]

Log de flujo en AWS VPC: Un Log de flujo que muestra tráfico aceptado es 2 123456789010 eni-1235b8ca123456789
172.31.16.139 172.31.16.21 20641 22 6 20 4249 1418530010 1418530070 ACCEPT OK

log de aplicación Node.js(Winston): Un Log en formato JSON es {"level":"info","message":"El cliente José Saavedra
compró un estante de ébano"}

Palabras en Inglés: Log, Event, Activity

Día 6 (Phishing)

¿Qué es Phishing?
R= El Phishing es una técnica de Ingeniería Social utilizada por Ciberdelincuentes para engañar a las victímas
haciéndose pasar por entidades de confianza, como bancos, redes sociales, empresas o instituciones públicas, con
el fin de robar información personal, credenciales de acceso, datos bancarios o instalar malware en sus dispositivos.
También ocurre a través de Mensajes de Texto(SMishing), llamadas telefónicas(Vishing) o publicaciones en redes sociales.
Aunque también existe el Phishing dirigido(Spearphishing) se enfoca en una persona o pequeña organización
especifíca. Y el Whaling es una variante del Spearphishing que se dirige a ejecutivos de alto nivel.

¿Cómo se ve el Phishing?
R= El Phishing se presenta como mensajes fraudulentos que imitan a fuentes confiables, como bancos, compañías de
tarjetas de crédito o servicios en línea.
Recibir un mensaje que informa de una compra sospechosa con la tarjeta de crédito, seguido de una solicitud
para llamar a un número falso que supuestamente pertenece al banco.

¿Por qué funciona el Phishing?
R= El Phishing funciona principalmente porque explota la psicología humana y las emociones, como el miedo,
la urgencia o la vanidad, para manipular a las victímas y hacer que realicen acciones que no deberían realizar.

Palabras en Inglés: Email, Fake, Password

         ////// Semana 2 //////////

Día 1 (Pensar como Analista SOC)

Entrar a Logs: cd var/log/, después ls, y al final sudo less auth.log
El comando "less", es para lectura segura de Logs, sin modificar y sin cargar todo.
El comando "pwd", es para ver en que ruta estas
El comando "ls", es para ver la lista y "ls -i" es para ver la lista detallada.

Palabras en Inglés:" Failed, Accepted, Login, Session.

Día 2 (Comportamiento normal o raro)
Aprender a diferenciar lo normal de lo raro. No todo lo raro es ataqu. Pero todo ataque, empieza viéndose raro.

Palabras en Inglés: Error, Warning, Process, System.

Día 3 (Intentos de acceso y fuerza bruta(CONCEPTO))
Un ataque de fuerza bruta no es un evento, es muchos intentos fallidos en poco tiempo.
UN ATAQUE NO ES UN INTENTO, ES UN PATRON.

Palabras en Inglés: Failed, Invalid, User, Authentication.

Día 4 (¿Qué es una alerta y de dónde sale?)
Una alerta NO es un ataque. Es una señal de que algo merece atención.

Evento → Log → Regla → Alerta → Analista

Palabras en Inglés: Alert, Event, Rule, Suspicious.

Día 5 (¿Qué hace un SOC con una Alerta?)
Alerta → Revisión → Contexto → Decisión → Acción   Eso es el corazón del SOC

El SOC no improvisa, sigue procesos - Analizar, Detectar, Accionar, Bloquear.

Palabras en Inglés: Review, Context, Decision, Action

Día 6 (REPASO INTEGRADO (PENSAMIENTO SOC))
Una alerta, no es un ataque confirmado. Viene de Logs(auth.log)

Cantidad de Intentos → Tiempo → Usuario → Horario
¿Normal? → ¿Error de usuario? → ¿Automatizado?
¿Cerrar? → ¿Observar? → ¿Escalar?

Palabras en Inglés: Alert, Review, Suspicious, Incident.

          ////////// Semana 3 //////////

Día 1 (¿Qué es un INCIDENTE de seguridad?)
Aprender a diferenciar EVENTO, ALERTA E INCIDENTE.

Regla de ORO SOC:
Evento = Login fallido
Alerta = 20 Logins fallidos
Incidente = Acceso no autorizado confirmado

NO TODO INCIDENTE EMPIEZA COMO ALERTA
NO TODA LA ALERTA TERMINA EN INCIDENTE

"Un SOC no persigue ataques, protege procesos."

Día 2 (Tipos de INCIDENTES reales(los que si dan trabajo))
Aprender a reconocer incidentes comunes y no confundirlos con ruido.

1-. Accesos no Autorizados
- Login exitoso fuera de horario
- IP desconocida
- Usuario no habitual

2-. Fuerza bruta
- Muchos intentos fallidos
- Mismo usuario o IP
- Corto intervalo de tiempo

3-. Phishing
- Usuario hace clic
- Credenciales Comprometidas
- Actividad rara posterior

4-. Malware(Básico)
- Proceso extraño
- Conexiones externas raras
- Alertas repetidas

¿Quién?, ¿Cuándo?, ¿Desde dónde?, ¿Cuántas veces?, ¿Es normal para este sistema?

Día 3 (Severidad y Clasificación de Incidentes)
Aprende qué tan grave es algo, no solo qué pasó.

¿Qué es la Severidad? R= Qué tanto impacto tiene un incidente.

Niveles típicos de Severidad
Baja: Informativo, Sin Impacto, No Requiere acción inmediata. Intentos fallidos aislados.
Media: Sospechosos, Puede escalar, Se Monjtorea. Fuerza bruta sin éxito.
Alta: Confirmado, Impacto Real, Acción Inmediata. Acceso no autorizado exitoso.

En SOC: Si todo es crítico, nada lo es.

Día 4 (Documentación de Incidentes(mentalidad profesional))
Aprender cómo pensar y escribir como analista SOC, auqnue aún no uses herramientas reales.

¿Por qué documentar? R= Si no está documentado, no pasó.
La documentación sirve para:
Continuidad del turno, Auditorías, Aprender de Incidentes, Protegerte como Analista

Estructura Básica De Un Reporte
1-. ¿Qué Pasó?R= Evento observado, tipo de alerta
2-. Evidencia: Logs,Horas,IPS,Usuarios
3-. Análisis: ¿Por qué es sospechoso? , ¿Qué patrón sigue?
4-. Impacto: Bajo/Medio/Alto, Sistemas o datos Afectados
5-. Acción tomada: Cerrado, Observado, Escalado

En SOC: Primero evidencia > luego análisis > luego decisión

Día 5 (Correlación básica (pensar como SOC real))
Aprender a unir eventos separados para ver un solo incidente

¿Qué es correlación?R= Correlación = unir piezas
SOC no ve logs aislados, ve secuencias.

¿Cómo correlacionar sin SIEM?R= ¿Mismo Usuario?, ¿Misma IP?, ¿Mismo horario?, ¿Misma máquina?
Si varías respuestas son si > Correlación

/////// NO TODO EVENTO ES ALERTA /////////
/////// NO TODA ALERTA ES INCIDENTE /////////
/////// Y NO TODO INCIDENTE EMPIEZA COMO ALERTA /////



"""