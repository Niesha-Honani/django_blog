# BLOG API
## Build List

- user_app -> user model
- post_app -> blog model
- comment_app -> comment model

 
 



## Relationships 
BlogUser
├── posts (1 → many)

```
author = models.ForeignKey('user_app.BlogUser', related_name="posts")

```

└── comments (1 → many)

```
author = models.ForeignKey('user_app.BlogUser', related_name = "comments" )

```

Posts
 └── comments (1 → many)

```
post = models.ForeignKey('post_app.Posts', related_name="comments")
```





