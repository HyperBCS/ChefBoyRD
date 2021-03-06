from peewee import CharField, DateTimeField, IntegrityError, BooleanField
from chefboyrd.models import BaseModel
from datetime import datetime

class Shift(BaseModel):
    name = CharField(max_length=250)
    shift_time_start = DateTimeField()
    shift_time_end = DateTimeField()
    role = CharField(max_length=250)

    @classmethod
    def create_shift(cls, name, shift_time_start, shift_time_end, role):
        '''
        Creates a new Shift

        Args:
            name(char): The name of the employee claiming the shift
            shift_time_start(time): Starting time of shift
            shift_time_end(time): Ending time of shift
            role(str): 
        Returns:
            N/A
        '''
        try:
            cls.create(
                name=name, 
                shift_time_start=shift_time_start,
                shift_time_end=shift_time_end,
                role=role)
        except IntegrityError:
            raise ValueError("This should not happen (Shift)") 

    @classmethod
    def claim_shift(cls, id, name):
        '''
        Attempts to claim a shift given an ID

        Args:
            cls(Shift): an object representing a shift
            id(int): the id of the shift that we want to claim
            name(char): name of the employee that wants to claim the shift
        '''
        res = cls.get(cls.id == id)
        res.name = name
        res.save()
        return

    @classmethod
    def post_shift(cls, id):
        '''
        Attempts to post a shift given an ID

        Args:
            cls(Shift): an object representing a shift
            id(int): the id of the shift we want to post
        Returns:
            N/A
        '''
        res = cls.get(cls.id == id)
        res.name = ""
        res.save()
        return

    @classmethod
    def remove_shift(cls, id):
        '''
        Attempts to remove a shift given an ID

        Args:
            cls(Shift): an object representing a shift
            id(int): the id of the shift we want to post
        Returns:
            N/A
        '''
        res = cls.get(cls.id == id)
        res.delete_instance()
        return

    @classmethod
    def get_shift(cls, id):
        '''
        Attempts to retrieve a shift given an ID

        Args:
            cls(Shift): an object representing a shift
            id(int): the id of the shift we want to retrieve
        Returns:
            N/A
        '''
        res = cls.get(cls.id == id)
        return res