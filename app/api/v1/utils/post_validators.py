from .validators import OrderItemsValodator
from ..responses.orders_responses import PostResponse

def is_post_data_valid(post_checker):
    def checker(**kwargs):
        if kwargs:
            if OrderItemsValodator(kwargs['item']).is_string_validator():
                if OrderItemsValodator(kwargs['description']).is_string_validator():
                    if OrderItemsValodator(kwargs['quantity']).is_int_validator():
                        return PostResponse().post_order_with_invalid_quantity_type_and_value_response()
                return PostResponse().post_order_with_invalid_description_type_and_value_response()
            return PostResponse().post_order_with_invalid_item_type_and_value_response()
        return PostResponse().post_order_with_empty_entries_response()
    return checker

            
        
            
        
            
        
            
