WattControl

WattControl es una aplicación web desarrollada con tecnologías como Django (Python), JavaScript, HTML y CSS. Está diseñada para ejecutarse en un entorno dockerizado que facilita su despliegue, monitoreo, y escalabilidad. Este repositorio contiene la configuración completa para levantar el proyecto usando Docker y Docker Compose.

Arquitectura del Sistema

La arquitectura del sistema está compuesta por varios servicios que interactúan a través de redes internas y externas dentro de contenedores Docker. La imagen siguiente ilustra la interacción entre los servicios:

| Servicio      | Puerto Externo | Puerto Interno | Red               | Acceso         |
| ------------- | -------------- | -------------- | ----------------- | -------------- |
| web           | No expuesto    | 8000           | Ambas redes       | Solo vía nginx |
| db            | 3309           | 3306           | internal\_network | Directo (dev)  |
| nginx         | 80, 443        | 80, 443        | external\_network | Público        |
| modsecurity   | 8080, 8443     | 80, 443        | external\_network | Público        |
| loki          | 3100           | 3100           | internal\_network | Privado        |
| grafana       | 3000           | 3000           | internal\_network | Privado        |
| falcosidekick | 2801           | 2801           | No definida       | Privado        |

Instrucciones para desplegar

1. Requisitos
-Docker
-Docker Compose
-Archivo .env con las siguientes variables:

MYSQL_DATABASE=nombre_de_base_de_datos
MYSQL_ROOT_PASSWORD=tu_contraseña

2. Construcción y despliegue
Desde la raíz del proyecto, ejecuta:

docker-compose up --build

Esto construirá la imagen del servicio web, iniciará la base de datos MySQL, esperará su disponibilidad, aplicará las migraciones de Django y ejecutará el servidor en el puerto 8000 (acceso interno).

Servicios Incluidos

-Web (Django): Backend principal del proyecto.
-MySQL: Base de datos relacional.
-Nginx: Servidor web de entrada con soporte para HTTPS.
-ModSecurity: Firewall de aplicaciones web para reforzar la seguridad.
-Grafana + Loki: Monitoreo y visualización de logs.
-Falco + Falcosidekick: Detección de amenazas y envío de alertas.

Volúmenes Persistentes

Se utilizan volúmenes para preservar datos de la base de datos y logs:

db_data → MySQL
loki_data → Logs para Loki
grafana_data → Dashboards y configuración

Monitoreo y Seguridad

El sistema incorpora herramientas avanzadas como:

Falco: Monitoriza comportamientos sospechosos en los contenedores.
Loki y Promtail: Recogen y envían logs.
Grafana: Visualiza métricas y eventos.
Slack: Recibe notificaciones críticas desde Falcosidekick.

**PASOS PARA LEVANTAR SERVICIOS DE LOKI CORRECTAMENTE**

Ejecutar el comando antes de el Docker-compose.yml con el fin de que se reconozca el servicio de Loki. Esto instala una extensión de Docker para que reconozca el servicio:

docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions

Una vez iniciados los Docker, accede al servicio Grafana:

1. Configuración de Grafana
Necesitas configurar una fuente de datos (data source) en Grafana para conectarte a Loki. Cuando tengas Grafana funcionando:

2. Accede a Grafana en http://localhost:3000 (usuario/contraseña por defecto: admin/admin)
Ve a Configuración > Data Sources > Add data source
Selecciona Loki
En la URL, ingresa: http://loki:3100
Guarda y prueba la conexión

3. Para cargar el dashboard creado:

Selecciona Dashboard -> create new dashboard -> Import Dashboard y selecciona el archivo JSON en la carpeta Dashboard

Siguiendo estos pasos Loki y todos sus servicios deberían de estar activos correctamente.