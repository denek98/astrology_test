{# Ім'я астролога, середній рейтинг астролога, суму зароблених ним грошей та долю його заробітку від усієї заробленої суми. Обмежте результат виконання запиту п'ятьма астрологами, доля заробітку яких була найвища. #}
with
    astrologer_metrics as (
        select a.astrologer_name, avg(r.rating) as avg_rating, sum(cp.price) as revenue
        from astrologers a
        left join chats c on a.astrologer_id = c.astrologer_id
        left join ratings r on c.chat_id = r.chat_id
        left join chat_pricing cp on cp.astrologer_level = a.astrologer_level
        group by a.astrologer_id, a.astrologer_name
    ),
    total_revenue as (select sum(revenue) as total_revenue from astrologer_metrics)

select
    astrologer_name,
    avg_rating,
    revenue,
    revenue * 1.0 / total_revenue * 100 as revenue_share
from astrologer_metrics
cross join total_revenue
order by revenue_share desc
limit 5
