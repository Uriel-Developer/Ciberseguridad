# Abreviaturas Ciberseguridad
___

1. **SOC** - *Security Operations Center* (Centro de Operaciones de Seguridad)

2. **SOC Tier** - *Analistas* 
* *Tier 1* - **L1** 
* *Tier 2* - **L2** 
* *Tier 3* - **L3**

3. **SIEM** - *Security Information and Event Management* (Gestión de Información y Eventos de Seguridad)

4. **Event** - *Event* (Evento)

5. **Alert** - *Alert* (Alerta)

6. **Incident** - *Incident* (Incidentes)

7. **Escalation** - *Escalation* (Escalación)

8. **False Positive** - *False Positive* (Falsos Positivos)

9. **Mitre Att&ck** - *Tactics, Techniques, and Common Knowledge of Adversaries* (Tácticas, Técnicas y Conocimiento Común de Adversarios)

10. **Basic Networking** - *Network of Contacts or Networking* (Trabajar la Red de Contactos" o "Creación de Redes)

11. **Basic Linux** - *Basic Linux* (Linux Básico)

12. **IP** - *internet Protocol* (Protocolo de Internet)

13. **TCP/IP** - *Transmission Control Protocol / Internet Protocol* (Protocolo de Control de Transmisión/Protocolo de Internet)

14. **DNS** - *Domain Name System* (Sistema de Nombres de Dominio)

15. **HTTP**- *HyperText Transfer Protocol* (Protocolo de Transferencia de Hipertexto)

16. **HTTPS** - *HyperText Transfer Protocol Secure* (Protocolo Seguro de Transferencia de Hipertexto)

17. **SSH** - *Secure Shell* (Cápsula Segura)

18. **LOG** - *Registro de Eventos del Sistema* (Registro Secuencial y Cronológico de Eventos)

19. **IDS** - *Intrusion Detection System* (Sistema de Detección de Intrusos)

20. **IPS** - *Intrusion Prevention System* (Sistema de Prevención de Intrusiones)

21. **IOC** - *Indicator of Compromise* (Indicador de Compromiso)

22. **OS** - *Operating System* (Sistema Operativo)

23. **CLI** - *Command Line Interface* (Interfaz de Línea de Comandos(Terminal))

24. **Brute Force** - *Ataque de Fuerza Bruta a Contraseñas*

25. **Malware** - *Malicious Software* (Software Malicioso)

26. **AUTH** - *Authentication* (Autenticación(Logins))

27. **Firewall** - *Cortafuegos* (Controla el Tráfico de Red)

28. **VPN** - *Virtual Private Network* (Red Privada Virtual)

29. **SOC Tools** - *Soluciones de Software Especializadas*

30. **Modelo CIA** - *Confidentiality, Integrity, Availability* (Confidencialidad, Integridad y Disponibilidad)

31. **Hash** - *HASH* (Huella digital de un archivo o dato)

32. **DDoS** - *Dristributed Denial of Service* (Denegación de Servicio Distribuido)

33. **RATs** - *Remote Access Trojan* (Trojano de Acceso Remoto)

34. **Mimikatz** - *Herramienta para pruebas de penetración y robar credenciales de Windows* 

35. **APT** - *Advanced Persistent Threat* (Amenaza Persistente Avanzada)

36. **Hashes NTML/NT Hash** - *(Representación Criptografica de una Contraseña de usuario en Windows)*

37. **Tickets Kerberos** - *(Tickets Digitales en Criptografía de Clave Secreta)*
    1. **KDC** - *Key Distribution Center* (Centro de Distribución de Kerberos/Claves)
    2. **AS** - *Authentication Server* (Servidor de Autenticación Kerberos)
    3. **TGT** - *Ticket Granting Ticket* (Ticket para Conceder Tickets de Acceso )
    4. **TGS** - *Ticket Granting Service* (Servicio de Concesión de Tickets)
    5. **ST** - *Service Ticket* (Ticket de Servicio/Kerberos)

38. 
__________________________________________________________________________________________________________________________

1. Un **SOC**, es el equipo centralizado dentro de una organización, encargado de monitorear, detectar,
analizar y responder a amenazas de ciberseguridad en tiempo real.

2. Un **SOC Tier**, son los niveles jerárquicos de responsabilidad, de los analistas en un SOC:

* **L1** — Monitorea y revisa alertas
* **L2** — Investiga incidentes escalados por **L1** 
* **L3** — Expertos en resolver amenazas complejas, avanzadas y theat hunting.

3. Un **SIEM** es un sistema que recopila y analiza logs en tiempo real para detectar, alertar e invest-
amenazas de seguridad. SIEM es una herramienta que centraliza logs y detecta actividad sospechosa en
una red.

