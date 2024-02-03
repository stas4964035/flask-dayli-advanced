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


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,
                    user_id=current_user.get_id())
        db.session.add(post)
        db.session.commit()
        flash('Ваш пост создан!')
        return redirect(url_for('posts.allpost'))
    return render_template('create_post.html', title="Новый пост",
                           form=form, legend="Новый пост")


@posts.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post_t = Post.query.get_or_404(post_id)
    if post_t.user_id != current_user:
        pass    # abort(403)

    form = PostForm()
    if form.validate_on_submit():
        post_t.title = form.title.data
        post_t.content = form.content.data
        db.session(post_t).commit()
        flash('Ваш пост обновлен!', 'success')
        return redirect(url_for('posts.post', post_id=post_t.id))
    elif request.method == 'GET':
        form.title.data = post_t.title
        form.content.data = post_t.content
    return render_template('create_post.html', title='Обновление поста',
                           form=form, legend='Обновление поста')
