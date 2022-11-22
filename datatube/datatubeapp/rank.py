from django.db import models
from django.db.models.functions import window
from datatubeapp.models import Video

videos = Video.objects.all().annotate(row_number=models.Window(
    expression=window.RowNumber(),
    partition_by=[models.F('category_id')],
    order_by=[models.F('views').desc()],
)).order_by('views')

sql, params = videos.query.sql_with_params()

count_per_category = 3
count = 10
videos_filtered = Video.objects.raw(
        SELECT * FROM videos
        LIMIT 10
    .format(sql),
    [*params, count_per_category, count],
)

selected_videos = list(videos_filtered)