Django shell

[執行]
    $ python manage.py shell
    $ exit() [退出]

[基本操作]
    $ from blog.models import Post
    $ from django.contrib.auth.models import User

    $ User.objects.all()
    $ user = User.objects.get(username='jingya.zeng')

    $ Post.objects.all()
    $ Post.objects.create(author=user, title='Sample title', text='Test') [新增文章]
    $ Post.objects.filter(author=user) [篩選作者]
    $ Post.objects.filter(published_date__isnull=False) [已發布的網誌]
    $ Post.objects.filter(published_date__isnull=True) [未發布的網誌]

[發布網誌]
    $ Post.objects.get(id=1).publish()

[排序]
    $ Post.objects.order_by('created_date') [正排]
    $ Post.objects.order_by('-created_date') [反排]

