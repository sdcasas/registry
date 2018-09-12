Django: Despliegue de un Proyecto
=================================

Configuración
-------------

 #. Descargar el proyecto a desplegar ::
    
        git clone https://github.com/sdcasas/registry

 #. Crear entorno virtualenv, tener en cuenta la versión de python a utilizar ::
    
        mkvirtualenv -p $(which python3) registry

 #. Instalación de dependencias el proyecto ::
    
        pip install -r deploy/requirements-prod.txt

 #. Se debe instalar el servidor que se encargará de ejecutar el proyecto django (chausette | etc) ::
    
        pip install chaussette==1.3.0

 #. Realizar pasos de ejecución proyecto django ::

        ./manager.py collectstatic
        ./manager.py makemigrations
        ./manager.py migrate

    esto se realiza solo para ver que el proyecto no presente errores ::

        ./manager.py runserver 


 #. Elegir un puerto para ser utilizado en el proyecto (ej: 8005)


 #. Agregar los archivos de configuración (nginx.conf | circus.ini)

    * <ruta-del-proyecto>/deploy/circus.ini ::

        [socket:registry]
        host = localhost
        port = 8005

        [watcher:registry]
        cmd = /home/apps/.envs/registry/bin/chaussette
        args = --fd $(circus.sockets.registry) config.wsgi.application
        use_sockets = True
        numprocesses = 3
        autostart = True

        [env:registry]
        PYTHONPATH = /home/apps/projects/registry/registry_project


    * <ruta-del-proyecto>/deploy/nging.conf ::

        server {
            listen 80;
            charset utf-8;
            server_name www.colmenacoop.com colmenacoop.com;
            
            client_max_body_size 4G;
            
            location /static {
                alias /home/apps/projects/registry/registry/static;
                autoindex on;
            }
            
            location /media {
                alias /home/apps/projects/registry/registry/media;
            }
            
            location / {
                proxy_pass http://localhost:8005;
                proxy_set_header X-Forwarded-Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header Host $host;
                proxy_set_header X-Scheme $scheme;
                proxy_connect_timeout 600;
                proxy_send_timeout 600;
                proxy_read_timeout 600;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
            }
            
            ## Log
            access_log /home/apps/projects/registry/deploy/log/nginx-access.log;
            error_log /home/apps/projects/registry/deploy/log/nginx-errors.log;
        }


 #. crear carpeta y archivos de log ::

        /ruta-del-proyecto/deploy/log/
        /ruta-del-proyecto/deploy/log/nginx-access.log
        /ruta-del-proyecto/deploy/log/nginx-errors.log

 #. crear los en los enlaces simbólicos de los archivos de configuración ::

        ln -s /ruta-del-proyecto/deploy/circus.ini /etc/circus/conf//registry
        ln -s /ruta-del-proyecto/deploy/nginx.ini /etc/nginx/sites-enabled/registry

 #. testear el archivo de configuración de circus ::
    
        # detener el demonio de circus, hacerlos en un horario que no se esten usando las aplicaciones
        circusctl quit

        # probar el funcionamiento
        circusd /ruta-del-proyecto/deploy/circus.ini

 #. algo me debo estar olvidando

 #. reiniciar nginx (root) ::

        /etc/init.d/nginx restart
        systemctl restart nginx
    
 #. Iniciar circus en modo demonio ::

        circusd --daemon /etc/circus/circus.ini
