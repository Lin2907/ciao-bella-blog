from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

#Blog post model

class BlogPost(models.Model):
    title = models.CharField(max_length=200 ,  unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name="blog_posts")
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    

    def __str__(self):
        return f"{self.title}"
    
    def like_count(self):
        return self.likes.count()


    #Method for getting an absolute url in order to use it for the gallery-posts showing
    
    #def get_absolute_url(self):
    #    return reverse('post_detail', args=[str(self.id)])

#Comment model for each post

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment"
     )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

#Tag model

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# BlogPostTag model for many-to-many relationship Blog post/Tag

class BlogPostTag(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} - {self.tag.name}'


class LikedPost(models.Model):
    #A model for user likes on a recipe

    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="likes"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_likes"
    )
    liked_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} likes {self.post.title}"
