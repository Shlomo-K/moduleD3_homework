from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.all().aggregate(PostRating=Sum('rating'))
        p_rating = 0
        p_rating += post_rating.get('PostRating')

        comment_rating = self.author_user.comment_set.all().aggregate(comment_rating=Sum('rating'))
        c_rating = 0
        c_rating += comment_rating.get('comment_rating')

        self.rating_author = p_rating * 3 + c_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )

    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    date_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()


    def preview(self):
        return self.text[0:123] + '...'


class PostCategory(models.Model):
    post_through = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_through = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.comment_user.username
    
    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -=1
        self.save()
# Create your models here.
