from django import template

register = template.Library()


@register.inclusion_tag('toys/toy_list.html')
def render_toy_list(toys):
    return {
        'toys': toys
    }


@register.inclusion_tag('toys/employee_list_for_render.html')
def render_employee_list(employees):
    return {
        'employee_list': employees
    }


@register.filter
def address(value=''):
    lines = value.split('\n')
    return ' '.join(lines)
