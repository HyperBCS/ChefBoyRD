from datetime import timedelta, datetime
from chefboyrd.models.shifts import Shift

def checkShiftConditions(start, end, role):
    """
    This method checks that the shift is a reasonable accommadation for the restaurant

    Args:
        start: the time that the shift starts
        end: the time that the shift ends
        role: role of the user that is required to claim the shift

    Returns:
        True: if the shift is reasonable
        False: if the shift is unreasonable
    """
    daily_hour_limit = timedelta(hours=8)
    if start-end > daily_hour_limit:
        return False

def checkAvailability(id, name, role):
    """
    This method checks the availability of the shifts and makes sure that there are no
    scheduling overlaps in terms of duration.

    Args:
        id: the id of the shift that will be in analysis
        name: name of the user that is attempting to claim the shift
        role: role of the user that is claiming the shift

    Returns:
        True: if there are no scheduling conflicts
        False: if the worker in question already has a schedule arranged
    """
    tryShift = Shift.get_shift(id)
    if tryShift.role!=role:
        return False
    for workShift in Shift.select().where(Shift.name==name):
        if tryShift.shift_time_start==workShift.shift_time_start or tryShift.shift_time_end==workShift.shift_time_end:
            print("Controller: False")
            return False
        elif workShift.shift_time_start<tryShift.shift_time_start and workShift.shift_time_end<tryShift.shift_time_end:
            print("Controller: False")
            return False
        elif workShift.shift_time_start>tryShift.shift_time_start and workShift.shift_time_start<tryShift.shift_time_end:
            print("Controller: False")
            return False
    print("Controller: True")
    return True

def checkPostConditions(id, name, role):
    """
    This method checks the ability for the user to post their shift and makes sure that
    the user is not posting another user's shift. The only exceptions are for admins
    and managers.

    Args:
        id: the id of the shift that will be in analysis
        name: name of the user that is attempting to claim the shift
        role: role of the user that is claiming the shift

    Returns:
        True: if the user or the role has the proper influence
        False: if the user or role does not meet the criteria
    """
    tryShift = Shift.get_shift(id)
    if role=='admin' or role=='manager' or tryShift.role==role:
        return True
    elif tryShift.name==name:
        return True
    else:
        return False
    