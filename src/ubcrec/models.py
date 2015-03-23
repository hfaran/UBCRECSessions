from django.db import models


class Player(models.Model):
    student_number = models.IntegerField()

    username = models.CharField()
    hashed_pass = models.CharField()
    salt = models.CharField()

    @classmethod
    def create(cls, student_number, username, hashed_pass, salt):
        return cls(
            student_number=student_number,
            username=username,
            hashed_pass=hashed_pass,
            salt=salt
        )


class Employee(models.Model):
    sin = models.IntegerField()
    first_name = models.CharField()
    last_name = models.CharField()

    username = models.CharField()
    hashed_pass = models.CharField()
    salt = models.CharField()

    @classmethod
    def create(cls, sin, first_name, last_name, username, hashed_pass, salt):
        return cls(
            sin=sin,
            first_name=first_name,
            last_name=last_name,
            username=username,
            hashed_pass=hashed_pass,
            salt=salt
        )


class Session(models.Model):
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    session_id = models.IntegerField()
    sport_id = models.IntegerField()
    venue_name = models.CharField()
    results = models.CharField()

    @classmethod
    def create(cls, start_time, end_time, session_id, sport_id, venue_name,
               results):
        return cls(
            start_time=start_time,
            end_time=end_time,
            session_id=session_id,
            sport_id=sport_id,
            venue_name=venue_name,
            results=results
        )


class Venue(models.Model):
    name = models.CharField()
    address = models.CharField()

    @classmethod
    def create(cls, name, address):
        return cls(
            name=name,
            address=address
        )
