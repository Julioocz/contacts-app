def set_dict_to_attrs(obj, dict_obj):
    """Simple helper to set a dict as attributes for an object"""
    for prop, value in dict_obj.items():
        setattr(obj, prop, value)
