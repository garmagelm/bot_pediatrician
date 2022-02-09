# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types

token = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [
        'ОРВИ/ОРЗ',
        'ГВ',
        'Витамин Д',
        'Паразитоз',
        'Анемия',
        'Аптечка',
        'Ожог',
        'Ушная боль',
        'Зубная боль',
        'Запор',
        'Диарея/Рвота',
        'Сон',
        'Падение',
        'Прикорм',
        'Онлайн консультация',
    ]])
    bot.send_message(m.chat.id, 'Выберите жалобу:', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'ОРВИ/ОРЗ':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in [
            'Сопли',
            'Красное горло',
            'Кашель',
            'Температура'
        ]])
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboardgostart)
    elif message.text == 'Сопли':
        bot.send_message(message.chat.id, '''
🍀 обеспечте прохладный23°, влажный 60%воздух в комнате где находится малыш.
🍀 уделите ему больше внимания носите на ручках.
🍀 промывайте носки водичкой (морской ⚓ или аптечной) не увлекайтесь и не перестарайтесь.
🍀 не капайте никакие масляные капли 💦 и масла в нос типа пиносола, хлорфилипта,сопелок.
🍀 кормите пупсиков по желанию, нет аппетита ненужно настаивать.
🍀 предлагайте напитки любые, какие считаете нужным и на какие нет аллергии (соки, воды, морсы, компоты, настои, чаи).
🍀 купать малышей можно, особенно с добавлением пачки соли на ванну.
🍀 гулять по погоде нужно.
🍀 чаще мойте руки и умывайтесь.
🍀 не приглашайте и не ходите в гости.
🍀 обратитесь к доктору, сдайте анализ (риноцитограмму), это поможет определить какой насморк аллергический, бактериальный...
🍀 не использовать без острой необходимости устройства аспирационные, не делать "кукушку "
🍀 не заливать в носики полаптеки.
🍀 не спешите непременно вставить в попу свечку.
🍀 ну раз уж заболел дайте поболеть спокойно, не подвергайте стрессу.
🍀 будьте в меру бдительны, я вам всегда готова помочь, назначить лекарства, и направить к лору при необходимости.
🍀 будьте счастливы и здоровы.

Для выбора другой жалобы, нажмите /start.''')
    elif message.text == 'Красное горло':
        bot.send_message(message.chat.id, '''
💚Красное горло и что с ним делать?
Для начала красное горло -это нормальная реакция слизистой в ответ на попадание вирусов или бактерий, это воспалительная реакция организма,то есть красное горло это не диагноз это симптом.
💜 При ОРВИ красное горло лечить бесполезно! Не придумали такого средства которое убило бы вирусы сидящие в клетках, поэтому единственное что нам остается-облегчить жизнь больному и убрать дискомфорт.
💜 Боль в горле 💜
Здесь поможет холод который приводит к сужению сосудов , что в свою очередь уменьшает отек тем самым уменьшая боль.холод не увеличивает сроки болезни и риски тяжелого течения и осложнений. Подойдет рассасывание кусочка льда или замороженного сока, мороженое, йогурт, для грудных детишек охлажденное грудное молоко. отофаг/фагодент прямо из холодильника.
💙Парацетамол и ибупрофен  обезболевают, снимают жар ( не увлекаться).
💙Более старшим детям можно использовать лизобакт, стрепсилс, граммидин и подобные но их нет в международных протоколах.
💙у детей до 6 лет спреи в горло не разрешены так как они могут синхронизировать вдох и выдох, есть риск ларингоспазма /вспомнили мирамистин / леденцы опасны удушьем.В любом случае обильное питье для увлажнения слизистых.

Для выбора другой жалобы, нажмите /start.''')
    elif message.text == 'Кашель':
        bot.send_message(message.chat.id, '''
Если у вашего ребенка кашель из-за соплей, то в первую очередь вылечить сопли.
Обратиться к педиатру, чтобы послушала какой кашель у ребенка (влажный или сухой).
В рацион добавить жиры и масла богатые витамином А.

Для выбора другой жалобы, нажмите /start.''')
    elif message.text == 'ГВ':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in [
            'Мало молока',
            'Лактостаз',
            'Правильное прикладывание'
        ]])
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboardgostart)
    elif message.text == 'Мало молока':
        bot.send_message(message.chat.id, '''
Тут текст про мало молока.

Для выбора другой жалобы, нажмите /start.''')
    elif message.text == 'Лактостаз':
        bot.send_message(message.chat.id, '''
    Тут текст про Лактостаз.

    Для выбора другой жалобы, нажмите /start.''')
    elif message.text == 'Правильное прикладывание':
        bot.send_message(message.chat.id, '''
Признаки правильного прикладывания к груди:
1️⃣ Мама не испытывает неприятных ощущений в области соска и ареолы (даже в первые минуты кормления);⠀
2️⃣ Рот широко открыт, губы не напряжены;⠀
3️⃣ Не слышно посторонних звуков (причмокивания, цоканья);⠀
4️⃣ Подбородок «утоплен» в грудь;⠀
5️⃣ Носик может касаться, может не касаться груди, но не утопает в
груди;⠀
6️⃣ Над нижней губой может быть виден язычок;⠀
7️⃣ Во время сосания ребенок захватывает снизу больше груди, чем
сверху (примерно 3-4 см снизу и 2-3 см сверху);⠀
8️⃣ После сосания сосок ровный, круглый, иногда может быть
удлинен. Не скошен, не сплющен;⠀
9️⃣ Ушко - плечико - бедро находятся на одной линии.

    Для выбора другой жалобы, нажмите /start.''')
    elif message.text == 'Витамин Д':
        bot.send_message(message.chat.id, '''💜ВИТАМИН Д💜
    Дозировка для новорожденного до 6месяцев жизни на гв (при том что у мамы хороший уровень витамин Д и она профилактически продолжает принимать 1000ме):
    - С 6месяцев до 1,6тэто 1600ме.
    - Ближе к 2м годика это 2000ме,без анализа!!!!с анализами другие подсчеты.
    Аквадетримы,детримаксы,эвалары дети приходят с рахитом, перевозбужденные, не спящие.
    Дело Ваше, Вам виднее что и как и когда давать.''')
    elif message.text == 'Паразитоз':
        bot.send_message(message.chat.id, '''
💜Подготовка к  исследованию на паразитоз.💜
1) Пьете желчегонные - фламин, артишок,хофитол, шиповник, по инструкции, за полчаса до еды три раза в день около месяца.
2) Примерно каждые  5-7-10 дней сдаете кал методами - парасеп, либо двойная седиментация, либо расширенное информативное копрологическое исследование Фарм-т(Казань).
💜 Чтобы повысить вероятность нахождения сдавать в период угасающей луны, в этот период паразиты выходят.💜
Ну а если нашли:
💚оак с лейкоформулой
💚оам
💚копрограмма
💚узи органов брюшной полости
👣Если есть атопия, то эозинофильнокатионный белок, с-реактивный белок, ig E иммуноглобулин, чтобы отличить аллергию от паразитоза.
💜Найдем причину и устраним вместе , обращайтесь на личную консультацию.''')
    elif message.text == 'Анемия':
        bot.send_message(message.chat.id, '''
Диагностика причин анемии :
🍀 Общий анализ крови +Соэ, L формула.
🍀 Общий анализ мочи
🍀 Ретикулоциты
🍀 Гематокрит
🍀 Витамин В12
🍀 Фолиевая кислота.
🍀 Железо (сыворотка крови) +ОЖСС.
🍀 Ферритин.
🍀 УЗИ брюшной полости.
Всем мамулечкам на гв обязательно дважды в год как минимум.''')
    elif message.text == 'Аптечка':
        bot.send_message(message.chat.id, '''
Летняя аптечка нужна для:
1️⃣экстренных ситуаций (ночью, оказания первой помощи)
2️⃣случаев, когда можно обойтись без помощи врача.
❌Любые другие препараты назначаются только врачом.
🚨Поэтому при выезде заграницу-ОБЯЗАТЕЛЬНО оформить мед.страховку!
🤔Не берите лекарства с недоказанной эффективностью и много лекарств (можно вынуть из пачки один блистер.
🚨ПРИМЕРНЫЙ СПИСОК:
✅Жаропонижающее и обезболивающее (на основе парацетамола-Панадол,Цефекон Д, Эффералган и ибупрофена-Ибуфен, Нурофен и др)- свечи или сироп, строго по инструкции!)
❗Анальгин/аспирин/димедрол-запрещены у детей! Не протирать уксусом/водкой!
✅Антигистаминные препараты (супрастин/фенистил/зиртек/зодак эриус)
✅Электролитный раствор (Хумана Электролит, Гидровит, Регидрон Био, адиарин регидро,биогая орс,)
✅Антибактериальная мазь (бактробан/агросульфан/левомеколь/банеоцин и др)
✅Перевязочный материал: пластыри, самоклеющийся бинт, марлевые салфетки (на небольшие ссадины можно нанести клей БФ или его аналоги)
✅Местные стероиды (гидрокортизон крем, Локоид)
✅Эластичный бинт
✅Пипетка, пинцет, ножницы
✅Противовоспалительные глазные капли (Тобрекс, левомицетиновые глазные капли).
✅Устройство для изъятия клещей
✅Гемостатическая губка или аналоги (порошок или бинт Целокс Celox, на основе хитозана или спрей на основе окисленной целлюлозы СМАРТ и аналоги (маркирован m-doc)
✅Криопакет (Холодок,Снежок)
✅Противоожоговый гель с антисептиком и анестетиком (например, «Аполло»)но первая помощь охлаждаете водой!
✅Антисептики (Мирамистин, Хлоргексидин)
✅Сорбенты (Активированный уголь, Смекта , полисорб,энтеросгель)
🚨Если в семье были случаи анафилаксии, в международных протоколах рекомендовано носить с собой авто-инъектор с адреналином (Epipen, Jext, Adrenaclick). Но в РФ удобной формы препарата нет.
👩🏼‍⚕В аптечке нет ушных капель, тк эти препараты назначаются после осмотра врачом и зависят от вида отита (для обезболивания при боли в ухе применяется жаропонижающее).но анауран можно даже при перфоративном отите.
🌊Также я не стала включать в аптечку солевой раствор в нос:думаю, это не срочная мед.помощь, спокойно успеете его купить или на крайний случай сделать самостоятельно.
Ну и как же без соленых ванн то.
❗Важно знать о ближайших мед пунктах!
🤓Корректируйте аптечку под себя!
❗Всегда следуйте инструкции!''')
    elif message.text == 'Ожог':
        bot.send_message(message.chat.id, '''
Первая помощь при ожоге и единственная - это холодная вода и точка, не пантенол не ещё что-то.
Даже если уже волдырь, даже если солнечный.
Цель-охладить и увлажнить,как можно быстрее, чтобы не усугубить. Долго ,пока не перестанет жечь.
Только на стадии заживления можно ранозаживляющие никак не в момент.
В момент только вода. Запомнить ожог - вода.
Берегите себя. В аптечке держите маленький пузырек масла чёрного тмина. На стадии заживления прекрасно справляется,без шрамов.''')
    elif message.text == 'Ушная боль':
        bot.send_message(message.chat.id, '''
При прорезывании зубов бывает ушная боль, даже если не красно там нигде.
Оталгия при синдроме прорезывания зубов.
Помогает вибрукол, парацетамол если очень больно, анауран всё таки, и капельки камелия.''')
    elif message.text == 'Зубная боль':
        bot.send_message(message.chat.id, '''
Что касается прорезывания зубов. Это одно из первых испытаний болевого порога малыша.
🌷 Почему же у некоторых детишек синдром прорезывания зубов проходит незаметно, а у некоторых с зудом, болью, слюнотечением, порой даже насморком и диареей.
Да всё по причине разного восприятия боли, всему виной особенности нервной системы.
И у взрослых также, зуб мудрости кто-то даже не замечает, а кто то страдает.
Если вы на ГВ, то при прорезывании обычно всегда помогает успокоение грудью.
Если сильно переживаете, ребенку больно и нет ГВ, то должны помочь Дантинорм Бэби или Камилия(iherb).''')
    elif message.text == 'Температура':
        bot.send_message(message.chat.id, '''Тут будет текст.''')
    elif message.text == 'Запор':
        bot.send_message(message.chat.id, '''
Если ваш ребенок на ГВ с 1,5 месяца до начала прикорма, то ребенок может не испражняться до 7-10 дней. Это считается нормой.
После начала прикорма запор чаще всего связан нехваткой жиров в рационе.
0-1,5 мес ребёнок должен ходить ежедневно. Если не ходит, то чаще всего причина в питании мамы (если на ГВ), надо разбираться индивидуально.
Если на ИВ или СВ, то надо разбираться со смесью.''')
    elif message.text == 'Диарея/Рвота':
        bot.send_message(message.chat.id, '''Отпаивайте водой (30мл на кг), регидрон био по инструкции.''')
    elif message.text == 'Сон':
        bot.send_message(message.chat.id, '''Тут текст про сон''')
    elif message.text == 'Падение':
        bot.send_message(message.chat.id, '''Про падение''')
    elif message.text == 'Прикорм':
        bot.send_message(message.chat.id, '''Про прикорм''')
    elif message.text == 'Онлайн консультация':
        bot.send_message(message.chat.id, '''
Вы можете обратиться за личной консультацией к Айгуль Фаридовне.
Для этого напишите ей личное сообщение по логину (@aigulfaridovna) с пометкой НУЖНА ЛИЧНАЯ КОНСУЛЬТАЦИЯ и сразу приложите ответы на вопросы ниже в этом же сообщении.
Стоимость консультации от 1000 рублей, в зависимости от сложности вопроса.

Вопросы:
💙Ваше имя и малыша
💜Рост вес ребёнка
💛Возраст
🤍Какие по счёту роды
💚Способ родовспоможения
🧡Перенесенное заболевание во время беременности
💛Наблюдался ли во время беременности токсикоз головные боли запоры расстройство стула симптомы неблагополучия на коже ногтях волосах  сыпь зуд сухость выпадения волос
🧡Какие лекарственные средства принимала мама во время беременности в каком триместре
💜Был ли приложен к груди
🤎Антибиотики в роддоме или в первые месяцы жизни
🖤Симптомы которые беспокоят настоящий момент
💓Стул сколько раз в день и какой аппетит сколько раз включая перекусы
💚Сколько и как спит
💜Есть ли бледность, желтушность, потливость, родинки, пигментные, пятна, гемангиомы
❤️Имеется ли аллергия какая и на что
💜Имеется ли отягощенный наследственный анамнез
❤️Хронические заболевания и патология
💛Было ли грудное вскармливание в первые 6 месяцев жизни ребёнка если смесь то какая смесь сейчас присутствует смесь? какая?
🤍Перенёс ли ротавирус норовирус коронавирус аденовирус кишечная инфекция
🧡Укачивает ли в автомобиле
💙Бывает ли рвота и как часто
💚Употребляет ли молочные продукты хлебобулочные изделия макароны крупы сладости полуфабрикаты соки и другие сладкие напитки
🥬Опишите подробнее Ваше традиционное питание
💛Посещает ли детский сад
❤️Все ли прививки по возрасту
🧡Если хоть какой-нибудь диагноз поставленный врачом
💙Когда и чем болел
💜Антибиотики были ли? когда ?гормоны и другие сильнодействующие препараты ?
💛Какой у вас запрос на консультацию?''')


bot.polling()
