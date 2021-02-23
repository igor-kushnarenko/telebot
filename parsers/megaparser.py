from parsers.calendar_parser import calendar_obj_text
from parsers.promotion_parser import promotion_obj_text
from parsers.restaurant_parser import rest_list, bar_list, child_list, sneck_list


parser_dict = {
    'calendar_parser': calendar_obj_text,
    'promotion_parser': promotion_obj_text,
    'rest_list': rest_list,
    'bar_list': bar_list,
    'child_list': child_list,
    'sneck_list': sneck_list,
}

