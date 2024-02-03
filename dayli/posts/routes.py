from flask import (render_template, url_for, flash, redirect, request,
                   abort, Blueprint)
from flask_login import current_user, login_required
from dayli import db
from dayli.models import Post
from dayli.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/allpost")
@login_required
def allpost():
    page = request.args.get('page', 1, type=int)
    allposts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,
                                                                  per_page=5)
    return render_template('allpost.html', posts=allposts)
