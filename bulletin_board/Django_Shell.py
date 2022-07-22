# python manage.py shell
from django.contrib.auth.models import User
from board.models import Category, Ad, Response, AdsCategory, Author


def todo():
    # полезно для отладки удалять объекты
    User.objects.all().delete()
    Category.objects.all().delete()


# Создание двух пользователей, с заполнением всех обязательных полей
user_petr = User.objects.create_user(username='petr', email='texno_log_90@mail.ru', password='12345')
user_ivan = User.objects.create_user(username='ivan', email='texno_log_90@mail.ru', password='12345')

petr = Author.objects.create(user=user_petr)
ivan = Author.objects.create(user=user_ivan)

# Добавляем категории в модель Category
perviy = Category.objects.create(name='Первый')
vtoroy = Category.objects.create(name='Второй')
tretiy = Category.objects.create(name='Третий')
chetvertiy = Category.objects.create(name='Четвертый')
pytiy = Category.objects.create(name='Пятый')
shestoy = Category.objects.create(name='Шестой')
sedmoy = Category.objects.create(name='Седьмой')
vosmoy = Category.objects.create(name='Восьмой')
devytiy = Category.objects.create(name='Девятый')
desytiy = Category.objects.create(name='Десятый')

# Описываем текст объявления
text_perviy = 'Объявления к первым '
text_vtoroy = 'Объявления ко вторым '
text_tretiy = 'Объявления к третим'
text_chetvertiy = 'Объявления четвертым '
text_pytiy = 'Объявления к пятым '
text_shestoy = 'Объявления к шестым '
text_sedmoy = 'Объявления к седьмым '
text_vosmoy = 'Объявления к восьмым '
text_devytiy = 'Объявления к девятым '
text_desytiy = 'Объявления к десятым '

# создаем объявление
I = Ad.objects.create(author=petr, article='perviy', text_ad=text_perviy)
II = Ad.objects.create(author=petr, article='vtoroy', text_ad=text_vtoroy)
III = Ad.objects.create(author=petr, article='tretiy', text_ad=text_tretiy)
IV = Ad.objects.create(author=petr, article='chetvertiy', text_ad=text_chetvertiy)
V = Ad.objects.create(author=petr, article='pytiy', text_ad=text_pytiy)
VI = Ad.objects.create(author=petr, article='shestoy', text_ad=text_shestoy)
VII = Ad.objects.create(author=petr, article='sedmoy', text_ad=text_sedmoy)
VIII = Ad.objects.create(author=petr, article='vosmoy', text_ad=text_vosmoy)
IX = Ad.objects.create(author=petr, article='devytiy', text_ad=text_devytiy)
X = Ad.objects.create(author=petr, article='desytiy', text_ad=text_desytiy)


# присваиваем категории
с1 = AdsCategory.objects.create(ads=I,  category=perviy)
c2 = AdsCategory.objects.create(ads=II,  category=vtoroy)
c3 = AdsCategory.objects.create(ads=III,  category=tretiy)
c4 = AdsCategory.objects.create(ads=IV,  category=chetvertiy)
c5 = AdsCategory.objects.create(ads=V, category=pytiy)
c6 = AdsCategory.objects.create(ads=VI,  category=shestoy)
c7 = AdsCategory.objects.create(ads=VII,  category=sedmoy)
c8 = AdsCategory.objects.create(ads=VIII,  category=vosmoy)
c9 = AdsCategory.objects.create(ads=IX,  category=devytiy)
c10 = AdsCategory.objects.create(ads=X,  category=desytiy)


# отклики
o1 = Response.objects.create(ads=I, user=ivan.user, text_response='o1 x')
o2 = Response.objects.create(ads=II, user=ivan.user, text_response='o2 xx')
o3 = Response.objects.create(ads=III, user=ivan.user, text_response='o3 xxx')
o4 = Response.objects.create(ads=IV, user=ivan.user, text_response='o4 xxxx')
o5 = Response.objects.create(ads=V, user=ivan.user, text_response='o5 xxxxx')
o6 = Response.objects.create(ads=VI, user=ivan.user, text_response='o6 xxxxxx')
o7 = Response.objects.create(ads=VII, user=ivan.user, text_response='o7 xxxxxxx')
o8 = Response.objects.create(ads=VIII, user=ivan.user, text_response='o8 xxxxxxxx')
o9 = Response.objects.create(ads=IX, user=ivan.user, text_response='o9 xxxxxxxxx')
o10 = Response.objects.create(ads=X, user=ivan.user, text_response='o10 xxxxxxxxxx')