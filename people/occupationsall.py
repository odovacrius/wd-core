#!/usr/bin/python3
"""

بوت إضافة الوصوف عن الأشخاص في ويكي بيانات

جميع اللغات

https://github.com/emijrp/wikidata/blob/master/human.descriptions.py

~ lithographer
~ Esperantist
~ ski jumper
~ troubadour
~ bishop

"""
#
# (C) Ibrahem Qasim, 2022
#
#

# ---
translationsOccupations_new = {
    '~ Indigenous artist': {
        'ar': {
            'male': 'فنان سكان أصليون ~',
            'female': 'فنانة سكان أصليون ~'
        },
        'en': {
            'male': '~ Indigenous artist',
            'female': '~ Indigenous artist'
        },
    },
    '~ papyrologist': {
        'ar': {
            'male': 'عالم برديات ~',
            'female': 'عالمة برديات ~'
        },
        'en': {
            'male': '~ papyrologist',
            'female': '~ papyrologist'
        },
    },
    '~ former military officer': {
        'ar': {
            'male': 'ضابط عسكري سابق ~',
            'female': 'ضابطة عسكرية سابقة ~'
        },
        'en': {
            'male': '~ former military officer',
            'female': '~ former military officer'
        },
    },
    '~ researcher': {
        'ar': {
            'male': 'باحث ~',
            'female': 'باحثة ~'
        },
        'en': {
            'male': '~ researcher',
            'female': '~ researcher'
        },
    },
    '~ sprinter': {
        'ar': {
            'male': 'عداء سريع ~',
            'female': 'عدائة سريعة ~'
        },
        'en': {
            'male': '~ sprinter',
            'female': '~ sprinter'
        },
    },
    '~ military officer': {
        'ar': {
            'male': 'ضابط عسكري ~',
            'female': 'ضابطة عسكرية ~'
        },
        'en': {
            'male': '~ military officer',
            'female': '~ military officer'
        },
    },
    '~ medievalist': {
        'ar': {
            'male': 'مختص في الدراسات القروسطية ~',
            'female': 'مختصة في الدراسات القروسطية ~'
        },
        'en': {
            'male': '~ medievalist',
            'female': '~ medievalist'
        },
        'es': {
            'male': 'medievalista ~',
            'female': 'medievalista ~'
        },
    },
    '~ philologist': {
        'ar': {
            'male': 'فقيه لغة ~',
            'female': 'فقيهة لغة ~'
        },
        'en': {
            'male': '~ philologist',
            'female': '~ philologist'
        },
        'es': {
            'male': 'filólogo ~',
            'female': 'filóloga ~'
        },
    },
    '~ physiologist': {
        'ar': {
            'male': 'عالم وظائف الأعضاء ~',
            'female': 'عالمة وظائف الأعضاء ~'
        },
        'en': {
            'male': '~ physiologist',
            'female': '~ physiologist'
        },
        'es': {
            'male': 'fisiólogo ~',
            'female': 'fisióloga ~'
        },
    },
    '~ political scientist': {
        'ar': {
            'male': 'عالم سياسة ~',
            'female': 'عالمة سياسة ~'
        },
        'en': {
            'male': '~ political scientist',
            'female': '~ political scientist'
        },
        'es': {
            'male': 'politólogo ~',
            'female': 'politóloga ~'
        },
    },
    '~ psychoanalyst': {
        'ar': {
            'male': 'معالج نفسي ~',
            'female': 'معالجة نفسية ~'
        },
        'en': {
            'male': '~ psychoanalyst',
            'female': '~ psychoanalyst'
        },
        'es': {
            'male': 'psicoanalista ~',
            'female': 'psicoanalista ~'
        },
    },
    '~ psychiatrist': {
        'ar': {
            'male': 'طبيب نفسي ~',
            'female': 'طبيبة نفسية ~'
        },
        'en': {
            'male': '~ psychiatrist',
            'female': '~ psychiatrist'
        },
        'es': {
            'male': 'psiquiatra ~',
            'female': 'psiquiatra ~'
        },
    },
    '~ psychologist': {
        'ar': {
            'male': 'عالم نفس ~',
            'female': 'عالمة نفس ~'
        },
        'en': {
            'male': '~ psychologist',
            'female': '~ psychologist'
        },
        'es': {
            'male': 'psicólogo ~',
            'female': 'psicóloga ~'
        },
    },
    '~ racing driver': {
        'ar': {
            'male': 'سائق سباق ~',
            'female': 'سائقة سباق ~'
        },
        'en': {
            'male': '~ racing driver',
            'female': '~ racing driver'
        },
        'es': {
            'male': 'piloto de automovilismo ~',
            'female': 'piloto de automovilismo ~'
        },
    },
    '~ basketball coach': {
        'ar': {
            'male': 'مدرب كرة سلة ~',
            'female': 'مدربة كرة سلة ~'
        },
        'en': {
            'male': '~ basketball coach',
            'female': '~ basketball coach'
        },
        'es': {
            'male': 'entrenador de baloncesto ~',
            'female': 'entrenadora de baloncesto ~'
        },
    },
    '~ violinist': {
        'ar': {
            'male': 'عازف كمان ~',
            'female': 'عازفة كمان ~'
        },
        'en': {
            'male': '~ violinist',
            'female': '~ violinist'
        },
        'es': {
            'male': 'violinista ~',
            'female': 'violinista ~'
        },
    },
    '~ virologist': {
        'ar': {
            'male': 'عالم فيروسات ~',
            'female': 'عالمة فيروسات ~'
        },
        'en': {
            'male': '~ virologist',
            'female': '~ virologist'
        },
        'es': {
            'male': 'virólogo ~',
            'female': 'viróloga ~'
        },
    },
    '~ rally driver': {
        'ar': {
            'male': 'سائق رالي ~',
            'female': 'سائقة رالي ~'
        },
        'en': {
            'male': '~ rally driver',
            'female': '~ rally driver'
        },
        'es': {
            'male': 'piloto de rally ~',
            'female': 'piloto de rally ~'
        },
    },
    '~ bishop': {
        # 'ar': { 'male': 'أسقف ~', 'female': 'أسقف ~' },
        'en': {
            'male': '~ bishop',
            'female': '~ bishop'
        },
        'es': {
            'male': 'obispo ~',
            'female': 'obispo ~'
        },
    },
    '~ pathologist': {
        'ar': {
            'male': 'عالم أمراض ~',
            'female': 'عالمة أمراض ~'
        },
        'en': {
            'male': '~ pathologist',
            'female': '~ pathologist'
        },
        'es': {
            'male': 'patólogo ~',
            'female': 'patóloga ~'
        },
    },
    '~ pharmacologist': {
        'ar': {
            'male': 'عالم صيدلية ~',
            'female': 'عالمة صيدلية ~'
        },
        'en': {
            'male': '~ pharmacologist',
            'female': '~ pharmacologist'
        },
        'es': {
            'male': 'farmacólogo ~',
            'female': 'farmacóloga ~'
        },
    },
    '~ rapper': {
        'ar': {
            'male': 'رابر ~',
            'female': 'مغنية راب ~'
        },
        'en': {
            'male': '~ rapper',
            'female': '~ rapper'
        },
        'es': {
            'male': 'rapero ~',
            'female': 'rapera ~'
        },
    },
    '~ saxophonist': {
        'ar': {
            'male': 'عازف ساكسفون ~',
            'female': 'عازفة ساكسفون ~'
        },
        'en': {
            'male': '~ saxophonist',
            'female': '~ saxophonist'
        },
        'es': {
            'male': 'saxofonista ~',
            'female': 'saxofonista ~'
        },
    },
    '~ scientist': {
        'ar': {
            'male': 'عالم ~',
            'female': 'عالمة ~'
        },
        'en': {
            'male': '~ scientist',
            'female': '~ scientist'
        },
        'es': {
            'male': 'científico ~',
            'female': 'científica ~'
        },
    },
    '~ singer-songwriter': {
        'ar': {
            'male': 'مغن مؤلف ~',
            'female': 'مغنية ومؤلفة ~'
        },
        'en': {
            'male': '~ singer-songwriter',
            'female': '~ singer-songwriter'
        },
        'es': {
            'male': 'cantautor ~',
            'female': 'cantautora ~'
        },
    },
    '~ radiologist': {
        'ar': {
            'male': 'أخصائي أشعة ~',
            'female': 'أخصائية أشعة ~'
        },
        'en': {
            'male': '~ radiologist',
            'female': '~ radiologist'
        },
        'es': {
            'male': 'radiólogo ~',
            'female': 'radióloga ~'
        },
    },
    '~ theatre director': {
        'ar': {
            'male': 'مخرج مسرح ~',
            'female': 'مخرجة مسرح ~'
        },
        'en': {
            'male': '~ theatre director',
            'female': '~ theatre director'
        },
        'es': {
            'male': 'director de teatro ~',
            'female': 'directora de teatro ~'
        },
    },
    '~ ski jumper': {
        'en': {
            'male': '~ ski jumper',
            'female': '~ ski jumper'
        },
        'es': {
            'male': 'saltador de esquí ~',
            'female': 'saltadora de esquí ~'
        },
    },
    '~ ethnologist': {
        'ar': {
            'male': 'عالم أثنولوجيا ~',
            'female': 'عالمة أثنولوجيا ~'
        },
        'en': {
            'male': '~ ethnologist',
            'female': '~ ethnologist'
        },
        'es': {
            'male': 'etnólogo ~',
            'female': 'etnóloga ~'
        },
    },
    '~ Esperantist': {
        'en': {
            'male': '~ Esperantist',
            'female': '~ Esperantist'
        },
        'es': {
            'male': 'esperantista ~',
            'female': 'esperantista ~'
        },
    },
    '~ lithographer': {
        'en': {
            'male': '~ lithographer',
            'female': '~ lithographer'
        },
        'es': {
            'male': 'litógrafo ~',
            'female': 'litógrafa ~'
        },
    },
    '~ handball player': {
        'ar': {
            'male': 'لاعب كرة يد ~',
            'female': 'لاعبة كرة يد ~'
        },
        'en': {
            'male': '~ handball player',
            'female': '~ handball player'
        },
        'es': {
            'male': 'balonmanista ~',
            'female': 'balonmanista ~'
        },
    },
    '~ geographer': {
        'ar': {
            'male': 'جغرافي ~',
            'female': 'جغرافية ~'
        },
        'en': {
            'male': '~ geographer',
            'female': '~ geographer'
        },
        'es': {
            'male': 'geógrafo ~',
            'female': 'geógrafa ~'
        },
    },
    '~ geologist': {
        'ar': {
            'male': 'جيولوجي ~',
            'female': 'جيولوجية ~'
        },
        'en': {
            'male': '~ geologist',
            'female': '~ geologist'
        },
        'es': {
            'male': 'geólogo ~',
            'female': 'geóloga ~'
        },
    },
    '~ theologian': {
        'ar': {
            'male': 'عالم عقيدة ~',
            'female': 'عالمة عقيدة ~'
        },
        'en': {
            'male': '~ theologian',
            'female': '~ theologian'
        },
        'es': {
            'male': 'teólogo ~',
            'female': 'teóloga ~'
        },
    },
    '~ volleyball player': {
        'ar': {
            'male': 'لاعب كرة طائرة ~',
            'female': 'لاعبة كرة طائرة ~'
        },
        'en': {
            'male': '~ volleyball player',
            'female': '~ volleyball player'
        },
        'es': {
            'male': 'jugador de voleibol ~',
            'female': 'jugadora de voleibol ~'
        },
    },
    '~ water polo player': {
        'ar': {
            'male': 'لاعب كرة ماء ~',
            'female': 'لاعبة كرة ماء ~'
        },
        'en': {
            'male': '~ water polo player',
            'female': '~ water polo player'
        },
        'es': {
            'male': 'jugador de waterpolo ~',
            'female': 'jugadora de waterpolo ~'
        },
    },
    '~ zoologist': {
        'ar': {
            'male': 'عالم حيوانات ~',
            'female': 'عالمة حيوانات ~'
        },
        'en': {
            'male': '~ zoologist',
            'female': '~ zoologist'
        },
        'es': {
            'male': 'zoólogo ~',
            'female': 'zoóloga ~'
        },
    },
    '~ archivist': {
        'ar': {
            'male': 'أمين أرشيف ~',
            'female': 'أمينة أرشيف ~'
        },
        'en': {
            'male': '~ archivist',
            'female': '~ archivist'
        },
        'es': {
            'male': 'archivero ~',
            'female': 'archivera ~'
        },
    },
    '~ rower': {
        'ar': {
            'male': 'مجدف ~',
            'female': 'مجدفة ~'
        },
        'en': {
            'male': '~ rower',
            'female': '~ rower'
        },
        'es': {
            'male': 'remero ~',
            'female': 'remera ~'
        },
    },
    '~ snowboarder': {
        'ar': {
            'male': 'متزلج ثلجي ~',
            'female': 'متزلجة ثلجية ~'
        },
        'en': {
            'male': '~ snowboarder',
            'female': '~ snowboarder'
        },
        'es': {
            'male': 'snowboarder ~',
            'female': 'snowboarder ~'
        },
    },
    '~ speleologist': {
        'ar': {
            'male': 'عالم كهوف ~',
            'female': 'عالمة كهوف ~'
        },
        'en': {
            'male': '~ speleologist',
            'female': '~ speleologist'
        },
        'es': {
            'male': 'espeleólogo ~',
            'female': 'espeleóloga ~'
        },
    },
    '~ spy': {
        'ar': {
            'male': 'جاسوس ~',
            'female': 'جاسوسة ~'
        },
        'en': {
            'male': '~ spy',
            'female': '~ spy'
        },
        'es': {
            'male': 'espía ~',
            'female': 'espía ~'
        },
    },
    '~ trade unionist': {
        'ar': {
            'male': 'نقابي ~',
            'female': 'نقابية ~'
        },
        'en': {
            'male': '~ trade unionist',
            'female': '~ trade unionist'
        },
        'es': {
            'male': 'sindicalista ~',
            'female': 'sindicalista ~'
        },
    },
    '~ troubadour': {
        'en': {
            'male': '~ troubadour',
            'female': '~ troubadour'
        },
        'es': {
            'male': 'trovador ~',
            'female': 'trovadora ~'
        },
    },
    '~ veterinarian': {
        'ar': {
            'male': 'طبيب بيطري ~',
            'female': 'طبيبة بيطرية ~'
        },
        'en': {
            'male': '~ veterinarian',
            'female': '~ veterinarian'
        },
        'es': {
            'male': 'veterinario ~',
            'female': 'veterinaria ~'
        },
    },
    '~ surgeon': {
        'ar': {
            'male': 'جراح ~',
            'female': 'جراحة ~'
        },
        'en': {
            'male': '~ surgeon',
            'female': '~ surgeon'
        },
        'es': {
            'male': 'cirujano ~',
            'female': 'cirujana ~'
        },
    },
    '~ academic': {
        'ar': {
            'male': 'أكاديمي ~',
            'female': 'أكاديمية ~'
        },
        'en': {
            'male': '~ academic',
            'female': '~ academic'
        },
        'es': {
            'male': 'académico ~',
            'female': 'académica ~'
        },
    },
    '~ archduke': {
        'ar': {
            'male': 'أرشيدوق ~',
            'female': 'أرشيدوقة ~'
        },
        'en': {
            'male': '~ archduke',
            'female': '~ archduke'
        },
    },
    '~ alpine skier': {
        'ar': {
            'male': 'متزحلق منحدرات ثلجية ~',
            'female': 'متزحلقة منحدرات ثلجية ~'
        },
        'en': {
            'male': '~ alpine skier',
            'female': '~ alpine skier'
        },
        'es': {
            'male': 'esquiador alpino ~',
            'female': 'esquiadora alpina ~'
        },
    },
    '~ cross-country skier': {
        'ar': {
            'male': 'متزلج ريفي ~',
            'female': 'متزلجة ريفية ~'
        },
        'en': {
            'male': '~ cross-country skier',
            'female': '~ cross-country skier'
        },
        'es': {
            'male': 'esquiador de fondo ~',
            'female': 'esquiadora de fondo ~'
        },
    },
    '~ chess player': {
        'ar': {
            'male': 'لاعب شطرنج ~',
            'female': 'لاعبة شطرنج ~'
        },
        'en': {
            'male': '~ chess player',
            'female': '~ chess player'
        },
        'es': {
            'male': 'ajedrecista ~',
            'female': 'ajedrecista ~'
        },
    },
    '~ caricaturist': {
        'ar': {
            'male': 'رسام كاريكاتير ~',
            'female': 'رسامة كاريكاتير ~'
        },
        'en': {
            'male': '~ caricaturist',
            'female': '~ caricaturist'
        },
        'es': {
            'male': 'caricaturista ~',
            'female': 'caricaturista ~'
        },
    },
    '~ chef': {
        'ar': {
            'male': 'طباخ ~',
            'female': 'طباخة ~'
        },
        'en': {
            'male': '~ chef',
            'female': '~ chef'
        },
        'es': {
            'male': 'chef ~',
            'female': 'chef ~'
        },
    },
    '~ boxer': {
        'ar': {
            'male': 'ملاكم ~',
            'female': 'ملاكمة ~'
        },
        'en': {
            'male': '~ boxer',
            'female': '~ boxer'
        },
        'es': {
            'male': 'boxeador ~',
            'female': 'boxeadora ~'
        },
    },
    '~ cartographer': {
        'ar': {
            'male': 'عالم خرائط ~',
            'female': 'عالمة خرائط ~'
        },
        'en': {
            'male': '~ cartographer',
            'female': '~ cartographer'
        },
        'es': {
            'male': 'cartógrafo ~',
            'female': 'cartógrafa ~'
        },
    },
    '~ dermatologist': {
        'ar': {
            'male': 'طبيب أمراض جلدية ~',
            'female': 'طبيبة أمراض جلدية ~'
        },
        'en': {
            'male': '~ dermatologist',
            'female': '~ dermatologist'
        },
        'es': {
            'male': 'dermatólogo ~',
            'female': 'dermatóloga ~'
        },
    },
    '~ biathlete': {
        'ar': {
            'male': 'لاعب بياثلون ~',
            'female': 'لاعبة بياثلون ~'
        },
        'en': {
            'male': '~ biathlete',
            'female': '~ biathlete'
        },
        'es': {
            'male': 'biatleta ~',
            'female': 'biatleta ~'
        },
    },
    '~ ice hockey player': {
        'ar': {
            'male': 'لاعب هوكي الجليد ~',
            'female': 'لاعبة هوكي الجليد ~'
        },
        'en': {
            'male': '~ ice hockey player',
            'female': '~ ice hockey player'
        },
        'es': {
            'male': 'jugador de hockey sobre hielo ~',
            'female': 'jugadora de hockey sobre hielo ~'
        },
    },
    '~ field hockey player': {
        'ar': {
            'male': 'لاعب هوكي الحقل ~',
            'female': 'لاعبة هوكي الحقل ~'
        },
        'en': {
            'male': '~ field hockey player',
            'female': '~ field hockey player'
        },
        'es': {
            'male': 'jugador de hockey sobre hierba ~',
            'female': 'jugadora de hockey sobre hierba ~'
        },
    },
    '~ geneticist': {
        'ar': {
            'male': 'عالم وراثة ~',
            'female': 'عالمة وراثة ~'
        },
        'en': {
            'male': '~ geneticist',
            'female': '~ geneticist'
        },
        'es': {
            'male': 'genetista ~',
            'female': 'genetista ~'
        },
    },
    '~ guitarist': {
        'ar': {
            'male': 'عازف قيثارة ~',
            'female': 'عازفة قيثارة ~'
        },
        'en': {
            'male': '~ guitarist',
            'female': '~ guitarist'
        },
        'es': {
            'male': 'guitarrista ~',
            'female': 'guitarrista ~'
        },
    },
    '~ gymnast': {
        'ar': {
            'male': 'لاعب جمباز ~',
            'female': 'لاعبة جمباز ~'
        },
        'en': {
            'male': '~ gymnast',
            'female': '~ gymnast'
        },
        'es': {
            'male': 'gimnasta ~',
            'female': 'gimnasta ~'
        },
    },
    '~ gynaecologist': {
        'ar': {
            'male': 'أخصائي أمراض نسائية ~',
            'female': 'أخصائية أمراض نسائية ~'
        },
        'en': {
            'male': '~ gynaecologist',
            'female': '~ gynaecologist'
        },
        'es': {
            'male': 'ginecólogo ~',
            'female': 'ginecóloga ~'
        },
    },
    '~ judoka': {
        'ar': {
            'male': 'لاعب جودو ~',
            'female': 'لاعبة جودو ~'
        },
        'en': {
            'male': '~ judoka',
            'female': '~ judoka'
        },
        'es': {
            'male': 'yudoca ~',
            'female': 'yudoca ~'
        },
    },
    '~ legal historian': {
        'ar': {
            'male': 'مؤرخ قانون ~',
            'female': 'مؤرخة قانون ~'
        },
        'en': {
            'male': '~ legal historian',
            'female': '~ legal historian'
        },
        'es': {
            'male': 'historiador del derecho ~',
            'female': 'historiadora del derecho ~'
        },
    },
    '~ librarian': {
        'ar': {
            'male': 'أمين مكتبة ~',
            'female': 'أمينة مكتبة ~'
        },
        'en': {
            'male': '~ librarian',
            'female': '~ librarian'
        },
        'es': {
            'male': 'bibliotecario ~',
            'female': 'bibliotecaria ~'
        },
    },
    '~ linguist': {
        'ar': {
            'male': 'لغوي ~',
            'female': 'لغوية ~'
        },
        'en': {
            'male': '~ linguist',
            'female': '~ linguist'
        },
        'es': {
            'male': 'lingüista ~',
            'female': 'lingüista ~'
        },
    },
    '~ literary critic': {
        'ar': {
            'male': 'ناقد أدبي ~',
            'female': 'ناقدة أدبية ~'
        },
        'en': {
            'male': '~ literary critic',
            'female': '~ literary critic'
        },
        'es': {
            'male': 'crítico literario ~',
            'female': 'crítica literaria ~'
        },
    },
    '~ association football referee': {
        'ar': {
            'male': 'حكم كرة قدم ~',
            'female': 'حكمة كرة قدم ~'
        },
        'en': {
            'male': '~ association football referee',
            'female': '~ association football referee'
        },
        'es': {
            'male': 'árbitro de fútbol ~',
            'female': 'árbitra de fútbol ~'
        },
    },
    '~ anatomist': {
        'ar': {
            'male': 'عالم تشريح ~',
            'female': 'عالمة تشريح ~'
        },
        'en': {
            'male': '~ anatomist',
            'female': '~ anatomist'
        },
        'es': {
            'male': 'anatomista ~',
            'female': 'anatomista ~'
        },
    },
    '~ anthropologist': {
        'ar': {
            'male': 'عالم أنثروبولوجيا ~',
            'female': 'عالمة أنثروبولوجيا ~'
        },
        'en': {
            'male': '~ anthropologist',
            'female': '~ anthropologist'
        },
        'es': {
            'male': 'antropólogo ~',
            'female': 'antropóloga ~'
        },
    },
    '~ archaeologist': {
        'ar': {
            'male': 'عالم آثار ~',
            'female': 'عالمة آثار ~'
        },
        'en': {
            'male': '~ archaeologist',
            'female': '~ archaeologist'
        },
        'es': {
            'male': 'arqueólogo ~',
            'female': 'arqueóloga ~'
        },
    },
    '~ archer': {
        'ar': {
            'male': 'نبال ~',
            'female': 'نبالة ~'
        },
        'en': {
            'male': '~ archer',
            'female': '~ archer'
        },
        'es': {
            'male': 'arquero ~',
            'female': 'arquera ~'
        },
    },
    '~ biologist': {
        'ar': {
            'male': 'عالم أحياء ~',
            'female': 'عالمة أحياء ~'
        },
        'en': {
            'male': '~ biologist',
            'female': '~ biologist'
        },
        'es': {
            'male': 'biólogo ~',
            'female': 'bióloga ~'
        },
    },
    '~ egyptologist': {
        'ar': {
            'male': 'عالم مصريات ~',
            'female': 'عالمة مصريات ~'
        },
        'en': {
            'male': '~ egyptologist',
            'female': '~ egyptologist'
        },
        'es': {
            'male': 'egiptólogo ~',
            'female': 'egiptóloga ~'
        },
    },
    '~ film critic': {
        'ar': {
            'male': 'ناقد أفلام ~',
            'female': 'ناقدة أفلام ~'
        },
        'en': {
            'male': '~ film critic',
            'female': '~ film critic'
        },
        'es': {
            'male': 'crítico de cine ~',
            'female': 'crítica de cine ~'
        },
    },
    '~ flying ace': {
        'ar': {
            'male': 'طيار عسكري ~',
            'female': 'قائدة طيارة عسكرية ~'
        },
        'en': {
            'male': '~ flying ace',
            'female': '~ flying ace'
        },
        'es': {
            'male': 'as de la aviación ~',
            'female': 'as de la aviación ~'
        },
    },
    '~ mineralogist': {
        'ar': {
            'male': 'عالم معادن ~',
            'female': 'عالمة معادن ~'
        },
        'en': {
            'male': '~ mineralogist',
            'female': '~ mineralogist'
        },
        'es': {
            'male': 'mineralogista ~',
            'female': 'mineralogista ~'
        },
    },
    '~ missionary': {
        'ar': {
            'male': 'مبشر ~',
            'female': 'مبشرة ~'
        },
        'en': {
            'male': '~ missionary',
            'female': '~ missionary'
        },
        'es': {
            'male': 'misionero ~',
            'female': 'misionera ~'
        },
    },
    '~ motorcycle racer': {
        'ar': {
            'male': 'متسابق دراجات نارية ~',
            'female': 'متسابقة دراجات نارية ~'
        },
        'en': {
            'male': '~ motorcycle racer',
            'female': '~ motorcycle racer'
        },
        'es': {
            'male': 'piloto de motociclismo ~',
            'female': 'piloto de motociclismo ~'
        },
    },
    '~ musicologist': {
        'ar': {
            'male': 'عالم موسيقي ~',
            'female': 'عالمة موسيقي ~'
        },
        'en': {
            'male': '~ musicologist',
            'female': '~ musicologist'
        },
        'es': {
            'male': 'musicólogo ~',
            'female': 'musicóloga ~'
        },
    },
    '~ mycologist': {
        'ar': {
            'male': 'أخصائي فطريات ~',
            'female': 'أخصائية فطريات ~'
        },
        'en': {
            'male': '~ mycologist',
            'female': '~ mycologist'
        },
        'es': {
            'male': 'micólogo ~',
            'female': 'micóloga ~'
        },
    },
    '~ naturalist': {
        'ar': {
            'male': 'عالم طبيعة ~',
            'female': 'عالمة طبيعة ~'
        },
        'en': {
            'male': '~ naturalist',
            'female': '~ naturalist'
        },
        'es': {
            'male': 'naturalista ~',
            'female': 'naturalista ~'
        },
    },
    '~ neurologist': {
        'ar': {
            'male': 'طبيب أعصاب ~',
            'female': 'طبيبة أعصاب ~'
        },
        'en': {
            'male': '~ neurologist',
            'female': '~ neurologist'
        },
        'es': {
            'male': 'neurólogo ~',
            'female': 'neuróloga ~'
        },
    },
    '~ essayist': {
        'ar': {
            'male': 'كاتب مقالات ~',
            'female': 'كاتبة مقالات ~'
        },
        'en': {
            'male': '~ essayist',
            'female': '~ essayist'
        },
        'es': {
            'male': 'ensayista ~',
            'female': 'ensayista ~'
        },
    },
    '~ engraver': {
        'ar': {
            'male': 'نقاش ~',
            'female': 'نقاشة ~'
        },
        'en': {
            'male': '~ engraver',
            'female': '~ engraver'
        },
        'es': {
            'male': 'grabador ~',
            'female': 'grabadora ~'
        },
    },
    '~ oncologist': {
        'ar': {
            'male': 'طبيب أورام ~',
            'female': 'طبيبة أورام ~'
        },
        'en': {
            'male': '~ oncologist',
            'female': '~ oncologist'
        },
        'es': {
            'male': 'oncólogo ~',
            'female': 'oncóloga ~'
        },
    },
    '~ opera singer': {
        'ar': {
            'male': 'فنان أوبرا ~',
            'female': 'فنانة أوبرا ~'
        },
        'en': {
            'male': '~ opera singer',
            'female': '~ opera singer'
        },
        'es': {
            'male': 'cantante de ópera ~',
            'female': 'cantante de ópera ~'
        },
    },
    '~ ophthalmologist': {
        'ar': {
            'male': 'طبيب عيون ~',
            'female': 'طبيبة عيون ~'
        },
        'en': {
            'male': '~ ophthalmologist',
            'female': '~ ophthalmologist'
        },
        'es': {
            'male': 'oftalmólogo ~',
            'female': 'oftalmóloga ~'
        },
    },
    '~ organist': {
        'ar': {
            'male': 'عازف أورغن ~',
            'female': 'عازفة أورغن ~'
        },
        'en': {
            'male': '~ organist',
            'female': '~ organist'
        },
        'es': {
            'male': 'organista ~',
            'female': 'organista ~'
        },
    },
    '~ orientalist': {
        'ar': {
            'male': 'مستشرق ~',
            'female': 'مستشرقة ~'
        },
        'en': {
            'male': '~ orientalist',
            'female': '~ orientalist'
        },
        'es': {
            'male': 'orientalista ~',
            'female': 'orientalista ~'
        },
    },
    '~ ornithologist': {
        'ar': {
            'male': 'عالم طيور ~',
            'female': 'عالمة طيور ~'
        },
        'en': {
            'male': '~ ornithologist',
            'female': '~ ornithologist'
        },
        'es': {
            'male': 'ornitólogo ~',
            'female': 'ornitóloga ~'
        },
    },
}
# ---
translationsOccupations = {
    '~ cartoonist': {
        'ar': {
            'male': 'رسام كارتون ~',
            'female': 'رسامة كارتون ~'
        },
        'en': {
            'male': '~ cartoonist',
            'female': '~ cartoonist'
        },
    },
    '~ businessman and philanthropist': {
        'ar': {
            'male': 'فاعل خير ورائد أعمال ~',
            'female': 'فاعلة خير ورائدة أعمال ~'
        },
        'en': {
            'male': '~ businessman and philanthropist',
            'female': '~ businesswomen and philanthropist'
        },
    },
    '~ philanthropist': {
        'ar': {
            'male': 'فاعل خير ~',
            'female': 'فاعلة خير ~'
        },
        'en': {
            'male': '~ philanthropist',
            'female': '~ philanthropist'
        },
    },
    '~ pharmacist': {
        'ar': {
            'male': 'صيدلي ~',
            'female': 'صيدلية ~'
        },
        'en': {
            'male': '~ pharmacist',
            'female': '~ pharmacist'
        },
        'es': {
            'male': 'farmacéutico ~',
            'female': 'farmacéutica ~'
        },
    },
    '~ archbishop': {
        'ar': {
            'male': 'رئيس أساقفة ~',
            'female': 'رئيسة أساقفة ~'
        },
        'en': {
            'male': '~ archbishop',
            'female': '~ archbishop'
        },
        'es': {
            'male': 'arzobispo ~',
            'female': 'arzobispo ~'
        },
    },
    '~ activist': {
        'ar': {
            'male': 'ناشط ~',
            'female': 'ناشطة ~'
        },
        'en': {
            'male': '~ activist',
            'female': '~ activist'
        },
    },
    '~ actor': {
        'ar': {
            'male': 'ممثل ~',
            'female': 'ممثلة ~'
        },
        'bn': {
            'male': '~ অভিনেতা',
            'female': '~ অভিনেত্রী'
        },
        'ca': {
            'male': 'actor ~',
            'female': 'actriu ~'
        },
        'en': {
            'male': '~ actor',
            'female': '~ actress'
        },
        'es': {
            'male': 'actor ~',
            'female': 'actriz ~'
        },
        'et': {
            'male': '~ näitleja',
            'female': '~ näitleja'
        },
        'fr': {
            'male': 'acteur ~',
            'female': 'actrice ~'
        },
        'gl': {
            'male': 'actor ~',
            'female': 'actriz ~'
        },
        'he': {
            'male': 'שחקן ~',
            'female': 'שחקנית ~'
        },
        'ro': {
            'male': 'actor ~',
            'female': 'actriță ~'
        },
        'sq': {
            'male': 'aktor ~',
            'female': 'aktore ~'
        },
    },
    '~ actress': {
        'ar': {
            'male': 'ممثل ~',
            'female': 'ممثلة ~'
        },
        'bn': {
            'male': '~ অভিনেতা',
            'female': '~ অভিনেত্রী'
        },
        'ca': {
            'male': 'actor ~',
            'female': 'actriu ~'
        },
        'en': {
            'male': '~ actor',
            'female': '~ actress'
        },
        'es': {
            'male': 'actor ~',
            'female': 'actriz ~'
        },
        'fr': {
            'male': 'acteur ~',
            'female': 'actrice ~'
        },
        'gl': {
            'male': 'actor ~',
            'female': 'actriz ~'
        },
        'he': {
            'male': 'שחקן ~',
            'female': 'שחקנית ~'
        },
        'ro': {
            'male': 'actor ~',
            'female': 'actriță ~'
        },
    },
    '~ architect': {
        'ar': {
            'male': 'مهندس معماري ~',
            'female': 'مهندسة معمارية ~'
        },
        'bn': {
            'male': '~ স্থপতি',
            'female': '~ স্থপতি'
        },
        'ca': {
            'male': 'arquitecte ~',
            'female': 'arquitecta ~'
        },
        'en': {
            'male': '~ architect',
            'female': '~ architect'
        },
        'es': {
            'male': 'arquitecto ~',
            'female': 'arquitecta ~'
        },
        'et': {
            'male': '~ arhitekt',
            'female': '~ arhitekt'
        },
        'fr': {
            'male': 'architecte ~',
            'female': 'architecte ~'
        },
        'gl': {
            'male': 'arquitecto ~',
            'female': 'arquitecta ~'
        },
        'he': {
            'male': 'אדריכל ~',
            'female': 'אדריכלית ~'
        },
        'ro': {
            'male': 'arhitect ~',
            'female': 'arhitectă ~'
        },
        'sq': {
            'male': 'arkitekt ~',
            'female': 'arkitekte ~'
        },
    },
    '~ art historian': {
        'ar': {
            'male': 'مؤرخ فن ~',
            'female': 'مؤرخة فن ~'
        },
        'bn': {
            'male': '~ শিল্প ইতিহাসবিদ',
            'female': '~ শিল্প ইতিহাসবিদ'
        },
        'ca': {
            'male': "historiador de l'art ~",
            'female': "historiadora de l'art ~"
        },
        'en': {
            'male': '~ art historian',
            'female': '~ art historian'
        },
        'es': {
            'male': 'historiador del arte ~',
            'female': 'historiadora del arte ~'
        },
        'et': {
            'male': '~ kunstiajaloolane',
            'female': '~ kunstiajaloolane'
        },
        'fr': {
            'male': "historien de l'art ~",
            'female': "historienne de l'art ~"
        },
        'gl': {
            'male': 'historiador da arte ~',
            'female': 'historiadora da arte ~'
        },
        'he': {
            'male': 'היסטוריון אמנות ~',
            'female': 'היסטוריונית אמנות ~'
        },
        'ro': {
            'male': 'istoric al artei ~',
            'female': 'istorică ~ a artei'
        },
        'sq': {
            'male': 'historian ~ i artit',
            'female': 'historiane ~ e artit'
        },
    },
    '~ artist': {
        'ar': {
            'male': 'فنان ~',
            'female': 'فنانة ~'
        },
        'bn': {
            'male': '~ শিল্পী',
            'female': '~ শিল্পী'
        },
        'ca': {
            'male': 'artista ~',
            'female': 'artista ~'
        },
        'en': {
            'male': '~ artist',
            'female': '~ artist'
        },
        'es': {
            'male': 'artista ~',
            'female': 'artista ~'
        },
        'et': {
            'male': '~ kunstnik',
            'female': '~ kunstnik'
        },
        'fr': {
            'male': 'artiste ~',
            'female': 'artiste ~'
        },
        'gl': {
            'male': 'artista ~',
            'female': 'artista ~'
        },
        'he': {
            'male': 'אמן ~',
            'female': 'אמנית ~'
        },
        'ro': {
            'male': 'artist ~',
            'female': 'artistă ~'
        },
        'sq': {
            'male': 'artist ~',
            'female': 'artiste ~'
        },
    },
    '~ association football player': {
        'ar': {
            'male': 'لاعب كرة قدم ~',
            'female': 'لاعبة كرة قدم ~'
        },
        'bn': {
            'male': '~ ফুটবল খেলোয়াড়',
            'female': '~ ফুটবল খেলোয়াড়'
        },
        'ca': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'en': {
            'male': '~ association football player',
            'female': '~ association football player'
        },
        'es': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'et': {
            'male': '~ jalgpallur',
            'female': '~ jalgpallur'
        },
        'fr': {
            'male': 'joueur de football ~',
            'female': 'joueuse de football ~'
        },
        'gl': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'he': {
            'male': 'שחקן כדורגל ~',
            'female': 'שחקנית כדורגל ~'
        },
        'ro': {
            'male': 'fotbalist ~',
            'female': 'fotbalistă ~'
        },
        'sq': {
            'male': 'futbollist ~',
            'female': 'futbolliste ~'
        },
    },
    '~ association football manager': {
        'ar': {
            'male': 'مدرب كرة قدم ~',
            'female': 'مدربة كرة قدم ~'
        },
        'bn': {
            'male': '~ ফুটবল ম্যানেজার',
            'female': '~ ফুটবল ম্যানেজার'
        },
        'ca': {
            'male': 'entrenador de futbol ~',
            'female': 'entrenadora de futbol ~'
        },
        'en': {
            'male': '~ association football manager',
            'female': '~ association football manager'
        },
        'es': {
            'male': 'entrenador de fútbol ~',
            'female': 'entrenadora de fútbol ~'
        },
        'et': {
            'male': '~ jalgpallitreener',
            'female': '~ jalgpallitreener'
        },
        'fr': {
            'male': 'entraîneur de football ~',
            'female': 'entraîneuse de football ~'
        },
        'gl': {
            'male': 'adestrador ~',
            'female': 'adestradora ~'
        },
        'he': {
            'male': 'מאמן כדורגל ~',
            'female': 'מאמנת כדורגל ~'
        },
        'ro': {
            'male': 'antrenor de fotbal ~',
            'female': 'antrenoare de fotbal ~'
        },
        'sq': {
            'male': 'menaxher futbolli ~',
            'female': 'menaxhere futbolli ~'
        },
    },
    '~ astronomer': {
        'ar': {
            'male': 'عالم فلك ~',
            'female': 'عالمة فلك ~'
        },
        'bn': {
            'male': '~ জ্যোতির্বিদ',
            'female': '~ জ্যোতির্বিদ'
        },
        'ca': {
            'male': 'astrònom ~',
            'female': 'astrònoma ~'
        },
        'en': {
            'male': '~ astronomer',
            'female': '~ astronomer'
        },
        'es': {
            'male': 'astrónomo ~',
            'female': 'astrónoma ~'
        },
        'et': {
            'male': '~ astronoom',
            'female': '~ astronoom'
        },
        'fr': {
            'male': 'astronome ~',
            'female': 'astronome ~'
        },
        'gl': {
            'male': 'astrónomo ~',
            'female': 'astrónoma ~'
        },
        'he': {
            'male': 'אסטרונום ~',
            'female': 'אסטרונומית ~'
        },
        'ro': {
            'male': 'astronom ~',
            'female': 'astronomă ~'
        },
        'sq': {
            'male': 'astronom ~',
            'female': 'astronome ~'
        },
    },
    '~ athlete': {
        'ar': {
            'male': 'رياضي ~',
            'female': 'رياضية ~'
        },
        'bn': {
            'male': '~ অ্যাথলেট',
            'female': '~ অ্যাথলেট'
        },
        'ca': {
            'male': 'atleta ~',
            'female': 'atleta ~'
        },
        'en': {
            'male': '~ athlete',
            'female': '~ athlete'
        },
        'es': {
            'male': 'atleta ~',
            'female': 'atleta ~'
        },
        'et': {
            'male': '~ sportlane',
            'female': '~ sportlane'
        },
        'fr': {
            'male': 'athlète ~',
            'female': 'athlète ~'
        },
        'gl': {
            'male': 'atleta ~',
            'female': 'atleta ~'
        },
        'he': {
            'male': 'אתלט ~',
            'female': 'אתלטית ~'
        },
        'ro': {
            'male': 'atlet ~',
            'female': 'atletă ~'
        },
        'sq': {
            'male': 'atlet ~',
            'female': 'atlete ~'
        },
    },
    '~ athletics competitor': {
        'ar': {
            'male': 'رياضي ~',
            'female': 'رياضية ~'
        },
        'bn': {
            'male': '~ অ্যাথলেটিক্স প্রতিযোগী',
            'female': '~ অ্যাথলেটিক্স প্রতিযোগী'
        },
        'ca': {
            'male': 'atleta ~',
            'female': 'atleta ~'
        },
        'en': {
            'male': '~ athletics competitor',
            'female': '~ athletics competitor'
        },
        'es': {
            'male': 'atleta ~',
            'female': 'atleta ~'
        },
        'et': {
            'male': '~ kergejõustiklane',
            'female': '~ kergejõustiklane'
        },
        'fr': {
            'male': 'athlète ~',
            'female': 'athlète ~'
        },
        'gl': {
            'male': 'atleta ~',
            'female': 'atleta ~'
        },
        'he': {
            'male': 'אתלט ~',
            'female': 'אתלטית ~'
        },
        'ro': {
            'male': 'atlet ~',
            'female': 'atletă ~'
        },
        'sq': {
            'male': 'atlet ~',
            'female': 'atlet ~'
        },
    },
    '~ basketball player': {
        'ar': {
            'male': 'لاعب كرة سلة ~',
            'female': 'لاعبة كرة سلة ~'
        },
        'bn': {
            'male': '~ বাস্কেটবল খেলোয়াড়',
            'female': '~ বাস্কেটবল খেলোয়াড়'
        },
        'ca': {
            'male': 'jugador de bàsquet ~',
            'female': 'jugadora de bàsquet ~'
        },
        'en': {
            'male': '~ basketball player',
            'female': '~ basketball player'
        },
        'es': {
            'male': 'baloncestista ~',
            'female': 'baloncestista ~'
        },
        'et': {
            'male': '~ korvpallur',
            'female': '~ korvpallur'
        },
        'fr': {
            'male': 'joueur de basket-ball ~',
            'female': 'joueuse de basket-ball ~'
        },
        'gl': {
            'male': 'baloncestista ~',
            'female': 'baloncestista ~'
        },
        'he': {
            'male': 'שחקן כדורסל ~',
            'female': 'שחקנית כדורסל ~'
        },
        'ro': {
            'male': 'baschetbalist ~',
            'female': 'baschetbalistă ~'
        },
        'sq': {
            'male': 'basketbollist ~',
            'female': 'basketbolliste ~'
        },
    },
    '~ bicycle racer': {
        'ar': {
            'male': 'دراج ~',
            'female': 'متسابقة دراجات ~'
        },
        'bn': {
            'male': '~ বাইসাইকেল প্রতিযোগী',
            'female': '~ বাইসাইকেল প্রতিযোগী'
        },
        'ca': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'en': {
            'male': '~ bicycle racer',
            'female': '~ bicycle racer'
        },
        'es': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'et': {
            'male': '~ jalgrattur',
            'female': '~ jalgrattur'
        },
        'fr': {
            'male': 'cycliste ~',
            'female': 'cycliste ~'
        },
        'gl': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'he': {
            'male': 'רוכב אופניים ~',
            'female': 'רוכבת אופניים ~'
        },
        'ro': {
            'male': 'ciclist ~',
            'female': 'ciclistă ~'
        },
        'sq': {
            'male': 'çiklist ~',
            'female': 'çikliste ~'
        },
    },
    '~ botanist': {
        'ar': {
            'male': 'عالم نبات ~',
            'female': 'عالمة نبات ~'
        },
        'bn': {
            'male': '~ উদ্ভিদবিদ',
            'female': '~ উদ্ভিদবিদ'
        },
        'ca': {
            'male': 'botànic ~',
            'female': 'botànica ~'
        },
        'en': {
            'male': '~ botanist',
            'female': '~ botanist'
        },
        'es': {
            'male': 'botánico ~',
            'female': 'botánica ~'
        },
        'et': {
            'male': '~ botaanik',
            'female': '~ botaanik'
        },
        'fr': {
            'male': 'botaniste ~',
            'female': 'botaniste ~'
        },
        'gl': {
            'male': 'botánico ~',
            'female': 'botánica ~'
        },
        'he': {
            'male': 'בוטנאי ~',
            'female': 'בוטנאית ~'
        },
        'ro': {
            'male': 'botanist ~',
            'female': 'botanistă ~'
        },
        'sq': {
            'male': 'botanist ~',
            'female': 'botaniste ~'
        },
    },
    '~ businessman': {
        'ar': {
            'male': 'رائد أعمال ~',
            'female': 'رائدة أعمال ~'
        },
        'en': {
            'male': '~ businessman',
            'female': '~ businesswomen'
        },
    },
    '~ businessperson': {
        'ar': {
            'male': 'رائد أعمال ~',
            'female': 'رائدة أعمال ~'
        },
        'bn': {
            'male': '~ ব্যবসায়ী',
            'female': '~ ব্যবসায়ী'
        },
        'ca': {
            'male': 'empresari ~',
            'female': 'empresària ~'
        },
        'en': {
            'male': '~ businessperson',
            'female': '~ businessperson'
        },
        'es': {
            'male': 'empresario ~',
            'female': 'empresaria ~'
        },
        'et': {
            'male': '~ ärimees',
            'female': '~ ärinaine'
        },
        'fr': {
            'male': "homme d'affaires ~",
            'female': "femme d'affaires ~"
        },
        'gl': {
            'male': 'empresario ~',
            'female': 'empresaria ~'
        },
        'he': {
            'male': 'איש עסקים ~',
            'female': 'אשת עסקים ~'
        },
        'ro': {
            'male': 'om de afaceri ~',
            'female': 'femeie de afaceri ~'
        },
        'sq': {
            'male': 'biznesmen ~',
            'female': 'biznesmene ~'
        },
    },
    '~ businesswomen': {
        'ar': {
            'male': 'رائد أعمال ~',
            'female': 'رائدة أعمال ~'
        },
        'en': {
            'male': '~ businessman',
            'female': '~ businesswomen'
        },
    },
    '~ catholic priest': {
        'ar': {
            'male': 'قس كاثوليكي ~',
            'female': ''
        },
        'bn': {
            'male': '~ ক্যাথলিক পুরোহিত',
            'female': '~ ক্যাথলিক পুরোহিত'
        },
        'ca': {
            'male': 'sacerdot catòlic ~',
            'female': 'sacerdot catòlica ~'
        },
        'en': {
            'male': '~ catholic priest',
            'female': '~ catholic priest'
        },
        'es': {
            'male': 'sacerdote católico ~',
            'female': 'sacerdote católica ~'
        },
        'et': {
            'male': '~ katoliku preester',
            'female': '~ katoliku preester'
        },
        'fr': {
            'male': 'prêtre catholique ~',
            'female': 'prêtresse catholique ~'
        },
        'gl': {
            'male': 'sacerdote católico ~',
            'female': 'sacerdote católica ~'
        },
        'he': {
            'male': 'כומר קתולי ~',
            'female': 'כומרה קתולית ~'
        },
        'ro': {
            'male': 'preot catolic ~',
            'female': 'preoteasă catolică ~'
        },
        'sq': {
            'male': 'prift katolik ~',
            'female': 'priftëreshë katolike ~'
        },
    },
    '~ Catholic priest': {
        'ar': {
            'male': 'قس كاثوليكي ~',
            'female': ''
        },
        'bn': {
            'male': '~ ক্যাথলিক পুরোহিত',
            'female': '~ ক্যাথলিক পুরোহিত'
        },
        'ca': {
            'male': 'sacerdot catòlic ~',
            'female': 'sacerdot catòlica ~'
        },
        'en': {
            'male': '~ Catholic priest',
            'female': '~ Catholic priest'
        },
        'es': {
            'male': 'sacerdote católico ~',
            'female': 'sacerdote católica ~'
        },
        'et': {
            'male': '~ katoliku preester',
            'female': '~ katoliku preester'
        },
        'fr': {
            'male': 'prêtre catholique ~',
            'female': 'prêtresse catholique ~'
        },
        'gl': {
            'male': 'sacerdote católico ~',
            'female': 'sacerdote católica ~'
        },
        'he': {
            'male': 'כומר קתולי ~',
            'female': 'כומרה קתולית ~'
        },
        'ro': {
            'male': 'preot catolic ~',
            'female': 'preot catolic ~'
        },
        'sq': {
            'male': 'prift katolik ~',
            'female': 'priftëreshë katolike ~'
        },
    },
    '~ chemist': {
        'ar': {
            'male': 'كيميائي ~',
            'female': 'كيميائية ~'
        },
        'bn': {
            'male': '~ রসায়নবিদ',
            'female': '~ রসায়নবিদ'
        },
        'ca': {
            'male': 'químic ~',
            'female': 'química ~'
        },
        'en': {
            'male': '~ chemist',
            'female': '~ chemist'
        },
        'es': {
            'male': 'químico ~',
            'female': 'química ~'
        },
        'et': {
            'male': '~ keemik',
            'female': '~ keemik'
        },
        'fr': {
            'male': 'chimiste ~',
            'female': 'chimiste ~'
        },
        'gl': {
            'male': 'químico ~',
            'female': 'química ~'
        },
        'he': {
            'male': 'כימאי ~',
            'female': 'כימאית ~'
        },
        'ro': {
            'male': 'chimist ~',
            'female': 'chimistă ~'
        },
        'sq': {
            'male': 'kimist ~',
            'female': 'kimiste ~'
        },
    },
    "~ children's writer": {
        'ar': {
            'male': 'كاتب أدب أطفال ~',
            'female': 'كاتبة أدب أطفال ~'
        },
        'bn': {
            'male': "~ শিশু সাহিত্যিক",
            'female': "~ শিশু সাহিত্যিক"
        },
        'ca': {
            'male': 'escriptor de literatura infantil ~',
            'female': 'escriptora de literatura infantil ~'
        },
        'en': {
            'male': "~ children's writer",
            'female': "~ children's writer"
        },
        'es': {
            'male': 'escritor de literatura infantil ~',
            'female': 'escritora de literatura infantil ~'
        },
        'et': {
            'male': '~ lastekirjanik',
            'female': '~ lastekirjanik'
        },
        'fr': {
            'male': "auteur de littérature d'enfance ~",
            'female': "auteure de littérature d'enfance ~"
        },
        'gl': {
            'male': 'escritor de literatura infantil ~',
            'female': 'escritora de literatura infantil ~'
        },
        'he': {
            'male': 'סופר ילדים ~',
            'female': 'סופרת ילדים ~'
        },
        'ro': {
            'male': 'scriitor de literatură pentru copii ~',
            'female': 'scriitoare de literatură pentru copii ~'
        },
        'sq': {
            'male': 'shkrimtar për fëmijë ~',
            'female': 'shkrimtare për fëmijë ~'
        },
    },
    '~ choreographer': {
        'ar': {
            'male': 'مصمم رقص ~',
            'female': 'مصممة رقص ~'
        },
        'bn': {
            'male': '~ কোরিওগ্রাফার',
            'female': '~ কোরিওগ্রাফার'
        },
        'ca': {
            'male': 'coreògraf ~',
            'female': 'coreògrafa ~'
        },
        'en': {
            'male': '~ choreographer',
            'female': '~ choreographer'
        },
        'es': {
            'male': 'coreógrafo ~',
            'female': 'coreógrafa ~'
        },
        'et': {
            'male': '~ koreograaf',
            'female': '~ koreograaf'
        },
        'fr': {
            'male': 'chorégraphe ~',
            'female': 'chorégraphe ~'
        },
        'gl': {
            'male': 'coreógrafo ~',
            'female': 'coreógrafa ~'
        },
        'he': {
            'male': 'כוריאוגרף ~',
            'female': 'כוריאוגרפית ~'
        },
        'ro': {
            'male': 'coregraf ~',
            'female': 'coregrafă ~'
        },
        'sq': {
            'male': 'koreograf ~',
            'female': 'koreografe ~'
        },
    },
    '~ comics artist': {
        'ar': {
            'male': 'فنان قصص مصورة ~',
            'female': 'فنانة قصص مصورة ~'
        },
        'bn': {
            'male': '~ কমিক শিল্পী',
            'female': '~ কমিক শিল্পী'
        },
        'ca': {
            'male': 'dibuixant de còmics ~',
            'female': 'dibuixant de còmics ~'
        },
        'en': {
            'male': '~ comics artist',
            'female': '~ comics artist'
        },
        'es': {
            'male': 'historietista ~',
            'female': 'historietista ~'
        },
        'et': {
            'male': '~ koomiksikunstnik',
            'female': '~ koomiksikunstnik'
        },
        'fr': {
            'male': 'auteur de bande dessinée ~',
            'female': 'auteure de bande dessinée ~'
        },
        'gl': {
            'male': 'historietista ~',
            'female': 'historietista ~'
        },
        'he': {
            'male': 'אמן קומיקס ~',
            'female': 'אמנית קומיקס ~'
        },
        'ro': {
            'male': 'autor de benzi desenate ~',
            'female': 'autoare de benzi desenate ~'
        },
        'sq': {
            'male': 'artist komikësh ~',
            'female': 'artiste komikësh ~'
        },
    },
    '~ composer': {
        'ar': {
            'male': 'ملحن ~',
            'female': 'ملحنة ~'
        },
        'bn': {
            'male': '~ সঙ্গীত রচয়িতা',
            'female': '~ সঙ্গীত রচয়িতা'
        },
        'ca': {
            'male': 'compositor ~',
            'female': 'compositora ~'
        },
        'en': {
            'male': '~ composer',
            'female': '~ composer'
        },
        'es': {
            'male': 'compositor ~',
            'female': 'compositora ~'
        },
        'et': {
            'male': '~ helilooja',
            'female': '~ helilooja'
        },
        'fr': {
            'male': 'compositeur ~',
            'female': 'compositrice ~'
        },
        'gl': {
            'male': 'compositor ~',
            'female': 'compositora ~'
        },
        'he': {
            'male': 'מלחין ~',
            'female': 'מלחינה ~'
        },
        'ro': {
            'male': 'compozitor ~',
            'female': 'compozitoare ~'
        },
        'sq': {
            'male': 'kompozitor ~',
            'female': 'kompozitore ~'
        },
    },
    '~ cyclist': {
        'ar': {
            'male': 'دراج ~',
            'female': 'متسابقة دراجات ~'
        },
        'bn': {
            'male': '~ সাইক্লিস্ট',
            'female': '~ সাইক্লিস্ট'
        },
        'ca': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'en': {
            'male': '~ cyclist',
            'female': '~ cyclist'
        },
        'es': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'et': {
            'male': '~ jalgrattur',
            'female': '~ jalgrattur'
        },
        'fr': {
            'male': 'cycliste ~',
            'female': 'cycliste ~'
        },
        'gl': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'he': {
            'male': 'רוכב אופניים ~',
            'female': 'רוכבת אופניים ~'
        },
        'ro': {
            'male': 'ciclist ~',
            'female': 'ciclistă ~'
        },
        'sq': {
            'male': 'çiklist ~',
            'female': 'çikliste ~'
        },
    },
    '~ diplomat': {
        'ar': {
            'male': 'دبلوماسي ~',
            'female': 'دبلوماسية ~'
        },
        'bn': {
            'male': '~ কূটনীতিক',
            'female': '~ কূটনীতিক'
        },
        'ca': {
            'male': 'diplomàtic ~',
            'female': 'diplomàtica ~'
        },
        'en': {
            'male': '~ diplomat',
            'female': '~ diplomat'
        },
        'es': {
            'male': 'diplomático ~',
            'female': 'diplomática ~'
        },
        'et': {
            'male': '~ diplomaat',
            'female': '~ diplomaat'
        },
        'fr': {
            'male': 'diplomate ~',
            'female': 'diplomate ~'
        },
        'gl': {
            'male': 'diplomático ~',
            'female': 'diplomática ~'
        },
        'he': {
            'male': 'דיפולמט ~',
            'female': 'דיפולמטית ~'
        },
        'ro': {
            'male': 'diplomat ~',
            'female': 'diplomată ~'
        },
        'sq': {
            'male': 'diplomat ~',
            'female': 'diplomate ~'
        },
    },
    '~ economist': {
        'ar': {
            'male': 'عالم اقتصاد ~',
            'female': 'عالمة اقتصاد ~'
        },
        'bn': {
            'male': '~ অর্থনীতিবিদ',
            'female': '~ অর্থনীতিবিদ'
        },
        'ca': {
            'male': 'economista ~',
            'female': 'economista ~'
        },
        'en': {
            'male': '~ economist',
            'female': '~ economist'
        },
        'es': {
            'male': 'economista ~',
            'female': 'economista ~'
        },
        'et': {
            'male': '~ majandusteadlane',
            'female': '~ majandusteadlane'
        },
        'fr': {
            'male': 'économiste ~',
            'female': 'économiste ~'
        },
        'gl': {
            'male': 'economista ~',
            'female': 'economista ~'
        },
        'he': {
            'male': 'כלכלן ~',
            'female': 'כלכלנית ~'
        },
        'ro': {
            'male': 'economist ~',
            'female': 'economistă ~'
        },
        'sq': {
            'male': 'ekonomist ~',
            'female': 'ekonomiste ~'
        },
    },
    '~ educator': {
        'ar': {
            'male': 'مدرب ~ ',
            'female': 'مدربة ~'
        },
        'bn': {
            'male': '~ শিক্ষাবিদ',
            'female': '~ শিক্ষাবিদ'
        },
        'en': {
            'male': '~ educator',
            'female': '~ educator'
        },
        'es': {
            'male': 'educador ~',
            'female': 'educadora ~'
        },
        'fr': {
            'male': 'éducateur ~',
            'female': 'éducatrice ~'
        },
        'he': {
            'male': 'מחנך ~',
            'female': 'מחנכת ~'
        },
    },
    '~ engineer': {
        'ar': {
            'male': 'مهندس ~',
            'female': 'مهندسة ~'
        },
        'bn': {
            'male': '~ প্রকৌশলী',
            'female': '~ প্রকৌশলী'
        },
        'ca': {
            'male': 'enginyer ~',
            'female': 'enginyera ~'
        },
        'en': {
            'male': '~ engineer',
            'female': '~ engineer'
        },
        'es': {
            'male': 'ingeniero ~',
            'female': 'ingeniera ~'
        },
        'et': {
            'male': '~ insener',
            'female': '~ insener'
        },
        'fr': {
            'male': 'ingénieur ~',
            'female': 'ingénieure ~'
        },
        'gl': {
            'male': 'enxeñeiro ~',
            'female': 'enxeñeira ~'
        },
        'he': {
            'male': 'מהנדס ~',
            'female': 'מהנדסת ~'
        },
        'ro': {
            'male': 'inginer ~',
            'female': 'ingineră ~'
        },
        'sq': {
            'male': 'inxhinier ~',
            'female': 'inxhiniere ~'
        },
    },
    '~ entomologist': {
        'ar': {
            'male': 'عالم حشرات ~',
            'female': 'عالمة حشرات ~'
        },
        'bn': {
            'male': '~ পতঙ্গবিশারদ',
            'female': '~ পতঙ্গবিশারদ'
        },
        'ca': {
            'male': 'entomòleg ~',
            'female': 'entomòloga ~'
        },
        'en': {
            'male': '~ entomologist',
            'female': '~ entomologist'
        },
        'es': {
            'male': 'entomólogo ~',
            'female': 'entomóloga ~'
        },
        'et': {
            'male': '~ entomoloog',
            'female': '~ entomoloog'
        },
        'fr': {
            'male': 'entomologiste ~',
            'female': 'entomologiste ~'
        },
        'gl': {
            'male': 'entomólogo ~',
            'female': 'entomóloga ~'
        },
        'he': {
            'male': 'אנטומולוג ~',
            'female': 'אנטומולוגית ~'
        },
        'ro': {
            'male': 'entomolog ~',
            'female': 'entomologă ~'
        },
        'sq': {
            'male': 'entomolog ~',
            'female': 'entomologe ~'
        },
    },
    '~ explorer': {
        'ar': {
            'male': 'مستكشف ~',
            'female': 'مستكشفة ~'
        },
        'bn': {
            'male': '~ অনুসন্ধানকারী',
            'female': '~ অনুসন্ধানকারী'
        },
        'ca': {
            'male': 'explorador ~',
            'female': 'exploradora ~'
        },
        'en': {
            'male': '~ explorer',
            'female': '~ explorer'
        },
        'es': {
            'male': 'explorador ~',
            'female': 'exploradora ~'
        },
        'et': {
            'male': '~ maadeavastaja',
            'female': '~ maadeavastaja'
        },
        'fr': {
            'male': 'explorateur ~',
            'female': 'exploratrice ~'
        },
        'gl': {
            'male': 'explorador ~',
            'female': 'exploradora ~'
        },
        'he': {
            'male': 'חוקר ארצות ~',
            'female': 'חוקרת ארצות ~'
        },
        'ro': {
            'male': 'explorator ~',
            'female': 'exploratoare ~'
        },
        'sq': {
            'male': 'eksplorues ~',
            'female': 'eksploruese ~'
        },
    },
    '~ fencer': {
        'ar': {
            'male': 'مسايف ~',
            'female': 'مسايفة ~'
        },
        'bn': {
            'male': '~ অসিক্রীড়াবিদ',
            'female': '~ অসিক্রীড়াবিদ'
        },
        'ca': {
            'male': "tirador d'esgrima ~",
            'female': "tiradora d'esgrima ~"
        },
        'en': {
            'male': '~ fencer',
            'female': '~ fencer'
        },
        'es': {
            'male': 'esgrimista ~',
            'female': 'esgrimista ~'
        },
        'et': {
            'male': '~ vehkleja',
            'female': '~ vehkleja'
        },
        'fr': {
            'male': 'escrimeur ~',
            'female': 'escrimeuse ~'
        },
        'gl': {
            'male': 'esgrimista ~',
            'female': 'esgrimista ~'
        },
        'he': {
            'male': 'סייף ~',
            'female': 'סייפת ~'
        },
        'ro': {
            'male': 'scrimer ~',
            'female': 'scrimeră ~'
        },
        'sq': {
            'male': 'skermist ~',
            'female': 'skermiste ~'
        },
    },
    '~ film actor': {
        'ar': {
            'male': 'ممثل ~',
            'female': 'ممثلة ~'
        },
        'bn': {
            'male': '~ অভিনেতা',
            'female': '~ অভিনেত্রী'
        },
        'ca': {
            'male': 'actor ~',
            'female': 'actriu ~'
        },
        'en': {
            'male': '~ actor',
            'female': '~ actress'
        },
        'es': {
            'male': 'actor ~',
            'female': 'actriz ~'
        },
        'et': {
            'male': '~ filminäitleja',
            'female': '~ filminäitleja'
        },
        'fr': {
            'male': 'acteur ~',
            'female': 'actrice ~'
        },
        'gl': {
            'male': 'actor ~',
            'female': 'actriz ~'
        },
        'he': {
            'male': 'שחקן ~',
            'female': 'שחקנית ~'
        },
        'ro': {
            'male': 'actor ~',
            'female': 'actriță ~'
        },
        'sq': {
            'male': 'aktor ~',
            'female': 'aktore ~'
        },
    },
    '~ film director': {
        'ar': {
            'male': 'مخرج أفلام ~',
            'female': 'مخرجة أفلام ~'
        },
        'bn': {
            'male': '~ চলচ্চিত্র পরিচালক',
            'female': '~ চলচ্চিত্র পরিচালিকা'
        },
        'ca': {
            'male': 'director de cinema ~',
            'female': 'directora de cinema ~'
        },
        'en': {
            'male': '~ film director',
            'female': '~ film director'
        },
        'es': {
            'male': 'director de cine ~',
            'female': 'directora de cine ~'
        },
        'et': {
            'male': '~ filmirežissöör',
            'female': '~ filmirežissöör'
        },
        'fr': {
            'male': 'réalisateur ~',
            'female': 'réalisatrice ~'
        },
        'gl': {
            'male': 'director de cinema ~',
            'female': 'directora de cinema ~'
        },
        'he': {
            'male': 'במאי קולנוע ~',
            'female': 'במאית קולנוע ~'
        },
        'ro': {
            'male': 'regizor de film ~',
            'female': 'regizoare de film ~'
        },
        'sq': {
            'male': 'regjisor ~',
            'female': 'regjisore ~'
        },
    },
    '~ film producer': {
        'ar': {
            'male': 'منتج أفلام ~',
            'female': 'منتجة أفلام ~'
        },
        'bn': {
            'male': '~ চলচ্চিত্র প্রযোজক',
            'female': '~ চলচ্চিত্র প্রযোজক'
        },
        'ca': {
            'male': 'productor de cinema ~',
            'female': 'productora de cinema ~'
        },
        'en': {
            'male': '~ film producer',
            'female': '~ film producer'
        },
        'es': {
            'male': 'productor de cine ~',
            'female': 'productora de cine ~'
        },
        'et': {
            'male': '~ filmiprodutsent',
            'female': '~ filmiprodutsent'
        },
        'fr': {
            'male': 'producteur ~',
            'female': 'productrice ~'
        },
        'gl': {
            'male': 'produtor de cinema ~',
            'female': 'produtora de cinema ~'
        },
        'he': {
            'male': 'מפיק קולנוע ~',
            'female': 'מפיקת קולנוע ~'
        },
        'ro': {
            'male': 'producător de film ~',
            'female': 'producătoare de film ~'
        },
        'sq': {
            'male': 'prodhues filmash ~',
            'female': 'prodhuese filmash ~'
        },
    },
    '~ football player': {
        'ar': {
            'male': 'لاعب كرة قدم ~',
            'female': 'لاعبة كرة قدم ~'
        },
        'bn': {
            'male': '~ ফুটবলার',
            'female': '~ ফুটবলার'
        },
        'ca': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'en': {
            'male': '~ footballer',
            'female': '~ footballer'
        },
        'nl': {
            'male': '~ footballspeler',
            'female': '~ footballspeelster'
        },
        'es': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'fr': {
            'male': 'joueur de football ~',
            'female': 'joueuse de football ~'
        },
        'gl': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'he': {
            'male': 'כדורגלן ~',
            'female': 'כדורגלנית ~'
        },
    },
    '~ footballer': {
        'ar': {
            'male': 'لاعب كرة قدم ~',
            'female': 'لاعبة كرة قدم ~'
        },
        'bn': {
            'male': '~ ফুটবলার',
            'female': '~ ফুটবলার'
        },
        'ca': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'en': {
            'male': '~ footballer',
            'female': '~ footballer'
        },
        'es': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'et': {
            'male': '~ jalgpallur',
            'female': '~ jalgpallur'
        },
        'fr': {
            'male': 'joueur de football ~',
            'female': 'joueuse de football ~'
        },
        'gl': {
            'male': 'futbolista ~',
            'female': 'futbolista ~'
        },
        'he': {
            'male': 'כדורגלן ~',
            'female': 'כדורגלנית ~'
        },
        'ro': {
            'male': 'fotbalist ~',
            'female': 'fotbalistă ~'
        },
        'sq': {
            'male': 'futbollist ~',
            'female': 'futbolliste ~'
        },
    },
    '~ historian': {
        'ar': {
            'male': 'مؤرخ ~',
            'female': 'مؤرخة ~'
        },
        'bn': {
            'male': '~ ইতিহাসবেত্তা',
            'female': '~ ইতিহাসবেত্তা'
        },
        'ca': {
            'male': 'historiador ~',
            'female': 'historiadora ~'
        },
        'en': {
            'male': '~ historian',
            'female': '~ historian'
        },
        'es': {
            'male': 'historiador ~',
            'female': 'historiadora ~'
        },
        'et': {
            'male': '~ ajaloolane',
            'female': '~ ajaloolane'
        },
        'fr': {
            'male': 'historien ~',
            'female': 'historienne ~'
        },
        'gl': {
            'male': 'historiador ~',
            'female': 'historiadora ~'
        },
        'he': {
            'male': 'היסטוריון ~',
            'female': 'היסטוריונית ~'
        },
        'ro': {
            'male': 'istoric ~',
            'female': 'istorică ~'
        },
        'sq': {
            'male': 'historian ~',
            'female': 'historiane ~'
        },
    },
    '~ illustrator': {
        'ar': {
            'male': 'رسام كتب ~',
            'female': 'رسامة كتب ~'
        },
        'bn': {
            'male': '~ অঙ্কনশিল্পী',
            'female': '~ অঙ্কনশিল্পী'
        },
        'ca': {
            'male': 'il·lustrador ~',
            'female': 'il·lustradora ~'
        },
        'en': {
            'male': '~ illustrator',
            'female': '~ illustrator'
        },
        'es': {
            'male': 'ilustrador ~',
            'female': 'ilustradora ~'
        },
        'et': {
            'male': '~ illustraator',
            'female': '~ illustraator'
        },
        'fr': {
            'male': 'illustrateur ~',
            'female': 'illustratrice ~'
        },
        'gl': {
            'male': 'ilustrador ~',
            'female': 'ilustradora ~'
        },
        'he': {
            'male': 'מאייר ~',
            'female': 'מאיירת ~'
        },
        'ro': {
            'male': 'ilustrator ~',
            'female': 'ilustratoare ~'
        },
        'sq': {
            'male': 'ilustrator ~',
            'female': 'ilustratore ~'
        },
    },
    '~ journalist': {
        'ar': {
            'male': 'صحفي ~',
            'female': 'صحفية ~'
        },
        'bn': {
            'male': '~ সাংবাদিক',
            'female': '~ সাংবাদিক'
        },
        'ca': {
            'male': 'periodista ~',
            'female': 'periodista ~'
        },
        'en': {
            'male': '~ journalist',
            'female': '~ journalist'
        },
        'es': {
            'male': 'periodista ~',
            'female': 'periodista ~'
        },
        'et': {
            'male': '~ ajakirjanik',
            'female': '~ ajakirjanik'
        },
        'fr': {
            'male': 'journaliste ~',
            'female': 'journaliste ~'
        },
        'gl': {
            'male': 'xornalista ~',
            'female': 'xornalista ~'
        },
        'he': {
            'male': 'עיתונאי ~',
            'female': 'עיתונאית ~'
        },
        'ro': {
            'male': 'jurnalist ~',
            'female': 'jurnalistă ~'
        },
        'sq': {
            'male': 'gazetar ~',
            'female': 'gazetare ~'
        },
    },
    '~ jurist': {
        'ar': {
            'male': 'حقوقي ~',
            'female': 'حقوقية ~'
        },
        'bn': {
            'male': '~ বিচারক',
            'female': '~ বিচারক'
        },
        'ca': {
            'male': 'jurista ~',
            'female': 'jurista ~'
        },
        'en': {
            'male': '~ jurist',
            'female': '~ jurist'
        },
        'es': {
            'male': 'jurista ~',
            'female': 'jurista ~'
        },
        'et': {
            'male': '~ jurist',
            'female': '~ jurist'
        },
        'fr': {
            'male': 'juriste ~',
            'female': 'juriste ~'
        },
        'gl': {
            'male': 'xurista ~',
            'female': 'xurista ~'
        },
        'he': {
            'male': 'משפטן ~',
            'female': 'משפטנית ~'
        },
        'ro': {
            'male': 'jurist ~',
            'female': 'juristă ~'
        },
        'sq': {
            'male': 'jurist ~',
            'female': 'juriste ~'
        },
    },
    '~ lawyer': {
        'ar': {
            'male': 'محامي ~',
            'female': 'محامية ~'
        },
        'bn': {
            'male': '~ আইনজীবী',
            'female': '~ আইনজীবী'
        },
        'ca': {
            'male': 'advocat ~',
            'female': 'advocada ~'
        },
        'en': {
            'male': '~ lawyer',
            'female': '~ lawyer'
        },
        'es': {
            'male': 'abogado ~',
            'female': 'abogada ~'
        },
        'et': {
            'male': '~ advokaat',
            'female': '~ advokaat'
        },
        'fr': {
            'male': 'avocat ~',
            'female': 'avocate ~'
        },
        'gl': {
            'male': 'xurista ~',
            'female': 'xurista ~'
        },
        'he': {
            'male': 'עורך דין ~',
            'female': 'עורכת דין ~'
        },
        'ro': {
            'male': 'avocat ~',
            'female': 'avocată ~'
        },
        'sq': {
            'male': 'avokat ~',
            'female': 'avokate ~'
        },
    },
    '~ lexicographer': {
        'ar': {
            'male': 'معجمي ~',
            'female': 'معجمية ~'
        },
        'en': {
            'male': '~ lexicographer',
            'female': '~ lexicographer'
        },
    },
    '~ mathematician': {
        'ar': {
            'male': 'رياضياتي ~',
            'female': 'رياضياتية ~'
        },
        'bn': {
            'male': '~ গণিতবিদ',
            'female': '~ গণিতবিদ'
        },
        'ca': {
            'male': 'matemàtic ~',
            'female': 'matemàtica ~'
        },
        'en': {
            'male': '~ mathematician',
            'female': '~ mathematician'
        },
        'es': {
            'male': 'matemático ~',
            'female': 'matemática ~'
        },
        'et': {
            'male': '~ matemaatik',
            'female': '~ matemaatik'
        },
        'fr': {
            'male': 'mathématicien ~',
            'female': 'mathématicienne ~'
        },
        'gl': {
            'male': 'matemático ~',
            'female': 'matemática ~'
        },
        'he': {
            'male': 'מתמטיקאי ~',
            'female': 'מתמטיקאית ~'
        },
        'ro': {
            'male': 'matematician ~',
            'female': 'matematiciană ~'
        },
        'sq': {
            'male': 'matematikan ~',
            'female': 'matematikane ~'
        },
    },
    '~ musician': {
        'ar': {
            'male': 'موسيقي ~',
            'female': 'موسيقية ~'
        },
        'bn': {
            'male': '~ সুরকার',
            'female': '~ সুরকার'
        },
        'ca': {
            'male': 'músic ~',
            'female': 'músic ~'
        },
        'en': {
            'male': '~ musician',
            'female': '~ musician'
        },
        'es': {
            'male': 'músico ~',
            'female': 'música ~'
        },
        'et': {
            'male': '~ muusik',
            'female': '~ muusik'
        },
        'fr': {
            'male': 'musicien ~',
            'female': 'musicienne ~'
        },
        'gl': {
            'male': 'músico ~',
            'female': 'música ~'
        },
        'he': {
            'male': 'מוזיקאי ~',
            'female': 'מוזיקאית ~'
        },
        'ro': {
            'male': 'muzician ~',
            'female': 'muziciană ~'
        },
        'sq': {
            'male': 'muzikant ~',
            'female': 'muzikante ~'
        },
    },
    '~ novelist': {
        'ar': {
            'male': 'روائي ~',
            'female': 'روائية ~'
        },
        'bn': {
            'male': '~ ঔপন্যাসিক',
            'female': '~ ঔপন্যাসিক'
        },
        'ca': {
            'male': 'novel·lista ~',
            'female': 'novel·lista ~'
        },
        'en': {
            'male': '~ novelist',
            'female': '~ novelist'
        },
        'es': {
            'male': 'novelista ~',
            'female': 'novelista ~'
        },
        'et': {
            'male': '~ romaanikirjanik',
            'female': '~ romaanikirjanik'
        },
        'fr': {
            'male': 'romancier ~',
            'female': 'romancière ~'
        },
        'gl': {
            'male': 'novelista ~',
            'female': 'novelista ~'
        },
        'he': {
            'male': 'מחבר רומנים ~',
            'female': 'מחברת רומנים ~'
        },
        'ro': {
            'male': 'romancier ~',
            'female': 'romancieră ~'
        },
        'sq': {
            'male': 'novelist ~',
            'female': 'noveliste ~'
        },
    },
    '~ painter': {
        'ar': {
            'male': 'رسام ~',
            'female': 'رسامة ~'
        },
        'bn': {
            'male': '~ চিত্রশিল্পী',
            'female': '~ চিত্রশিল্পী'
        },
        'ca': {
            'male': 'pintor ~',
            'female': 'pintora ~'
        },
        'en': {
            'male': '~ painter',
            'female': '~ painter'
        },
        'es': {
            'male': 'pintor ~',
            'female': 'pintora ~'
        },
        'et': {
            'male': '~ maalikunstnik',
            'female': '~ maalikunstnik'
        },
        'fr': {
            'male': 'peintre ~',
            'female': 'peintre ~'
        },
        'gl': {
            'male': 'pintor ~',
            'female': 'pintora ~'
        },
        'he': {
            'male': 'צייר ~',
            'female': 'ציירת ~'
        },
        'ro': {
            'male': 'pictor ~',
            'female': 'pictoriță ~'
        },
        'sq': {
            'male': 'piktor ~',
            'female': 'piktore ~'
        },
    },
    '~ philosopher': {
        'ar': {
            'male': 'فيلسوف ~',
            'female': 'فيلسوفة ~'
        },
        'bn': {
            'male': '~ দার্শনিক',
            'female': '~ দার্শনিক'
        },
        'ca': {
            'male': 'filòsof ~',
            'female': 'filòsofa ~'
        },
        'en': {
            'male': '~ philosopher',
            'female': '~ philosopher'
        },
        'es': {
            'male': 'filósofo ~',
            'female': 'filósofa ~'
        },
        'et': {
            'male': '~ filosoof',
            'female': '~ filosoof'
        },
        'fr': {
            'male': 'philosophe ~',
            'female': 'philosophe ~'
        },
        'gl': {
            'male': 'filósofo ~',
            'female': 'filósofa ~'
        },
        'he': {
            'male': 'פילוסוף ~',
            'female': 'פילוסופית ~'
        },
        'ro': {
            'male': 'filosof ~',
            'female': 'filosoafă ~'
        },
        'sq': {
            'male': 'filozof ~',
            'female': 'filozofe ~'
        },
    },
    '~ photographer': {
        'ar': {
            'male': 'مصور ~',
            'female': 'مصورة ~'
        },
        'bn': {
            'male': '~ আলোকচিত্র শিল্পী',
            'female': '~ আলোকচিত্র শিল্পী'
        },
        'ca': {
            'male': 'fotògraf ~',
            'female': 'fotògrafa ~'
        },
        'en': {
            'male': '~ photographer',
            'female': '~ photographer'
        },
        'es': {
            'male': 'fotógrafo ~',
            'female': 'fotógrafa ~'
        },
        'et': {
            'male': '~ fotograaf',
            'female': '~ fotograaf'
        },
        'fr': {
            'male': 'photographe ~',
            'female': 'photographe ~'
        },
        'gl': {
            'male': 'fotógrafo ~',
            'female': 'fotógrafa ~'
        },
        'he': {
            'male': 'צלם ~',
            'female': 'צלמת ~'
        },
        'ro': {
            'male': 'fotograf ~',
            'female': 'fotografă ~'
        },
        'sq': {
            'male': 'fotograf ~',
            'female': 'fotografe ~'
        },
    },
    '~ physician': {
        'ar': {
            'male': 'طبيب ~',
            'female': 'طبيبة ~'
        },
        'bn': {
            'male': '~ চিকিৎসক',
            'female': '~ চিকিৎসক'
        },
        'ca': {
            'male': 'metge ~',
            'female': 'metgessa ~'
        },
        'en': {
            'male': '~ physician',
            'female': '~ physician'
        },
        'es': {
            'male': 'médico ~',
            'female': 'médica ~'
        },
        'et': {
            'male': '~ arst',
            'female': '~ arst'
        },
        'fr': {
            'male': 'médecin ~',
            'female': 'médecin ~'
        },
        'gl': {
            'male': 'médico ~',
            'female': 'médica ~'
        },
        'he': {
            'male': 'רופא ~',
            'female': 'רופאה ~'
        },
        'ro': {
            'male': 'medic ~',
            'female': 'doctoriță ~'
        },
        'sq': {
            'male': 'mjek ~',
            'female': 'mjeke ~'
        },
    },
    '~ physicist': {
        'ar': {
            'male': 'فيزيائي ~',
            'female': 'فيزيائية ~'
        },
        'bn': {
            'male': '~ পদার্থবিজ্ঞানী',
            'female': '~ পদার্থবিজ্ঞানী'
        },
        'ca': {
            'male': 'físic ~',
            'female': 'física ~'
        },
        'en': {
            'male': '~ physicist',
            'female': '~ physicist'
        },
        'es': {
            'male': 'físico ~',
            'female': 'física ~'
        },
        'et': {
            'male': '~ füüsik',
            'female': '~ füüsik'
        },
        'fr': {
            'male': 'physicien ~',
            'female': 'physicienne ~'
        },
        'gl': {
            'male': 'físico ~',
            'female': 'física ~'
        },
        'he': {
            'male': 'פיזיקאי ~',
            'female': 'פיזיקאית ~'
        },
        'ro': {
            'male': 'fizician ~',
            'female': 'fiziciană ~'
        },
        'sq': {
            'male': 'fizikan ~',
            'female': 'fizikane ~'
        },
    },
    '~ pianist': {
        'ar': {
            'male': 'عازف بيانو ~',
            'female': 'عازفة بيانو ~'
        },
        'bn': {
            'male': '~ পিয়ানো বাদক',
            'female': '~ পিয়ানো বাদক'
        },
        'ca': {
            'male': 'pianista ~',
            'female': 'pianista ~'
        },
        'en': {
            'male': '~ pianist',
            'female': '~ pianist'
        },
        'es': {
            'male': 'pianista ~',
            'female': 'pianista ~'
        },
        'et': {
            'male': '~ pianist',
            'female': '~ pianist'
        },
        'fr': {
            'male': 'pianiste ~',
            'female': 'pianiste ~'
        },
        'gl': {
            'male': 'pianista ~',
            'female': 'pianista ~'
        },
        'he': {
            'male': 'פסנתרן ~',
            'female': 'פסנתרנית ~'
        },
        'ro': {
            'male': 'pianist ~',
            'female': 'pianistă ~'
        },
        'sq': {
            'male': 'pianist ~',
            'female': 'pianiste ~'
        },
    },
    '~ playwright': {
        'ar': {
            'male': 'كاتب مسرحي ~',
            'female': 'كاتبة مسرحية ~'
        },
        'bn': {
            'male': '~ নাট্যকার',
            'female': '~ নাট্যকার'
        },
        'ca': {
            'male': 'dramaturg ~',
            'female': 'dramaturga ~'
        },
        'en': {
            'male': '~ playwright',
            'female': '~ playwright'
        },
        'es': {
            'male': 'dramaturgo ~',
            'female': 'dramaturga ~'
        },
        'et': {
            'male': '~ näitekirjanik',
            'female': '~ näitekirjanik'
        },
        'fr': {
            'male': 'dramaturge ~',
            'female': 'dramaturge ~'
        },
        'gl': {
            'male': 'dramaturgo ~',
            'female': 'dramaturga ~'
        },
        'he': {
            'male': 'מחזאי ~',
            'female': 'מחזאית ~'
        },
        'ro': {
            'male': 'dramaturg ~',
            'female': 'dramaturgă ~'
        },
        'sq': {
            'male': 'dramaturg ~',
            'female': 'dramaturge ~'
        },
    },
    '~ poet': {
        'ar': {
            'male': 'شاعر ~',
            'female': 'شاعرة ~'
        },
        'bn': {
            'male': '~ কবি',
            'female': '~ কবি'
        },
        'ca': {
            'male': 'poeta ~',
            'female': 'poetessa ~'
        },
        'en': {
            'male': '~ poet',
            'female': '~ poet'
        },
        'es': {
            'male': 'poeta ~',
            'female': 'poetisa ~'
        },
        'et': {
            'male': '~ luuletaja',
            'female': '~ luuletaja'
        },
        'fr': {
            'male': 'poète ~',
            'female': 'poétesse ~'
        },
        'gl': {
            'male': 'poeta ~',
            'female': 'poetisa ~'
        },
        'he': {
            'male': 'משורר ~',
            'female': 'משוררת ~'
        },
        'ro': {
            'male': 'poet ~',
            'female': 'poetă ~'
        },
        'sq': {
            'male': 'poet ~',
            'female': 'poete ~'
        },
    },
    '~ politician': {
        'ar': {
            'male': 'سياسي ~',
            'female': 'سياسية ~'
        },
        'bn': {
            'male': '~ রাজনীতিবিদ',
            'female': '~ রাজনীতিবিদ'
        },
        'ca': {
            'male': 'polític ~',
            'female': 'política ~'
        },
        'en': {
            'male': '~ politician',
            'female': '~ politician'
        },
        'es': {
            'male': 'político ~',
            'female': 'política ~'
        },
        'et': {
            'male': '~ poliitik',
            'female': '~ poliitik'
        },
        'fr': {
            'male': 'homme politique ~',
            'female': 'femme politique ~'
        },
        'gl': {
            'male': 'político ~',
            'female': 'política ~'
        },
        'he': {
            'male': 'פוליטיקאי ~',
            'female': 'פוליטיקאית ~'
        },
        'ro': {
            'male': 'politician ~',
            'female': 'politiciană ~'
        },
        'sq': {
            'male': 'politikan ~',
            'female': 'politikane ~'
        },
    },
    '~ publisher': {
        'ar': {
            'male': 'ناشر ~',
            'female': 'ناشرة ~'
        },
        'bn': {
            'male': '~ প্রকাশক',
            'female': '~ প্রকাশক'
        },
        'ca': {
            'male': 'editor ~',
            'female': 'editora ~'
        },
        'en': {
            'male': '~ publisher',
            'female': '~ publisher'
        },
        'es': {
            'male': 'editor ~',
            'female': 'editora ~'
        },
        'et': {
            'male': '~ kirjastaja',
            'female': '~ kirjastaja'
        },
        'fr': {
            'male': 'éditeur ~',
            'female': 'éditrice ~'
        },
        'gl': {
            'male': 'editor ~',
            'female': 'editora ~'
        },
        'he': {
            'male': 'מוציא לאור ~',
            'female': 'מוציאה לאור ~'
        },
        'ro': {
            'male': 'editor ~',
            'female': 'editoare ~'
        },
        'sq': {
            'male': 'botues ~',
            'female': 'botuese ~'
        },
    },
    '~ rabbi': {
        'ar': {
            'male': 'حاخام ~',
            'female': 'حاخامة ~'
        },
        'bn': {
            'male': '~ রাব্বি',
            'female': '~ রাব্বি'
        },
        'ca': {
            'male': 'rabí ~',
            'female': 'rabí ~'
        },
        'en': {
            'male': '~ rabbi',
            'female': '~ rabbi'
        },
        'es': {
            'male': 'rabino ~',
            'female': 'rabina ~'
        },
        'et': {
            'male': '~ rabi',
            'female': '~ rabi'
        },
        'fr': {
            'male': 'rabbin ~',
            'female': 'rabbine ~'
        },
        'gl': {
            'male': 'rabino ~',
            'female': 'rabina ~'
        },
        'he': {
            'male': 'רב ~',
            'female': 'רבנית ~'
        },
        'ro': {
            'male': 'rabin ~',
            'female': 'rabină ~'
        },
        'sq': {
            'male': 'rabin ~',
            'female': 'rabine ~'
        },
    },
    '~ racing cyclist': {
        'ar': {
            'male': 'دراج ~',
            'female': 'متسابقة دراجات ~'
        },
        'bn': {
            'male': '~ সাইক্লিস্ট',
            'female': '~ সাইক্লিস্ট'
        },
        'ca': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'en': {
            'male': '~ racing cyclist',
            'female': '~ racing cyclist'
        },
        'es': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'et': {
            'male': '~ jalgrattur',
            'female': '~ jalgrattur'
        },
        'fr': {
            'male': 'cycliste ~',
            'female': 'cycliste ~'
        },
        'gl': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'he': {
            'male': 'רוכב אופניים ~',
            'female': 'רוכבת אופניים ~'
        },
        'ro': {
            'male': 'ciclist ~',
            'female': 'ciclistă ~'
        },
        'sq': {
            'male': 'çiklist ~',
            'female': 'çikliste ~'
        },
    },
    '~ rugby union player': {
        'ar': {
            'male': 'لاعب رغبي ~',
            'female': 'لاعبة رغبي ~'
        },
        'bn': {
            'male': '~ রাগবি ইউনিয়ন খেলোয়াড়',
            'female': '~ রাগবি ইউনিয়ন খেলোয়াড়'
        },
        'ca': {
            'male': 'jugador de rugbi ~',
            'female': 'jugadora de rugbi ~'
        },
        'en': {
            'male': '~ rugby union player',
            'female': '~ rugby union player'
        },
        'es': {
            'male': 'jugador de rugby ~',
            'female': 'jugadora de rugby ~'
        },
        'et': {
            'male': '~ ragbimängija',
            'female': '~ ragbimängija'
        },
        'fr': {
            'male': 'joueur de rugby ~',
            'female': 'joueuse de rugby ~'
        },
        'gl': {
            'male': 'xogador de rugby ~',
            'female': 'xogadora de rugby ~'
        },
        'he': {
            'male': 'שחקן רוגבי יוניון ~',
            'female': 'שחקנית רוגבי יוניון ~'
        },
        'ro': {
            'male': 'rugbist ~',
            'female': 'rugbistă ~'
        },
        'sq': {
            'male': 'lojtar rugby ~',
            'female': 'lojtare rugby ~'
        },
    },
    '~ rules footballer': {
        'ar': {
            'male': 'لاعب كرة قدم ~',
            'female': 'لاعبة كرة قدم ~'
        },
        'en': {
            'male': '~ rules footballer',
            'female': '~ rules footballer'
        },
        'nl': {
            'male': '~ Gridiron Footballspeler',
            'female': '~ Gridiron Footballspeler'
        },
    },
    '~ screenwriter': {
        'ar': {
            'male': 'كاتب سيناريو ~',
            'female': 'كاتبة سيناريو ~'
        },
        'bn': {
            'male': '~ চিত্রনাট্যকার',
            'female': '~ চিত্রনাট্যকার'
        },
        'ca': {
            'male': 'guionista ~',
            'female': 'guionista ~'
        },
        'en': {
            'male': '~ screenwriter',
            'female': '~ screenwriter'
        },
        'es': {
            'male': 'guionista ~',
            'female': 'guionista ~'
        },
        'et': {
            'male': '~ stsenarist',
            'female': '~ stsenarist'
        },
        'fr': {
            'male': 'scénariste ~',
            'female': 'scénariste ~'
        },
        'gl': {
            'male': 'guionista ~',
            'female': 'guionista ~'
        },
        'he': {
            'male': 'תסריטאי ~',
            'female': 'תסריטאית ~'
        },
        'ro': {
            'male': 'scenarist ~',
            'female': 'scenaristă ~'
        },
        'sq': {
            'male': 'skenarist ~',
            'female': 'skenariste ~'
        },
    },
    '~ sculptor': {
        'ar': {
            'male': 'نحات ~',
            'female': 'نحاتة ~'
        },
        'bn': {
            'male': '~ ভাস্কর',
            'female': '~ ভাস্কর'
        },
        'ca': {
            'male': 'escultor ~',
            'female': 'escultora ~'
        },
        'en': {
            'male': '~ sculptor',
            'female': '~ sculptor'
        },
        'es': {
            'male': 'escultor ~',
            'female': 'escultora ~'
        },
        'et': {
            'male': '~ skulptor',
            'female': '~ skulptor'
        },
        'fr': {
            'male': 'sculpteur ~',
            'female': 'sculptrice ~'
        },
        'gl': {
            'male': 'escultor ~',
            'female': 'escultora ~'
        },
        'he': {
            'male': 'פסל ~',
            'female': 'פסלת ~'
        },
        'ro': {
            'male': 'sculptor ~',
            'female': 'sculptoriță ~'
        },
        'sq': {
            'male': 'skulptor ~',
            'female': 'skupltore ~'
        },
    },
    '~ singer': {
        'ar': {
            'male': 'مغني ~',
            'female': 'مغنية ~'
        },
        'bn': {
            'male': '~ গায়ক',
            'female': '~ গায়িকা'
        },
        'ca': {
            'male': 'cantant ~',
            'female': 'cantant ~'
        },
        'en': {
            'male': '~ singer',
            'female': '~ singer'
        },
        'es': {
            'male': 'cantante ~',
            'female': 'cantante ~'
        },
        'et': {
            'male': '~ laulja',
            'female': '~ laulja'
        },
        'fr': {
            'male': 'chanteur ~',
            'female': 'chanteuse ~'
        },
        'gl': {
            'male': 'cantante ~',
            'female': 'cantante ~'
        },
        'he': {
            'male': 'זמר ~',
            'female': 'זמרת ~'
        },
        'ro': {
            'male': 'cântăreț ~',
            'female': 'cântăreață ~'
        },
        'sq': {
            'male': 'këngëtar ~',
            'female': 'këngëtare ~'
        },
    },
    '~ skier': {
        'ar': {
            'male': 'متزحلق ~',
            'female': 'متزحلقة ~'
        },
        'bn': {
            'male': '~ স্কিয়ার',
            'female': '~ স্কিয়ার'
        },
        'en': {
            'male': '~ skier',
            'female': '~ skier'
        },
        'es': {
            'male': 'esquiador ~',
            'female': 'esquiadora ~'
        },
        'fr': {
            'male': 'skieur ~',
            'female': 'skieuse ~'
        },
        'he': {
            'male': 'גולש סקי ~',
            'female': 'גולשת סקי ~'
        },
    },
    '~ sociologist': {
        'ar': {
            'male': 'عالم اجتماع ~',
            'female': 'عالمة اجتماع ~'
        },
        'bn': {
            'male': '~ সমাজবিজ্ঞানী',
            'female': '~ সমাজবিজ্ঞানী'
        },
        'ca': {
            'male': 'sociòleg ~',
            'female': 'sociòloga ~'
        },
        'en': {
            'male': '~ sociologist',
            'female': '~ sociologist'
        },
        'es': {
            'male': 'sociólogo ~',
            'female': 'socióloga ~'
        },
        'et': {
            'male': '~ sotsioloog',
            'female': '~ sotsioloog'
        },
        'fr': {
            'male': 'sociologue ~',
            'female': 'sociologue ~'
        },
        'gl': {
            'male': 'sociólogo ~',
            'female': 'socióloga ~'
        },
        'he': {
            'male': 'סוציולוג ~',
            'female': 'סוציולוגית ~'
        },
        'ro': {
            'male': 'sociolog ~',
            'female': 'sociologă ~'
        },
        'sq': {
            'male': 'sociolog ~',
            'female': 'sociologe ~'
        },
    },
    '~ soldier': {
        'ar': {
            'male': 'جندي ~',
            'female': 'جندية ~'
        },
        'bn': {
            'male': '~ সৈনিক',
            'female': '~ সৈনিক'
        },
        'ca': {
            'male': 'militar ~',
            'female': 'militar ~'
        },
        'en': {
            'male': '~ soldier',
            'female': '~ soldier'
        },
        'es': {
            'male': 'militar ~',
            'female': 'militar ~'
        },
        'et': {
            'male': '~ sõjaväelane',
            'female': '~ sõjaväelane'
        },
        'fr': {
            'male': 'militaire ~',
            'female': 'militaire ~'
        },
        'gl': {
            'male': 'militar ~',
            'female': 'militar ~'
        },
        'he': {
            'male': 'חייל ~',
            'female': 'חיילת ~'
        },
        'ro': {
            'male': 'soldat ~',
            'female': 'femeie soldat ~'
        },
        'sq': {
            'male': 'ushtar ~',
            'female': 'ushtare ~'
        },
    },
    '~ sport cyclist': {
        'ar': {
            'male': 'دراج ~',
            'female': 'متسابقة دراجات ~'
        },
        'bn': {
            'male': '~ সাইক্লিস্ট',
            'female': '~ সাইক্লিস্ট'
        },
        'ca': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'en': {
            'male': '~ sport cyclist',
            'female': '~ sport cyclist'
        },
        'es': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'et': {
            'male': '~ jalgrattur',
            'female': '~ jalgrattur'
        },
        'fr': {
            'male': 'cycliste ~',
            'female': 'cycliste ~'
        },
        'gl': {
            'male': 'ciclista ~',
            'female': 'ciclista ~'
        },
        'he': {
            'male': 'רוכב אופניים ~',
            'female': 'רוכבת אופניים ~'
        },
        'ro': {
            'male': 'ciclist ~',
            'female': 'ciclistă ~'
        },
        'sq': {
            'male': 'çiklist ~',
            'female': 'çikliste ~'
        },
    },
    '~ swimmer': {
        'ar': {
            'male': 'سباح ~',
            'female': 'سباحة ~'
        },
        'bn': {
            'male': '~ সাঁতারু',
            'female': '~ সাঁতারু'
        },
        'ca': {
            'male': 'nedador ~',
            'female': 'nedadora ~'
        },
        'en': {
            'male': '~ swimmer',
            'female': '~ swimmer'
        },
        'es': {
            'male': 'nadador ~',
            'female': 'nadadora ~'
        },
        'et': {
            'male': '~ ujuja',
            'female': '~ ujuja'
        },
        'fr': {
            'male': 'nageur ~',
            'female': 'nageuse ~'
        },
        'gl': {
            'male': 'nadador ~',
            'female': 'nadadora ~'
        },
        'he': {
            'male': 'שחיין ~',
            'female': 'שחיינית ~'
        },
        'ro': {
            'male': 'înotător ~',
            'female': 'înotătoare ~'
        },
        'sq': {
            'male': 'notues ~',
            'female': 'notuese ~'
        },
    },
    '~ tennis player': {
        'ar': {
            'male': 'لاعب كرة مضرب ~',
            'female': 'لاعبة كرة مضرب ~'
        },
        'bn': {
            'male': '~ টেনিস খেলোয়াড়',
            'female': '~ টেনিস খেলোয়াড়'
        },
        'ca': {
            'male': 'tennista professional ~',
            'female': 'tennista professional ~'
        },
        'en': {
            'male': '~ tennis player',
            'female': '~ tennis player'
        },
        'es': {
            'male': 'tenista profesional ~',
            'female': 'tenista profesional ~'
        },
        'et': {
            'male': '~ tennisist',
            'female': '~ tennisist'
        },
        'fr': {
            'male': 'joueur de tennis ~',
            'female': 'joueuse de tennis ~'
        },
        'gl': {
            'male': 'tenista profesional ~',
            'female': 'tenista profesional ~'
        },
        'he': {
            'male': 'טניסאי ~',
            'female': 'טניסאית ~'
        },
        'ro': {
            'male': 'jucător de tenis ~',
            'female': 'jucătoare de tenis ~'
        },
        'sq': {
            'male': 'lojtar tenisi ~',
            'female': 'lojtare tenisi ~'
        },
    },
    '~ translator': {
        'ar': {
            'male': 'مترجم ~',
            'female': 'مترجمة ~'
        },
        'bn': {
            'male': '~ অনুবাদক',
            'female': '~ অনুবাদক'
        },
        'en': {
            'male': '~ translator',
            'female': '~ translator'
        },
        'es': {
            'male': 'traductor ~',
            'female': 'traductora ~'
        },
        'fr': {
            'male': 'traducteur ~',
            'female': 'traductrice ~'
        },
        'he': {
            'male': 'מתרגם ~',
            'female': 'מתרגמת ~'
        },
    },
    '~ university teacher': {
        'ar': {
            'male': "أستاذ جامعي ~",
            'female': "أستاذة جامعية ~"
        },
        'bn': {
            'male': '~ বিশ্ববিদ্যালয়ের শিক্ষক',
            'female': '~ বিশ্ববিদ্যালয়ের শিক্ষিকা'
        },
        'ca': {
            'male': "professor d'universitat ~",
            'female': "professora d'universitat ~"
        },
        'en': {
            'male': '~ university teacher',
            'female': '~ university teacher'
        },
        'es': {
            'male': 'profesor universitario ~',
            'female': 'profesora universitaria ~'
        },
        'et': {
            'male': '~ ülikooli õppejõud',
            'female': '~ ülikooli õppejõud'
        },
        'fr': {
            'male': "professeur d'université ~",
            'female': "professeure d'université ~"
        },
        'gl': {
            'male': 'profesor universitario ~',
            'female': 'profesora universitaria ~'
        },
        'he': {
            'male': 'מרצה באוניברסיטה ~',
            'female': 'מרצה באוניברסיטה ~'
        },
        'ro': {
            'male': 'profesor universitar ~',
            'female': 'profesoară universitară ~'
        },
        'sq': {
            'male': 'profesor universitar ~',
            'female': 'profesore universitare ~'
        },
    },
    '~ writer': {
        'ar': {
            'male': 'كاتب ~',
            'female': 'كاتبة ~'
        },
        'bn': {
            'male': '~ লেখক',
            'female': '~ লেখিকা'
        },
        'ca': {
            'male': 'escriptor ~',
            'female': 'escriptora ~'
        },
        'en': {
            'male': '~ writer',
            'female': '~ writer'
        },
        'es': {
            'male': 'escritor ~',
            'female': 'escritora ~'
        },
        'et': {
            'male': '~ kirjanik',
            'female': '~ kirjanik'
        },
        'fr': {
            'male': 'écrivain ~',
            'female': 'écrivaine ~'
        },
        'gl': {
            'male': 'escritor ~',
            'female': 'escritora ~'
        },
        'he': {
            'male': 'סופר ~',
            'female': 'סופרת ~'
        },
        'ro': {
            'male': 'scriitor ~',
            'female': 'scriitoare ~'
        },
        'sq': {
            'male': 'shkrimtar ~',
            'female': 'shkrimtare ~'
        },
    },
}
# ---
translations_all = {
    **translationsOccupations,
    **translationsOccupations
}
# ---
# for x in translationsOccupations:
# if "ar" not in translationsOccupations[x]:
# print( x )
# ---
for x, yy in translationsOccupations_new.items():
    if "ar" in yy:
        translationsOccupations[x] = yy
    translations_all[x] = yy
# ---
'''
from stub.list import tempse_all
# ---
arl = {}
for x in tempse_all:
    arl[x.strip().lower()] = tempse_all[x]["ar"]
# ---
for x in New_Keys_occ:
    if "ar" not in translationsOccupations[x]:
        x2 = x.replace("~","").strip().lower()
        ar2 = arl.get(x2)
        if ar2:
            print( "        '%s': {" % x )
            print("            'ar': { 'male': '%s ~', 'female': '%s ~' },\n" % ( ar2 , ar2 ) )
# ---
'''

# ---
for x, yy in translationsOccupations.items():
    if "ar" in yy and yy["ar"]["male"] == yy["ar"]["female"]:
        print(f" male:{yy['ar']['male']} == female")
# ---

# ---
