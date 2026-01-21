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

## Foreign Key v Reverse Access 
* One way pointer:
Foreign Key --> comment.post -> parent Post

* Reverse relationship (reverse access)
related_name = "comments" : Posts -> comments

equivalent to : "Get me all the comments of this Post 
```
post.comments.all()

```

related_name = "posts"

"Get me all the posts made by this user"
```
user.posts.all()

```
| Relationship | related_name | Reads as |
| --- | --- | --- |
| User → Posts | `posts` | user.posts |
| User → Comments | `comments` | user.comments |
| Post → Comments | `comments` | post.comments |




