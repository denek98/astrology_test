{# Ім'я астролога, кількість користувачів, які з ним спілкувалися, кількість чатів з максимальною оцінкою та максимальну тривалість чату з астрологом;  #}
with max_rating as (select max(rating) as max_rating from ratings)

select
    a.astrologer_name,
    count(distinct(c.user_id)) as contacted_users,
    count(case when r.rating = max_rating then 1 end) as max_rating_amount,
    max(c.session_duration) as max_session_duration
from astrologers a
left join chats c on a.astrologer_id = c.astrologer_id
left join ratings r on c.chat_id = r.chat_id
cross join max_rating
group by a.astrologer_id, a.astrologer_name
