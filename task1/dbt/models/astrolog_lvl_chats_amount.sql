{# Кількість чатів в залежності від рівня астролога #}
select a.astrologer_level, count(c.chat_id) as chats_amount
from chats c
left join astrologers a on c.astrologer_id = a.astrologer_id
group by a.astrologer_level
