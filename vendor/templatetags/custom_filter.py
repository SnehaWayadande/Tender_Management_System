from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)



@register.filter(name='addition')
def addition(number , number1):
    return number + number1