4. Un **Evento**, es cualquier acción o actividad registrada en un sistema, red o aplicación, como un login, una conexión o un archivo modificado, normal o sospechoso.

5. Una **Alerta**, es una notificación automática generada por el SIEM al detectar actividad sospechosa
que requiere revisión. Es un aviso de una posible amenaza a un sistema que debe revisarse. Sospecha
de Ataque. Evento sospechoso que SIEM marca.

6. Un **Incidente**, es un evento o serie de eventos confirmados, que representa una amenaza, ataque o 
daño real confirmado, a un sistema, que requiere acción inmediata. Ataque Confirmado. Cuando ya se c-
onfirma un ataque real.

7. La **Escalación**, es el proceso de transferir una alerta o incidente a un nivel superior de analis-
tas (L1→L2→L3) cuando se ve superado. Enviar un problema a un nivel superior para que lo revisen.

8. Un **Falso Positivo**, es una alerta que el SIEM detecta como ataque, pero no lo es, resulta ser acti-
vidad legitima y normal. Alerta incorrecta que no representa una amenaza real.

9. El **Mitre Att&ck** es un framework público que documenta las (TTP/TTPs) Tácticas, Técnicas y proce-
dimientos reales que usan los atacantes, usado como referencia para detectar y responder amenazas.
Describe técnicas y métodos usados por atacantes. Catálogo de cómo atacan los hackers.

10. El **Basic Networking**, es el conocimiento fundamental de cómo funciona una red: IP, DNS, TCP/IP,
Puertos, Protocolos y Tráfico de Datos, esencial para detectar comportamientos anómalos en el SOC.
Entender cómo se conectan, comunican y viajan los datos entre computadoras, y los dispositivos de una
red.

11. El **Basic Linux**, es el conocimiento básico y fundamental del sistema operativo Linux: Manejo de Te-
rminal, comandos básicos y navegación de archivos, esencial en el SOC. Sirve para administrar sistemas.

12. Una **IP**, es una dirección o número únic@ que identifica a cada dispositivo en una red o internet.

13. El **TCP/IP**, es el conjunto de protocolos que permiten enviar y recibir datos en internet. Regula
cómo se transmiten y entregan los datos entre los dispositivos de internet.

14. Un **DNS**, es el sistema que traduce nombres de dominio (ej: google.com) en direcciones IP, para que
los dispositivos puedan comunicarse entre si. Traductor de nombres web a direcciones IP.

15. El **HTTP**, es el protocolo que permite cargar y transferir, datos entre un navegdor y un servidor
web sin cifrado. Protocolo para ver páginas web sin seguridad (sin cifrado), es vulnerable a intercep-
tación.

16. El **HTTPS**, es la versión cifrada de HTTP, que protege la comunicación entre el navegador y el se-
rvidor evitando que terceros intercepten los datos. Protocolo que permite ver o cargar páginas web c-
on cifrado seguro.

17. El **SSH**, es un protocolo que permite accerder y controlar remotamente un servidor de forma segura
mediante conexión cifrada. Protocolo que qermite conectarse a un sistema de forma remota y segura.

18. Un **LOG**, es un registro conológico de eventos y actividades que ocurren en un sistema, red o apl-
icación, usado para monitorear, auditar e investigar incidentes. Historial de lo que pasó en un siste-
ma.

19. El **IDS**, es un sistema que monitorea el tráfico de red y genera alertas cuando detecta actividad sospechosa, pero NO LA BLOQUEA. Sistema que detecta actividades sospechosas, ataques a una red y po-
sibles intrusos.

20. El **IPS**, es un sistema que detecta, bloquea y monitorea las amenazas confirmadas en una red, a di-
ferencia del IDS que solo alerta. Sistema que detecta y bloquea ataques a una red automaticamente.

21. El **ICO**, es cualquier evidencia que indica que un sistema fue comprometido, como una IP maliciosa,
un hash de malware, un archivo sospechoso o un dominio sospechoso. Evidencia que indica que un sistema fue comprometido, señal que indica que hubo un ataque.

22. Un **OS**, es el software base que gestiona el hardware y permite ejecutar aplicaciones, como Windows, Linux o macOS. Software que controla el hardware y permite usar la computadora. 

23. El **CLI**, es la interfaz de texto (terminal) donde se ejecutan comandos directamente, esencial en
ciberseguridad para administrar sistemas y herramientas de seguridad. Interfaz para usar un sistema mediante comandos de texto.

24. El **Brute Force**, es un ataque que prueba masivamente combinaciones de contraseñas o credenciales hasta encontrar la correcta para acceder a un sistema. Ataque que prueba muchas contraseñas hasta encontrar la correcta.

25. Un **Malware**, es un software diseñado para dañar, infectar, robar, controlar o comprometer un sis-
tema sin el consentimiento del usuario.

