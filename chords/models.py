from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = '')

    def __str__(self):
        return self.name
    

class LiturgicalTime(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Tempo Liturgico')

    def __str__(self):
        return self.name
    

class Chord(models.Model):
    name = models.CharField(verbose_name = '',max_length = 100)
    pdf_file = models.FileField(verbose_name = '', upload_to = 'pdf')
    category = models.ForeignKey(Category, verbose_name = '', on_delete = models.PROTECT)
    liturgical_time = models.ForeignKey(LiturgicalTime, verbose_name = '', on_delete = models.PROTECT)

    def __str__(self):
        return self.name


class Mass(models.Model):
    entrance = models.ForeignKey(Chord, verbose_name = '', related_name = 'entrance_chord', on_delete = models.DO_NOTHING)
    penitential = models.ForeignKey(Chord, verbose_name = '', related_name = 'penitential_chord', on_delete = models.DO_NOTHING)
    glory = models.ForeignKey(Chord, verbose_name = '', related_name = 'glory_chord', on_delete = models.DO_NOTHING)
    acclaim = models.ForeignKey(Chord, verbose_name = '', related_name = 'acclaim_chord', on_delete = models.DO_NOTHING)
    offertory = models.ForeignKey(Chord, verbose_name = '', related_name = 'offertory_chord', on_delete = models.DO_NOTHING)
    holy = models.ForeignKey(Chord, verbose_name = '', related_name = 'holy_chord', on_delete = models.DO_NOTHING)
    communion = models.ForeignKey(Chord, verbose_name = '', related_name = 'communion_chord', on_delete = models.DO_NOTHING)
    post_communion = models.ForeignKey(Chord, verbose_name = '', related_name = 'post_communion_chord', blank = True, null = True, on_delete = models.DO_NOTHING)
    final = models.ForeignKey(Chord, verbose_name = '', related_name = 'final_chord', on_delete = models.DO_NOTHING)
    generic = models.ForeignKey(Chord, verbose_name = '', related_name = 'generic_chord', blank = True, null = True, on_delete = models.DO_NOTHING)
    date = models.DateField(verbose_name = '')