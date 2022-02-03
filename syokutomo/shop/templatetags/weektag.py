from django import template

register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムフィルタとして登録する
@register.filter
def cusweek(value):
    weeks={1:"日",2:"月",3:"火",4:"水",5:"木",6:"金",7:"土"}
    if value in weeks:
        week = weeks[value]
    return week

