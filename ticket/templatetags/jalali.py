from django import template
import jdatetime
from datetime import datetime, timezone
import pytz


register = template.Library()

@register.simple_tag
def jalali(value: datetime):
    if value == None: return 'ثبت نشده است'


    local_tz = pytz.timezone('Asia/Tehran')
    tehran = local_tz.normalize(value.replace(tzinfo=timezone.utc).astimezone(local_tz))
    jalali_date = jdatetime.datetime.fromgregorian(datetime=tehran).strftime("(%H:%M:%S) %Y - %m - %d")
    arabic = '۰١٢٣٤٥٦٧٨٩'
    english = '0123456789'
    translation_table = str.maketrans(english, arabic)
    return jalali_date.translate(translation_table)