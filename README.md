# AdvancedWebMapping
AdvancedWebMappingAssignment#1
Main purpose is to create and deploy a location based service.
Successfully created the pycharm program that displays the map and locates users current location
Successfuly updates the databse with the users location.
Was unsuccssful to complete the deploying.
However was able to create a virtual machine with digital ocean,
was able to create a domain under the name gavinfahy.xyz,
Was able to modify the DNS enrty at the domain name register using DNS 'A',
Was able install Certbot,
Was able to create the docker network using docker network create wmap_network,
Was able to create a vim file named Dockerfile to store,
#FROM nginx
#MAINTAINER Mark Foley
#RUN apt-get -y update && apt-get -y upgrade && apt-get -y install software-properties-common certbot python3-certbot-nginx
Was able to create the container 
#docker create --name wmap_nginx_certbot --network wmap_network --network-alias wmap-nginx-certbot -p 80:80 -p 443:443 -t -v #wmap_web_data:/usr/share/nginx/html -v $HOME/wmap_nginx_certbot/conf:/etc/nginx/conf.d -v /etc/letsencrypt:/etc/letsencrypt -v /var/www/certbot -v #html_data:/usr/share/nginx/html/static  wmap_nginx_certbot
Was able to create the pgadmin4 container
#docker create --name wmap_pgadmin4 --network wmap_network --network-alias wmap-pgadmin4 -t -v wmap_pgadmin_data:/var/lib/pgadmin -e #'PGADMIN_DEFAULT_EMAIL=mark.foley@tudublin.ie' -e 'PGADMIN_DEFAULT_PASSWORD=mypassword' dpage/pgadmin4
Was able to creaet the PostGIS container 
#docker create --name wmap_postgis --network wmap_network --network-alias wmap-postgis -t -v wmap_postgis_data:/var/lib/postgresql -e #'POSTGRES_USER=docker' -e 'POSTGRES_PASS=docker' kartoza/postgis
However I was unable to proceed any further.
