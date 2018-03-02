
"""
    Content Management System
"""

LANG = 'ar'  # default website language 

ara = 'ar'
eng = 'en'


# replace login in the D_INDEX
LOG_Out = {     
    ara: u'خروج',
    eng: 'Logout'
}

# language link, direction
LANGUAGE = {
    ara:['English', 'rtl'],
    eng:[u'عربــي', 'ltr']
}

D_BRAND = {
        ara:u' بستاكت ',
        eng:' BesTakt '
    }


D_FOOTER = { # site map - (title, items)
    ara: [(u'')],
    eng: [('Services',)]
}

D_INDEX = {
    'soon':{
        ara:u'قريبآ',
        eng:'Coming soon'
    },

    'brand':{
            ara:u' بستاكت ',
            eng:' BesTakt '
    },

    'menu':{
        ara:[u'تسجيل الدخول',u'إستشارة ',u'خدمات',u' حسابك'],
        eng:['Login','Consultation','Services', 'Your Account' ], 
        'href':['/login','/consult','#services','/account']
    },

    'sub_menu': {
        ara: [u'رقم المبايل', u'الإسم بالكامل', u'إبدأ شهر مجاني' ],
        eng: ['Your Mobule Number', 'Your Full Name', 'Start 1 Month Free']
    },

    'free_btn':{
        ara: u' شهر مجاني',
        eng:'1 Month Free'
    },

    'free_form': {
        ara: [u'رقم المبايل', u'الإسم بالكامل', u'إبدأ شهر مجاني' ],
        eng: ['Your Mobule Number', 'Your Full Name', 'Start 1 Month Free']
    },

    'title':{
        ara:u'  بستاكت مستشارك المالي والإداري - نساعدك علي زيادة أرباحك ',
        eng:'BesTakt Your Finance & Management Consultant - We Help You Grow Your Profit'
    },

    'top_par':{
        ara:u'للشركات الصغيرة والمتوسطة بالسعودية والإمارات ، وفر الوقت والمال وإتصل بالمستشاريين الماليين ببستاكت ، نقوم بإعداد دراسات الجدوي الإقتصادية ومتطلبات الحصول علي قروض بنكية و المحاسبة وضريبة القيمة المضافة والزكاه وإستشارات مالية بأسعار تبدأ من ١٩٩٩ ريال / درهم في الشهر ',
        eng:'For Saudi and UAE Small and Medium companies, save time and money with our prefessional finance and tax consultants, and outsource your accounting, VAT, Zakat, starting from SAR/AED 1999 per month '
    },

    'top-par-btn':{
        ara: u'سجل وأحصل علي شهر مجاني',
        eng: 'Register and Get 1 Month Free'
    },

    'price':{
        ara:u'  فقط ١٩٩٩ ريال / درهم في الشهر ',
        eng:' Only 1999 SAR / AED per month '
    },

    'services': {
        ara: u'خدماتنا',
        eng: 'Our Services'
    },

    'card-a':{
        ara: [u'عرض خاص', u'خدمات المحاسبة وضريبة القيمة المضافة والزكاه وإستشارات مالية مرتين بالسنة', u'يبدأ بـ ١٩٩٩ ريال/درهم في الشهر', u'إشترك'],
        eng: ['Special Offer', 'Accouting services, VAT, ZAKAT, and financial consultation twice a year', 'Starts at 1999 SAR/AED Monthly', 'Subscribe']
    },

    'card-b':{
        ara: [u'إستشارة مالية', u'٤٠٠ ريال/درهم للساعة', u'', u'إحجز موعد'],
        eng: ['Online Finance Consutlation','SAR/AED 400 for 1 Hour','','Schedule Now']
    },

    'card-1-1':{
        eng: ['Feasibility Study', 'Our professional finance team in few days will prepare your fesibility study and requirements for bank loans', '' ],
        ara: [u'دراسات الجدوي الإقتصادية', u'فريق العمل المحترف لدينا يمكنه إعداد دراسات الجدوي الإقتصادية ومتطلبات الحصول علي القروض البنكية في أيام معدودة', '']
    },

    'card-1-2':{
        ara: [u'المحاسبة', u'نقوم بإعداد التقارير المحاسبية وإعداد إقرارات ضريبة القيمة المضافة والزكاه و القوائم المالية ', u'' ],
        eng: ['Accounting', 'Outsource fully your accounting bookkeeping, VAT, ZAKAT, financial statements for your company', '']
    },

    'card-1-3':{
        ara: [u'الإجراءات الإداية', u'نحن سنساعدك في وضع إجراءات وسياسات إداية لتنظيم سير العمل وتحسين الرقابة وتخفيض المصروفات بشركتك', u'' ],
        eng: ['Business Process', 'We help you develop your company process, policies and procedures for better control and cost reduction in your comapny', '']
    },

    'card-2-1':{
        ara: [u'المرتبات', u'تقارير المرتبات الشهرية ومصروفات الموظفين', u'' ],
        eng: ['Payroll', 'Monthly payroll reports and employee expenses', '']
    },

    'card-2-3':{
        ara: [u'إستشارات مالية', u'إستشارات مالية مباشرة على النت', u'' ],
        eng: ['Finance Consultation', 'Online finance consultation under your fingertip', '']
    },

    'card-2-2':{
        ara: [u'تنبيهات شهرية', u'نرسل لك تنبيهات شهرية عن إيجابيات ونقاط يمكن تطورها ', u'' ],
        eng: ['Monthly Alerts', 'We send you monthly alerts about positive and areas for improvement in your business', '']
    },

    'card-3-1':{
        ara: [u'', u'', u'' ],
        eng: ['', '', '']
    },

    'card-3-2':{
        ara: [u'', u'', u'' ],
        eng: ['', '', '']
    },

    'card-3-3':{
        ara: [u'', u'', u'' ],
        eng: ['', '', '']
    },

    'card-l':{
        ara: [u'مؤشرات شركتك علي النت', u'يوميآ تابع مؤشرات نمو شركتك علي النت عن طريق مستشارين محترفين لهم عشرات السنوات من الخبرة بالخليج', u'' ],
        eng: ['Online Business Dashboard', 'Take the right decision at the right time, our professional consultants will help you visualize your business dashboard with the right KPIs ', '']
    },


    'login': {
        ara: [u'عنوان البريد الإلكتروني', u'كلمة المرور',u'الدخول علي حسابك' ],
        eng: ['Email','Password','Login']
    }

    
}