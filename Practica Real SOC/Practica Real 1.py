"""           /////// SEMANA 4 /////////
Día 1 (Análisis de logs Linux(auth.log))
Analizar logs reales, detectar patrones y tomar una decisión como analista SOC Jr.

● ¿Qué pasó?
● Evidencia
● Impacto
● Aacción

Análisis
1-. ¿Qué tipo de evento ves primero?
2-. ¿Qué patrón aparece?
3-. ¿Por qué esto ya no es solo una alerta?

Clasificación
4-. ¿Evento, alerta o incidente?
5-. ¿Severidad?

Decisión
6-. ¿Cerrarías, observarías o escalarías?
7-. ¿Por qué?

Un login exitoso después de intentos fallidos desde la misma IP es una señal muy seria.

        ********** REVISIÓN *************
Caso: auth.log - Acceso SSH

1-. ¿Qué eventos hay?
– Múltiples intentos fallidos de login SSH
– Login exitoso posterior
No es solo un evento, son varios.

2-. ¿Qué patrón aparece?
Patron claro de fuerza bruta + acceso exitoso
– Misma IP
– Mismo servicio (SSH)
– Corto intervalo de tiempo
– Usuario inválido → luego usuario válido
Este patrón NO es normal

3-. ¿Por qué ya no es solo alerta?
– El acceso fue exitoso
– Ocurrió después de intentos fallidos
– Desde IP externa
– En horario inusual (02:00 am)
Aquí ya hay riesgo real

4-. Clasificación correcta
Incidente
– Tipo: Acceso no autorizado / Posible compromiso de credenciales

5-. Severidad
Alta
– Hay acceso exitoso
– Posible compromiso
– Impacto potencial en el sistema

6-. Decisión correcta
Escalar
No cerrar. No solo observar.
Requiere
– Contención
– Investigación más profunda
– Posible cambio de credenciales

7-. Documentación (Cómo debería verse)
¿Qué pasó?
Se detectaron múltiples intentos fallidos de autenticación SSH seguidos de un login exitoso
desde la misma IP externa.

Evidencia
– IP: 185.220.101.7
– Hora: 02:11 - 02: 12
– Servicio: SSH
– Log: auth.log

Impacto
– Acceso no autorizado potencial
– Riesgo alto

Acción
– Escalado al equipo correspondiente


Día 2


 """