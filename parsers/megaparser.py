from parsers.calendar_parser import calendar_obj_text
from parsers.news_parser import news_obj_text
from parsers.promotion_parser import promotion_obj_text
from parsers.restaurant_parser import restaurant_obj_text

parser_dict = {
    'calendar_parser': calendar_obj_text,
    'news_parser': news_obj_text,
    'promotion_parser': promotion_obj_text,
    'restaurant_parser': restaurant_obj_text,
}