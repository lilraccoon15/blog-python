from models import Post

def get_post_by_id(post_id):
    return Post.query.get(post_id)
