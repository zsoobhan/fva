from django.conf import settings

CONTEXT_SETTINGS = [
    'GA_TRACKING_CODE',
    'FACEBOOK_APP_ID',
]


def add_context_settings(request):
    ctx = {}
    for setting_key in CONTEXT_SETTINGS:
        ctx.update({setting_key: getattr(settings, setting_key)})
    return ctx


def add_robots_question(request):
    ctx = {}
    q_and_a = request.session.get('q_and_a', None)
    if q_and_a:
        ctx.update({'QUESTION': q_and_a['question']})
    return ctx
