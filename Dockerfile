# Use an existing Nginx image from Docker Hub
FROM nginx:alpine

# Copy the custom Nginx configuration file
COPY nginx.cfg etc/nginx/sites-available/nginx.cfg

EXPOSE 80