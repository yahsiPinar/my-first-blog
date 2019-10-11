from django.db import models
from django.utils import timezone

#models.Model djangoya bu bir django modeli onu veritabanında saklaman gerek demek içindir.
class Post(models.Model):
    #ForeignKey başka bir modele referans tanımlar
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) #postu yazan kişi
    title = models.CharField(max_length=200) #postun başlığı
    text = models.TextField() #içerik
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.published_date=timezone.now()
        self.save() #save() objeyi veritabanına kaydeder
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    def __str__(self):
        return self.title

class Commit(models.Model):
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment=True
        self.save()
    def __str__(self):
        return self.text