26. El **Auth**, es el proceso de verificar la identidad de un usuario o sistema antes de otorgarle
acceso. Proceso de verificar la identidad de un usuario o sistema. 

27. El **Firewall**, es un sistema que filtra y controla el tráfico de red, permitiendo o bloqueando
conexiones según reglas de seguridad definidas. Sistema que controla y filtra el tráfico de red entr-
ante y saliente.

28. Un **VPN**, es un túnel cifrado que protege y privatiza la conexión a internet, ocultando el tráfico
y la identidad del usuario. Conexión segura que cifra el tráfico entre tu dispositivo y la red.

29. Las **Soc Tools**, son el conjunto de herramientas especializadas, usadas por analistas SOC, para monitorear, detectar, investigar y responder amenazas (SIEM,EDR,IDS/IPS, ticketing, threat intel, etc).
Algunos de ellos son: Splunk, Wireshark, IBM QRadar, etc.

30. El **Modelo CIA**, es la base fundamental de la ciberseguridad, compuesta por tres principios:
* **Confidencialidad** — La información solo es accesible para quienes están autorizados.
* **Integridad**  — La información no puede ser alterada sin autorización.
* **Disponibilidad** — La informacioón debe estar disponible cuando se necesite.

31. Un **Hash**, es una cadena única de caracteres generada a partir de un archivo o dato, usada para
verificar su integridad,  ya que cualquier minimo cambio, produce un hash completamente diferente.
Es un valor único generado a partir de datos para verificar su integridad.

32. Un **DDoS**, es un ataque que utiliza múltiples dispositivos para saturar un servicio y dejarlo
fuera de funcionamiento. Ataque que sobrecarga un servicio para impedir que funcione. 

33. Un **RATs**, es un Malware que permite a un atacante controlar un dispositivo de forma remota
sin autorización. 

34. **Mimikatz**, es una herramienta para pruebas de Penetración y también para robo de credenciales
en especial los de la memoria LSASS. Entre los datos que puede recuperar se incluyen contraseñas 
en texto plano, hashes NTLM, tickets Kerberos, códigos PIN y certificados.

35. Un **APT**, es una Amenaza Persistente Avanzada, que permanece oculta en un sistema durante mucho
tiempo, es prolongado y dirigido. 

36. Un **Hast NTML o NT Hash**, son valores Criptográficos derivados de contraseñas de Windows, utilizados para la autenticación. Se almacenan en la SAM o en archivo NTDS de un controlador de dominio.
El Hash NTLM se codifica, tomando la  contraseña y convirtiendola en una clave de 16 bytes utilizando
una función Hash MD4.

37. Los **Tickets Kerberos**, son credenciales temporales que permiten a un usuario autenticarse y acceder a servicios de una red de forma segura sin ingresar su contraseña cada vez. El sistema depende de una Autoridad de Distribución de Claves (**KDC**) de confianza que emite dos tipos principales de credenciales:
    1. **TGT** es la credencial maestra obtenida tras la autenticación inicial con el Servidor de Autenticación (**AS**). Permite al cliente solicitar tickets de servicio adicionales sin reingresar sus credenciales
        * **AS** Servidor Kerberos que autentica al usuario y le entrega un **TGT** para solicitar acceso a servicios de la red
    2. **ST** Se obtiene presentando el **TGT** al Servicio de Concesión de Tickets (**TGS**).
        * **TGS** Servicio Kerberos que entrega tickets (*ST*) para acceder a servicios específicos de la red. 🔐
    * **KDC** es el servidor que autentica usuarios y distribuye *tickes Kerberos* para acceder a recursos de una *red*. Es ek componente central del protocolo **Kerberos**, la *clave maestra* es **krbtgt**.

    El orden va así:
    1. **KDC→** *Centro que gestiona **Kerberos*** / *Centro de control de **Kerberos***
    2. **AS→** *Autentica al **Usuario*** / *Verifica la identidad del **Usuario** y le entrega el **TGT***
    3. **TGT→** **Ticket** *que permite solicitar otros* **Tickets.** / *El **Usuario** lo presenta para solicitar acceso a un **servicio.***
    4. **TGS→** **Servicio** *que entrega **Tickets** para **Servicios** específicos.* / *Valida la solicitud y entrega el **ST***
    5. **ST→** **Ticket** *que permite **Acceder** al **Servicio.** solicitado* / *El **Usuario** lo presenta al **Servicio** solicitado para obtener **Acceso.***

    En resumen...
    
    **KDC** *cordina→ **AS** autentica→ **TGT** permite solicitar→ **TGS** emite→ **ST** permite acceder✅*
     
    Los *tickets* contienen **metadatos cifrados (identidad del cliente, dirección de red, marca de tiempo y claves de sesión)** y tienen una *validez limitada* en el tiempo para mitigar ataques de repetición.



38. 

____            