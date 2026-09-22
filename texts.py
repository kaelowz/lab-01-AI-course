"""Parallel test corpus for Lab 01.

The same three items in English, Russian and Kazakh. Parallel meaning is the
point: any difference in token count is a property of the tokenizer, not of
what is being said.

Instructors: the Kazakh and Russian wordings are a starting point. Substitute
your own if you prefer -- but keep the three versions semantically parallel,
otherwise the comparison measures translation length instead of tokenization.
"""

from __future__ import annotations

from typing import Dict

LANGUAGES = ("en", "ru", "kk")

#: One sentence. Short enough to inspect token by token.
SENTENCE: Dict[str, str] = {
    "en": "The bank raised interest rates by two percentage points last quarter.",
    "ru": "Банк повысил процентные ставки на два процентных пункта в прошлом квартале.",
    "kk": "Банк өткен тоқсанда пайыздық мөлшерлемені екі пайыздық тармаққа көтерді.",
}

#: A realistic support request -- the kind of text a production system pays for
#: thousands of times a day.
COMPLAINT: Dict[str, str] = {
    "en": (
        "Good afternoon. I opened a deposit at your branch in March and was told "
        "the rate was fixed for twelve months. In August the rate on my account "
        "dropped without any notice. I have attached the contract and the "
        "statement. Please explain on what basis the rate was changed and "
        "restore the original terms."
    ),
    "ru": (
        "Добрый день. Я открыл депозит в вашем отделении в марте, и мне сказали, "
        "что ставка зафиксирована на двенадцать месяцев. В августе ставка по "
        "моему счёту снизилась без какого-либо уведомления. Прилагаю договор и "
        "выписку. Прошу объяснить, на каком основании была изменена ставка, и "
        "восстановить первоначальные условия."
    ),
    "kk": (
        "Қайырлы күн. Мен наурыз айында сіздің бөлімшеңізде депозит аштым, маған "
        "мөлшерлеме он екі айға бекітілген деп айтылды. Тамыз айында менің "
        "шотымдағы мөлшерлеме ешқандай хабарламасыз төмендеді. Шартты және "
        "үзінді көшірмені қоса тіркеп отырмын. Мөлшерлеме қандай негізде "
        "өзгертілгенін түсіндіріп, бастапқы шарттарды қалпына келтіруіңізді "
        "сұраймын."
    ),
}

#: A system prompt -- the part you resend on every single request.
SYSTEM_PROMPT: Dict[str, str] = {
    "en": (
        "You are a support assistant for a retail bank. Answer only from the "
        "documents provided. If the answer is not in them, say so. Never invent "
        "an account number, a rate or a date."
    ),
    "ru": (
        "Вы — ассистент поддержки розничного банка. Отвечайте только по "
        "предоставленным документам. Если ответа в них нет, так и скажите. "
        "Никогда не выдумывайте номер счёта, ставку или дату."
    ),
    "kk": (
        "Сіз — бөлшек банктің қолдау көрсету ассистентісіз. Тек берілген "
        "құжаттар бойынша жауап беріңіз. Егер жауап оларда болмаса, солай деп "
        "айтыңыз. Шот нөмірін, мөлшерлемені немесе күнді ешқашан ойдан "
        "шығармаңыз."
    ),
}

#: Everything the lab measures, keyed by a short id.
CORPUS: Dict[str, Dict[str, str]] = {
    "sentence": SENTENCE,
    "complaint": COMPLAINT,
    "system_prompt": SYSTEM_PROMPT,
    #CORE TASK 1:
    "my_custom_text": {
        "en": "Your password will expire in 3 days. Please update it immediately to maintain access to your account.",
        "ru": "Ваш пароль истекает через 3 дня. Пожалуйста, немедленно обновите его для сохранения доступа к аккаунту.",
        "kk": "Сіздің құпия сөзіңіздің мерзімі 3 күннен кейін аяқталады. Аккаунтқа кіруді сақтау үшін оны дереу жаңартыңыз."
    },

    #CORE TASK 2: 
    "kk_shared_letters": {
        "en": "Marat found an apple outside.", 
        "ru": "Марат нашел яблоко на улице.", 
        "kk": "Марат далада алма тапты" 
    },
    "kk_specific_letters": {
        "en": "Grandma lives in the region.", 
        "ru": "Бабушка живет в регионе.",     
        "kk": "Әжең өңірде өмір сүреді" 
    },

    #CORE TASK 3: Prose vs JSON
    "complaint_json": {
        "en": '{"opened": "March", "message": "I have attached the contract and the statement. Why did the rate change?", "documents_attached": true}',
        "ru": '{"opened": "Март", "message": "Я прикрепил договор и выписку. Почему изменилась ставка?", "documents_attached": true}',
        "kk": '{"opened": "Наурыз", "message": "Мен келісімшарт пен үзінді көшірмені тіркедім. Неліктен мөлшерлеме өзгерді?", "documents_attached": true}'
    },

    #ADVANCED TASK 4:
    "system_prompt_short": {
        "en": "Answer strictly based on documents. Be concise.",
        "ru": "Отвечай строго по документам. Будь краток. Не придумывай факты.",
        "kk": "Құжаттарға сүйеніп қана қысқа жауап беріңіз. Фактілерді ойдан шығармаңыз."
    }
}
