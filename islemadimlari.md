# Django ile adım adım web sitesi oluşturma
Ornek klasörü içinde bu işlemler sırasıyla uygulandı<br>
* Projeyi Başlatmak için
    - django-admin startproject websitesi .
* Veritabanını oluşturmak için
    - python manage.py migrate
* Sisteme Süper Kullanıcı Eklemek için (Şifreleri yazarken ekranda görünmez dikkat edin)
    - python manage.py createsuperuser
* Web Sitesinin Çalıştırmak için
    - python manage.py runserver
* Bir uygulama oluşturmak için  (blog adı örnek değiştirilebilir)
    - python manage.py startapp blog
* Uygulamada ürettiğiniz modelin veritabanına yansıması için 
    - python manage.py makemigrations blog
    - python manage.py migrate
* Web Sayfasının ayarlarını yapmak için
    -settings.py
* adresler için
    -urls.py