from django.db import models

# try managed=True and managed=False


class Zoo(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    entry_fee = models.CharField(max_length=30)
    
    def __repr__(self):
        return self.name
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Animal(models.Model):
    kingdom = models.CharField(max_length=30)
    phylum = models.CharField(max_length=30)
    class_name = models.CharField(max_length=30)
    order = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    genus = models.CharField(max_length=30)

    def __repr__(self):
        return self.kingdom
    
    def __unicode__(self):
        return self.kingdom
  
    def __str__(self):
        return self.kingdom


class AnimalCount(models.Model):
    zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE) #, related_name='name')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE) #, related_name='kingdom')
    count = models.IntegerField()

    def __repr__(self):
        return self.zoo    

    def __unicode__(self):
        return self.zoo

    def __str__(self):
        return self.zoo