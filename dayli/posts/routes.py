from flask import (render_template, url_for, flash, redirect, request,
                   abort, Blueprint)
from flask_login import current_user, login_required
from dayli import db
from dayli.models import Post, Comment, Like
from dayli.posts.forms import PostForm, CommentForm, LikeForm
from dayli.users.utils import save_picture

posts = Blueprint('posts', __name__)


@posts.route("/allpost")
def allpost():
    page = request.args.get('page', 1, type=int)
    allposts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,
                                                                     per_page=5)
    return render_template('allpost.html', posts=allposts)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    picture_name = None
    if form.validate_on_submit():
        if form.picture.data:
            picture_name = save_picture(form.picture.data)
        post = Post(title=form.title.data, content=form.content.data,
                    user_id=current_user.get_id(), image_file=picture_name)
        db.session.add(post)
        db.session.commit()
        flash('Ваш пост создан!')
        return redirect(url_for('posts.allpost'))
    return render_template('create_post.html', title="Новый пост",
                           form=form, image_file=picture_name,
                           legend="Новый пост")


@posts.route('/post/<int:post_id>', methods=['POST', 'GET'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    like_form = LikeForm()
    like_count = Like.query.filter_by(post_id=post_id).count()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.comment.data, post_id=post_id,
                          username=current_user.username)
        db.session.add(comment)
        db.session.commit()
        flash('Ваш комментарий добавлен.', 'success')
        return redirect(f'/post/{post_id}')
    return render_template('post.html', title=post.title, post=post,
                           form=form, like_form=like_form,
                           like_count=like_count)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != int(current_user.get_id()):
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            post.image_file = picture_file
        db.session.commit()
        flash('Ваш пост обновлен!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        image_file = url_for('static', filename='post_pics/' + post.image_file)
    return render_template('create_post.html', title='Обновление поста',
                           image_file=image_file,
                           form=form, legend='Обновление поста')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != int(current_user.get_id()):
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Пост был удален', 'success')
    return redirect(url_for('posts.allpost'))


@posts.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.username != current_user.username:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Ваш комментарий удален.', 'success')
    return redirect(url_for('posts.post', post_id=comment.post_id))


@posts.route('/post/<int:post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id == current_user.id:
        flash('Вы не можете ставить лайк на свой пост!', 'warning')
    elif Like.query.filter_by(user_id=current_user.id,
                              post_id=post_id).count():
        Like.query.filter_by(user_id=current_user.id, post_id=post_id).delete()
        db.session.commit()
        flash('Вам больше не нравиться этот пост', 'succes')
    else:
        like = Like(user_id=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
        flash('Вам нравиться этот пост.', 'success')
    return redirect(url_for('posts.post', post_id=post_id))
