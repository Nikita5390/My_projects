## Запуск приложения

### 1. Установка дополнительного ПО
```apt update```  
```apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools net-tools htop nginx python3-certbot-nginx -y```

### 2.Создаем Виртуальное Окружение Python - myenv1: 
```apt install python3-venv```  
```adduser user1```  
```chmod 755 /home/user1/```  
```su user1```  
```$ mkdir ~/myproject```  
```$ cd ~/myproject```  
```$ python3 -m venv myenv1```  
```$ source myenv1/bin/activate```  

### 3.Ставим пакеты через менеджер pip:
```pip install requirements.txt```

### 4.Конфигурация Gunicorn: 
```$ cd ~/myproject```  
```$ gunicorn --bind 0.0.0.0:5000 wsgi:app```

### 5.Проверяем вход через 5000 порт: 
```http://Server_IP:5000/```

### 6. Перемещаем файл myproject.service по указанному пути:
```/etc/systemd/system/myproject.service```

### 7.Запускаем юнит, добавляем в автозагрузку и проверяем статус: 
``` systemctl start myproject```  
```systemctl enable myproject```  
```systemctl status myproject```  

### 8.Настраиваем проксирование для нашего домена через nginx на наш unix:app.sock:  
``` vi /etc/nginx/sites-available/app ```  
```
server {
   listen 80;
   server_name site.ru www.site.ru;
   location / {
       include proxy_params;
       proxy_pass http://unix:/home/user1/myproject/app.sock;
   }
}
```
``` ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/```

### 9.Затем запустите следующую команду для активации конфигурации блока сервера "myapp.conf", затем проверьте конфигурацию Nginx. Если вы не получите никакой ошибки, вы увидите выходное сообщение, такое как «Syntax OK - тест успешно».
```sudo ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/```  
```sudo nginx -t```

### 10.После этого вы можете перезапустить службу Nginx, используя следующую команду для внесения новых изменений в конфигурацию Nginx.
```sudo systemctl restart nginx```