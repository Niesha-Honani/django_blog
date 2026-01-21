# BLOG API
## Build List

- user_app -> user model
- post_app -> blog model
- comment_app -> comment model

## Relationships 
- BlogUser --> Posts (One to Many)
```
author = models.ForeignKey('user_app.BlogUser', related_name="posts")
```

- Blog User --> Comments (One to Many)
```
author = models.ForeignKey('user_app.BlogUser', related_name = "comments" )
```
- Post -- > Comments (One to Many)
```
post = models.ForeignKey('post_app.Posts', related_name="comments")
```

BlogUser
 ├── posts (1 → many)
 └── comments (1 → many)

Posts
 └── comments (1 → many)



