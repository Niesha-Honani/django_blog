# BLOG API
## Build List

- user_app -> user model
- post_app -> blog model
- comment_app -> comment model

## Relationships 
- BlogUser --> Posts (One to Many)
'''
author = models.ForeignKey('user_app.BlogUser', related_name="posts")
'''

- Blog User --> Comments (One to Many)
- Post -- > Comments (One to Many)

BlogUser
 ├── posts (1 → many)
 └── comments (1 → many)

Posts
 └── comments (1 → many)



